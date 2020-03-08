from torch.utils import data
import numpy as np

class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()
        ```
        Your code should be written here
        ```
    def __len__(self):
        ```
        Your code should be written here
        ```
    def __getitem__(self, index):
        ```
        Your code should be written here
        ```

class MyDatasetAdvanced(data.Dataset):
    def __init__(self, mode):
        super().__init__()
        ```
        Your code should be written here
        ```
    def __len__(self):
        ```
        Your code should be written here
        ```
    def __getitem__(self, index):
        ```
        Your code should be written here
        ```

if __name__ == '__main__':
    mydataset = MyDataset()
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
