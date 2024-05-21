from django.urls import path
from site_users_auth import views

urlpatterns = [
    path('', views.SiteUsersAuth.as_view(), name="site_users_api"),
    path('login-history/', views.SiteUsersAuthHistory.as_view(), name="site_users_api"),
]