import django_filters

from the_net.models import Seller


class SellerFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name="country", lookup_expr="icontains")

    class Meta:
        model = Seller
        fields = ("country",)
