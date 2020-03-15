import torch.nn as nn
from torch.utils import data
import numpy as np

class MyDataset(data.Dataset):
    def __init__(self, mode):
        if mode == 'train':
            self.df = np.random.randint(20, size=(800, 21))
        elif mode == 'val':
            self.df = np.random.randint(20, size=(200, 21))
        self.features = # Implement code here
        self.labels = # Implement code here

        """
            The last column should be the label.
            First 20 columns will be the features(Input to the model)
        """
    
    def __len__(self):
        return len(self.df)
        
    def __getitem__(self, index):
        return torch.FloatTensor(self.features[index, :]), torch.FloatTensor(self.lables[index])
    
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = # Implement code here

        """
            Considering the feature and label constraint mentioned in MyDataset
            Only model input dimension size and output dimension size are fixed.
            Activation function and hidden layer dimensions are free.
        """
        
    def forward(self, features):
        result = self.model(features)
        return result

class MyTrainer:
    def __init__(self, batch_size, lr, total_epochs):
        self.model = MyModel()
        self.train_dataset = MyDataset(mode='train')
        self.val_dataset = MyDataset(mode='val')
        self.train_datagenerator = data.DataLoader(self.train_dataset, batch_size=batch_size)
        self.val_datagenerator = data.DataLoader(self.val_dataset, batch_size=batch_size)
        self.optimizer = torch.optim.Adam(self.model.parameters(), lr=lr)
        self.loss = nn.MSELoss(reduce=False)
        self.total_epochs = total_epochs
    
    def update(self, loss):
        self.optimizer.zero_grad()
        loss.mean().backward()
        self.optimizer.step()

    def train(self):
        for epoch in range(self.epochs):
            for feature, label in self.train_datagenerator:
                """
                    Implement training part.
                """
            for feature, label in self.val_datagenerator:
                """
                    Implement validation part.
                """
        
if __name__ == '__main__':
    """
        Implement code here.
    """