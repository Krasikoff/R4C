from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'xls/', views.export_robots_xls, name='export_robots_xls'),
]
