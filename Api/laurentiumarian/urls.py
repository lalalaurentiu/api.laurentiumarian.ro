from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppsView.as_view()),
]
