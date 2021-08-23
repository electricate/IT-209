# Program File Name: IT209_aiden_vosoghi_A7.py
# Assignment #7 (A7): Extending the Dictionary Class
# Author: Aiden Vosoghi

# The purpose of this assignment is to demonstrate
# working knowledge of extending built-in classes,
# including the dictionary class.

# First, define a list of lists, including movie year and
# the title of the film, along with the category.

movies = [[1965, 'The Sound of Music', 'musical'],
          [1972, 'The Godfather', 'drama'],
          [1977, 'Annie Hall', 'comedy'],
          [1990, 'Dances with Wolves', 'western'],
          [1992, 'Unforgiven', 'western'],
          [2011, 'The Artist', 'comedy'],
          [2012, 'Argo', 'historical'],
          [2013, '12 Years a Slave', 'drama'],
          [2014, 'Birdman', 'comedy'],
          [2015, 'Spotlight', 'drama'],
          [1994, 'Forrest Gump', 'comedy'],
          [1995, 'Braveheart', 'historical'],
          [1997, 'Titanic', 'historical'],
          [1998, 'Shakespeare in Love', 'comedy'],
          [2000, 'Gladiator', 'action'],
          [2002, 'Chicago', 'musical'],
          [2009, 'The Hurt Locker','action'],
          [2010, 'The Kings Speech', 'historical'],          
          [2016, 'Moonlight', 'drama'],
          [2017, 'The Shape of Water', 'fantasy']]

# Create a second list, which will be used later in the
# program to test out adding another list to the existing
# 'NewDict' object.

movies1 = [[1939, 'Gone with the Wind', 'historical'],
          [1976, 'Rocky', 'drama'],
          [1983, 'Amadeus', 'historical'],
          [1980, 'Ordinary People', 'drama']]

# Finally, the 'removeKeys' contains a list of years which
# will be used by the 'removefromlist' method to remove films
# from the 'NewDict' object.

removeKeys = [1990, 2000, 2005, 2010, 2015]

# Create a 'NewDict' class which extends the dictionary built-in
# class and contains a few methods which are used to display, add,
# retrieve, or remove items from the 'NewDict' object.

class NewDict (dict):

# The first method 'displaysorted' displays the information depending
# on the input character. If the input is 'D' or anything else, print
# a display of the keys in sorted order along with their values. If the
# input is 'R', create a list of all the key-value pairs and return it
# to the global code. Otherwise, if the input is 'B', print the key-value
# pairs and append all those key-value pairs to a 'returnList' list, which
# is then returned to the global code.

    def displaysorted(self, ret = 'D'):
        returnList = [ ]
        if ret not in ('D','R','B') or ret == 'D':
            for m in sorted(self):
                print(m,self[m])
        if ret == 'R':
            for m in sorted(self.items()):
                returnList.append(m)
            return returnList
        if ret == 'B':
            self.displaysorted('D')
            self.displaysorted('R')
            return returnList

# 'addfromlist' takes an input list of lists and tries to append it to
# the exisiting movies dictionary. First, the methods checks to see if
# the input is a list type, if not, return False and a reason explaining
# why. If the input is a list of lists, then the method checks to see if
# each individual item is a list type. If not, repeat the same thing as
# above. Otherwise, assign the year as the key and the movie title and
# category as the values. When finished, return True along with 'Added'
        
    def addfromlist (self, L):
        if not isinstance (L, list): return False, 'Not a List!'
        for item in L:
            if not isinstance (item, list): return False, 'Not a List!'
            self[item[0]] = [item[1], item[2]]
            sorted(self)
        return True,'Added'

# The 'retrieve' method takes in a list of years, which act as the keys
# to items within the dictionary. The method first checks to see if the
# input is in fact a list. If not, return False and the reason why.
# Otherwise, the method runs through each item in the list and appends
# the key-value pair that are present in the movie dictionary. If the
# input year cannot be found within the list, then the year and a 'Not Found'
# message are appended to that list. The resulting list is then returned along
# with True.

    def retrieve (self, KL):
        result = [ ]
        if not isinstance (KL, list): return False, 'Not a List!'
        for item in KL:
            if item in self:
                result.append((item, self[item]))
            else:
                result.append((item, 'Not Found'))
        return True, sorted(result)

# The final method within the 'NewDict' class is 'removefromlist'. This method
# first identifies the instance of the input. If the input is a list type, then
# the program loops through the keys of the movie dictionary, deleting the
# key-value pairs that match the input list of keys. The resulting dictionary
# is then returned to the global code.

    def removefromlist (self, listOfKeys):
        removed = [ ]
        if not isinstance (listOfKeys, list): return False, 'Not a List!', removed
        for k in list(self.keys()):
            if k in listOfKeys:
                removed.append((k, self[k]))
                del self[k]
        return True, sorted(removed)

# The code below was provided by the instructor and defines some cases that
# are used to test the code's validity and accuracy.
        
MD = NewDict()
for m in movies:
    MD[m[0]] = [m[1], m[2]]
print('\n\nMovie dictionary built from a list follows...')

for md in MD:
    print(md, MD[md])

print('\n\nMovie dictionary printed using "displaysorted()" method...')
MD.displaysorted()

print('\n\nThe dictionary via "displaySorted("B")" method...')
L1 = MD.displaysorted('B')

print('\n\n')
L2 = MD.displaysorted('L')

print('\n\n"movies1" list..."')
for m in movies1:
    print(m)
    
print('\n\nThe dictionary after "MD.addfromlist(movies1)"...')
MD.addfromlist(movies1)
for m in MD:
    print(m, MD[m])

print('\n\nMovie dictionary printed using "displaysorted()" method...')
MD.displaysorted()

print('\n\nThe list returned after "MD.retrieve([1939, 1960, 1961, 1976, 1992, 2000])"...')
x, L5 = MD.retrieve([1939, 1960, 1961, 1976, 1992, 2000])
for n in L5:
    print(n)

print('\n\nThe dictionary after "MD.removefromlist([1965,1990,2000])"...')
MD.removefromlist([1965, 1990, 2000])
for m in MD:
    print(m, MD[m])

print('\n\nMovie dictionary printed using "displaysorted()" method...')
MD.displaysorted()

input('\nHit "Enter" to end program')