from torch.utils import data
import numpy as np
import pandas as pd

class MyDataset(data.Dataset):
    
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv("classscore.csv")
        
    def __len__(self):
        return self.df.shape[0]
        
    def __getitem__(self, index):
        item = self.df.loc[index]
        return item

class MyDatasetAdvanced(data.Dataset):
    
    def __init__(self, mode):
        super().__init__()
        self.df = pd.read_csv("classscore.csv")
        
        if mode == 'train':
            self.df2 = self.df.sample(frac=0.7)
            
        elif mode == 'val':
            self.df2 = self.df.sample(frac=0.1)
            
        elif mode == 'test':
            self.df2 = self.df.sample(frac=0.2)
        
        else:
            print("다시")
            
    def __len__(self):
        return self.df2.shape[0] 
    
    def __getitem__(self, index):
        item = self.df2.loc[index]
        return item




if __name__ == '__main__':
    mydataset = MyDataset()
    print(mydataset[0])
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
