from django.db.models.query_utils import Q
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets
from .models import Interns
from .serializers import *
from students.serializers import StudentSerializer

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework as filters
from django.db.models import Avg, Count, Min, Sum, Max, F

class SearchFilter(filters.FilterSet):
    city = filters.CharFilter(lookup_expr='contains')
    university = filters.CharFilter(lookup_expr='contains')
    state = filters.CharFilter(lookup_expr='contains')
    company = filters.CharFilter(lookup_expr='contains')
    salary_min = filters.NumberFilter(field_name="salary", lookup_expr='gte')
    salary_max = filters.NumberFilter(field_name="salary", lookup_expr='lte')

    class Meta:
            model = Interns
            fields = ['city', 'salary_min', 'salary_max']

class SetPaginationStyle(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class SetLimitOffset(LimitOffsetPagination):
    default_limit = 20


class InternViewSet(viewsets.ModelViewSet):
    queryset = Interns.objects.all().order_by('-post_date')
    serializer_class = StudentSerializer
    pagination_class = SetLimitOffset
    http_method_names = ['get', 'post', 'head']

class SearchAPIView(viewsets.ModelViewSet):
    queryset = Interns.objects.all().order_by('-salary')
    serializer_class = StudentSerializer
    filter_class = SearchFilter
    pagination_class = SetLimitOffset

class CompanyView(viewsets.ViewSet):

    def list(self, request):
        companyName = request.query_params.get('company', '')
        queryset = Interns.objects.filter(company__contains=companyName)
        freshmen = Interns.objects.filter(company__contains=companyName, grade_year="Freshman")
        sophmore = Interns.objects.filter(company__contains=companyName, grade_year="Sophmore")
        junior = Interns.objects.filter(company__contains=companyName, grade_year="Junior")
        senior = Interns.objects.filter(company__contains=companyName, grade_year="Senior")

        locations = queryset.values_list('city', flat=True).distinct()

        totalAvg = queryset.aggregate(Avg('salary'))
        totalMax = queryset.aggregate(Max('salary'))
        totalMin = queryset.aggregate(Min('salary'))
        totalCount = len(queryset)

        freshmenAvg = freshmen.aggregate(Avg('salary'))
        freshmenMax = freshmen.aggregate(Max('salary'))
        freshmenMin = freshmen.aggregate(Min('salary'))
        freshmenCount = len(freshmen)

        sophmoreAvg = sophmore.aggregate(Avg('salary'))
        sophmoreMax = sophmore.aggregate(Max('salary'))
        sophmoreMin = sophmore.aggregate(Min('salary'))
        sophmoreCount = len(sophmore)

        juniorAvg = junior.aggregate(Avg('salary'))
        juniorMax = junior.aggregate(Max('salary'))
        juniorMin = junior.aggregate(Min('salary'))
        juniorCount = len(junior)

        seniorAvg = senior.aggregate(Avg('salary'))
        seniorMax = senior.aggregate(Max('salary'))
        seniorMin = senior.aggregate(Min('salary'))
        seniorCount = len(senior)

        return Response({"cities" : locations, "total" : {"avg" : totalAvg, "max" : totalMax, "min" : totalMin, "count" : totalCount},
        "freshmen" : {"avg" : freshmenAvg, "max" : freshmenMax, "min" : freshmenMin, "count" : freshmenCount},
        "sophmore" : {"avg" : sophmoreAvg, "max" : sophmoreMax, "min" : sophmoreMin, "count" :sophmoreCount},
        "junior" : {"avg" : juniorAvg, "max" : juniorMax, "min" : juniorMin, "count" : juniorCount},
        "senior" : {"avg" : seniorAvg, "max" : seniorMax, "min" : seniorMin, "count" : seniorCount}
        })

class RankView(viewsets.ViewSet):

    def list(self, request):
        cityName = request.query_params.get('city', '')
        queryset = Interns.objects.annotate(label=F('company')).values('label').filter(city__contains=cityName).annotate(y=Avg('salary'), min=Min('salary'), max=Max('salary'), cp=Count('company')).order_by()
        sort = sorted(queryset, key = lambda i: i['y'], reverse=True)

        all_count = Interns.objects.filter(city__contains=cityName).count()
        s10 = round(Interns.objects.filter(city__contains=cityName, salary__range=(0, 10)).count() / all_count * 100, 1)
        s20 = round(Interns.objects.filter(city__contains=cityName, salary__range=(10.0001, 20)).count() / all_count * 100, 1)
        s30 = round(Interns.objects.filter(city__contains=cityName, salary__range=(20.0001, 30)).count() / all_count * 100, 1)
        s40 = round(Interns.objects.filter(city__contains=cityName, salary__range=(30.0001, 40)).count() / all_count * 100, 1)
        s50 = round(Interns.objects.filter(city__contains=cityName, salary__range=(40.0001, 50)).count() / all_count * 100, 1)
        s60 = round(Interns.objects.filter(city__contains=cityName, salary__range=(50.0001, 60)).count() / all_count * 100, 1)
        s70 = round(Interns.objects.filter(city__contains=cityName, salary__range=(60.0001, 70)).count() / all_count * 100, 1)
        s80 = round(Interns.objects.filter(city__contains=cityName, salary__range=(70.0001, 80)).count() / all_count * 100, 1)
        pulus80 = round(Interns.objects.filter(city__contains=cityName, salary__gt=80).count() / all_count * 100, 1)

        #ranges = {'all': all_count, 's10': s10, 's20': s20, 's30': s30, 's40': s40, 's50': s50, 's60': s60, 's70': s70, 's80': s80, 'pulus80': pulus80}
        ranges = [{'y': s10, 'label': 'less than $10'}, {'y': s20, 'label': '$10-$20'}, {'y': s30, 'label': '$20-$30'},
                 {'y': s40, 'label': '$30-$50'}, {'y': s50, 'label': '$40-$50'}, {'y': s60, 'label': '$50-$70'}, 
                 {'y': s80, 'label': '$70-$80'}, {'y': pulus80, 'label': '80+'},]
        
        return Response({'agg': sort, 'ranges': ranges})