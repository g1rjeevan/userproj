from django.http import Http404
from rest_framework import status, generics
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from category.models import Category
from category.serializers import CategorySerializer
from usermgmt.models import Users


@authentication_classes([])
@permission_classes([])
class CategoryFilterList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    filter_backends = (OrderingFilter,)
    ordering_fields = ('name', 'id', 'is_active', 'users')


@authentication_classes([])
@permission_classes([])
class CategoryList(APIView):
    def get(self, request, format=None):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        users = Users.objects.get(id=request.data['users_id'])
        request.data['users'] = users
        serializer = Category(id=request.data['id'], name=request.data['name'], parent=request.data['parent'],
                              is_featured=request.data['is_featured'], is_active=request.data['is_active'],
                              description=request.data['description'], users=request.data['users'])
        if serializer:
            serializer.save()
            return Response("Added", status=status.HTTP_201_CREATED)
        return Response(serializer, status=status.HTTP_400_BAD_REQUEST)


@authentication_classes([])
@permission_classes([])
class CategoryDetail(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes((AllowAny,))
def get_search(request, param):
    data = Category.objects.all().values(str(param)).order_by(str(param))

    try:
        auth_token, _ = Token.objects.get_or_create(user=request.user)
        if (request.user.is_authenticated):
            status = True
    except:
        return Response({"data": data, 'auth_status': False})

    return Response({"data": data, 'auth_token': auth_token.key, 'auth_status': status})
