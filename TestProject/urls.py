"""
URL configuration for TestProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf.urls import handler404
from django.contrib import admin
from django.contrib.redirects.models import Redirect
from django.urls import path
from django.urls import path

import TestProjectApp.views
from TestProjectApp import views
from django.contrib import admin
from django.urls import path
from TestProjectApp.views import login_view, home_view, conditions_view, logout_view

from django.shortcuts import redirect



handler404 = 'TestProjectApp.views.custom_404_view'
handler500 = 'TestProjectApp.views.custom_500_view'



urlpatterns = [


    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('conditions/<int:inspection_id>/', conditions_view, name='conditions'),
    path('logout/', logout_view, name='logout'),
    path('conditions/<int:inspection_id>/', conditions_view, name='conditions'),
]
