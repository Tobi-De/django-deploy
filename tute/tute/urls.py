from django.contrib import admin
from django.urls import path

from counter import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('people', views.people),
    path('', views.index),
]
