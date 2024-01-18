from django.contrib import admin

from the_net.models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('title', 'contacts', 'product', 'provider', 'debt', 'create_date')
    list_filter = ('contacts.city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)


admin.site.register(Seller, SellerAdmin)
