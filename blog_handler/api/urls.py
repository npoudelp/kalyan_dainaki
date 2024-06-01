from django.urls import path
from . import apis

urlpatterns = [
    path('', apis.Home.as_view(), name='home'),
    path('catagory/', apis.CatagoryList.as_view(), name='catagory'),
    path('users/', apis.RegisterUsers.as_view(), name='users'),
    path('manage_blogs/', apis.BlogManager.as_view(), name='blog_manager'),
    path('blogs/', apis.GetAllBlogs.as_view(), name='get_blogs'),
    path('blogs/<int:id>/', apis.GetBlogById.as_view(), name='get_blog_by_id'),
]