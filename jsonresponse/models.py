from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class JsonResponse(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  slackUsername = models.CharField(max_length=200, blank=True, null=True)
  backend = models.BooleanField(default=False)
  age = models.IntegerField(blank=True, null=True)
  bio = models.CharField(max_length=500, blank=True, null=True)

  def __str__(self):
    return self.name