from django.urls import path
from skill import views

urlpatterns = [
    path('', views.skills_api.as_view(), name="skills_api"),
    path('<str:skill_id>', views.skills_api.as_view(), name="skills_api"),
]