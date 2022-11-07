from rest_framework.decorators import api_view, permission_classes
from helper.mainFunc import createItem, deleteItem, getAllItems, getAllItemsWithoutPagination, getItem, updateItem
from .serializers import ProductSerializer
from product.models import Product




# ################################################### Api ######################################

############################### crud for Product ###########################
@api_view(['POST'])
def createProduct(request):
    return createItem(request,ProductSerializer)

@api_view(['PUT'])
def updateProduct(request, id):
    return updateItem(request=request, model=Product, serializer=ProductSerializer, id=id)

@api_view(['GET'])
def Products(request):
        return getAllItemsWithoutPagination(request=request, model=Product, serializer=ProductSerializer )


@api_view(['GET'])
def getProduct(request, id):
    return getItem(request=request,model=Product, serializer=ProductSerializer ,id=id)

@api_view(['DELETE'])
def deleteProduct(request, id):

    return deleteItem(request=request,model=Product, id=id)

