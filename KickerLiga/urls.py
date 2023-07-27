"""
URL configuration for KickerLiga project.

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
from django.views.generic import RedirectView
from django.urls import re_path
from django.urls import path

from League import views

urlpatterns = [
    path("", views.scoreboard, name="members"),
    path("admin/", admin.site.urls),
    # path("",views.scoreboard,name="members"),
    re_path(r"^favicon\.ico$", RedirectView.as_view(url="/static/images/favicon.ico")),
]
