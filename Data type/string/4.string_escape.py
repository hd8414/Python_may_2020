# string escape sequences

# Strings can contain escape sequences:
#...................................................................................#
#1.  \'	single quote character
#2.  \"	double quote character
#3.  \\	backslash character
#4.  \b	backspace character
#5.  \f	formfeed character
#6.  \n	new line character (starts a new line)
#7.  \r	carriage return character
#8.  \t	horizontal tab character (moves to next tab position, which is every eight characters)
#9.  \v	vertical tab character
#10. \x<var>NN</var>	ASCII character represented by a hexidecimal number NN


str1 = "Hello World"
str2 = "this is a string example"
str3 = "10203040506070809"

print ("Hellow World \"this is a string example\" ") # use of \
print()

print ("Hellow World \\ this is a string example") # use of \\ to print \
print()

print ("Hello \bWorld") # backspace
print()

print ("Hello \nWorld")
print ()

print ("Hello\rWorld")
print()

print ("Hello\tWorld")
print()

