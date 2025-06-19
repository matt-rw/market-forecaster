from torch.optim import Adam
from sklearn.metrics import mean_squared_error


def train_model(model, train_loader, val_loader, epochs=20, lr=1e-3, device='cpu'):
    optimizer = Adam(model.parameters(), lr=lr)
    loss_fn = nn.MSELoss()
