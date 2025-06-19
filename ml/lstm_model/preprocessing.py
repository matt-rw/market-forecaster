import pandas as pd
from sklearn.model_selection import train_test_split


from market.models import MarketData
from ml.models import TechnicalIndicator



def load_and_preprocess(index_id=1):
    market_qs = MarketData.objects.filter(index_id=index_id).order_by('date')
    tech_qs = TechnicalIndicator.objects.filter(index_id=index_id).order_by('date')
    
    market_df = pd.DataFrame.from_records(market_qs.values('date', 'close_price'))
    tech_df = pd.DataFrame.from_records(tech_qs.values(
        'date', 'rsi', 'macd', 'macd_signal', 'sma_20', 'sma_50'
    ))

    df = market_df.merge(tech_df, on='date').dropna()

    df['target'] = df['close_price'].shift(-1)
    df = df[:-1]  # drop last row with NaN target

    features = df[['rsi', 'macd', 'macd_signal', 'sma_20', 'sma_50']]
    targets = df['target'].values

    # time-based split without shuffling
    X_train, X_val, y_train, y_val = train_test_split(
        features, targets, test_size=0.2, shuffle=False
    )
    
    return X_train, X_val, y_train, y_val
