from django.urls import path, include
from students import views
from rest_framework import renderers
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'all', views.InternViewSet, basename='students')
router.register(r'search', views.SearchAPIView, basename='search')
router.register(r'top_avg', views.AverageView, basename='top_avg')

urlpatterns = [
    path('', include(router.urls)),
]

