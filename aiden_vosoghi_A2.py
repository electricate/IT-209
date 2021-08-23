# Program file name: aiden_vosoghi_A2.py
# Assignment #2 (A2): Student Class
# Author: Aiden Vosoghi

# The purpose of this assignment is to demonstrate knowledge
# of Classes and Objects and how to properly implement
# them in Python.

# We start off by creating a Student Class which contains
# several methods that will be used to neatly populate
# information about a set number of students. Before creating
# any methods within the class we define two variables:
# totalEnrollment and g_num. The 'totalEnrollment' will be
# used to count the total number of students in the system
# whereas the 'g_num' assigns each student a unique student ID number.

class Student (object):

    totalEnrollment = 0
    g_num = 1

# Inside the class, we must define a few methods which will
# be responsible for sorting through the data and making sure
# all the information is accurate. The __init__ method
# initializes the variables name, major, enrolled, credits,
# and qpoints, all of which will be discussed later. An
# increment counter is also made for the totalEnrollment
# and g_num variables.
    
    def __init__ (self, name, major = 'IST', enrolled = 'y',
                  credits = 0, qpoints = 0):
        self.name = str(name)
        self.major = str(major)
        self.enrolled = str(enrolled)
        self.credits = credits
        self.qpoints = qpoints
        self.totalEnrollment = Student.totalEnrollment
        Student.totalEnrollment += 1
        self.g_num = Student.g_num
        Student.g_num += 1

# The 'gpa' method takes the credits and quality points
# of a student and uses those to define a new variable, 
# gradePoint, which displays the GPA of that particular 
# student. If there is a zero division error, the GPA is
# automatically assigned as 0.0. Otherwise, the result
# is rounded to the nearest two (2) decimal places and returned.

    def gpa (self):
        gradePoint = 0.0
        self.gradePoint = gradePoint
        try:
            self.gradePoint = self.qpoints / self.credits
        except ZeroDivisionError:
            return 0.0
        else:
            return(round(self.gradePoint, 2))

# The next method is simply called 'isEnrolled' and takes
# the 'enrolled' variable from each student and runs a
# quick test to see if the student is enrolled ('y') or
# is not enrolled ('n') and returns the result.
        
    def isEnrolled (self):
        if self.enrolled == 'y':
            return True
        elif self.enrolled == 'n':
            return False

# The 'status' method takes the number of credits
# completed by each student and assigns them their
# correct 'grade level.'

    def status (self):
        if self.credits >= 90:
            return "Senior"
        if self.credits < 90 and self.credits >= 60:
            return "Junior"
        if self.credits < 60 and self.credits >= 30:
            return "Sophomore"
        if self.credits < 30:
            return "Freshman"

# 'sameStudent' compares two student objects by their
# name and their g Number (g_num). If they are not
# identical, then a False value is returned. Otherwise,
# if both the name AND the g number match, then a True
# value is returned. Also, if a value is not the same
# format as the Student class, the value is immediately
# returned as False.

    def sameStudent (self, other):
        if self == other:
            return True
        if not isinstance(other, Student):
            return False
        else:
            return(int(self.g_num) == int(other.g_num) and
                   str(self.name) == str(other.name))

# The final method __str__ prints out the final results
# for each student object in an organized and easy to
# read format with the name, G Number, major, enrollment,
# credits, quality points, and GPA displayed.

    def __str__ (self):
        return(str(self.name) + ', ' + 'G0000' + str(self.g_num) + ', '
              + str(self.major) + ', ' + str(self.enrolled)
              + ', ' + str(self.credits) + ', ' + str(self.qpoints) + ', '
              + str(self.gpa()))

# Sample code which was taken from the A2 demo file
# provided to us by the instructor. Contains many
# statements which are used to test the validity
# of some of the objects created, including
# identifying class status and equality between
# two students.

print('\nStart of A2 Student class demo ')
s1 = Student('David Miller', major = 'Hist',
 enrolled = 'y', credits = 0, qpoints = 0)
s2 = Student('Sonia Fillmore', major = 'Math',
 enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('A. Einstein', major = 'Phys',
 enrolled = 'y', credits = 0, qpoints = 0)
s4 = Student('W. A. Mozart', major = 'Mus',
 enrolled = 'n', credits = 29, qpoints = 105)
s5 = Student('Sonia Fillmore', major = 'CSci',
 enrolled = 'y', credits = 60, qpoints = 130)
s5.g_num = s2.g_num
s6 = Student('Pierre Renoir', major = 'Art',
 enrolled = 'y', credits = 120, qpoints = 315)
print('s1 = ', s1)
print('s2 = ', s2)
print('s3 = ', s3)
print('s4 = ', s4)
print('s5 = ', s5)
print('s6 = ', s6)
print('\nTotal number of students: ', Student.totalEnrollment)
print('The gpa of ', s1.name, ' is ', s2.gpa())
print('Class standing of ', s4.name, ' is ', s4.status())
print('Class standing of ', s2.name, ' is ', s2.status())
if s1.sameStudent(s2):
 print (s1.name, ' and ', s2.name, ' are the same student')
else:
 print (s1.name, ' and ', s2.name, ' are not the same student')
if s2.sameStudent(s5):
 print (s2.name, ' and ', s5.name, ' are the same student')
else:
 print (s2.name, ' and ', s5.name, ' are not the same student')
if s1.isEnrolled():
 print (s1.name, ' is currently enrolled')
else:
 print (s1.name, ' is not currently enrolled')
if s4.isEnrolled():
 print (s4.name, ' is currently enrolled')
else:
 print (s4.name, ' is not currently enrolled')
print('\nEnd of A2 Student class demo')
