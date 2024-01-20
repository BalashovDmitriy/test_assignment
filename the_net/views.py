from django.shortcuts import render
from rest_framework import viewsets, permissions

from the_net.models import Seller
from the_net.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)

