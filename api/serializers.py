from rest_framework.serializers import ModelSerializer

from market.models import Index


class IndexSerializer(ModelSerializer):
    class Meta:
        model = Index
        fields = ['id', 'name', 'symbol']

