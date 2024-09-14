from django.urls import path
from about import views

urlpatterns = [
    path('', views.about_api.as_view(), name="about_api"),
    path('<str:about_id>', views.about_api.as_view(), name="about_api"),
]