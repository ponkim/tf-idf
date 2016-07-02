### parse

##read the file
allLines = open('foo-Timon.txt').read()
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
stri= filter(lambda s:s != '', stri)
print stri



