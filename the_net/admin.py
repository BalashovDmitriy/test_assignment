from django.contrib import admin

from the_net.models import Seller, Product, Connector


class ConnectorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Connector._meta.fields]
    actions = ['clear_debt']

    def clear_debt(self, request, queryset):
        queryset.update(debt=0)
        self.message_user(request, 'Успешно')

    clear_debt.short_description = 'Очистить задолженность'


admin.site.register(Seller)
admin.site.register(Product)
admin.site.register(Connector, ConnectorAdmin)
