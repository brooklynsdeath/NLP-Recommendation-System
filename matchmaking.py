# -*- coding: utf-8 -*-
"""newrec12.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1noFgPTjqhxZtW19vHZBayln-YNG5iuQ9
"""

#importing libraries
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import sys

#importing data and preprocessing the data
interest = sys.argv[1]
interest1 = pd.read_csv('samcsvfinal.csv')
interest1 = interest1.fillna("")
df = interest1.drop(['__v', 'password', 'email', 'lastname', 'firstname'], axis=1)
df = interest1.drop(['Unnamed: 0'], axis =1)
#b = df['_id'].tolist()
#df

'''pd.set_option('display.max_columns', 100)
#df = pd.read_csv('dataset.csv')

#df = df[['Title','Genre','Director','Actors','Plot']]

# initializing the new column
df['Key_words'] = ""

for index, row in df.iterrows():
    plot = row['Plot']
    
    # instantiating Rake, by default is uses english stopwords from NLTK
    # and discard all puntuation characters
    r = Rake()

    # extracting the words by passing the text
    r.extract_keywords_from_text(plot)

    # getting the dictionary whith key words and their scores
    key_words_dict_scores = r.get_word_degrees()
    
    # assigning the key words to the new column
    row['Key_words'] = list(key_words_dict_scores.keys())

'''

#seting user id to index column
df.set_index('_id', inplace = True)

#creating bag of words of interest 
df['bag_of_words'] = ''
columns = df.columns
for index, row in df.iterrows():
    words = ''
    for col in columns:
        if col != 'Director':
            words = words + row[col]+ ' '
        else:
            words = words + row[col]+ ' '
    row['bag_of_words'] = words
    
df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)

# instantiating and generating the count matrix
count = TfidfVectorizer()
count_matrix = count.fit_transform(df['bag_of_words'])

# creating a Series for the interest id so they are associated to an ordered numerical
# list I will use later to match the indexes
indices = pd.Series(df.index)
indices[:5]

cosine_sim = cosine_similarity(count_matrix, count_matrix)
cosine_sim

def recommendations(title, cosine_sim = cosine_sim):
    
    recommended_user = []
    
    # gettin the index of the interest that matches the title(id)
    idx = indices[indices == title].index[0]

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[idx]*100).sort_values(ascending = False)
    print(score_series.iloc[1:15])
    # getting the indexes of the 10 most similar interest
    top_30_indexes = list(score_series.iloc[1:15].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_30_indexes:
        recommended_user.append(list(df.index)[i])
        
    return recommended_user




fr = sys.argv[2]
fw = open("op.txt",'w')
title = 45

#title = title[:-1]

z = recommendations(title)

for x in range(len(z)):
    #fw.write(str(z[x]) + "\n")
    print(z[x])