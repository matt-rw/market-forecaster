## Architecture

| Component              | Handled By  | Reasoning                                                                    |
| ---------------------- | ----------- | ---------------------------------------------------------------------------- |
| Data collection        | **Server**  | Fetch from APIs like yfinance, centralize ingestion                          |
| Feature engineering    | **Server**  | Standardized logic, reproducibility                                          |
| Dataset preparation    | **Server**  | Store preprocessed datasets in a versioned way                               |
| Model training (core)  | **Server**  | For production-grade models                                                  |
| Model experimentation  | **Clients** | For flexibility — users can request a dataset, train, and return predictions |
| Model registry/storage | **Server**  | Saves .pt, metadata, version, metrics                                        |
| Inference for users    | **Server**  | Serve predictions via API                                                    |

## CLI Commands

| Command           | Action                              |
|-------------------|-------------------------------------|
| list\_stocks      | Generate list of all saved assets   |
| rsi               | View as plot or table over timespan |
| macd              |                                     |
| price             |                                     |

## Building a Dataset

``export SYMBOL``

## Upload a Model

``upload path/to/model NAME SYMBOL``

``list_models --filter SYMBOL

``pred MODELNAME``



Examples:

``rsi 2 --table --time 2w --interval day``

``macd 1 --plot --time 1y --interval week``

## LSTM Training

Train a LSTM (long short term memory) neural network:

``train 2 --name model-1 --fc sigmoid``
``evaluate model-1``
``predict model-1 --time 1w``


