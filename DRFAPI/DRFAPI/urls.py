"""
URL configuration for DRFAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.sample_fun),
    path('fun1',views.fun1),
    path('fun2/<id>',views.fun2),
    path('fun3',views.fun3),
    path('fun4/<d>',views.fun4),
    path('fun5',views.fun5.as_view()),
    path('fun6/<d>',views.fun6.as_view()),
    path('ge',views.genericapiview.as_view()),
    path('update/<id>',views.update.as_view()),







]
