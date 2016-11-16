# PLOT TREND WEB-APP DEVELOPMENT
# Function Overview for "pt_lin_reg"
# Purpose: This function serves to perform linear regression.
# Input = {X}, {Y} : Two 1 D arrays of the same length, containing real numbers.
# Output = dSlope & dYo : These two values can define a line. Y(X) = dSlope * X + dYo.

def pt_LinearRegression(dX, dY):

    # 1. Defining the number of data points (or length of the 1D arrays) for looping.
    iLenData = len(dX)

    # 2. Summation of  X, Y, XY, XX values.
    # The reason for summing these values won't be mentioned.
    # It could be understood from the derivation of linear regression, which could be lengthy to write here.

    # 2.1. assigning zero values to variables
    # to these variables X, Y, XY, XX values are to be cumulatively summed as looping is performed
    dSum_X = 0.0
    dSum_Y = 0.0
    dSum_XY = 0.0
    dSum_XX = 0.0

    # 2.2 looping for summation
    for i in range(iLenData):
        dSum_X = dSum_X + dX[i]
        dSum_Y = dSum_Y + dY[i]
        dSum_XY = dSum_XY + (dX[i] * dY[i])
        dSum_XX = dSum_XX + dX[i] ** 2

    # 3. Calculating the slope and constant that defines a line : dSlope & dYo
    dSlope = ((iLenData * dSum_XY) - (dSum_X * dSum_Y)) / ((iLenData * dSum_XX) - (dSum_X ** 2))
    dYo = (dSum_Y - (dSlope * dSum_X)) / iLenData

    return dSlope, dYo


# Function Overview for "pt_lin_reg_price_calc"
# Purpose: This function serves to calculate Y based on linear-regression parameters, and user inputted time.
# Input = The slope and constant that defines a line. And the target X value at which Y is to be calculated
# Output = Y(X), that is Y(X) = dSlope * X + dYo.
def pt_LinearRegression_y_calc(dSlope, dYo, dX):
    dY = dSlope * dX + dYo
    return dY


