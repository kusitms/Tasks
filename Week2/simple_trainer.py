import torch
import torch.nn as nn
from torch.utils import data
import numpy as np

class MyDataset(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        if mode == 'train':
            self.df = np.random.randint(20, size=(800, 21))
        elif mode == 'val':
            self.df = np.random.randint(20, size=(200, 21))

        self.features = self.df[:, :20]
        self.labels = self.df[:, -1]
        self.labels = np.expand_dims(self.labels,axis=1)

    def __len__(self):
        return len(self.df)

    def __getitem__(self, index):
        return torch.FloatTensor(self.features[index, :]), torch.FloatTensor(self.labels[index])


class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        linear1 = nn.Linear(20, 10, bias=True)
        linear2 = nn.Linear(10, 10, bias=True)
        linear3 = nn.Linear(10, 1, bias=True)
        relu = nn.ReLU()
        self.model = nn.Sequential(
            linear1, relu, linear2, relu, linear3
        )

    def forward(self, features):
        result = self.model(features)
        return result


class MyTrainer:
    def __init__(self, batch_size, lr, total_epochs):
        self.model = MyModel()
        self.train_dataset = MyDataset(mode='train')
        self.val_dataset = MyDataset(mode='val')
        self.train_datagenerator = data.DataLoader(self.train_dataset, batch_size, drop_last=True)
        self.val_datagenerator = data.DataLoader(self.val_dataset, batch_size, drop_last=True)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr)
        self.loss = nn.MSELoss(reduce=False)
        self.total_epochs = total_epochs

    def update(self, loss):
        self.optimizer.zero_grad()
        loss.mean().backward()
        self.optimizer.step()

    def train(self):
        for epoch in range(self.total_epochs):
            for feature, label in self.train_datagenerator:
                hypothesis = self.model(feature)
                loss = self.loss(hypothesis, label.float())
                self.update(loss)
            if epoch % 10 == 0:
                print('Train -- Epoch: {} Loss: {}'.format(epoch,loss))

            for feature, label in self.val_datagenerator:
                hypothesis = self.model(feature)
                loss = self.loss(hypothesis, label.float())
            if epoch % 10 == 0:
                print('Val -- Epoch: {} Loss: {}'.format(epoch, loss))
                print('')

if __name__ == '__main__':
    trainer = MyTrainer(8, 0.001, 100)
    trainer.train()
