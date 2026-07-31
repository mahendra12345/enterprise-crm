from django.urls import path,include
from mydb1.views import all_data

urlpatterns = [
    path('all/',all_data,name='all_data')
]
