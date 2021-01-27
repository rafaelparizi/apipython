import pandas as pd
from pandas import read_excel
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
!pip install xlrd

def constructorData():
    pd.set_option('display.max_columns', 100)
    df = read_excel('parcial.xlsx')
    df.rename(columns={"Unnamed: 0": "Definicao", "Unnamed: 1":"When to use","Unnamed: 2": "How to use", "Unnamed: 3":"Caracteristicas","Unnamed: 4":"Caracteristicas 2", "Unnamed: 5":"Modelo", "Unnamed: 6":"Tecnicas sugeridas"})
    df = df[['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
    df.set_index('Unnamed: 0', inplace = True)

    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            words = words + str(row[col])+ ' '
        row['bag_of_words'] = words
    
    df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)
    tf = TfidfVectorizer()
    tfidf_matrix = tf.fit_transform(df['bag_of_words'])

    indices = pd.Series(df.index)
    indices[:6]

    # gerando  a matrix de similaridade do cosseno
    return cosine_similarity(tfidf_matrix , tfidf_matrix )

def constructorData2():
    pd.set_option('display.max_columns', 100)
    df = read_excel('parcial.xlsx')
    df.rename(columns={"Unnamed: 0": "Definicao", "Unnamed: 1":"When to use","Unnamed: 2": "How to use", "Unnamed: 3":"Caracteristicas","Unnamed: 4":"Caracteristicas 2", "Unnamed: 5":"Modelo", "Unnamed: 6":"Tecnicas sugeridas"})
    df = df[['Unnamed: 0','Unnamed: 1','Unnamed: 2','Unnamed: 3','Unnamed: 4','Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7']]
    df.set_index('Unnamed: 0', inplace = True)

    df['bag_of_words'] = ''
    columns = df.columns
    for index, row in df.iterrows():
        words = ''
        for col in columns:
            words = words + str(row[col])+ ' '
        row['bag_of_words'] = words
    
    df.drop(columns = [col for col in df.columns if col!= 'bag_of_words'], inplace = True)
    tf = TfidfVectorizer()
    tfidf_matrix = tf.fit_transform(df['bag_of_words'])

    return pd.Series(df.index)

def getCosine():
    return constructorData()

def getIndice():
    return constructorData2()
