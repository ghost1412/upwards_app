"""upwards_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url, include
from upwards_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/2xx', views.create_2xx_view, name='2xx_view'),
    url(r'^api/5xx', views.create_5xx_view, name='5xx_view'),
    url(r'^api/4xx', views.create_4xx_view, name='4xx_view'),
    url(r'^api/', views.api_view, name='exception_view'),
]
