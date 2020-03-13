from torch.utils import data
import numpy as np
import pandas as pd
import random as rd

class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()
        self.matrix = pd.read_csv(r'C:\Users\dgfghsjd\Desktop\Week1\classscore.csv')
        #print(self.matrix)
        
    def __len__(self):
        return len(self.matrix)
        
    def __getitem__(self, index):
        item = self.matrix.iloc[index, : ]
        return item

class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        self.matrix = pd.read_csv(r'C:\Users\dgfghsjd\Desktop\Week1\classscore.csv')
        self.mode = mode

        if mode == "val":
            print("------------VALIDATION DATA ", int(len(self.matrix) * 0.1), " 개------------")
            for i in range( int(len(self.matrix) * 0.1)):
                print(self[ np.random.randint(30)])
        elif mode == "test":
            print("------------TEST DATA ", int(len(self.matrix) * 0.2), " 개------------")
            for i in range( int(len(self.matrix) * 0.2)):
                print(self[np.random.randint(30)])
        elif mode == "train":
            print("------------TRAINING DATA ", int(len(self.matrix) * 0.7), " 개------------")
            for i in range( int(len(self.matrix) * 0.7)):
                print(self[np.random.randint(30)])
        
    def __len__(self):
        return len(self.matrix)
    
    def __getitem__(self, index):
        item = self.matrix.iloc[index, : ]
        return item
        
if __name__ == '__main__':
    mydataset = MyDataset()
    print(mydataset[0])
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
