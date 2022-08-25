from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import CryptoSerializer
from main.models import Crypto
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class CryptoListViewset(ListAPIView):
    queryset = Crypto.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CryptoSerializer

class CryptoRetrieveUpdateViewset(RetrieveUpdateAPIView):
    queryset = Crypto.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = CryptoSerializer