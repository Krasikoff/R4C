from django.urls import path

from . import views

app_name = 'api/v1/'

urlpatterns = [
    path('robots/', views.index, name='robots'),
]
