from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Catagory
from django.contrib.auth.models import User
from .serializers import CatagorySerializers , UserSerializers

class Home(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("Hello, World!")
    

# catagory management
class CatagoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        GetCatagory = CatagorySerializers(Catagory.objects.all(), many=True)
        return Response(GetCatagory.data)

    def post(self, request):
        try:
            CatagoryData = CatagorySerializers(data=request.data)
            if CatagoryData.is_valid():
                CatagoryData.save()
                return Response(CatagoryData.data)
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
                return Response(CatagoryData.data)
            else:
                return Response(CatagoryData.errors)
        except:
            return Response("Error")



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
            return Response("User added successfully...")
        except:
            return Response("Error")