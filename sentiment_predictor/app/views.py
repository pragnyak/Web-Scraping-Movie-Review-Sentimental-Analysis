from django.shortcuts import render
import requests 
from django.http import HttpResponse
from django import forms

def classifier(request):
	if request.method == 'POST':
		from sklearn.externals import joblib 
		from joblib import dump, load   
		r=[]

		s=str(request.POST.get('review'))
		print(s)
		path = r"C:\Users\Smruti\Desktop\pickle" + "\\"
		clf = load(path + 'pkl_filename')
		r = load(path + 'pkl_2')
		cv=load(path + 'pkl_3')
		import pandas as pd
		import numpy as np
		stop=['ourselves','hers','between','yourself','but','again','there','about','once','during','out','very','having','with','they','own','an','be','some','for','do','its','yours','such','into','of','most','itself','other','off','is','s','am','or','who','as','from','him','each','the','themselves','until','below','are','we','these','your','his','through','don','nor','me','were','her','more','himself','this','down','should','our','their','while','above','both','up','to','ours','had','she','all','no','when','at','any','before','them','same','and','been','have','in','will','on','does','yourselves','then','that','because','what','over','why','so','can','did','not','now','under','he','you','herself','has','just','where','too','only','myself','which','those','i','after','few','whom','t','being','if','theirs','my','against','a','by','doing','it','how','further','was','here','than']

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
		y=int(Ypredict[0])

		if y==0:
			sen="Negative"
		elif y==1:
			sen="Positive"

		my_dict = {'insert_me': sen }
	else:
		my_dict = {'insert_me': ' ' }
	return render(request,'app/home.html',context=my_dict)

	