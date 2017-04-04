'''
Created on Apr 1, 2017

@author: phani
'''

import pandas as pd
from nltk.tokenize import word_tokenize

dataframe = pd.read_pickle("C:/Users/phani/Downloads/fintech_cleaned.pkl")
# print(dataframe.head())
df = dataframe[:500]
#df.to_csv('C:/Users/phani/Downloads/data.csv')
tok = df.tweet

import re,string

def strip_links(text):
    link_regex    = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
    links         = re.findall(link_regex, text)
    for link in links:
        text = text.replace(link[0], ', ')
    return text

def strip_all_entities(text):
    entity_prefixes = ['@','#']
    for separator in  string.punctuation:
        if separator not in entity_prefixes :
            text = text.replace(separator,' ')
    words = []
    for word in text.split():
        word = word.strip()
        if word:
            if word[0] not in entity_prefixes:
                words.append(word)
    return ' '.join(words)

gh = []
for t in tok:
    a = strip_all_entities(strip_links(t))
    gh.append(re.sub('[^A-Za-z0-9]+', ' ', a))

#print(gh)

tokenized_docs = [word_tokenize(doc) for doc in gh]
print(tokenized_docs)

from nltk.corpus import stopwords

tokenized_docs_no_stopwords = []
for doc in tokenized_docs:
    new_term_vector = []
    for word in doc:
        if not word in stopwords.words('english'):
            new_term_vector.append(word)
    tokenized_docs_no_stopwords.append(new_term_vector)

print(tokenized_docs_no_stopwords)

