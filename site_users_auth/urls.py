from django.urls import path
from site_users_auth import views

urlpatterns = [
    path('', views.SiteUsersAuth.as_view(), name="site_users_api"),
    path('refresh/', views.ChangeToken.as_view(), name="site_users_api"),
    path('login-history/', views.SiteUsersAuthHistory.as_view(), name="site_users_api"),
    path('get-token/', views.ViewerToken.as_view(), name="site_users_api_for_get_method_only"),
]