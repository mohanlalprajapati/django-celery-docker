"""app URL Configuration

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
from django.urls import re_path, include
from .views import AdditionView,show_task_results

app_name = 'core'
urlpatterns = [
    re_path(r'^add', AdditionView.as_view(), name='index'),
    re_path(r'^show_task_results/(?P<task_id>[\w-]+)/$', show_task_results, name='show_task_result'),

]
