from django.urls import path
from experience import views

urlpatterns = [
    path('', views.experience_api.as_view(), name="experience_api"),
]