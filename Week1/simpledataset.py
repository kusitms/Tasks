from torch.utils import data
import numpy as np
import pandas as pd

data_cs = pd.read_csv('C:/Users/nsd96/final_week1/Week1/classscore.csv',encoding='utf-8')


class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()

        self.sample_array = data_cs

    def __len__(self):
        return len(self.sample_array)

    def __getitem__(self, index):
        item = self.sample_array.iloc[index, :]
        return item


class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        self.sample_array = data_cs
        self.mode = mode
        if mode == 'train':
            self.sample_array = self.sample_array.iloc[:21, :]
        elif mode == 'val':
            self.sample_array = self.sample_array.iloc[21:24, :]
        elif mode == 'test':
            self.sample_array = self.sample_array.iloc[24:, :]
        print(self.sample_array)

    def __len__(self):
        return len(self.sample_array(mode))

    def __getitem__(self, index):
        item = self.sample_array.iloc[index, :]
        return item

if __name__ == '__main__':
    mydataset = MyDataset()
    print(mydataset[0])
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
