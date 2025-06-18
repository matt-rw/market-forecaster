from django.contrib import admin

from .models import Index, MarketData


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name', 'symbol')


@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'close_price', 'volume')
    list_filter = ('index',)
    search_fields = ('index__name',)
