from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline
from .models import Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, Kryshki, Koltsa, KonusnyePerehody, ProductImage

class ProductImageInline(GenericTabularInline):
    model = ProductImage
    extra = 3
    fields = ('image', 'image_preview')
    readonly_fields = ('image_preview',)

    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 100px; max-width: 100px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Предпросмотр'
    image_preview.allow_tags = True

@admin.register(Lyuk)
class LyukAdmin(admin.ModelAdmin):
    list_display = ('name', 'tip_vesa', 'ves', 'image_preview')
    search_fields = ('name',)
    list_filter = ('tip_vesa',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True

@admin.register(Dozhdiepriemnik)
class DozhdiepriemnikAdmin(admin.ModelAdmin):
    list_display = ('name', 'vysota', 'ves', 'image_preview')
    search_fields = ('name',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True

@admin.register(VodootvodnyyLotok)
class VodootvodnyyLotokAdmin(admin.ModelAdmin):
    list_display = ('name', 'vysota', 'ves', 'image_preview')
    search_fields = ('name',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True

@admin.register(Kryshki)
class KryshkiAdmin(admin.ModelAdmin):
    list_display = ('name', 'tip', 'razmer', 'image_preview')
    search_fields = ('name',)
    list_filter = ('tip',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True

@admin.register(Koltsa)
class KoltsaAdmin(admin.ModelAdmin):
    list_display = ('name', 'tip', 'vnutrenniy_diametr', 'image_preview')
    search_fields = ('name',)
    list_filter = ('tip',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True

@admin.register(KonusnyePerehody)
class KonusnyePerehodyAdmin(admin.ModelAdmin):
    list_display = ('name', 'diametr_verhniy', 'diametr_nizhniy', 'image_preview')
    search_fields = ('name',)
    inlines = [ProductImageInline]
    
    def image_preview(self, obj):
        if obj.image:
            return '<img src="{}" style="max-height: 50px; max-width: 50px;" />'.format(obj.image.url)
        return "No image"
    image_preview.short_description = 'Превью'
    image_preview.allow_tags = True