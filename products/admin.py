from django.contrib import admin
from . models import Product, Shirt

# Register your models here.
class productAdmin(admin.ModelAdmin):
    readonly_fields=("slug",)
    list_display = ("title", "id", "category","is_bestseller")
    list_filter = ("is_bestseller",)
    search_fields = ("title","category","brand")

admin.site.register(Shirt)
admin.site.register(Product, productAdmin)