from django.contrib import admin
from django.contrib.admin import register
from catalogue.models import Category, Brand, ProductType, Product, ProductAttribute, ProductAttributeValue


class ProductAttributeInline(admin.TabularInline):
    model = ProductAttribute
    extra = 5


@register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("title", "product_type", "upc", "is_active", "category", "brand", "created_at", "modify_at", )
    list_display_links = ("title", "upc", )
    list_filter = ("is_active",)
    search_fields = ("title", "product_type", "upc", "category__name", "brand__name",)
    list_editable = ("is_active",)


@register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "modify_at", )
    list_display_links = ("name", )
    list_filter = ("is_active", )
    search_fields = ("name", "parent", )
    list_editable = ("parent", "is_active", )


@register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "parent", "is_active", "modify_at", )
    list_display_links = ("name", )
    list_filter = ("is_active", )
    search_fields = ("name", "parent", )
    list_editable = ("parent", "is_active", )


@register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "modify_at", )
    list_display_links = ("title", )
    list_filter = ("is_active", )
    search_fields = ("title", )
    inlines = (ProductAttributeInline, )


# @register(ProductAttribute)
# class ProductAttributeAdmin(admin.ModelAdmin):
#     list_display = ("title", "product_type__title", "is_active", "attribute_type", )


@register(ProductAttributeValue)
class ProductAttributeValueAdmin(admin.ModelAdmin):
    list_display = ("product__title", "value", "attribute__title", "is_active", )
