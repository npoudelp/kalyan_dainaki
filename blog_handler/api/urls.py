from django.urls import path
from . import apis

urlpatterns = [
    path('', apis.Home.as_view(), name='home'),
    path('manage_catagory/', apis.CatagoryManager.as_view(), name='catagory'),
    path('users/', apis.RegisterUsers.as_view(), name='users'),
    path('manage_blogs/', apis.BlogManager.as_view(), name='blog_manager'),
    path('blogs/', apis.GetAllBlogs.as_view(), name='get_blogs'),
    path('blogs/get/<int:id>/', apis.GetBlogById.as_view(), name='get_blog_by_id'),
    path('blogs/find/<str:key>/', apis.SearchBlog.as_view(), name='search_blog'),
    path('blogs/add_view/<int:id>', apis.UpdateViewCount.as_view(), name='update_view'),
    path('blogs/by_view/', apis.GetBlogsByView.as_view(), name='get_blog_by_view'),
    path('blogs/by_catagory/<str:category>/', apis.GetBlogsByCatagory.as_view(), name='get_blog_by_catagory'),
]