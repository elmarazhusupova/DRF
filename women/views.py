from rest_framework import generics

from women.models import Category
from women.serializers import CategorySerializer
from .models import Women
from .serializers import WomenSerializer


class WomenAPIList(generics.ListCreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer


class WomenAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializer










class CategoryView(generics.CreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#
