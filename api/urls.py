from django.urls import path

from .views import (
    FetchMarketDataView,
    IndexListCreateView,
    MarketDataListCreateView,
    MarketDataRetrieveView,
    MarketDataListView,
    TechnicalIndicatorListView
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
        MarketDataListView.as_view(),
        name='marketdata-list-create'
    ),
    path('marketdata/', MarketDataRetrieveView.as_view(), name='marketdata-retrieve'),
    path(
        'technicalindicators/', 
        TechnicalIndicatorListView.as_view(), 
        name='technical-indicators-list'
    )
]
