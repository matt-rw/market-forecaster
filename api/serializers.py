from rest_framework.serializers import ModelSerializer

from market.models import Index, MarketData


class IndexSerializer(ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name', 'symbol']


class MarketDataSerializer(ModelSerializer):
    class Meta:
        model = MarketData
        fields = ['index', 'date', 'open_price', 'close_price']

