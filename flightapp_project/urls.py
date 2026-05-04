"""
URL configuration for flightapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from flightapp import views as app_views
from flightapp_project import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',app_views.index, name='index'), #ja importirame funkcijata index od app_views za da redirektirame na /index
    path('details/<id>',app_views.details,name='details'), # <id> za da znae za koj let se odnesuva
    path('add_form',app_views.addForm,name='addForm'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
