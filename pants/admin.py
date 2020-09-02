from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Pants)
class PantsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("id", "brand", "product", "item_url",)},),
    )


@admin.register(models.PantsImage)
class PantsImageAdmin(admin.ModelAdmin):

    """Pants Image Admin Definition"""

    fieldsets = (("Custom Profile", {"fields": ("id", "img_url", "img", "pants",)},),)

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.img_url}" width=50>')

    get_thumbnail.short_description = "Thumbnail"
