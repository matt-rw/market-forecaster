import torch
from torch.utils.data import Dataset

from .preprocessing import load_and_preprocess


class MarketSequenceDataset(Dataset):
    def __init__(self, features, targets, seq_len=20):
        self.features = torch.tensor(features.values, dtype=torch.float32)
        self.targets = torch.tensor(targets, dtype=torch.float32)
        self.seq_len = seq_len

    def __len__(self):
        return len(self.features) - self.seq_len

    def __getitem__(self, idx):
        x_seq = self.features[idx: idx + self.seq_len]
        y = self.targets[idx + self.seq_len]
        return x_seq, y


def load_datasets(seq_len):
    X_train, X_val, y_train, y_val = load_and_preprocess()

    train_ds = MarketSequenceDataset(X_train, y_train, seq_len=seq_len)
    val_ds = MarketSequenceDataset(X_val, y_val, seq_len=seq_len)

    return train_ds, val_ds

