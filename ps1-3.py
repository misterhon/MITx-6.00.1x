##########################################################################
# ALPHABETICAL SUBSTRINGS  (15/15 points)
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the
# letters occur in alphabetical order.
# For example, if s = 'azcbobobegghakl', then your program should print:
#   Longest substring in alphabetical order is: beggh
#   
# In the case of ties, print the first substring. For example, if
# s = 'abcbcd', then your program should print:
#   Longest substring in alphabetical order is: abc
#   
##########################################################################

def streak(str, h, k):
    if (len(str) == 0):
        if (len(h) > len(k)):
            return h;
        return k;
    elif (len(h) == 0):
        return streak(str[1:], str[0], k);
    else:
        if ( h[-1] <= str[0] ):
            return streak(str[1:], h + str[0], k);
        else:
            if (len(h)>len(k)):
                return streak(str[1:], str[0], h);
            return streak(str[1:], str[0], k);

print 'Longest substring in alphabetical order is: ' + streak(s, '', '');