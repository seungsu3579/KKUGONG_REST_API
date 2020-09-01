from django.contrib import admin
from django.utils.html import mark_safe
from . import models


@admin.register(models.Tops)
class TopsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Custom Profile", {"fields": ("_id", "brand", "product", "item_url",)},),
    )


@admin.register(models.TopsImage)
class TopsImageAdmin(admin.ModelAdmin):

    """Tops Image Admin Definition"""

    fieldsets = (
        (
            "Custom Profile",
            {"fields": ("_id", "img_url", "img_dir", "vector", "top",)},
        ),
    )

    list_display = ("__str__", "get_thumbnail")

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.img_url}" width=50>')

    get_thumbnail.short_description = "Thumbnail"
