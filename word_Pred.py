#Gagan Talreja
#12-09-2018 10:43 PM

#Imports

import csv,random
from collections import Counter
import time


#This function finds all the occurences of the input in the
#list and suggests all the next words that can occur after the entered word/sentence.

def predict(array,sentence):
    x=len(sentence.split())
    y=[]
    for i in range(len(array)):
        #print(" ".join(l[i:i+x]))
        if((" ".join(array[i:i+x])).lower()==sentence.lower()):
            if(i+x<len(array)-1):
                y.append(array[i+x])
    return dict(Counter(y))

#Calculation of CDF of the sample space of the
#input sentence/word to predict the next word that is to occur
      
def CDF(d):
    s=sum(d.values())
    sp=0
    for k,v in d.items():
        pmf=v/s
        sp=sp+pmf
        d[k]=sp
    return d

#In this function we read the file and call the other
#functions to predict the next n-length(input) words

def process():

    sent=input("Enter sentence or 0 to exit: ")
    while(sent!='0'):
        x=len(sent.split())
        n=int(input("Enter length of sentence: "))
        startTime=time.time()
        file=open("lab4.txt",'r')
        l=file.read().split()
        l=l[:5000:]
        p=""
        out=sent+" "
        for i in range(n-x):
            d=predict(l,sent)
            d=CDF(d)
            #print(d)
            rand=random.uniform(0,1)
            #print(rand)
            try:
                key,val=zip(*d.items())
            except:
                continue
            nge=max(val)
            for j in range(len(val)):
                if(val[j]>=rand):
                    if(val[j]<=nge):
                        nge=val[j]
                        pos=j
            p=key[pos]
            out+=p+" "
            sent=p
        print(out,end="\n\n")
        print("Prediction completed in: ",time.time()-startTime)
        sent=input("\nEnter sentence or 0 to exit: ")

        
st=time.time()
if(__name__=="__main__"):
    process()

print("\n\n****BYE****")
print("You were with us for",time.time()-st,"seconds")
