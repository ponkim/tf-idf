###This program is parsing the txt file
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
if __name__=="__main__":
	stri = parse('foo-Othello.txt')
	print stri
