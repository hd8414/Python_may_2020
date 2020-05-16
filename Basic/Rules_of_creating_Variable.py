# Rule of creating a Variables in Python

'''

a-z
A-Z
0-9
_
a-zA-Z0-9_

'''

# # use for single line comment
# '''  ''' and """  """ use for multi line comment


# string data Types

Course_name = 'Python Programming' # String Value
Duration = "35 hours"
course_index = ''' please see
website for index
of full course 
'''  # can define as """  """

# number date Types

Python_version = 3.7 # Floating Values
Student_count = 10 # Integer Value
Course_rating = 9.99 #Floating Value
just_complex_example = c=34.+5j # Complex

# boolen value

iS_course_started = True # Boolen Value
is_published = False # Boolen Value


# calling variables

print (Python_version)  # calling single Variable
print ( Student_count,Course_rating,just_complex_example ) # calling multiple Variable

# calling Variable with prefix and suffix sentence

print('We will be using Python_Version', Python_version,"It's easily available online as it's opensourse ")

# blank line

print () # blank line

# use of function type () - to know data Type of Variable value

print (Course_name, type (Course_name))

# use of function len () - to know length of string , it can not be use for number data Type value

print (Course_name, len (Course_name))

print ()

print(Course_name,type(Course_name),len(Course_name))

print (Duration,type(Duration),len(Duration))

print (Python_version,type(Python_version))

print (Course_rating,type(Course_rating))

print (Student_count,type(Student_count))

print (Course_rating,type(Course_rating))

print (iS_course_started,type(iS_course_started))

print (is_published,type(is_published))