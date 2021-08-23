# Program Name: IT209_aiden_vosoghi_A3.py
# Assignment #3 (A3): University Department Class Definition
# Author: Aiden Vosoghi

# The purpose of this assignment is to demonstrate
# knowlegde of container classes and passing info
# between the classes Student and Department.

class Student (object):

    totalEnrollment = 0
    studentMajor = ('Acctg','Art','CSci','Hist','IST','Math','Physics','ENGR','CHHS','ARTS')

# Inside the class, we must define a few methods which will
# be responsible for sorting through the data and making sure
# all the information is accurate. The __init__ method
# initializes the variables name, major, enrolled, credits,
# and qpoints, all of which will be discussed later. An
# increment counter is also made for the totalEnrollment
# and g_num variables.
    
    def __init__ (self, g_num, name, status, major = 'IST', enrolled = 'y',
                  credits = 0, qpoints = 0):

            self.g_num = str(g_num)
            self.name = str(name)
            self.status = str(status)
            self.major = str(major)
            self.enrolled = str(enrolled)
            self.credits = credits
            self.qpoints = qpoints
            self.totalEnrollment = Student.totalEnrollment
            Student.totalEnrollment += 1
            if self.major not in Student.studentMajor:
                self.major = 'IST'

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

# 'sameStudent' compares two student objects by their
# name and their g Number (g_num). If they are not
# identical, then a False value is returned. Otherwise,
# if both the name AND the g number match, then a True
# value is returned. Also, if a value is not the same
# format as the Student class, the value is immediately
# returned as False.

    def _sameStudent (self, other):
        if self == other:
            return True
        if not isinstance(other, Student):
            return False
        else:
            return(str(self.g_num) == str(other.g_num) and
                   str(self.name) == str(other.name))

# The final method __str__ prints out the final results
# for each student object in an organized and easy to
# read format with the name, G Number, major, enrollment,
# credits, quality points, and GPA displayed.

    def __str__ (self):
        return(str(self.name) + ', ' + str(self.g_num) + ', '
              + str(self.major) + ', ' + str(self.enrolled)
              + ', ' + str(self.credits) + ', ' + str(self.qpoints) + ', '
              + str(self.gpa()))

# Add 'setMajor' method in the Student Class which will
# be used by the Department Class to update a student's
# major corresponding to the department they are in.

    def setMajor (self, other):
        self.major = other
        return True

# Define the Department Class, which will be used in
# conjunction with the Student Class in order to
# populate departments with students.
    
class Department ():

# Initialize university students and Department Code
# variables which contain the total number of university
# students and the different departments respectively.

    univ_students = 0
    deptCode = ('ENGR','ARTS','CHHS')

# The __init__ method initializes the department code and
# name, max capacity, and minimum GPA required.

    def __init__ (self, d_code = '', d_name = '', capacity = 0, minGPA = 0):
        if d_code in Department.deptCode:
            self.d_code = str(d_code)
            self.d_name = str(d_name)
            self.capacity = capacity
            self.minGPA = minGPA
            self.num_students = 0
            self.avgGPA = 0.0
            self.totalGPA = 0.0
            self.univ_students = Department.univ_students
            self.stuList = []
        else:
            return False

# The __str__ method will be used to print out information
# about the department objects created. This includes the
# attributes that were defined in the __init__ constructor.

    def __str__ (self):
        return('(' + str(self.d_code) + ') - ' + str(self.d_name) + ', Capacity: ' +
              str(self.capacity) + ', Number of Students: ' + str(self.num_students))

# '_isQualified' checks to see if a student object is
# eligible to be added to a department. If the
# student object is not enrolled, has a low GPA, or
# the capacity of the department has been reached, a
# False is returned. A for loop iterates through
# 'stuList' and checks to see if a duplicate student 
# already exists within the department using the 'sameStudent' 
# method from the Student Class by comparing student 'name' 
# and 'g_num'. If True, don't add the student. Otherwise, 
# add the student to the department.

    def _isQualified(self, other):
        if self.num_students >= self.capacity:
            return False, '- The maximum capacity has been reached'
        if other.enrolled != 'y':
            return False, '- The student is not enrolled'
        if other.gpa() < self.minGPA:
            return False, "- The student's GPA is too low"
        for student in self.stuList:        # for loop to check for duplicates within 'stuList'
            if student._sameStudent(other):
                return False, '- Duplicate Student'
        return True, 'Qualified'

# The 'addStudent' method is called by main() to add
# a student to the department. First, the '_isQualified'
# method is executed to determine if a student object is
# eligible to be added to a department. If True is
# returned, then the student object is added, the number
# of students within that department is updated along
# with the total number of students within the university.
# The average GPA for that department is also updated.

    def addStudent (self, other):
        trueOrFalse, reason = self._isQualified(other)
        if trueOrFalse:
            other.setMajor(self.d_code)
            self.stuList.append(other)
            self.num_students += 1
            Department.univ_students += 1
            self.totalGPA += other.gpa()
            self.avgGPA = round(self.totalGPA / self.num_students, 2)
            return True, reason
        else:
            return False, reason

# The final method in the Department Class, 'printstuList',
# iterates through the stuList List and prints out all the
# students within that department object. Afterwards, the
# department's average GPA is printed, which is dynamically
# updated everytime a student object is added.
        
    def printstuList(self):
        for p in self.stuList:
            print(p)
        print('\nDepartment Average GPA:',self.avgGPA,'\n')

# Beginning of the main() method, which contains test code
# provided from Blackboard. It defines several student
# objects as well as the three main department objects.
# A series of tests are run to test the validity of the
# code and detect any errors that may be present.

print('\nStart of Department and Student class demo **************')

s1 = Student('G34568', 'David Miller', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 30, qpoints = 90)           
s2 = Student('G21345', 'Sonia Fillmore', status = 'senior', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('G42156', 'Chris Squire', status = 'sophomore', major = 'Musc',
      enrolled = 'y', credits = 45, qpoints = 160)           
s4 = Student('G10928', 'Tal wilkenfeld', status = 'junior', major = 'ARTS',
      enrolled = 'y', credits = 70, qpoints = 225)
s5 = Student('G22157', 'Larry Graham', status = 'senior', major = 'CHHS',
      enrolled = 'y', credits = 105, qpoints = 290)           
s6 = Student('G31345', 'John Entwistle', status = 'freshman', major = 'CSci',
      enrolled = 'y', credits = 15, qpoints = 35)
s7 = Student('G44568', 'Esperanza Spalding', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 65, qpoints = 250)           
s8 = Student('G55345', 'Tim Bogert', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 120)
s9 = Student('G66113', 'Gordon Sumner', status = 'freshman', major = 'Musc',
      enrolled = 'y', credits = 15, qpoints = 45)           
s10 = Student('G11311', 'Paul McCartney', status = 'senior', major = 'ARTS',
      enrolled = 'y', credits = 110, qpoints = 275)
s11 = Student('G22111', 'Elizabeth Smythe', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 85, qpoints = 250)
s12 = Student('G31312', 'John McVie', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 120)
s13 = Student('G31312', 'Nawt Enrolled', status = 'sophomore', major = 'Hist',
      enrolled = 'n', credits = 45, qpoints = 120)
s14 = Student('G11112', 'Toolow G. Peyay', status = 'freshman', major = 'Undc',
      enrolled = 'y', credits = 20, qpoints = 38)           


print('List of Students created: ')
print('s1=  ',s1)
print('s2=  ',s2)
print('s3=  ',s3)
print('s4=  ',s4)      
print('s5=  ',s5)
print('s6=  ',s6)      
print('s7=  ',s7)
print('s8=  ',s8)
print('s9=  ', s9)
print('s10= ',s10)
print('s11= ',s11)
print('s12= ',s12)      
print('s13= ',s13)
print('s14= ',s14)      
d1 = Department('ENGR', 'Engineering', 5, 2.75)
d2 = Department('ARTS', 'Art and Architecture', 15, 2.0)
d3 = Department('CHHS', 'College of Health and Human Sevrices', 10, 2.5)
print('\n\nDepartments established:')
print(d1)
print(d2)
print(d3)
print('\n\nAdding s1 - s5 to ENGR Department- print Roster follows')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)      
d1.addStudent(s4)
d1.addStudent(s5)
d1.printstuList()      

a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, ' - over capacity, ret values: ', a, b)
d1.printstuList()
      
print('\n\nAdding ', s6.name, ' and ', s7.name, ' to ', d2.d_code, ', printRoster follows: ')
d2.addStudent(s6)
d2.addStudent(s7)
d2.printstuList()

print('\n\nAdding ', s8.name, ' and ', s9.name, ' to ', d3.d_code, ', printRoster follows: ')
d3.addStudent(s8)
a, b = d3.addStudent(s9)
print('\nAttempting to add qualified student , ', s9.name, ' to ', d3.d_code, ', CHHS, return values; ', a, b)
d3.printstuList()

a, b = d3.addStudent(s14)
print('\n\nAttempting to add low GPA student ', s14.name, ', return values: ', a, b) 

a, b = d2.addStudent(s13)
print('\n\nAttempting to add non-enrolled student ', s13.name, ', return values: ', a, b) 

a, b = d3.addStudent(s8)
print('\n\nAttempting to add dupe student ', s8.name, ', return values: ', a, b) 

print('\n\nAdding s10 to ENGR, s11 to ARTS, s12 to CHHS, then print all 3 roster')
d1.addStudent(s10)
d2.addStudent(s11)
d3.addStudent(s12)

d1.printstuList()
d2.printstuList()
d3.printstuList()      
print('\n\n\n***** End of Student class demo **********')
