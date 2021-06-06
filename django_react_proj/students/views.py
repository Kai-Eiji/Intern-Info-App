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
from django.db.models import Avg, Count, Min, Sum, Max

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

