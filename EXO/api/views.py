from django.shortcuts import render
import django_filters.rest_framework
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializer import UserSerializer, CohortSerializer, cohortInfosSerializer
from cohort.models import cohort, cohortInfos, ExamInfo, QuesModel
from rest_framework import generics
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']

class CohortViewSet(viewsets.ModelViewSet):
    queryset = cohort.objects.all()
    serializer_class = CohortSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['CohortID', 'CohortName','Admin']

    
    

class CohortInfosViewSet(viewsets.ModelViewSet):
    queryset = cohortInfos.objects.all()
    serializer_class = cohortInfosSerializer    
    filter_backends = [filters.SearchFilter]
    search_fields = ['Member__email']
