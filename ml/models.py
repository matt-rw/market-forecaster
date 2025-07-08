from django.db import models

from market.models import Index


class MLModel(models.Model):
    name = models.CharField(max_length=50)
    version = models.CharField(max_length=20)
    # TODO: allow full export/delete so client can store model/dataset locally
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    trained_at = models.DateTimeField(auto_now_add=True)
    metrics = models.JSONField(default=dict)
    path = models.FilePathField(path='stored_models', recursive=True)


class Forecast(models.Model):
    index = models.ForeignKey(Index, on_delete=models.CASCADE)
    date = models.DateField()
    prediction = models.FloatField()
    confidence = models.FloatField(null=True, blank=True)
    model_version = models.CharField(max_length=50)

    class Meta:
        unique_together = ('index', 'date', 'model_version')
        ordering = ['-date']
