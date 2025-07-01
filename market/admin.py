from django.contrib import admin

from .models import Index, MarketData, TechnicalIndicator


@admin.register(Index)
class IndexAdmin(admin.ModelAdmin):
    list_display = ('name', 'symbol')
    search_fields = ('name', 'symbol')


@admin.register(MarketData)
class MarketDataAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'close_price', 'volume')
    list_filter = ('index',)
    search_fields = ('index__name',)


@admin.register(TechnicalIndicator)
class TechnicalIndicatorAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'rsi', 'macd', 'sma_20', 'sma_50')
    list_filter = ('index',)
