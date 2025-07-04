from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status

from market.tasks import compute_technical_indicators, fetch_market_data
from market.models import Index, MarketData
from .serializers import IndexSerializer, MarketDataSerializer


class FetchMarketDataView(APIView):
    def post(self, request):
        task = fetch_market_data.delay()
        data = {
            'message': 'Task queued',
            'task_id': task.id
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)


class ComputeTechnicalIndicatorsView(APIView):
    def post(self, request):
        task = compute_technical_indicators.delay()
        data = {
            'message': 'Task queued',
            'task_id': task.id
        }
        return Response(data, status=status.HTTP_202_ACCEPTED)


class IndexListCreateView(ListCreateAPIView):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer


class MarketDataListCreateView(ListCreateAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['index',]


class MarketDataRetrieveView(RetrieveAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer

