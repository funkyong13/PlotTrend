def Dyn_Curr(CurrFrom, CurrTo):

	#Web Crawling
	import urllib2
	sURL ='https://www.google.com/finance/converter?a=1&from=' + CurrFrom + '&to=' + CurrTo
	html = urllib2.urlopen(sURL)
	ByteData = html.read()
	
	#Crawled data as 1D array of string
	StrData = ByteData.decode("ISO-8859-1").strip().split('\n')
	
	#Extract Currency from the string array
	NumLine = len(StrData)
	for i in range(0,NumLine):
    		if StrData[i][0:34] == '<div id=currency_converter_result>':
        		LineCurrency=StrData[i]

	PosStartText = '<span class=bld>'
	PosEndText = '</span>'
	LenPosStart = len(PosStartText)
	LenPosEnd = len(PosEndText)
	PosStart =(LineCurrency.find(PosStartText) + LenPosStart) - len(LineCurrency)
	PosEnd = LineCurrency.find(PosEndText)-4
	Curr = LineCurrency[PosStart:PosEnd]
	Curr = float(Curr)
	return Curr