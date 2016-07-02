###parse and tf-idf
import nltk
import re
#read the file
allLines = open('foo-Anthony.txt').read()
##char size down
allLines = allLines.lower()
        #print allLines
#seikika
p = re.compile(r'<[^>]*?>')
allLines = p.sub("",allLines)
print allLines
##str->list
#stri = allLines.split()
#print stri
##delete ""
#stri = filter(lambda s:s != '', stri)
#print stri

