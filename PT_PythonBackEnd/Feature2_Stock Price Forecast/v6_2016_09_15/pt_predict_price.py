# PLOT TREND WEB-APP DEVELOPMENT
# Script Overview :  "stock_reg.py"
# This scripts serves to predict stock price using linear or nonlinear regression.
# The stock price data is collected dynamically from 'Yahoo Finance'

from pt_collect_HistoricalStock import pt_collect_HistoricalStock
import time
from matplotlib import pylab as plt
import datetime

# Section 1. Stock Data crawling =======================================================================================
print('STEP 1. Indicating the target company. ========================================================================')
# 1.1 Select company whose stock to analyze
#     User inputs the company code in string (Note: Include double quotation mark for python to know it is a string)
sCompanyCode = str(input('    Please enter the company stock code.'))

# 1.2 data collecting from yahoo finance
(dtDate, dPrice) = pt_collect_HistoricalStock(sCompanyCode)
# Data is collected by the function "pt_get_stock" .
# dtData = 1D array of date data whose type is  python date type
# dPrice = 1D array of price data whose type is double

# 1.3 manipulation and plotting of the collected data
# 1.3.1 One-Dimensional array reversal
dtDate.reverse()  # The array is reversed. The collecting starts with row #1 being the most recent.
dPrice.reverse()  # I personally like it such that row #1 starts from the oldest date.
# 1.3.2 Selecting an printing the first and the last date:
# so that in Section 2.XX the user knows in what range of analysis.
lLenData = len(dtDate) # Number of the data points collected
dtDateFirstData = dtDate[0]         # the first date of all dates
dtDateLastData = dtDate[lLenData-1] # the last date of all dates
# printing the first and the last date, so that the user knows the date to enter should be within these two dates. (refer to Section 2.1.2)
print("    The collected data begins at " + dtDateFirstData.strftime("%Y-%m-%d"))
print("    The collected data ends at " + dtDateLastData.strftime("%Y-%m-%d"))

# 1.3.3 Plotting date vs price:
# An user observes the trend in the data, then in Section 2.1, the user could select the range over which to perform regression.
plt.plot(dtDate, dPrice, color="grey")
sChartTitle = "The collected historical stock price for: " + sCompanyCode
plt.title(sChartTitle)
plt.show()

# Section 2 Defining the range of dates to analyze =====================================================================
# 2.1 user inputs the range for regression
print('STEP 2. Defining the time period to be analyzed. ==============================================================')
iStartYear = int(input('    Please enter the year of the start-date.'))
iStartMonth = int(input('    Please enter the month of the start-date.'))
iStartDay = int(input('    Please enter the day of the start-date.'))
iEndYear = int(input('    Please enter the year of the end-date.'))
iEndMonth = int(input('    Please enter the month of the end-date.'))
iEndDay = int(input('    Please enter the day of the end-date.'))

# 2.2 printing of the entered range.
sStartDate = '    The start-date entered is ' + str(iStartYear) + '-' + str(iStartMonth) + '-' + str(iStartDay)
sEndDate = '    The start-date entered is ' + str(iEndYear) + '-' + str(iEndMonth) + '-' + str(iEndDay)
print(sStartDate)
print(sEndDate)

# 2.3 error checking (i think error checking is better to be done by the front end, in general)
dtDateStart = datetime.date(iStartYear, iStartMonth, iStartDay)
dtDateEnd = datetime.date(iEndYear, iEndMonth, iEndDay)

if dtDateStart < dtDateFirstData:
    print("The selected start-date is inappropriate.")
    quit()
elif dtDateEnd > dtDateLastData:
    print("The selected end-date is inappropriate.")
    quit()

# 2.4 detecting the row number of the selected start-date and the end date.
# 2.4.1 Detecting the row # of the start-date selected.
lPositionStart = 0
for i in range(lLenData):
    dtDeltaStart = dtDate[i] - dtDateStart
    if dtDeltaStart == abs(dtDeltaStart):
        lPositionStart = i
        break
# 2.4.2 detecting the row # of the end-date selected.
lPositionEnd = 0
for i in reversed(range(lLenData)):
    dtDeltaEnd = dtDateEnd - dtDate[i]
    if dtDeltaEnd == abs(dtDeltaEnd):
        lPositionEnd = i
        break

# 2.4.3 the total number of data insides the selected range of dates.
lLenDataSelected = (lPositionEnd - lPositionStart) + 1

# 2.5 Writing the prices & dates of the selected dates in seperate 1D arrays
# 2.5.1 declaring 1D arrays to which to write
dtDateSelected = []  # This array is to store the date-formatted dates
lDateSelected = []   # This array is to store the numbers (long) that represents a date. '0' represents 1970 Jan 1st 00 hr:00sec. '1' represents 1970 Jan 1st 00 hr: 01 sec
dDateSelected = []   # This array is to store the numbers (double) that represents a date, converted to year-based time. (Refer to Section 2.5.3)
dPriceSelected = []

# 2.5.2 looping and appending to write the data
for index in range(lLenDataSelected):
    dtDateSelected.append(dtDate[lPositionStart + index])
    lDateSelected.append(dtDate[lPositionStart + index].timetuple())
    lDateSelected[index] = time.mktime(lDateSelected[index])
    dPriceSelected.append(dPrice[lPositionStart + index])

# 2.5.3 Scaling to year-based time
#       Usually interest rates, or rate of return in finance is conventionally represent per annum.
#       Thus the second-based time stored currently in lDateSelected scaled down to a year-based time.
dMultFactor = 86400  # 86400 is the multiplicative conversion factor between second based time and day-based time. (24 hr/day = 24 hr X 60 min/hr X 60 sec/min = 86400 sec/day)
dSubFactor = lDateSelected[0] / 86400 # this subtraction factor is used to offset the dates --> such that the first date of the selected date-range becomes time = 0.
dScaleFactor = 365.25 # Year to day scale factor is seperately used to indicates that the year conversion factor is 365.25 instead of 365. Because every four year, there is 366 days.

for i in range(lLenDataSelected):
    dDateSelected.append(0.0)
    dDateSelected[i] = lDateSelected[i] / dMultFactor - dSubFactor  #convert to day-based time then offset to time = 0
    dDateSelected[i] = dDateSelected[i] / dScaleFactor  # convert again from day-based tiem to yr-based time

# 2.6 Expressing the start-date as number (to display in the equation
#
dInitialYearSelected = dtDateSelected[0].year + (dtDateSelected[0].month - 1) / 12.0 + (dtDateSelected[0].day) / 30.0 / 12.0
sInitialYearSelected = str(round(dInitialYearSelected, 3))



# Section 3. Regression Analysis =======================================================================================
# 3.1 Selecting the analysis type
print('STEP 3. Selecting the analysis type. ==========================================================================')
analysis_type = int(input('    Please select 0 for linear analysis and 1 for non linear analysis.'))

# 3.2 Linear regression ------------------------------------------------------------------------------------------------
if analysis_type == 0:
    from pt_LinearRegression import pt_LinearRegression
    from pt_LinearRegression import pt_LinearRegression_y_calc as LinearRegression_price_calc

    # 3.2.1 Running the linear regression (through the function 'pt_lin_reg')
    (dSlope, dPo) = pt_LinearRegression(dDateSelected, dPriceSelected)

    # 3.2.2 Calculating prices on the first & last dates using the linear regression equation
    # the lin_reg_price_calc is found in pt_lin_reg.py
    # it calculates,  P(t) = Slope * time + Po
    dPrice_LinReg_start = LinearRegression_price_calc(dSlope, dPo, dDateSelected[0])
    dPrice_LinReg_end = LinearRegression_price_calc(dSlope, dPo, dDateSelected[lLenDataSelected-1])

    # 3.2.3 Placing the first & last dates and prices for plotting in Sectioin 3.2.5
    dtDate_LinReg_plot = [dtDateSelected[0], dtDateSelected[lLenDataSelected-1]]
    dPrice_LinReg_plot = [dPrice_LinReg_start, dPrice_LinReg_end]

    # 3.2.4 Calculating/displaying the yearly yield.
    # (Slope [$/yr]) / (Price[$] ) * 100% = Yield [%/Yr]
    dYield_LinReg = dSlope / dPrice_LinReg_end * 100
    sYield_LinReg = str(round(dYield_LinReg, 2)) + ' %'
    print('OUTPUT: The yearly yield due to price change (linear regression) = ' + sYield_LinReg)

    # 3.2.5 Graphing the best-fitted line through data.
    # Note that the two variables from Section 3.2.3 are used. (dtDate_LinReg_plot & dPrice_LinReg_plot)
    plt.plot(dtDate_LinReg_plot, dPrice_LinReg_plot, color='red')
    plt.plot(dtDate, dPrice, color='grey')
    plt.title('The yearly yield due to price change (linear regression) = ' + sYield_LinReg)
    plt.xlabel('Year')
    plt.ylabel('Stock Price [$]')  # I need to be careful with the unit of currency. (USD or CAD). For now let's just put $.
    plt.show()

    # 3.2.6

# 3.3 Non-linear regression (Gauss Newton) -----------------------------------------------------------------------------
elif analysis_type == 1:
    from pt_NonlinearRegression import pt_NonlinearRegression
    from pt_NonlinearRegression import pt_NonlinearRegression_price_calc as NonlinearRegression_price_calc

    # 3.3.1 Running the nonlinear regression (Gauss-Newton method)
    (Po, dYield_NonlinReg) = pt_NonlinearRegression(dDateSelected, dPriceSelected)

    #printing the converged parameters for the equation P(t) = P*(1+r)^t
    print('    The converged solution obtains Po = ' + str(round(Po, 1)) + " and r =" + str(round(dYield_NonlinReg, 3)))

    # 3.2.2 Define points to be outputted & calculate fitted price based on the regression
    #   Plotting on every available date takes a lot of data points.
    #   Not as many points are needed for visualizing the best-fitted curve.
    #   Therefore, around 100 points are to be plotted to construct the curve.
    #   If selected range of dates contain more than 300 data points, then only around 100 will be used to show the curve.

    import math
    if lLenDataSelected > 300:
        #if more than 300 points, the time step (in days) is the closest integer to (Total # points / 100)
        iTimeStepSize = int(lLenDataSelected/100.0)
        iNumPointsToPlot = int(math.ceil(lLenDataSelected/(iTimeStepSize*1.0))) #Python is weird, integer/integer = has to be integered and the decimal points are truncated. I had to X 1.0)
        #Note that ceil is for round up to integer.
    else:
        iTimeStepSize = 1
        iNumPointsToPlot = lLenDataSelected

    # 3.3.3 Calculating the price fitted by the regression best-fit (they will later be plotted)
    dDate_NonlinReg = []  #Time values for output (101 points)
    dPrice_NonlinReg_plot = [] #Price values to be calculated

    for i in range(iNumPointsToPlot-1):
        dDate_NonlinReg.append(dDateSelected[(i) * iTimeStepSize])       #time values into the array
        dPrice_NonlinReg_plot.append(NonlinearRegression_price_calc(Po, dYield_NonlinReg, dDate_NonlinReg[i]))        #Price calculation
    dDate_NonlinReg.append(dDateSelected[lLenDataSelected-1])                      #end value manually appended
    dPrice_NonlinReg_plot.append(NonlinearRegression_price_calc(Po, dYield_NonlinReg, dDateSelected[lLenDataSelected-1]))    #end value manually appended

    # 3.3.4 Converting the time to date
    # (I know this section is ugly, but it works.
    # Digging deeper to make the script bit cleaner is not worth the working hours)
    lDate_NonlinReg = []
    dtDate_NonlinReg_plot = []
    from pt_datetime import ctime_to_dtDate
    for i in range(iNumPointsToPlot):
        dDate_NonlinReg[i] = (((dDate_NonlinReg[i] * dScaleFactor) + dSubFactor) * dMultFactor)
        lDate_NonlinReg.append(round(dDate_NonlinReg[i]))
        dtDate_NonlinReg_plot.append(time.ctime(lDate_NonlinReg[i]))  # time.ctime function converts the numbers back to string. But it is not in the python datetime format which I use to plot.
        dtDate_NonlinReg_plot[i] = ctime_to_dtDate(dtDate_NonlinReg_plot[i]) # Therefore, i write the ctime_to_sDate function to convert into the desired form of date-string. (datetime) Perhaps this step is not necessary in the web-fronto end that does not use matplotlib.

    # 3.2.5 Displaying the yearly yield.
    sYield_NonlinReg = str(round(dYield_NonlinReg * 100, 2)) + ' %' # times 100 for percentage
    print('OUTPUT: The yearly yield due to price change (non-linear regression) = ' + sYield_NonlinReg)


    # 3.3.5 graphing the best-fit curve
    plt.title('The yearly yield due to price change (non-linear regression) = ' + sYield_NonlinReg)
    plt.plot(dtDate_NonlinReg_plot, dPrice_NonlinReg_plot, color='red')
    plt.plot(dtDate, dPrice, color='grey')
    plt.xlabel('Year')
    plt.ylabel('Stock Price [USD]') # I need to be careful with the unit of currency. (USD or CAD). For now let's just put $.
    plt.show()

else:
    print("analysis type wrongly inputted")