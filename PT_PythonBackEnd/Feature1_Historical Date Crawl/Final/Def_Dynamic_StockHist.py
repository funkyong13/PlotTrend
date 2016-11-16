def Dyn_StockHist(sCompCode):
	import requests
	import datetime

	url = 'http://ichart.finance.yahoo.com/table.csv?s={}&c=2005'.format(sCompCode)
	response = requests.get(url)
	table = [line.split(',') for line in response.content.decode().strip().split('\n')]

	headers = table[0]
	data = table[1:]
	series = {}

	for entry in data:
    		entry[0] = datetime.datetime.strptime(entry[0], "%Y-%m-%d")
    		entry[1:] = [float(n) for n in entry[1:]]

	    	for key, value in zip(headers, entry):
        		if key not in series:
            			series[key] = [value]
        		else:
            			series[key].append(value)


	Date = series.pop('Date')
	Price = series.pop('Adj Close')
	Vol = series.pop('Volume')

	return Date, Price, Vol