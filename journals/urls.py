from django.urls import path

from . import views

urlpatterns = [
    path('publications/<str:publisher>', views.PublicationsView.as_view(), name='publications'),
    path('publishers', views.PublishersView.as_view(), name='publishers'),
]