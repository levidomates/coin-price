from django.urls import path 

from . import views 

urlpatterns = [
    path('coin',views.index),
]