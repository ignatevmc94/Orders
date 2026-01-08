from django.shortcuts import render
from rest_framework import viewsets
from .serializers import ShopSerializer, CategorySerializer, ProductSerializer, ProductInfoSerializer, ParameterSerializer, ProductParameterSerializer, OrderSerializer
from .models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductInfoViewSet(viewsets.ModelViewSet):
    queryset = ProductInfo.objects.all()
    serializer_class = ProductInfoSerializer


class ParameterViewSet(viewsets.ModelViewSet):
    queryset = Parameter.objects.all()
    serializer_class = ParameterSerializer


class ProductParameterViewSet(viewsets.ModelViewSet):
    queryset = ProductParameter.objects.all()
    serializer_class = ProductParameterSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
