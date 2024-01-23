from django.urls import path
from projects import views

urlpatterns = [
    path('', views.project_api.as_view(), name="project_api"),
]