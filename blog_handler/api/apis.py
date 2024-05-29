from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Catagory
from .serializers import CatagorySerializers 

class Home(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response("Hello, World!")
    

# catagory management
class CatagoryList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        get_catagory = CatagorySerializers(Catagory.objects.all(), many=True)
        return Response(get_catagory.data)

    def post(self, request):
        CatagoryData = CatagorySerializers(data=request.data)
        if CatagoryData.is_valid():
            CatagoryData.save()
            return Response(CatagoryData.data)
        else:
            return Response(CatagoryData.errors)
    
    def put(self, request):
        CatagoryData = Catagory.objects.get(id=request.data['id'])
        CatagoryData = CatagorySerializers(CatagoryData, data=request.data)
        if CatagoryData.is_valid():
            CatagoryData.save()
            return Response(CatagoryData.data)
        else:
            return Response(CatagoryData.errors)