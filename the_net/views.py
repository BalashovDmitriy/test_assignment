from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from the_net.filters import SellerFilter
from the_net.models import Seller
from the_net.serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = SellerFilter
