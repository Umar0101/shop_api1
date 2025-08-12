from django.shortcuts import render

# Create your views here.


from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .permissions import IsAuthorOrAdmin, IsAuthor
from .models import Product
from .serializers import ProductSerializer

class ProductCreateAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ('category', 'customer')
    search_fields = ('title', )


    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'request': self.request})
        return context

class ProductRetriveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly, CustomerPermission]

    def get_permissions(self):
        if self.action == 'destroy':
            return [IsAuthorOrAdmin()]
        elif self.action in ['update', 'partial_update']:
            return [IsAuthor()]
        return [IsAuthenticatedOrReadOnly()]
