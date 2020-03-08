# Week1 Assignment

The objective is to make a Dataset using PyTorch and Pandas. Using the appropriate python type is encouraged. According to which type you make use of, your code can be under 10 lines, or can be more than a hundred lines.

## Let's get friendly with Git.

First, make a branch with your full name in this repository `Tasks`. For example, if your name is Piljae Chae, please set the branch name as piljaechae.

Then, clone the branch you have just created. The terminal command will be `git clone -b <YOUR NAME> git@github.com:kusitms/Tasks.git <THE FOLDER NAME YOU DESIRE>`

Then, at the place you typed the command, a new folder named THE FOLDER NAME YOU DESIRE shall appear. Change the skeleton code provided inside the Week1 folder.

When the codes are changed, and your results are satisfactory, you now follow these procedures.

1. `git add <FILE YOU CHANGED>`
(`git add simpledataset.py`)
2. `git commit -m 'ANY MESSAGE YOU WANT TO LEAVE'`
3. `git push`

# What you have to do.

`classscore.csv` is a csv containing the results of 30 students, each with 60 test results. One student, is one data. `MyDataset` is an easy version, and `MyDatasetAdvanced` is advanced version. If you wish to complete this assignment (As completing the assignment is not mandatory), you can only change MyDataset if advanced version is difficult for you. However, completing the advanced version will be very useful for the Team Project.

For `MyDataset` you just have to load the csv file provided, and when `print(mydataset[0])` is executed, the result should be the first whole row of the csv provided.

For `MyDatasetAdvanced` you will have to receive additional arg `mode`. `mode` should be 'train', 'val', or 'test'. The ratio should be 7:1:2. So, when `mode == 'train'`, there should be only 21 rows, and so on. You have to keep in mind that 'train', 'val', 'test' dataset should not have any duplicate rows.

# Due

Friday (3.13)
