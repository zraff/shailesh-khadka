from django.urls import path
from . import views

urlpatterns = [
    path('', views.tools_index, name='tools_index'),
]
