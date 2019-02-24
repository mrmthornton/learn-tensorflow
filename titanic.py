import numpy as np
import tflearn

# download the dataset
from tflearn.datasets import titanic
titanic.download_dataset('titanic_dataset.csv')

#load file, first column is labels
from tflearn.data_utils import load_csv
data, labels = load_csv('titanic_dataset.csv', target_column=0, categorical_labels=True, n_classes=2)


#data cleaning
def preprocess(data, columns_to_ignore):

