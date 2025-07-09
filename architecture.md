# Architecture

## Server/Client roles

| Component              | Handled By  | Reasoning                                                                    |
| ---------------------- | ----------- | ---------------------------------------------------------------------------- |
| Data collection        | **Server**  | Fetch from APIs like yfinance, centralize ingestion                          |
| Feature engineering    | **Server**  | Standardized logic, reproducibility                                          |
| Dataset preparation    | **Server**  | Store preprocessed datasets in a versioned way                               |
| Model training (core)  | **Server**  | For production-grade models                                                  |
| Model experimentation  | **Clients** | For flexibility — users can request a dataset, train, and return predictions |
| Model registry/storage | **Server**  | Saves .pt, metadata, version, metrics                                        |
| Inference for users    | **Server**  | Serve predictions via API                                                    |

