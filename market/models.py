from django.db import models


class Index(models.Model):
    name = models.CharField(max_length=50)
    symbol = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f'{self.name} ({self.symbol})'


class MarketData(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.FloatField()
    high_price = models.FloatField()
    low_price = models.FloatField()
    close_price = models.FloatField()
    volume = models.BigIntegerField()

    class Meta:
        unique_together = ('index', 'date')
        ordering = ['-date']


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
