"""journals_archive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from journals import views as journals_views
from journals_archive import settings



urlpatterns = [
    path('', journals_views.PublishersView.as_view()),
    path('accounts/', include('accounts.urls')),
    path('journals/', include('journals.urls')),
    path('admin/', admin.site.urls),
    path('media/publications/<str:publisher>/<str:publication>', journals_views.publication_serve_view)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
