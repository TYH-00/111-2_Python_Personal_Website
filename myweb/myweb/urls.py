"""myweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from mainsite import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('all/', views.all_data),
    path('filter/', views.filtered_data),
    path('nkustnews/', views.nkustnews),
    path('phonelist/', views.phonelist),
    path('phonelist/maker/<int:id>/', views.phonelist),
    path('phonelist/country/<int:id>/', views.phonelist),
    path('stock300list/', views.stock300list),
    path('chart/', views.chart),
]
