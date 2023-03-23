from django.shortcuts import render
from product.models import *
from product.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.



class ProductData(APIView):
    def get(self, request, format=None):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)