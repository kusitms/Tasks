# Week2 Assignment

The objective is to train a simple FC (Fully Connected) Model, asserting you have understood the concept of train and validation.

## What you have to do.

`simple_trainer.py` contains 3 part. `MyModel`, `MyDataset`, `MyTrainer`. This week's dataset is also a random generated dataset.

In `MyDatset`, the total dataset is of size 1000. Train and Test dataset are split into ratio of 8 and 2. The last column (the most right column) of the dataset is the label, and the first 20 columns are features. So, in __init__, you should implement self.features and self.labels.

In `MyModel`, you should implement a simple FC Model. Consider the input and label size in `MyDataset`. So, the input dimension and output dimension will be fixed. However, the activation function and hidden layer dimensions are not fixed. These are up to your choice. Feel free.

In `MyTrainer`, you should implement the `train(self)` part. Current implementation is one validation for one train. Keep in mind that train data cause the model to be updated, but validation data should NOT cause the model to be updated.

Show that your model is successfully working by initializing and running your built model at the bottom of your code.

# Due

Friday (3.20)