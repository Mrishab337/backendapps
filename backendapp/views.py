from django.shortcuts import render
from rest_framework import generics
from .models import Businessregister
from .serializers import BusinessSerializer


# Create your views here.

class BusinessCreateView(generics.CreateAPIView):
    queryset = Businessregister.objects.all()
    serializer_class = BusinessSerializer