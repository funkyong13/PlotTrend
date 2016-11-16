import requests
from datetime import datetime

def pt_collect_HistoricalStock(sCompanyCode):
    # PLOT TREND WEB-APP DEVELOPMENT
    # Function Overview for "pt_get_stock"
    # Purpose: This function serves to collect stock price data from 'Yahoo Finance'
    # Input = The string containing the company's stock code. Ex) "AAPL"
    # Output = 1D arrays for 'date', 'stock price', 'traded volume.'
    # 1. Downloading CSV data from Yahoo Finance =======================================================================

    sURL = 'http://ichart.finance.yahoo.com/table.csv?s=' + sCompanyCode
    sStock_data_collected = requests.get(sURL) # CSV data is saved in sStock_data_collected

    # 2. Placing the collected data into an array ======================================================================
    sData_array = [line.split(',') for line in sStock_data_collected.content.decode().strip().split('\n')]

    # 3. Declare an empty array that will later be an 1D array (vector) to save date, price and volume =================
    dtDate = []
    dPrice = []
    #iVolume = []

    # 4. Placing column of the data array into 1D array ================================================================
    # here, the variables are not date and double...they are strings. But price will be rewritten with doubles,
    # and the date will be rewritten with date type. I leave them they way they are to save number of variables used.
    for column in sData_array:
        dtDate.append(column[0])
        dPrice.append(column[6])
        #iVolume.append(column[5])
    del dtDate[0]    # Deleting the first row, as it is the title of the data
    del dPrice[0]    # Deleting the first row, as it is the title of the data
    #del iVolume[0]  # Deleting the first row, as it is the title of the data


    # 5. Converting into appropriate data type.
    # All data right right now is in string.
    # Stringed price will now be replaced with numeric (double) price
    # Stringed date will now be replaced with python-specific date type (which actually is also a string)
    # Stringed volume will now be replaced with numeric (integer) volume
    #---------------------converting price into numeric-------------
    lLenData = len(dtDate) # the total number (or length) of the collected data points
    for i in range(lLenData):
        dtDate[i] = datetime.strptime(dtDate[i], "%Y-%m-%d").date()
        dPrice[i] = float(dPrice[i])
        #iVolume[i] = int(float(iVolume[i]))

    return (dtDate, dPrice) #Volume could be added in export. For now not included


