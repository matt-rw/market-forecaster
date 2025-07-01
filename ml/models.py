from django.db import models

from market.models import Index


class Forecast(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField()
    prediction = models.FloatField()
    confidence = models.FloatField(null=True, blank=True)
    model_version = models.CharField(max_length=50)

    class Meta:
        unique_together = ('index', 'date', 'model_version')
        ordering = ['-date']
