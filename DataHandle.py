import numpy as np
import pandas as pd
import os

# Read .csv
data = pd.read_csv('bilgisayarla_goru_season.csv')

# Split data frame.
print(data.head())
category = data.category
seasons = data.season
x = data.drop('season', axis=1)
images = x.drop('category', axis=1)

# Create an empty list.
names = []

# Read the names of all training images.
for dirname, dirnames, filenames in os.walk('C:/Users/hakan/OneDrive/Masaüstü/ESOGÜ/20-21-Güz/Bilgisayarla Görü/Ödev/BilgisayarlaGoru/trainval/train/'):
    for filename in filenames:
        if filename.endswith('.jpg'):
            names.append(filename)

# Drop all rows that does not belong to training dataset. Use set(a) & set(b) or set(a).intersection(b).
training_labels = list(set(data["image"].tolist()) & set(names))

# Get training and test data as data frame.
training_data = data[data["image"].isin(training_labels)]
test_data = data[~data["image"].isin(training_labels)]

print(len(training_data))
print(len(test_data))

# Save data which is split into training and test as .csv.
training_data.to_csv(r"C:/Users/hakan/OneDrive/Masaüstü/ESOGÜ/20-21-Güz/Bilgisayarla Görü/Ödev/BilgisayarlaGoru/trainval/train/train.csv", index = False)
test_data.to_csv(r"C:/Users/hakan/OneDrive/Masaüstü/ESOGÜ/20-21-Güz/Bilgisayarla Görü/Ödev/BilgisayarlaGoru/trainval/val/val.csv", index = False)
