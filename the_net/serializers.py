from rest_framework import serializers

from the_net.models import Seller, Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title', 'model', 'release_date', 'seller')


class SupplierSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = ('title', 'supplier', 'email', 'country', 'city', 'street', 'house', 'debt', 'products')
