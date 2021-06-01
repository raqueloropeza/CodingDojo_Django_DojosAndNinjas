from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('dojos', views.dojos),
    path('ninjas', views.ninjas)
]