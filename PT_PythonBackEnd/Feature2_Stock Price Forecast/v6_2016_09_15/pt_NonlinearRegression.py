# PLOT TREND WEB-APP DEVELOPMENT
# Function Overview for "pt_nonlin_reg"
# Purpose: This function serves to perform non-linear regression.
#          Amongst the various types of non-linear regression, it employs Gaess-Newton Method.
#          The specific nonlinear function to which Gauess-Newton Method is applied is P(t) = Po * [ (1 + r)^t ]
#          This function is formulated assuming constant growth of the stock price.
# Input: {X}, {Y} (Two 1 D arrays of the same length, containing real numbers.)
# Output: Po & r     (Po = initial price,    r = yield or rate of return)


#To Junho.
# This method is pretty deep mathematically. If interested in knowing the formulation, please refer to the pdf I uploaded.
# If not, I suggest you take the code as granted.

import numpy

# Sub Function #1 to serve the main function ---------------------------------------------------------------------------
def pt_NonlinearRegression_df_over_Po(Po, r, t): #Jacobian Calculation
    dx_Po = Po * pow(1+r, t)   #is this supposed to be like this or is it really just pow(1+r,t), because this gives me an error
    return dx_Po

# Sub Function #2 to serve the main function ---------------------------------------------------------------------------
def pt_NonlinearRegression_df_over_r(Po, r, t):  #Jacobian Calculation
    dx_r = Po * t * pow(1+r, t-1)
    return dx_r


# Main Function ========================================================================================================
def pt_NonlinearRegression(t, P):
# Note that P stands for price & r stands for rate of return (or yield)

    # 1. Number of data points imported
    lLenData = len(P) #Number of data points

    # 2. Initial guess for price and yield
    P_guessed = P[0]
    r_guessed = 0.1    #for now a reasonable assumption. I may later change the code such that the guessed value is calculated from the data.

    # 3. P and r values for looping assigned from the initial guess
    P_loop = P_guessed
    r_loop = r_guessed

    # 4. Looping till convergence
    minimum_percent_diff = 10000 #Initial very high value prior to looping

    while minimum_percent_diff > 0.0001:
        # 4.1 Jacobian calculation
        Jacobian = numpy.zeros(shape=(lLenData ,2))    #Declare Jacobian matrix with all zeros
        f = numpy.zeros(shape=(lLenData, 1))           #Declare f function, which is  fi = P(ti) - Pi
        for i in range(0, lLenData):
            Jacobian[i, 0] = pt_NonlinearRegression_df_over_Po(P_loop, r_loop, t[i])
            Jacobian[i, 1] = pt_NonlinearRegression_df_over_r(P_loop, r_loop, t[i])
            f[i] = (P_loop * pow( 1 + r_loop, t[i]))-P[i]

        # 4.2 Transpose of Jacobian
        Trans_Jacobian = Jacobian.transpose()  #Transpose of Jacobian

        # 4.3 delta calculation (new P = old P + delta P.  &   new r = old r + delta r)
        JT_J = numpy.dot(Trans_Jacobian, Jacobian)
        inv_JT_J = numpy.linalg.inv(JT_J)
        JT_f = numpy.dot(Trans_Jacobian,f)
        delta = -1*numpy.dot(inv_JT_J,JT_f)

        # 4.4 updating P and r values after 1 loop.
        P_new = P_loop + delta[0]  #Current the delta[0] value is a 1X1 matrix. need to convert it to a scalar in the future to make the code clean
        r_new = r_loop + delta[1]

        # 4.5 % diff calculation
        Percent_diff_P = abs((P_new-P_loop)/P_loop)*100
        Percent_diff_r = abs((r_new-r_loop)/r_loop)*100

        # 4.6 determining the lower % diff between 'price % diff' and 'yield % diff'
        if Percent_diff_P > Percent_diff_r:
            minimum_percent_diff = Percent_diff_r
        else:
            minimum_percent_diff = Percent_diff_P

        # 4.7 Assigning the new values of P and r for the next loop
        P_loop = P_new
        r_loop = r_new
    #LOOP ENDS

    # 5. Converged solution
    P_converged = P_loop
    r_converged = r_loop
    return P_converged, r_converged


def pt_NonlinearRegression_price_calc(Po, r, t):
    Pt = Po*pow(1+r,t)
    return Pt
