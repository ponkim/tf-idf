dic =  {'one':1,'two':2,'three':3,'four':4,'five':5,'sex':6}
i=0
for k,v in sorted(dic.items(), key=lambda x:x[1], reverse=True):
   print k,v
   i=i+1
   if i==3:break
