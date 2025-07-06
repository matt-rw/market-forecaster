import math
from rest_framework.serializers import ModelSerializer

from market.models import Index, MarketData, TechnicalIndicator


class IndexSerializer(ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name', 'symbol']


class MarketDataSerializer(ModelSerializer):
    class Meta:
        model = MarketData
        fields = [
            'id', 'index_id', 'date', 'open_price', 'high_price',
            'low_price', 'close_price'
        ]


class TechnicalIndicatorSerializer(ModelSerializer):
    class Meta:
        model = TechnicalIndicator
        fields = '__all__'
        #[
        #    'id', 'date', 'rsi', 'macd', 'macd_signal', 'sma_20', 'sma_50'
        #]

    def to_representation(self, instance):
        """Sanitize 'nan' values."""
        data = super().to_representation(instance)
        for key, value in data.items():
            if isinstance(value, float) and (math.isnan(value) or math.isinf(value)):
                data[key] = None
        return data

