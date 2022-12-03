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


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(ContactFormModelMixin, ContactFormModelMixinAdmin)