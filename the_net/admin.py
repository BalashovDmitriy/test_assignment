from django.contrib import admin

from the_net.models import Seller, Product


class SellerAdmin(admin.ModelAdmin):
    readonly_fields = ('level',)
    list_display = ('title', 'supplier', 'email', 'country', 'city', 'street', 'house', 'debt', 'level')
    list_filter = ('city',)
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, f'Задолженность погашена')

    clear_debt.short_description = 'Погасить задолженность'


admin.site.register(Seller, SellerAdmin)
admin.site.register(Product)
