from rest_framework import serializers

from the_net.models import Seller


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('title', 'email', 'country', 'city', 'street', 'house', 'product', 'supplier', 'debt')
        read_only_fields = ('debt',)
