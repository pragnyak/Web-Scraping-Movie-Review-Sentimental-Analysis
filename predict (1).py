from sklearn.externals import joblib 
from joblib import dump, load   

r=[]

path = r"---insert path of pickle file" + "\\"
clf = load(path + 'pkl_filename')
r = load(path + 'pkl_2')
cv=load(path + 'pkl_3')
import pandas as pd
import numpy as np
df=pd.read_csv(r'---insert path of csv file---')
df=df.dropna(axis=0)
stop=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did','not','now','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']
s='''Although this movie wasn't particularly bad, it's unfortunate that its a complete copy and ripoff of the Japanese movie Battle Royale, which is unfortunate as it was rumored that Battle Royale was going to be remade into an American Film. However, that can't happen anymore as all these little girls will think its copying the Hunger Games when in fact BR came out in 2001. The author of the books should be ashamed of herself and BR should seriously sue the production company for lost potential profit. Hunger Games is a watered down mainstream version of BR and horror fans everywhere will be disappointed that it will never get the chance to be remade, it had true potential to be an extremely disturbing film. Suzanne Collins should be sued, and this issue should be brought to light.'''

import re

s = re.sub(r'\d', '', s)
s = s.lower()
s = re.sub(r'[^\w\s]',' ',s)
s=s.split()
s_t = [x for x in s if x not in stop]
s = ( " ".join(s_t))

r.append(s)
X = cv.fit_transform(r).toarray() 
Y=X[-1].reshape(-1,1)
z=Y.transpose()
Ypredict = clf.predict(z) 
print(Ypredict)