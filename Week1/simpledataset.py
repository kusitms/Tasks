
from torch.utils import data
import numpy as np
import pandas as pd

class MyDataset(data.Dataset):
    def __init__(self):
        super().__init__()
        #self.csv_data = numpy.loadtxt('classsocore'.csv, delimiter=',')
        self.df = pd.read_csv('./classscore.csv')
        #print(self.df.head())
        feature_names = ['Task{}'.format(i) for i in range(1,61)] 
        #print(feature_names)
        #print(self.df)
        #print(self.df['Task1'])
        #print(self.df[feature_names])
        self.lables = self.df[feature_names].to_numpy()
        #print(self.lables)
        
    def __len__(self):
        return len(self.df)
    def __getitem__(self, index):
        return self.lables[index, :]

class MyDatasetAdvanced(data.Dataset):
   def __init__(self, mode):
        super().__init__()
        if mode=='train':
            self.df = pd.read_csv('./classscore.csv',skiprows=0, nrows=21)
        elif mode == 'val':
            self.df = pd.read_csv('./classscore.csv',skiprows=(1,21), nrows=3)
        elif mode == 'test':
            self.df = pd.read_csv('./classscore.csv',skiprows=(1,25), nrows=6)
        feature_names = ['Task{}'.format(i) for i in range(1,61)]
        self.labels=self.df[feature_names].to_numpy()

   def __len__(self):
        return len(self.df)

   def __getitem__(self, index):
       return self.labels[index,:]
       

if __name__ == '__main__':
    mydataset = MyDataset()
    print(mydataset[0])
    #print(mydataset.__getitem__(0)) 
    #data_list = [[1,1,1],[2,2,2],[3,3,3]]
    #arr=np.array(data_list)
    #print(arr)
    
    advanced_dataset_train = MyDatasetAdvanced(mode='train')
    advanced_dataset_val = MyDatasetAdvanced(mode='val')
    advanced_dataset_test = MyDatasetAdvanced(mode='test')
