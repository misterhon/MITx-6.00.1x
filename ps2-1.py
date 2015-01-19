##########################################################################
# PROBLEM 1: PAYING THE MINIMUM  (10 points possible)
# Write a program to calculate the credit card balance after one year
# if a person only pays the minimum monthly payment required by the
# credit card company each month.
# 
# The following variables contain values as described below:
# 	balance - the outstanding balance on the credit card
# 	annualInterestRate - annual interest rate as a decimal
# 	monthlyPaymentRate - minimum monthly payment rate as a decimal
# 	
# For each month, calculate statements on the monthly payment and 
# emaining balance, and print to screen something of the format:
# 	Month: 1
# 	Minimum monthly payment: 96.0
# 	Remaining balance: 4784.0
#
# Be sure to print out no more than two decimal digits
# of accuracy - so print
#	Remaining balance: 813.41
# instead of
#	Remaining balance: 813.4141998135
#
# Finally, print out the total amount paid that year and the remaining
# balance at the end of the year in the format:
#	Total paid: 96.0
#	Remaining balance: 4784.0
#
# A summary of the required math is found below:
#	Monthly interest rate= (Annual interest rate) / 12.0
#	Minimum monthly payment = (Minimum monthly payment rate)
#								x (Previous balance)
#	Monthly unpaid balance = (Previous balance)
#								- (Minimum monthly payment)
#	Updated balance each month = (Monthly unpaid balance)
#									+ (Monthly interest rate
#										x Monthly unpaid balance)
#
##########################################################################

def PayTheMinimum( balance, annualInterestRate, monthlyPaymentRate ):
    
    m = 0;
    ir = ( annualInterestRate / 12.0 ) + 1.0;
    to = 0.0;

    while ( m < 12 ):
        m += 1;
        p = round( monthlyPaymentRate * balance, 2 );
        balance = round( ( ( balance - p ) * ir ), 2 );
        to = round( to + p, 2);

        print "Month: " + `m`;
        print "Minimum monthly payment: " + `p`;
        print "Remaining balance: " + `balance`;
        
    print "Total paid: " + `to`;
    print "Remaining balance: " + `balance`;
    
PayTheMinimum( balance, annualInterestRate, monthlyPaymentRate );