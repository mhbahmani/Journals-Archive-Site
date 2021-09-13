from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login_publisher_admin, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('upload', views.upload_publication, name='upload_publication'),
]