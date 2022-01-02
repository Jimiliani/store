from django.contrib import admin
from items.models import Item, ItemImage


class ItemImageInlineAdmin(admin.StackedInline):
    fields = ['image']
    model = ItemImage


class ItemImageAdmin(admin.ModelAdmin):
    fields = ['item', 'image']


class ItemAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'in_stock']
    inlines = [ItemImageInlineAdmin, ]


admin.site.register(Item, ItemAdmin)
admin.site.register(ItemImage, ItemImageAdmin)
