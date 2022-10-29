from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import JsonResponse
from .serializers import JsonSerializer
# from .serializers import serializers

# Create your views here.


def home(request):
  return HttpResponse('HOME')

@api_view(['GET'])
def json_list(request):
  jsonresponses = JsonResponse.objects.all()
  serializer = JsonSerializer(jsonresponses, many=True)
  return Response(serializer.data)
