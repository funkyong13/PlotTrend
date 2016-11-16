# PLOT TREND WEB-APP DEVELOPMENT
# Script Overview for "pt_datetime.py"
# Purpose: This script contains function necessary to perform date and time related operations for Plot Trend project

import datetime

def ctime_to_dtDate(sCtimeDate):
    # Function Overview for "ctime_to_dtDate"
    # Purpose: This function serves to convert one form of date (ctime) to another form of date (dtDate)
    # Explanation: ctime is a function to convert number (that represents a date) into a string.
    # For example   time.ctime(0) generates the string, "Wed Dec 31 19:00:00 1969"
    # I wish to get a date in string form that is "1969-12-31 00:00:00". This form is generated when using the 'datetime' module.
    # This functions serve to convert from 'ctime' form of date to 'datetime' form of date.

    # 1. Truncate the strings to strings to indicate yr, month and day____________
    sYear = sCtimeDate[20:24]
    sMonth = sCtimeDate[4:7]
    sDay = sCtimeDate[8:10]

    # 2. Manually change the three-letter abbreviated month strings to numbered string
    #This is n ecessary because the datetime-operation requires numbered string but not three lettered string (ex. "Jan"--> not ok.  "1"-->ok
    if sMonth == "Jan":
        sMonth = "1"
    elif sMonth == "Feb":
        sMonth = "2"
    elif sMonth == "Mar":
        sMonth = "3"
    elif sMonth == "Apr":
        sMonth = "4"
    elif sMonth == "May":
        sMonth = "5"
    elif sMonth == "Jun":
        sMonth = "6"
    elif sMonth == "Jul":
        sMonth = "7"
    elif sMonth == "Aug":
        sMonth = "8"
    elif sMonth == "Sep":
        sMonth = "9"
    elif sMonth == "Oct":
        sMonth = "10"
    elif sMonth == "Nov":
        sMonth = "11"
    elif sMonth == "Dec":
        sMonth = "12"

    # 3. Sum strings with hyphen to construct a datte-representing string in the form "YYYY-MM-DD"
    sDate = sYear + "-" + sMonth + "-" + sDay
    sDate = datetime.datetime.strptime(sDate, "%Y-%m-%d")

    return sDate