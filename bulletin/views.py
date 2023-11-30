from django.shortcuts import render
from rest_framework import generics

from bulletin.models import Ad
from bulletin.paginators import AdPaginator
from bulletin.serializers import AdSerializers


class AdListAPIView(generics.ListAPIView):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()
    pagination_class = AdPaginator


class AdCreateAPIView(generics.CreateAPIView):
    serializer_class = AdSerializers


class AdRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()


class AdDestroyAPIView(generics.DestroyAPIView):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()


class AdUpdateAPIView(generics.UpdateAPIView):
    serializer_class = AdSerializers
    queryset = Ad.objects.all()