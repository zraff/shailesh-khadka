from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_resume, name='view_resume'),
]
