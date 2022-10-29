from rest_framework.serializers import ModelSerializer
from .models import JsonResponse


class JsonSerializer(ModelSerializer):
  class Meta:
      model = JsonResponse
      exclude = ['id','name']