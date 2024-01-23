from django.urls import path
from blog import views

urlpatterns = [
    path('<int:page_no>/', views.blog_api.as_view(), name="blog_api"),
    path('<str:post_id>/', views.blog_details.as_view(), name="blog_details"),
]