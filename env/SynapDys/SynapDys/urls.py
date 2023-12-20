"""
URL configuration for SynapDys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from backoffice.views import lesson_detail, track_progress
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('lesson/<int:lesson_id>/', lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/track_progress/', track_progress, name='track_progress'),
    path('', TemplateView.as_view(template_name='landing_page.html'), name='landing_page'),
    
]

