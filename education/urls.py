from django.urls import path
from education import views

urlpatterns = [
    path('', views.education_api.as_view(), name="education_api"),
]