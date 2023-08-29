from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import BoothData2019Serializer, BoothData2014Serializer
from .models import BoothData2019, BoothData2014


class Poll2019ViewSet(viewsets.ModelViewSet):
    queryset = BoothData2019.objects.all()
    serializer_class = BoothData2019Serializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "__all__"
    search_fields = ["polling_booth_name", "polling_booth_number", "winner_2019"]
    ordering_fields = "__all__"


class Poll2014ViewSet(viewsets.ModelViewSet):
    queryset = BoothData2014.objects.all()
    serializer_class = BoothData2014Serializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = "__all__"
    search_fields = ["polling_booth_name", "polling_booth_number", "winner_2014"]
    ordering_fields = "__all__"
