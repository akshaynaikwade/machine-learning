p="C:\\Users\\Akshay\\Desktop\\mnist.pkl.gz"
import numpy as np
import pickle
import gzip
with gzip.open(p,'rb') as f:
    u=pickle._Unpickler(f)
    u.encoding='latin1'
    data=u.load()
train,valid,test=data
trainx,trainy=train
testx,testy=test
t=0
f=0
for k in range(0,20):
    l=[]
    for i in range(0,30000):
        d=0
        for j in range(0,len(trainx[0])):
            d=d+abs(testx[k][j]-trainx[i][j])
        l.append(d)
    ind=l.index(min(l))
    if trainy[ind]==testy[k]:
        t=t+1
        print(trainy[ind],"\t",testy[k],'true')
    else:
        f=f+1
        print(trainy[ind],"\t",testy[k],'false')
print('accuracy=',(t/(t+f))*100)
