##########################################################################
# COUNTING BOBS  (15/15 points)
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob'
# occurs in s. For example, if s = 'azcbobobegghakl', then your program
# should print
# 	Number of times bob occurs is: 2
##########################################################################

def occurrences(string, sub):
    count = start = 0
    while True:
        start = string.find(sub, start) + 1;
        if start > 0:
            count += 1;
        else:
            return count;
            
print "Number of times bob occurs is: " + `occurrences(s, 'bob')`;