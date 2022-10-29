from django.urls import path
from . import views

urlpatterns = [
    path('respond/', views.respond, name='respond'),
    path('', views.index, name='index'),
]