from celery import shared_task
import pandas as pd

from market.models import MarketData, Index, TechnicalIndicator


@shared_task
def compute_technical_indicators():
    for index in Index.objects.all():
        qs = MarketData.objects.filter(index=index).order_by('date')
        if qs.count() < 50:
            continue

        df = pd.DataFrame.from_records(qs.values('date', 'close_price'))
        df.set_index('date', inplace=True)
        
        df['sma_20'] = df['close_price'].rolling(window=20, min_periods=20).mean()
        df['sma_50'] = df['close_price'].rolling(window=50, min_periods=50).mean()
        delta = df['close_price'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / loss
        df['rsi'] = 100 - (100 / (1 + rs))

        exp1 = df['close_price'].ewm(span=12, adjust=False).mean()
        exp2 = df['close_price'].ewm(span=26, adjust=False).mean()
        df['macd'] = exp1 - exp2
        df['macd_signal'] = df['macd'].ewm(span=9, adjust=False).mean()

        for date, row in df.iterrows():
            # Uncomment to remove any entries with missing field
            # if any(pd.isna(row[field]) for field in [
            #    'sma_20', 'sma_50', 'rsi', 'macd', 'macd_signal'
            # ]):
            #    continue

            TechnicalIndicator.objects.update_or_create(
                index=index,
                date=date,
                defaults={
                    'sma_20': row['sma_20'],
                    'sma_50': row['sma_50'],
                    'rsi': row['rsi'],
                    'macd': row['macd'],
                    'macd_signal': row['macd_signal'],
                }
            )


@shared_task
def train_lstm():
    seq_len = 20
    train_ds, val_ds = load_datasets()
    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=32)

    model = LSTMRegressor(input_dim=5)
    train_model(model, train_loader, val_loader, epochs=20)
