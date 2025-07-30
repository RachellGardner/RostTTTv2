from django.contrib import admin
from django.utils.html import format_html
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import (
    Lyuk, Dozhdiepriemnik, VodootvodnyyLotok,
    Kryshki, Koltsa, KonusnyePerehody,
    ProductImage
)


class ProductImageInline(GenericTabularInline):
    model = ProductImage
    extra = 1
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)
    verbose_name = "Изображение"
    verbose_name_plural = "Изображения"

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 100px; max-width: 100px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Предпросмотр'


class BaseProductAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    readonly_fields = ('image_preview',)
    inlines = [ProductImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" />', obj.image.url)
        return "Нет изображения"
    image_preview.short_description = 'Превью'


@admin.register(Lyuk)
class LyukAdmin(BaseProductAdmin):
    list_display = ('name', 'tip_vesa', 'ves', 'image_preview')
    list_filter = ('tip_vesa',)


@admin.register(Dozhdiepriemnik)
class DozhdiepriemnikAdmin(BaseProductAdmin):
    list_display = ('name', 'vysota', 'ves', 'image_preview')


@admin.register(VodootvodnyyLotok)
class VodootvodnyyLotokAdmin(BaseProductAdmin):
    list_display = ('name', 'vysota', 'ves', 'image_preview')


@admin.register(Kryshki)
class KryshkiAdmin(BaseProductAdmin):
    list_display = ('name', 'tip', 'razmer', 'image_preview')
    list_filter = ('tip',)


@admin.register(Koltsa)
class KoltsaAdmin(BaseProductAdmin):
    list_display = ('name', 'tip', 'vnutrenniy_diametr', 'image_preview')
    list_filter = ('tip',)


@admin.register(KonusnyePerehody)
class KonusnyePerehodyAdmin(BaseProductAdmin):
    list_display = ('name', 'diametr_verhniy', 'diametr_nizhniy', 'image_preview')
