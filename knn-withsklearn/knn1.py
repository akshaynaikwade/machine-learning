p="C:\\Users\\Akshay\\Desktop\\mnist.pkl.gz"
import numpy as np
import pickle
import sklearn
from sklearn.neighbors import KNeighborsClassifier
import gzip
with gzip.open(p,'rb') as f:
    u=pickle._Unpickler(f)
    u.encoding='latin1'
    data=u.load()
train,valid,test=data
trainx,trainy=train
testx,testy=test
clf=KNeighborsClassifier()
clf.fit(trainx[0:30000],trainy[0:30000])
clf.score(testx,testy)
