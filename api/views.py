from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from market.tasks import fetch_market_data
from ml.tasks import compute_technical_indicators


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

