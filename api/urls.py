from django.urls import path

from .views import (
    FetchMarketDataView,
    IndexListCreateView
)


urlpatterns = [
    path(
        'fetch-market-data/', 
        FetchMarketDataView.as_view(), 
        name='fetch-market-data'
    ),
    path(
        'compute-technical-indicators/',
        FetchMarketDataView.as_view(), 
        name='compute-technical-indicators'
    ),
    path('indexes/', IndexListCreateView.as_view(), name='index-list-create'),
    path(
        'marketdata/',
        MarketDataListCreateView.as_view(),
        name='marketdata-list-create'
    ),
]
