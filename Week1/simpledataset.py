from torch.utils import data
import numpy as np
import pandas as pd

class_score = pd.read_csv('C:/Users/nsd96/final_week1/Week1/classscore.csv',encoding='utf-8')


class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()

        self.sample_array = class_score

    def __len__(self):
        return len(self.sample_array)

    def __getitem__(self, index):
        item = self.sample_array.iloc[index, :]
        return item


class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        self.sample_array = class_score
        self.mode = mode
        if mode == 'train':
            self.sample_array = self.sample_array.sample(frac=0.7, replace=True, random_state=1)
        elif mode == 'val':
            self.sample_array = self.sample_array.sample(frac=0.1, replace=True, random_state=1)
        elif mode == 'test':
            self.sample_array = self.sample_array.sample(frac=0.2, replace=True, random_state=1)
        print('{} Data is \n {}'.format(mode, self.sample_array))

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
