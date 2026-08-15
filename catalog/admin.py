from django.contrib import admin

from .models import Product, ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "is_active", "display_order", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_active", "display_order")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("display_order", "name")


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "brand",
        "category",
        "is_active",
        "featured",
        "display_order",
        "updated_at",
    )
    list_filter = ("is_active", "featured", "category", "brand", "created_at")
    search_fields = ("name", "brand", "short_description", "description")
    prepopulated_fields = {"slug": ("name",)}
    list_editable = ("is_active", "featured", "display_order")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("display_order", "name")
