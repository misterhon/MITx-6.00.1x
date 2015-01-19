##########################################################################
# PROBLEM 2: PAYING DEBT OFF IN A YEAR  (15 points possible)
# 
# Now write a program that calculates the minimum fixed monthly payment
# needed in order pay off a credit card balance within 12 months.
# By a fixed monthly payment, we mean a single number which does not
# change each month, but instead is a constant amount that will be paid
# each month.
# 
# In this problem, we will not be dealing with a minimum monthly
# payment rate.
# The following variables contain values as described below:
# 	balance - the outstanding balance on the credit card
# 	annualInterestRate - annual interest rate as a decimal
# 	
# The program should print out one line: the lowest monthly payment that
# will pay off all debt in under 1 year, for example:
# 	Lowest Payment: 180
##########################################################################

rate = 1.0 + ( annualInterestRate / 12.0 );

def PayOffInAYear( balance, rate, payment ):

	m = 0;
	bal = balance;

	while ( m < 12 ):
		m += 1;
		bal = round( ( ( bal - payment ) * rate ), 2 );

	if ( bal > 0.0 ) :
		return PayOffInAYear( balance, rate, payment + 10 );

	return payment;

print "Lowest Payment: " + `PayOffInAYear( balance, rate, 10 )`;