import pandas as pd
import numpy as np
import pickle

df=pd.read_csv(r'----insert path of csv file-----')
df=df.drop(columns=['label'])
labels=[]
for i in range(0,len(df.index)):
    if 0<int(df.iloc[i]['rating'])<=5:
        labels.append('0')
    elif 6<=int(df.iloc[i]['rating'])<=10:
        labels.append('1')
    
df['label']=labels

import string
df['review'] = df['review'].str.replace("[^a-zA-Z#]", " ")
df['review'] = df['review'].apply(lambda x: ' '.join([w for w in x.split() if len(w)>2]))
import nltk
nltk.download('punkt')
df['review'] = df['review'].str.lower()
import nltk
df['review'] = df.apply(lambda row: nltk.word_tokenize(row['review']), axis=1)
stop=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did','not','now','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']
l1=[]
for i in range(0,len(df.index)):
    l=df.iloc[i]['review']
    l = [x for x in l if x not in stop]
    joined_words = ( " ".join(l))
    l1.append(joined_words)
df['Clean_Rev']=l1
df=df.drop(columns=['rating', 'review'])

r=[]
l=[]
for i in range(0,len(df.index)):
    r.append(df.iloc[i]['Clean_Rev'])
    l.append(df.iloc[i]['label'])

from sklearn.feature_extraction.text import CountVectorizer 
cv = CountVectorizer(max_features =5000)

X = cv.fit_transform(r).toarray() 
y = df.iloc[:, -2].values

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size = 0.25,random_state=0) 

from sklearn.naive_bayes import MultinomialNB 
from sklearn.metrics import confusion_matrix 

classifier = MultinomialNB(); 
classifier.fit(X_train, y_train)

path = r"----insert path of pickle file--- " + "\\"

with open(path + 'pkl_2', 'wb') as f:  
    pickle.dump(r, f)

with open(path + 'pkl_filename', 'wb') as file:  
    pickle.dump(classifier, file)
    
with open(path + 'pkl_3', 'wb') as f1:  
    pickle.dump(cv, f1)

