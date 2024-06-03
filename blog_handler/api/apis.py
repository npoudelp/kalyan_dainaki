from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Catagory, Blogs
from django.utils import timezone
from django.contrib.auth.models import User
from .serializers import CatagorySerializers , UserSerializers, BlogSerializers
from django.db.models import Q

class Home(APIView):
    permission_classes = []
    def get(self, request):
        return Response({
            "status": "Welcome to blog handler api",
            "data": {
                "author": "Group tantraNsa",
                "email": None,
                "date": f"{timezone.now().hour}:{timezone.now().minute}:{timezone.now().second}",
            }
        })
    

# catagory management
class CatagoryManager(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        GetCatagory = CatagorySerializers(Catagory.objects.all(), many=True)
        return Response(GetCatagory.data)


    def post(self, request):
        try:
            CatagoryData = CatagorySerializers(data=request.data)
            if CatagoryData.is_valid():
                CatagoryData.save()
                return Response({
                    "status": "Catagory added successfully...",
                    "data": CatagoryData.data
                })
            else:
                return Response(CatagoryData.errors)
        except:
            return Response("Error")
    

    def put(self, request):
        try:
            CatagoryData = Catagory.objects.get(id=request.data['id'])
            CatagoryData = CatagorySerializers(CatagoryData, data=request.data)
            if CatagoryData.is_valid():
                CatagoryData.save()
                return Response({
                    "status": "Catagory updated successfully...",
                    "data": CatagoryData.data
                })
            else:
                return Response(CatagoryData.errors)
        except:
            return Response("Error")


    def delete(self, request):
        try:
            CatagoryData = Catagory.objects.get(id=request.data['id'])
            CatagoryData.delete()
            return Response({
                "status": "Catagory deleted successfully...",
                "data": CatagoryData
            })
        except:
            return Response({
                "status": "Error",
                "data": "No catagory found with this id"
            })



# addign users in database
class RegisterUsers(APIView):
    permission_classes = []

    def get(self, request):
        GetUsers = UserSerializers(User.objects.all().order_by('-id'), many=True)
        return Response(GetUsers.data)
    

    def post(self, request):
        try:
            UserName = request.data['username']
            Password = request.data['password']
            Email = request.data['email']
            NewUser = User.objects.create_user(username=UserName, password=Password, email=Email)
            NewUser.first_name = request.data['first_name']
            NewUser.last_name = request.data['last_name']
            NewUser.save()
            return Response({
                "status": "User added successfully...",
                "data": {
                    "username": NewUser.username,
                    "email": NewUser.email,
                    "first_name": NewUser.first_name,
                    "last_name": NewUser.last_name
                }
            })
        except:
            return Response("Error")
        

#handeling blogs by admin
class BlogManager(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            GetBlogs = BlogSerializers(Blogs.objects.all().order_by('-id'), many=True)
            return Response(GetBlogs.data)
        except:
            return Response("Error")


    def post(self, request):
        try:
            NewBlog = BlogSerializers(data=request.data)
            if NewBlog.is_valid():
                NewBlog.save()
                return Response({
                    "status": "Blog added successfully...",
                    "data": NewBlog.data
                
                })
            else:
                return Response(NewBlog.errors)
        except:
            return Response("Error")


    def put(self, request):
        try:
            GetBlog = Blogs.objects.get(id=request.data['id'])
            UpdateBlog = BlogSerializers(GetBlog, data=request.data)
            if UpdateBlog.is_valid():
                UpdateBlog.save()
                return Response({
                    "status": "Blog updated successfully...",
                    "data": UpdateBlog.data                })
            else:
                return Response({
                    "status": "Error",
                    "data": UpdateBlog.errors
                })
        except:
            return Response("Error")
    

    def delete(self, request):
        try:
            GetBlog = Blogs.objects.get(id=request.data['id'])
            GetBlog.delete()
            return Response({
                "status": "Blog deleted successfully...",
                "data": GetBlog,
            })
        except:
            return Response({
                "status": "Error",
                "data": "No blog found with this id"
            })
        

#getting all blog
class GetAllBlogs(APIView):
    permission_classes = []

    def get(self, request):
        try:
            GetBlogs = Blogs.objects.all().order_by('-id')
            GetBlogs = BlogSerializers(GetBlogs, many=True)
            return Response(GetBlogs.data)
        except:
            return Response("Error")


#getting blog by id
class GetBlogById(APIView):
    permission_classes = []

    def get(self, request, id):
        try:
            GetBlog = Blogs.objects.get(id=id)
            GetBlog = BlogSerializers(GetBlog)
            return Response(GetBlog.data)
        except:
            return Response({
                "status": "Error",
                "data": "No blog found with this id"
            })


# search for blog
class SearchBlog(APIView):
    permission_classes = []

    def get(self, request, key):
        try:
            GetBlog = Blogs.objects.filter(Q(title__contains=key) | Q(content__contains=key))
            GetBlog = BlogSerializers(GetBlog, many=True)
            return Response({
                "key": key,
                "data": GetBlog.data
            
            })
        except:
            return Response({
                "status": "Error",
                "data": "No blog found with this key"
            })
        

# update view count
class UpdateViewCount(APIView):
    permission_classes = []

    def put(self, request, id):
        try:
            GetBlog = Blogs.objects.get(id=id)
            GetBlog.views += 1
            GetBlog.save()
            return Response({
                "status": "View updated successfully...",
                "data": GetBlog.views,
                "ip": request.META['REMOTE_ADDR'],
                "user_agent": request.META['HTTP_USER_AGENT'],
            })
        except:
            return Response({
                "status": "Error",
                "data": "No blog found with this id"
            })


# get blogs by view count
class GetBlogsByView(APIView):
    permission_classes = []

    def get(self, request):
        try:
            GetBlog = Blogs.objects.all().order_by('-views')
            GetBlog = BlogSerializers(GetBlog, many=True)
            return Response(GetBlog.data)
        except:
            return Response("Error")


# get blogs by catagory
class GetBlogsByCatagory(APIView):
    permission_classes = []

    def get(self, request, category):
        try:
            GetBlog = Blogs.objects.filter(catagory=category)
            if len(GetBlog) == 0:
                return Response({
                    "status": "Error",
                    "data": "No blog found with this catagory"
                })
            GetBlog = BlogSerializers(GetBlog, many=True)
            return Response(GetBlog.data)
        except:
            return Response({
                "status": "Error"
            })