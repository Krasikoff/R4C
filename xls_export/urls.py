from . import views
from django.urls import re_path

urlpatterns = [

    re_path(r'^export/xls/$', views.export_users_xls, name='export_users_xls'),
]
