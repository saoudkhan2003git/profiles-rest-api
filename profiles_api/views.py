from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers
# Create your views here.


class HelloAppView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIView feature"""
        an_appview =[
            'User method as function (get, post, patch, put, delete',
            'Gives the most control on the applicatoin logic',
            'Is mapped manually to url',
        ]
        return Response({'message':'Hello','an_appview':an_appview})
    
    def post(self,request):
        """create a hello method with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name= serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({"message":message})
        
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST
                            )

    def put(self,request,pk=None):
        """Handle updating an object"""
        return Response({'methon':'PUT'})
    
    def patch(self,requst,pk=None):
        """handle partial update"""
        return Response({'methond':'PATCH'})
    
    def delete(self,request,pk=None):
        """handle delete an object"""
        return Response({'methohd':'DELETE'})
    
class HelloViewSet(viewsets.ViewSet):
    """Test APIViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self,request):
        """Return a message"""

        a_viewset = [
            'Use actions (list, create, retrieve, update, partial update)',
            'Automatically map to urls using routers',
            'Provide more functionality with less code',
        ]
        return Response({'message':'Hello','a_viewset':a_viewset})
    
    def create(self,request):
        """View Set ceate method"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"Hell {name}!"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self,request,pk=None):
        """Test retrieve method"""
        return Response({'http_method':'retrieve'})
    
    def update(self,request,pk=None):
        """Test update method"""
        return Response({'http_method':'PUT'})
    
    def partial_update(self,request,pk=None):
        """Test partial update"""
        return Response({'http_method':'Patch'})

    def destroy(self,request,pk=None):
        """Test destroy method"""
        return Response({'http_method':'DELETE'})
