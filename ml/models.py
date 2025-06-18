from django.db import models

from market.models import Index


class TechnicalIndicator(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField()
    rsi = models.FloatField(null=True, blank=True)
    macd = models.FloatField(null=True, blank=True)
    macd_signal = models.FloatField(null=True, blank=True)
    sma_20 = models.FloatField(null=True, blank=True)
    sma_50 = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ('index', 'date')
        ordering = ['-date']


class Forecast(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField()
    prediction = models.FloatField()
    confidence = models.FloatField(null=True, blank=True)
    model_version = models.CharField(max_length=50)

    class Meta:
        unique_together = ('index', 'date', 'model_version')
        ordering = ['-date']
