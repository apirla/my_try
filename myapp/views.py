# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from .serializers import myserializer
from rest_framework import viewsets
from .models import mymodel

# Create your views here.
class myviewset(viewsets.ModelViewSet):
    queryset = mymodel.objects.all()
    serializer_class = myserializer

def index(request):
    return HttpResponse("hello world")

