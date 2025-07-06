from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status

from market.tasks import compute_technical_indicators, fetch_market_data
from market.models import Index, MarketData, TechnicalIndicator
from .serializers import IndexSerializer, MarketDataSerializer, TechnicalIndicatorSerializer


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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name',]


class MarketDataListCreateView(ListCreateAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['index',]


class MarketDataListView(ListAPIView):
    serializer_class = MarketDataSerializer
    
    def get_queryset(self):
        queryset = MarketData.objects.all()
        index = self.request.query_params.get('index')
        if index:
            queryset = queryset.filter(index__id=int(index))
        return queryset


class MarketDataRetrieveView(RetrieveAPIView):
    queryset = MarketData.objects.all()
    serializer_class = MarketDataSerializer


class TechnicalIndicatorListView(ListAPIView):
    serializer_class = TechnicalIndicatorSerializer

    def get_queryset(self):
        task = compute_technical_indicators.delay()
        output = task.get()  # blocking
        queryset = TechnicalIndicator.objects.all()
        index = self.request.query_params.get('index')
        print(index)
        if index:
            queryset = queryset.filter(index__id=int(index))
        return queryset
