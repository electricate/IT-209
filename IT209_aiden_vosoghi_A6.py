# Program File Name: IT209_aiden_vosoghi_A6.py
# Assignment #6 (A6): Student/Faculty Polymorphism
# Author: Aiden Vosoghi

# For this assignment, we are to implement Polymorphism to the
# Student and Faculty classes by adding three new methods: 'activate',
# 'deactivate', and 'status_summary'. More information about these
# methods will be explained in the following comments.

class Person (object):

# the __init__ constructor creates the basic information of a Person
# object along with a class attribute of 2020, which will be used
# for the Faculty class later on.

    currentYear = 2020

    def __init__ (self, g_num, name, address, telephone, email):
        self.g_num = g_num
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email
        self.currentYear = Person.currentYear

# the __str__ method takes the attributes for each Person object and
# prints them in a neat format for the user to see.

    def __str__ (self):
        return ('\n{} , {}\nAddress: {}\nTel: {}\n{}'.format(str(self.name),str(self.g_num),
                str(self.address),str(self.telephone),str(self.email)))

# the 'dupePerson' method replaces the 'sameStudent' method from
# assignment 3 (A3). The new method acts the same, comparing the
# g_num and name of a person object to an existing object. if
# they are the same, return True. Else, return False.

    def dupePerson (self, person):
        if self == person:
            return True
        if not isinstance(person, Person):
            return False
        return (str(self.g_num) == str(person.g_num) and
                str(self.name) == str(person.name))

# The Student subclass inherits from the Person class and adds
# a few extra attributes including status, major, enrolled, credits,
# and qpoints. The attributes defined in the Person class are
# referenced using 'super().__init__'. Class variables 'totalEnrollment'
# and 'studentMajor' are also defined which are used to keep track of the
# total number of students and category of valid majors, respectively. If
# the student's major is not listed in the 'studentMajor' tuple, then the
# default of 'IST' is assigned.

class Student (Person):

    totalEnrollment = 0
    studentMajor = ('Acctg','Art','CSci','Hist','IST','Math','Physics','ENGR','CHHS','ARTS')
    
    def __init__ (self, g_num, name, address, telephone, email, status, major = 'IST',
                  enrolled = 'y', credits = 0.0, qpoints = 0.0):
            super().__init__(g_num, name, address, telephone, email)
            self.status = str(status)
            self.major = str(major)
            self.enrolled = str(enrolled)
            self.credits = credits
            self.qpoints = qpoints
            self.totalEnrollment = Student.totalEnrollment
            self.totalEnrollment += 1
            if self.major not in Student.studentMajor:
                self.major = 'IST'

# the 'gpa' method calculates a Student object's GPA. If the student does
# not have any credits, then a value of 0.0 is automatically returned.
# Otherwise, the student's GPA to the nearest two decimal points is returned.

    def gpa (self):
        gradePoint = 0.0
        self.gradePoint = gradePoint
        try:
            self.gradePoint = self.qpoints / self.credits
        except ZeroDivisionError:
            return 0.0
        else:
            return(round(self.gradePoint, 2))

# 'isEnrolled' checks to see if a Student object is currently enrolled at the
# university. If they are enrolled, return True. Otherwise, return False.

    def isEnrolled (self):
        if self.enrolled == 'y':
            return True
        if self.enrolled == 'n':
            return False

# the __str__ method takes the attributes for each Student object and
# prints them in a neat format for the user to see.

    def __str__ (self):
        return('{}\nMajor: {}\nStatus: {}\nActive: {}\nCredits: {}\nQuality Points: {}'
               '\nGPA: {}\n'.format(super().__str__(),str(self.major),str(self.status),
                str(self.enrolled),str(self.credits),str(self.qpoints),str(self.gpa())))

# The 'status_summary' method is responsible for printing the information
# for a particular student object, and determine if they are active or not. If
# they are not active, the output correctly states the student is not active.
# Otherwise, the student is printed as active.

    def status_summary(self):
        activity = ''
        if self.enrolled == 'y':
            activity = 'active'
        else:
            activity = 'NOT active'
        print('\nSummary:\n{} is a {} at GMU, with g-number {}\nThey are a {} majoring'
              ' in {}\nTheir GPA is {} and they are currently {}\n'.format(str(self.name),
              type(self).__name__,str(self.g_num),str(self.status),str(self.major),
              str(self.gpa()),activity))

# 'setMajor' is used in conjunction with the 'addStudent' method defined in
# the Department class to change a student's major to the associated department
# they were placed in.

    def setMajor (self, other):
        self.major = other
        return True

# The 'activate' method changes a student object's enrollment to 'y' and
# returns True

    def activate (self):
        self.enrolled = 'y'
        return True

# The 'deactivate' method changes a student object's enrollment to 'n' and
# returns True

    def deactivate (self):
        self.enrolled = 'n'
        return True

# The Faculty class inherits from the Person superclass and, similarly to the
# Student class, adds a few new attributes including rank, active, teach_load,
# specialty, and yearStarted. facultyRank and facultySpec are class variables
# which contain a tuple of acceptable ranks and specialities. If the Faculty
# object does not meet this criteria, then the faculty object is not created.

class Faculty (Person):

    facultyRank = ('Professor', 'Associate Professor', 'Assistant Professor','Instructor')
    facultySpec = ('teaching', 'research', 'administration', 'combination')
    
    def __init__ (self, g_num, name, address, telephone, email, rank, active, teach_load,
                  specialty, yearStarted):
        super().__init__(g_num, name, address, telephone, email)
        self.rank = rank
        self.specialty = specialty
        if self.rank not in Faculty.facultyRank or self.specialty not in Faculty.facultySpec:
            return None
        self.active = active
        self.teach_load = teach_load
        self.yearStarted = yearStarted

# the __str__ method takes the attributes for each Faculty object and
# prints them in a neat format for the user to see.

    def __str__ (self):
        return ('{}\nRank: {}\nSpecialty: {}\nTenure: {} years\n'.format(str(super().__str__()),
                str(self.rank), str(self.specialty),str(self.tenure())))

# 'tenure' takes the starting year of a Faculty object and subtracts it from the
# currentYear attribute which was defined in the Person class. The difference is
# returned for the user to see.
    
    def tenure (self):
        facultyTenure = self.currentYear - self.yearStarted
        return facultyTenure

# The 'activate' method changes a faculty object's active attribute to 'y'
# and returns True

    def activate (self):
        self.active = 'y'
        return True

# The 'activate' method changes a faculty object's active attribute to 'n'
# and returns True

    def deactivate (self):
        self.active = 'n'
        return True

# 'status_summary' prints the information about a particular faculty object.
# It lists their name, g number, rank, specialty, and teaching load. If the
# faculty object is not currently active, then an alternate output is printed
# which explicitly tells the user that the faculty object is not currently active.

    def status_summary(self):
        if self.active == 'y':
            print('Summary:\n{} is a {} member at GMU with g-number {}\n'
                  'Their rank is {} specializing in {}\n'
                  'Their teaching load is {} credit hours per year\n'
                  .format(str(self.name),type(self).__name__,str(self.g_num),
                  str(self.rank),str(self.specialty),str(self.teach_load)))
        else:
            print('Summary:\n{} is a {} member at GMU with g-number {}\n'
                  'Their rank is {} specializing in {}\n'
                  'They are currently NOT active'
                  .format(str(self.name),type(self).__name__,str(self.g_num),
                  str(self.rank),str(self.specialty)))

# The Department class is separate from the Person, Student, and Faculty
# classes because it stores information about Person objects, including
# students and faculty members.

class Department (object):

# Inside the Department class, a 'univ_students' class variable is defined
# which keeps track of the total number of students within the university.
# Each department contains a department code (d_code), department name (d_name),
# capacity, and minimum GPA required. A 'deptPeople' list is created which will be
# used to contain all Student and Faculty objects created and place them in the
# deptPeople list.

    deptCount = 0
    univ_students = 0

    def __init__ (self, d_code = '', d_name = '', capacity = 0, minGPA = 0.0):
            self.d_code = str(d_code)
            self.d_name = str(d_name)
            self.capacity = capacity
            self.minGPA = minGPA
            self.avgGPA = 0.0
            self.num_students = 0
            self.deptPeople = []
            Department.deptCount += 1

# the __str__ method takes the attributes for each Department object and
# prints them in a neat format for the user to see.

    def __str__ (self):
        return('Department Name: {}\nDepartment code: {}\nCapacity: {}\nNumber of Students: {}\n'
               'Minimum GPA = {}\n'.format(str(self.d_name),str(self.d_code),str(self.capacity),
                str(self.num_students),str(self.minGPA)))

# The 'addFaculty' method determines whether the argument being passed is
# of a Faculty object or not. if not, a False is returned. Otherwise, the
# Faculty object is appended to the list and a value of True is returned.

    def addFaculty(self, faculty):
        if not faculty or not isinstance(faculty, Faculty):
            return False, 'Not Added: Invalid or Missing Faculty Object'
        self.deptPeople.append(faculty)
        return True, 'Added'

# The 'isQualified' method determines whether a student object is qualified to be
# added to a department. the 'dupePerson' method is used again to determine if a
# duplicate student object is present. If so, the student object is not added
# and a value of False and reason is returned. Otherwise, return True

    def isQualified(self, other):
        if self.num_students >= self.capacity:
            return False, 'Not Added: The maximum capacity has been reached'
        if not other.isEnrolled():
            return False, 'Not Added: The student is not enrolled'
        if other.gpa() < self.minGPA:
            return False, "Not Added: The student's GPA is too low"
        else:
            if len(self.deptPeople) > 0:
                for person in self.deptPeople:
                    if person.dupePerson(other):
                        return False, 'Not Added: Person already in department'
        return True, ''

# 'addStudent' is responsible for determining if a student is eligible to be
# added ot a department by first checking to see if the argument is of a
# Student object. If it is, run the 'isQualified' method. if a True value is returned,
# set the student's major to whatever it is for that department, add the student to the
# deptPeople list, increment the num_students in the department and the overall univ_students,
# and calculate the average GPA for that department.

    def addStudent (self, student):
        if not student or not isinstance(student, Student):
            return False, 'Not Added: Invalid or Missing Student Object'
        trueOrFalse, reason = self.isQualified(student)
        if trueOrFalse:
            self.deptPeople.append(student)
            student.setMajor(self.d_code)
            self.num_students += 1
            Department.univ_students += 1
            return True, reason
        return False, reason

# 'AvgGPA' is used to determine the average GPA for all the student objects within a particular
# department object. The method only checks for student objects, since they are the only ones
# that have a GPA attribute. Each student object's GPA is added to a running total and then
# divided by the number of students within that department. The result is rounded to the
# nearest two decimal points and returned.

    def AvgGPA (self):
        for student in self.deptPeople:
            if isinstance(student, Student):
                self.avgGPA += student.gpa()
        return round(self.avgGPA / self.num_students, 2)

# The 'printdeptPeople' method categorizes the group of people that are to be printed. by
# default, a value of 'a' is assigned so that if the user leaves the argument blank, it prints
# a list of all PEOPLE within a certain department. If an argument of 's' is passed, the method
# prints all STUDENTS within that department. If an argument of 'f' is passed, then print all
# FACULTY objects within that department.

    def printdeptPeople (self, group = 'a'):
        if group == 's':
            print('\nList of all STUDENTS in {} department:\n'.format(self.d_name))
            print('-'*50)
        elif group == 'f':
            print('\nList of all FACULTY in {} department:\n'.format(self.d_name))
            print('-'*50)
        else:
            print('\nList of all PEOPLE in {} department:\n'.format(self.d_name))
            print('-'*50)

        for person in self.deptPeople:
            if group == 'a':
                person.status_summary()
            if group == 's' and isinstance(person, Student):
                person.status_summary()
            if group == 'f' and isinstance(person, Faculty):
                person.status_summary()

# Start of global code where test input has been provided by the instructor. The main purpose of
# the code below is to test several cases from the code above in order to verify integrity and
# accuracy of the results.


print('\nStart of Department, Person, Student, Faculty Class test run ***********')
print('\n1. Create 14 student objects for use in the demo ')
s1 = Student('G34568', 'David Miller', '321 Maple Lane, Vienna, VA',
      '571-285-4567', 'dmiller8@gmu.edu',
      status = 'sophomore', major = 'Hist', enrolled = 'y',
      credits = 30, qpoints = 90)           
s2 = Student('G21345', 'Sonia Fillmore', '123 Oak Street, Potomac, MD',
      '301-285-4567', 'sfillmor8@gmu.edu',status = 'senior', major = 'Math',
      enrolled = 'y', credits = 90, qpoints = 315)
s3 = Student('G42156', 'Chris Squire', '4567 Park Lane, London, UK',
      '425-285-4567', 'csquire8@gmu.edu',status = 'sophomore', major = 'Musc',
      enrolled = 'y', credits = 45, qpoints = 160)
s4 = Student('G10928', 'Tal Wilkenfeld', '423 Outback Way, Sydney, AU',
      '524-485-5674', 'twilkenfeld@AU.gov',status = 'junior', major = 'Musc',
      enrolled = 'y', credits = 75, qpoints = 250)    
s5 = Student('G22157', 'Larry Graham', '1240 Pacific Road, Loa Angeles, CA',
      '231-44-2596', 'grahamcentralsta@gmail.com', status = 'senior',
      major = 'CHHS', enrolled = 'y', credits = 105, qpoints = 320)           
s6 = Student('G31345', 'John Entwistle', '6 Stable Way, Leeds, UK',
      '416-223-1967', 'johnwho@apple.com', status = 'freshman', major = 'CSci',
      enrolled = 'y', credits = 15, qpoints = 35)
s7 = Student('G44568', 'Esperanza Spalding', '9122 King Hwy, Upper Marlboror, MD',
      '310-247-1954', 'esperanza@jazzy.org', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 65, qpoints = 250)           
s8 = Student('G55345', 'Tim Bogert', '2713 Santa Monica Blvd, Venice, CA',
      '912-333-1968', 'vfudge@yahoo.net', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 160)
s9 = Student('G66113', 'Gordon Sumner', '145 Nigel Path, Manchester, U.K.',
      '011-11-0203-2202', 'sting@police.com', status = 'freshman', major = 'Musc',
      enrolled = 'y', credits = 15, qpoints = 45)           
s10 = Student('G11311', 'Paul McCartney', '422 Hagis Road, Edinburgh, U.K.',
      '481-221-1970', 'paullinda@wings.org', status = 'senior', major = 'ARTS',
      enrolled = 'y', credits = 110, qpoints = 275)
s11 = Student('G22111', 'Elizabeth Smythe', '2215 Yonge Street, Toronto, CA',
      '416-676-2983', 'esmythe12@ontario.gov', status = 'junior', major = 'ENGR',
      enrolled = 'y', credits = 85, qpoints = 250)
s12 = Student('G31312', 'John McVie', '27 Casino Lane, Monte Carlo, Monico',
      '011-56-2233-9945', 'johnmac@blues.net', status = 'sophomore', major = 'Hist',
      enrolled = 'y', credits = 45, qpoints = 120)
s13 = Student('G31312', 'Nawt Enrolled', '13 Failed Street, Cantenroll, AZ',
      '320-445-2938', 'nenrolled@gmu.ed', status = 'sophomore', major = 'Hist',
      enrolled = 'n', credits = 45, qpoints = 120)
s14 = Student('G11112', 'Toolow G. Peyay', '1313 LowGrade Drive, Mustwait, NE',
      '678-901-2345','Toolowgpa@gmu.edu', status = 'freshman', major = 'Undc',
      enrolled = 'y', credits = 20, qpoints = 38)           
f1 = Faculty('G98765', 'Gene Shuman', '3062 Covington Street, Fairfax, VA',
             '571-235-2345', 'gshuman@gmu.edu', 'Assistant Professor', 'y',
             18, 'teaching', 2017)     
f2 = Faculty('G56789', 'A. Einstein', '2741 University Blvd, Priceton, NJ',
             '212-346-3456', 'aeinstein@gmu.edu', 'Professor', 'y',
             6, 'research', 1938)

print('List of Students and Faculty created-----------------------------: ')
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
print('f1= ', f1)
print('f2= ', f2)
d1 = Department('ENGR', 'Engineering', 5, 3.0)
d2 = Department('ARTS', 'Art and Architecture', 10, 2.5)
d3 = Department('CHHS', 'College of Health and Human Services', 3, 2.75)

input('\n2. Hit "Enter" to see the list of departments created ')
print('\n\nDepartments established-------------------------:')
print(d1)
print(d2)
print(d3)

input('\n\n\n\n3. Hit "Enter" to add s1 - s5 to ENGR Department- print Dept. personnel follows\n')
d1.addStudent(s1)      
d1.addStudent(s2)
d1.addStudent(s3)
d2.addStudent(s4)
d1.addFaculty(f1)
d1.addFaculty(f2)
d1.addStudent(s4)
d1.addStudent(s5)

print ('\nTenure of f1: ', f1.tenure())
print ('\nTenure of f2: ', f2.tenure())
a, b = d1.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, ' - over capacity, ret values: ', a, b)
input('\n\n\n\n4. Hit "Enter" to add additional students to various departments -------------------:')
print('\nAttempting to add ', s6.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
print('\nDepartment ', d1.d_name, ' student roster is now: ')
d1.printdeptPeople()
      
input('\n\n\n\n5. Hit "Enter" to add two students to the ARTS Department ')
a, b = d2.addStudent(s6)
print('\nAttempting to add ', s6.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s7)
print('\nAttempting to add ', s7.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d2.printdeptPeople()

input('\n\n\n\n6. Hit "Enter" to add two student to the CHHS Department' )
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s9)
print('\nAttempting to add ', s9.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
d3.printdeptPeople()

input('\n\n\n\n7. Hit "Enter" to try adding a student with low GPA to CHHS')
a, b = d3.addStudent(s14)
print('\nAttempting to add ', s14.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\n8. Hit "Enter" to try to add a non-enrolled student to the CHHS Department')
a, b = d3.addStudent(s13)
print('\nAttempting to add ', s13.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

input('\n\n\n\n9. Reactivate nonenrolled student, then add them to the CHHS Department')
s13.activate( )
a, b = d3.addStudent(s13)
print('\nAttempting to add ', s13.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)

input('\n\n\n\n9. Hit "Enter" to try adding a duplicate student ')
a, b = d3.addStudent(s8)
print('\nAttempting to add ', s8.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)


input('\n\n\n\n10. Hit "Enter" to add s10 to ENGR, s11 to ARTS, s12 to CHHS, then print all 3 ')
a, b = d1.addStudent(s10)
print('\nAttempting to add ', s10.name, ' to ', d1.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d2.addStudent(s11)
print('\nAttempting to add ', s11.name, ' to ', d2.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
a, b = d3.addStudent(s12)
print('\nAttempting to add ', s12.name, ' to ', d3.d_code, ' result: ')
print('\t\t\treturn values: ', a, '  reason code: ', b)
input ('\n\n\nHit "Enter" to see all personnel for all departments')
d1.printdeptPeople()
d2.printdeptPeople()
d3.printdeptPeople()

input ('\n\n\nHit "Enter" to see all personnel divided by students and faculty')
d1.printdeptPeople('s')
d1.printdeptPeople('f')
d2.printdeptPeople('s')
d2.printdeptPeople('f')
d3.printdeptPeople('s')
d3.printdeptPeople('f')



print('\n\n\n***** End of Student class demo **********')
