from django.contrib import admin
from .models import Lyuk, Dozhdiepriemnik, VodootvodnyyLotok, TrotuarnayaPlitka, Cherepitsa

@admin.register(Lyuk)
class LyukAdmin(admin.ModelAdmin):
    list_display = ('name', 'tip_vesa', 'ves')
    search_fields = ('name',)
    list_filter = ('tip_vesa',)


@admin.register(Dozhdiepriemnik)
class DozhdiepriemnikAdmin(admin.ModelAdmin):
    list_display = ('name', 'vysota', 'ves')
    search_fields = ('name',)


@admin.register(VodootvodnyyLotok)
class VodootvodnyyLotokAdmin(admin.ModelAdmin):
    list_display = ('name', 'vysota', 'ves')
    search_fields = ('name',)


@admin.register(TrotuarnayaPlitka)
class TrotuarnayaPlitkaAdmin(admin.ModelAdmin):
    list_display = ('name', 'razmery', 'kolichestvo_na_km')
    search_fields = ('name',)


@admin.register(Cherepitsa)
class CherepitsaAdmin(admin.ModelAdmin):
    list_display = ('name', 'massa_ryadnoy', 'temperaturnyy_diapazon')
    search_fields = ('name',)