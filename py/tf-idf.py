#coding:utf-8

import nltk

docs = [
    ['asita','no','tenki','ha','hare'],
    ['kyo','no','tenki','ha','kumori'],
    ['kino','no','tenki','ha','hare']]

collection = nltk.TextCollection(docs)
uniqTerms = list(set(collection))

for doc in docs:
    print "===================="
    for term in uniqTerms:
        print "%s : %f" % (term, collection.tf_idf(term, doc))
    print "===================="
