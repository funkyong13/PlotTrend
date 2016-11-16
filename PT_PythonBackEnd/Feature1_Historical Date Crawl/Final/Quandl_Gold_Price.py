sNameVar = "Gold Price"
sSaveFileName = "Gold.pdf"

import time
import quandl
API_Key="UkxUv83QwwKsQk8TWCrz"
QuandlImported = quandl.get("WGC/GOLD_DAILY_USD", trim_start = "2000-01-01", authtoken=API_Key)
IndexCol = QuandlImported.index.tolist() #Conserving the dates in the index column
QuandlImported.insert(0, "Date", IndexCol) #inserting the dates in the 1st column to export to numpy array

import pandas
import numpy
import datetime

GoldPrice = QuandlImported.as_matrix(columns=None)
LenData = len(GoldPrice)
dPrice = numpy.zeros(LenData)
sDate =  ["" for x in range(LenData)]

for i in range (0, LenData):
	sDate[i] =pandas.to_datetime(GoldPrice[i][0])
	dPrice[i]= GoldPrice[i][1]

import matplotlib.pyplot as plt
plt.plot(sDate,dPrice)
plt.title(sNameVar, fontname="Times New Roman",fontweight="bold", fontsize = 25)
plt.xlabel('Time', fontname="Times New Roman",fontweight="bold", fontsize = 20)
plt.ylabel('Price [USD]', fontname="Times New Roman",fontweight="bold", fontsize = 20)
plt.grid(b=True, which="both", color="0.65", linestyle="-")
plt.savefig(sSaveFileName) #saving as EPS doens't export the labels.
plt.show()