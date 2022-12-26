from django.contrib import admin
from .models import Category, ContactFormModelMixin, Product, Order, Cart



class ContactFormModelMixinAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'subject',
                    'message', 'cc_myself', 'date_sent')
    list_filter = ('full_name', 'email', 'subject',
                   'message', 'cc_myself', 'date_sent')
    search_fields = ('full_name', 'email', 'subject',
                     'message', 'cc_myself', 'date_sent')
    ordering = ('full_name', 'date_sent', 'email',
                'subject', 'message', 'cc_myself')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('name', 'slug')
    search_fields = ('name', 'slug')
    ordering = ('name', 'slug')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'stock',)
    list_filter = ('name', 'slug', 'price', 'stock',)
    search_fields = ('name', 'slug', 'price', 'stock',)
    ordering = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(ContactFormModelMixin, ContactFormModelMixinAdmin)


'''
class ProductRessource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'slug', 'price', 'image', 'category__name', 'available')
        export_order = ('id', 'name', 'description', 'slug', 'price', 'image', 'category__name', 'available')

'''