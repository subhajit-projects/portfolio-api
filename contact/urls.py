from django.urls import path
from contact import views

urlpatterns = [
    path('', views.contact_api.as_view(), name="contact_api"),
]