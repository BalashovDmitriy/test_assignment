from rest_framework import serializers

from the_net.models import Seller


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ('title', 'contacts', 'product', 'provider', 'debt')
        read_only_fields = ('debt',)
