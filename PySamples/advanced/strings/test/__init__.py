
''' 
This file contains sample code to work with strings
'''

sample_string = "The quick brown fox jumped over the lazy dog"
# print the string
print "sample_string (original value):\n" + sample_string

# split the string and display
print "\n string after splitting (default split criteria):\n" + str(sample_string.split())

#split the string based on specific character
print "\n custom splitting (character 'o' as separator) :\n" + str(sample_string.split('o'))