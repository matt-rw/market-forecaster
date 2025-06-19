from celery import shared_task
import yfinance as yf

from .models import Index, MarketData


@shared_task
def fetch_market_data():
    for index in Index.objects.all():
        ticker = yf.Ticker(index.symbol)
        hist = ticker.history(period='365d')  # last 30 days of data

        for date, row in hist.iterrows():
            MarketData.objects.update_or_create(
                index=index,
                date=date.date(),
                defaults={
                    'open_price': row['Open'],
                    'high_price': row['High'],
                    'low_price': row['Low'],
                    'close_price': row['Close'],
                    'volume': row['Volume'],
                }
            )
