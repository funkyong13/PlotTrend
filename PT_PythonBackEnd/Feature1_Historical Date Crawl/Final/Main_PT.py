#This is the main program for Plot Trend project

from Def_Dynamic_Currency import Dyn_Curr #Import the Dynamic Currency Crawler
from Def_Dynamic_StockHist import Dyn_StockHist #Import the Dynamic Currency Crawler


#Manual User Inputs   START_________________________________

# A. CURRENCY CRAWLING
#CurrFrom = 'USD'
#CurrTo = 'KRW'
#Curr = Dyn_Curr(CurrFrom, CurrTo)
#print(CurrFrom + " to " + CurrTo, Curr)



# B. Stock History CRAWLING


sCompCode = 'AAPL'
StockHist = Dyn_StockHist(sCompCode)
import matplotlib.pyplot as plt
plt.plot(StockHist[0],StockHist[1])
plt.show()
#Manual User Inputs   END___________________________________