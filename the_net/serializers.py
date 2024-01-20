from rest_framework import serializers

from the_net.models import Seller


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('level', 'title', 'email', 'country', 'city', 'street', 'house')
        read_only_fields = ('debt',)
