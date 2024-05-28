from django.urls import path
from . import apis

urlpatterns = [
    path('', apis.Home.as_view(), name='home'),
    path('catagory/', apis.CatagoryList.as_view(), name='catagory'),
]