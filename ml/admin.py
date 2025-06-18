from django.contrib import admin

from .models import TechnicalIndicator, Forecast


@admin.register(TechnicalIndicator)
class TechnicalIndicatorAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'rsi', 'macd', 'sma_20', 'sma_50')
    list_filter = ('index',)


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'prediction', 'confidence', 'model_version')
    list_filter = ('index', 'model_version')
