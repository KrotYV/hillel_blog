from django.urls import path

from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='index'),
    path('create_post', views.PostCreate.as_view(), name='post_create')
]
