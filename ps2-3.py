##########################################################################
# PROBLEM 3: USING BISECTION SEARCH TO MAKE THE PROGRAM FASTER
# (25 points possible)
# 
# You'll notice that in Problem 2, your monthly payment had to be a
# multiple of $10. Why did we make it that way? You can try running your
# code locally so that the payment can be any dollar and cent amount
# (in other words, the monthly payment is a multiple of $0.01). Does your
# code still work? It should, but you may notice that your code runs more
# slowly, especially in cases with very large balances and interest rates.
#
# We can make this program run faster using a technique introduced
# in lecture - bisection search!
#
# The following variables contain values as described below:
#	balance - the outstanding balance on the credit card
#	annualInterestRate - annual interest rate as a decimal
#
# Monthly interest rate = (Annual interest rate) / 12.0
# Monthly payment lower bound = Balance / 12
# Monthly payment upper bound = (Balance x
# 									(1 + Monthly interest rate)^12)
# 										/ 12.0
##########################################################################

rate = 1.0 + ( annualInterestRate / 12.0 );
lo = balance / 12;
up = ( ( balance * pow( rate, 12 ) ) / 12.0 );

def PayWithBiSearch(bal, rate, lo, up) :
    rem = bal;
    while ( abs( rem ) > 0.01 ) :
        m = 0;
        rem = bal;
        ans = ( lo + up ) / 2.0;
        while ( m < 12 ) :
            m += 1;
            rem = ( rem - ans ) * rate;
        if ( rem > 0 ) :
            lo = ans;
        else :
            up = ans;
    return round( ans, 2 );

print "Lowest Payment: " + `PayWithBiSearch( balance, rate, lo, up )`;