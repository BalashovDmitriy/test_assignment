from django.contrib import admin

from the_net.models import Seller, Product


class SellerAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'email', 'country', 'city', 'street', 'house', 'product', 'supplier', 'debt', 'create_date')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product)