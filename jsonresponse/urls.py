from django import views
from django.contrib import admin
from django.urls import path
from jsonresponse import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.json_list),
    path('api/', views.json_list),
]
