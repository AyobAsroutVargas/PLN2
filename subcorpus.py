import spacy
import openpyxl
from pathlib import Path
import numpy as np
import re
import pandas as pd

data = pd.read_excel('COV_train.xlsx', header=None, engine="openpyxl")
data.columns = ["Tweet", "Target"]

is_negative = data["Target"]=="Negative"
is_positive = data["Target"]=="Positive"

tweets = data.iloc[:,0]

negative_tweets = data[is_negative]
positive_tweets = data[is_positive]

negative_list = np.array(negative_tweets.iloc[:,0].tolist())
positive_list = np.array(positive_tweets.iloc[:,0].tolist())


# print(tweets.shape)
# print(negative_list)
print(len(negative_list))

file = open("cropusP.txt", "w+")
file.write("Number of twets: " + str(positive_list.size) + "\n\n")
for word in positive_list:
    file.write(word + "\n")
file.close()

file = open("cropusN.txt", "w+")
file.write("Number of twets: " + str(negative_list.size) + "\n\n")
for word in negative_list:
    file.write(word + "\n")
file.close()