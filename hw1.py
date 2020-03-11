from torch.utils import data
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
from operator import eq

Kusitms = pd.read_csv("C:/Users/USER/Desktop/2016726091/KUSITMS/21기/인공지능스터디/1주차/classscore.csv")

class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()
        self.sample_array = Kusitms
        print(self.sample_array)
    def __len__(self):
        return len(self.sample_array)
    def __getitem__(self, index):
        item = self.sample_array.iloc[index, :]
        return item
    
class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        self.sample_array = Kusitms
        
        K_dev, K_test = train_test_split(self.sample_array, test_size=0.2)
        K_train, K_val = train_test_split(K_dev, test_size=0.1)
        
        if eq(mode,'train'):
            print(K_train)
        if eq(mode,'val'):
            print(K_val)
        if eq(mode,'test'):
            print(K_test)
            
    def __len__(self):
        return len(self.sample_array)
    def __getitem__(self, index):
        item = self.sample_array.loc[index, :]
        return item
    
if __name__ == '__main__':
    mydataset = MyDataset()

    print(mydataset[0])
    print()
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    print()
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    print()
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
    print()