##########################################################################
# COUNTING VOWELS  (10/10 points)
# Assume s is a string of lower case characters.
# 
# Write a program that counts up the number of vowels contained in the
# string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example,
# if s = 'azcbobobegghakl', your program should print:
# 	Number of vowels: 5
#   
##########################################################################

print "Number of vowels: " + `(s.count('a') + s.count('A')
    + s.count('e') + s.count('E')
    + s.count('i') + s.count('I')
    + s.count('o') + s.count('O')
    + s.count('u') + s.count('U'))`;