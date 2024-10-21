from django.urls import path
from site_users import views

urlpatterns = [
    path('', views.siteusers.as_view(), name="site_users_api"),
    path('<str:user_id>', views.siteusers.as_view(), name="site_users_api"),
]