from django.shortcuts import render
from rest_framework import generics
from .serializers import NewSerializer
from .models import Student

class ListApiView(generics.ListAPIView):
      queryset = Student.objects.all()
      serializer_class = NewSerializer

class CreateApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = NewSerializer

class UpdateApiView(generics.UpdateAPIView):   
    queryset = Student.objects.all()
    serializer_class = NewSerializer

class DetailApiView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = NewSerializer