from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_publisher_admin, name='login'),
    path('upload', views.upload_publication, name='upload_publication'),
]