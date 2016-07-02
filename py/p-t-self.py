# -*- coding: utf-8 -*-
import nltk
import math
import re

###parse and tf-idf
#read the file
def parse(x):
        allLines = open(x).read()
##char size down
        allLines = allLines.lower()
        #print allLines

##replace unnecessary terms
        allLines = allLines.replace("<","")
        allLines = allLines.replace(">","")
        allLines = allLines.replace("/","")
        allLines = allLines.replace(",","")
        allLines = allLines.replace("!","")
        allLines = allLines.replace(".","")
        allLines = allLines.replace("?","")
        allLines = allLines.replace(":","")
        allLines = allLines.replace(";","")
        allLines = allLines.replace("%","")
        allLines = allLines.replace("'"," ")

##str->list
        stri = allLines.split()
#print stri
##delete ""
        stri = filter(lambda s:s != '', stri)
        return stri

##### tf-idf
def tf_idf_manual(docs):
    tf = {}
    total_token = 0
    df = {}
    total_document = 0
    for doc in docs:
        total_document += 1
        df_list = []
        for token in doc:
            total_token += 1
            tf.setdefault(token, 0)
            tf[token] += 1
            if token not in df_list:
                df.setdefault(token, 0)
                df[token] += 1
                df_list.append(token)

    tfidf = {}
    for k, v in tf.items():
        TF = float(v) / total_token
        IDF = math.log(float(total_document) / df[k])
        tfidf[k] = TF * IDF

    # ソートして出力
    return sorted(tfidf.items(), key=lambda x:x[1])

if __name__=="__main__":
	anth = parse('foo-Anthony.txt')
	cori = parse('foo-Corio.txt')
	haml = parse('foo-Hamlet.txt')
	juli = parse('foo-Julius.txt')
	king = parse('foo-King.txt')
	macb = parse('foo-Macbeth.txt')
	othe = parse('foo-Othello.txt')
	rome = parse('foo-Romeo.txt')
	timo = parse('foo-Timon.txt')
	titu = parse('foo-Titus.txt')

docs = [anth,cori,haml,juli,king,macb,othe,rome,timo,titu]
result = tf_idf_manual(docs)
print result
