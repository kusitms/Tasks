from torch.utils import data
import numpy as np
import pandas as pd

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
        array_TR = np.random.randint(30, size = int(len(self.matrix)*0.7))
        array_TS = np.random.randint(30, size = int(len(self.matrix)*0.2))
        array_VA = np.random.randint(30, size = int(len(self.matrix)*0.1))
        if mode == "val":
            print("------------VALIDATION DATA ", len(array_VA), " 개------------")
            for i in array_VA:
                print(self[i])
        elif mode == "test":
            print("------------TEST DATA ", len(array_TS), " 개------------")
            for i in array_TS:
                print(self[i])
        elif mode == "train":
            print("------------TRAINING DATA ", len(array_TR), " 개------------")
            for i in array_TR:
                print(self[i])
        
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
