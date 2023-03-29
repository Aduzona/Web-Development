from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Products, User
#from .producer import publish
from .serializers import ProductSerializer
import random

class ProductViewSet(viewsets.ViewSet):


    def list(self,request):
        '''
        List Products
        /api/products get
        '''
        products = Products.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def create(self,request):
        '''
        /api/products  post
        '''
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #publish('product_created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        '''
         /api/products/<str:id>  get

         gets a product with a specific id number.
        '''
        product = Products.objects.get(id=pk)
        # any time a product is retrieved, it must have a serializer.
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self,request,pk=None):
        '''
         /api/products/<str:id>  put
        '''
        product = Products.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self,request,pk=None):
        '''
         /api/products/<str:id>  delete
        '''
        product = Products.objects.get(id=pk)
        product.delete()
        #publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })
