from torch.utils import data
import numpy as np
import pandas as pd

class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()
        #self.data = pd.read_csv("classscore.csv", index_col=0).to_dict(orient='records')
        self.data = pd.read_csv("classscore.csv")
        
    def __len__(self):
        return len(self.data)
        
    def __getitem__(self, index):
        item = self.data.loc[index]
        return item

class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        self.data = pd.read_csv("classscore.csv")
        if mode == 'train':
            self.data2 = self.data.sample(frac=0.7)
        if mode == 'val':
            self.data2 = self.data.sample(frac=0.1)
        if mode == 'test':
            self.data2 = self.data.sample(frac=0.2) 
        
    def __len__(self):
        return len(self.data2)
        
    def __getitem__(self, index):
        item = self.data2.iloc[index]
        return item
                

if __name__ == '__main__':
    mydataset = MyDataset()
    print(mydataset[0])
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
