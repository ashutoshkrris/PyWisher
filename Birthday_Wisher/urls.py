"""Birthday_Wisher URL Configuration

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
from sender import execute
from django.contrib import admin
from django.urls import path
from uploader.views import home, dashboard, uploader, add_form
from sender.views import sender, email_temp
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type='text/plain')),
    path('', home, name="home"),
    path('dashboard/', dashboard, name="dashboard"),
    path('add/', add_form, name="add_form"),
    path("uploader/", uploader, name="uploader"),
    path('sender/', sender, name="sender"),
    path('wish/<str:sender>/<str:receiver>/', email_temp, name="email_temp")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
