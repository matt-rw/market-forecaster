from torch.optim import Adam
from sklearn.metrics import mean_squared_error

import os
import django

from torch.utils.data import DataLoader
import torch.nn as nn
import torch

import sys

sys.path.append("/app")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "market_forecaster.settings")
django.setup()

from ml.lstm_model.dataset import load_datasets
from ml.lstm_model.model import LSTMRegressor

import matplotlib.pyplot as plt

def plot_predictions(val_preds, val_targets, out_path="predictions.png"):
    plt.figure(figsize=(12, 6))
    plt.plot(val_targets, label="Actual", color="blue")
    plt.plot(val_preds, label="Predicted", color="orange")
    plt.title("Predicted vs Actual Closing Prices")
    plt.xlabel("Time Step")
    plt.ylabel("Closing Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(out_path)
    print(f"✅ Saved prediction plot to: {out_path}")
    plt.close()


def train_model(model, train_loader, val_loader, epochs=20, lr=1e-3, device='cpu'):
    optimizer = Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()

    model.to(device)
    
    for epoch in range(epochs):
        model.train()
        train_losses = []
        for x_batch, y_batch in train_loader:
            x_batch, y_batch = x_batch.to(device), y_batch.to(device)

            optimizer.zero_grad()
            preds = model(x_batch)
            loss = loss_fn(preds, y_batch)
            loss.backward()
            optimizer.step()

            train_losses.append(loss.item())

        model.eval()
        val_preds, val_targets = [], []
        with torch.no_grad():
            # Move input and target tensors to CPU
            for x_val, y_val in val_loader:
                x_val, y_val = x_val.to(device), y_val.to(device)
                pred = model(x_val)
                print(f'Prediction: {pred}')
                val_preds.extend(pred.cpu().numpy())
                val_targets.extend(y_val.cpu().numpy())

        # plot_predictions(val_preds, val_targets)

        val_rmse = mean_squared_error(val_targets, val_preds) #, squared=False)
        print(f'Epoch {epoch+1} | Train loss: {sum(train_losses)/len(train_losses):.4f} | Val RMSE: {val_rmse:.4f}')

        torch.save(model.state_dict(), 'ml/lstm_model/trained_lstm.pt')
   

if __name__ == '__main__':
    seq_len = 20
    train_ds, val_ds = load_datasets(seq_len)
    train_loader = DataLoader(train_ds, batch_size=32, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=32)

    model = LSTMRegressor(input_dim=5)
    train_model(model, train_loader, val_loader, epochs=20)
