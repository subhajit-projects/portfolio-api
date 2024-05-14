from django.urls import path
from site_users_auth import views

urlpatterns = [
    path('login-history/', views.SiteUsersAuth.as_view(), name="site_users_api"),
]