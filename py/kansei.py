###parse and tf-idf
import nltk
import re 
#read the file
def parse(x):
        allLines = open(x).read()
##char size down
        allLines = allLines.lower()
        #print allLines
#seikika
        p = re.compile(r'<[^>]*?>')
	allLines = p.sub("",allLines)
#iranai moji kesu
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

collection = nltk.TextCollection(docs)
uniqTerms = list(set(collection))

for doc in docs:
    print "====================" 
    print "%s: %f" % ('julius', collection.tf_idf('julius',doc))
    print "%s: %f" % ('brutus', collection.tf_idf('brutus',doc))
    print "===================="
#     for term in uniqTerms:
#        print "%s : %f" % (term, collection.tf_idf(term, doc))
rank={}
for doc in docs:
    print "=====rank====="
    for term in uniqTerms:
	rank[term]= collection.tf_idf(term,doc)
    i=0
    for k,v in sorted(rank.items(), key=lambda x:x[1], reverse=True):
	print k,v
	i = i+1
	if i==5:
	    break
    print"=====end====="
