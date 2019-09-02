from django.conf import settings
from django.conf.urls import url,static
from django.views.generic import TemplateView
from myapp import views
from django.urls import path

urlpatterns = [
    path('app/', views.homepage),
    path('content/', views.content),
]