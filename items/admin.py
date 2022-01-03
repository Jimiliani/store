from django.contrib import admin
from django.contrib.auth.models import User, Group
from items.models import Item, ItemImage

admin.site.unregister(User)
admin.site.unregister(Group)


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
