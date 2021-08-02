from django.contrib import admin
from .models import product, product_type, role
from .models import user, receipt_status, delivery_type
from .models import receipt
from .models import receipt_has_product


class productAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'amount', 'animal', 'product_type_id')


class product_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class roleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class userAdmin(admin.ModelAdmin):
    list_display = ('id', 'login', 'password', 'name', 'phone', 'address', 'role_id',)


class receipt_statusAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class delivery_typeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class receiptAdmin(admin.ModelAdmin):
    list_display = ('id', 'contact', 'address', 'sum_cost', 'status_id', 'delivery_id', 'user_id',)


class receipt_has_productAdmin(admin.ModelAdmin):
    list_display = ('receipt_id', 'product_id', 'price', 'amount')


admin.site.register(product, productAdmin)
admin.site.register(product_type, product_typeAdmin)
admin.site.register(role, roleAdmin)
admin.site.register(user, userAdmin)
admin.site.register(receipt_status, receipt_statusAdmin)
admin.site.register(delivery_type, delivery_typeAdmin)
admin.site.register(receipt, receiptAdmin)
admin.site.register(receipt_has_product, receipt_has_productAdmin)
