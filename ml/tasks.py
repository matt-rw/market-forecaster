from celery import shared_task

from ml.lstm_model.train import main
# from ml.binary_model.train import main


@shared_task
def train_lstm():
    # seq_len = 20
    # train_ds, val_ds = load_datasets()
    # train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    # val_loader = DataLoader(val_ds, batch_size=32)

    # model = LSTMRegressor(input_dim=5)
    # train_model(model, train_loader, val_loader, epochs=20)
    main()
