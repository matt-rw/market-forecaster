from django.contrib import admin

from .models import Forecast


@admin.register(Forecast)
class ForecastAdmin(admin.ModelAdmin):
    list_display = ('index', 'date', 'prediction', 'confidence', 'model_version')
    list_filter = ('index', 'model_version')
