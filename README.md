# Split Data into Train-Validation-Test
 This is created for handling huge data to split it. 
 Especially for huge image dataset with unseperated .csv or .txt label file. 
 - Firstly, we split image dataset folder into two or three folders as training, validation and test using split_folders.py. 
 - Secondly, we split .csv or .txt file according to new train, validation and test folders using DataHandle.py. Thus, we have 3 folders and 3 .csv files. 
 - Now that we have data and its label, we are ready to implement deep learning methods as we desire. 
