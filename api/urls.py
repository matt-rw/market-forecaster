from django.urls import path
from .views import FetchMarketDataView


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
    )
]
