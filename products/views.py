from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from django.shortcuts import render
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["type", "manufacturer", "in_stock"]
    search_fields = ["name"]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


def phones_view(request):
    phones = Product.objects.filter(type="phone")
    return render(request, "products/phones.html", {"products": phones})
