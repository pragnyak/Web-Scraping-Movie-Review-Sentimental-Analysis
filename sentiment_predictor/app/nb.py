def classifier() :
	from sklearn.externals import joblib 
	from joblib import dump, load   
	import pandas as pd
	import numpy as np

	clf = load('pickle_model.pkl')


	df=pd.read_csv(r'D:\se_miniproject_ml\movie_dataset\naivebayes.csv')
	df=df.dropna(axis=0)

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




