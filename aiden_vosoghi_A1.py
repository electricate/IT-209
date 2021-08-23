# Program File Name: aiden_vosoghi_A1.py
# Assignment #1 (A1): Read, Write, Lists, Dictionaries, Functions
# Author: Aiden Vosoghi

# The purpose of this assignment is to demonstrate basic proficiency
# reading and writing files as well as using dictionaries and functions.
# This program consists of four functions, each of which have their
# own unique set of operations. This assignment also builds upon
# Lab #1. More information below.

# The first function "loadItems" takes the A1input.txt file, reads it,
# and converts the contents into a list of lists. This is done by taking
# each individual line from the file, stripping any unnecessary characters,
# and making each its own list. The resulting list of lists is returned to
# main.

def loadItems():
    f = open("C:/Users/Aiden Vosoghi/Desktop/Important Files/GMU/Fall 2020/IT 209/Assignments/A1input.txt")
    list_of_items = []
    for line in f:
        item_list = line.split(",")
        list_of_items.append(item_list)
        item_list[-1] = item_list[-1].strip()
    f.close()
    return list_of_items

# Function "displayItems" takes the list of lists that was created in
# "loadItems" and formats it nicely. The information is converted from the
# list of lists into each corresponding element separated by columns.

def displayItems(itemList):
    print('{0:4s}  {1:5s}  {2:25s}   {3:8s}'.format('Item No.', 'Item Category',
          'Item Description', '  Price '))
    print('{0:4s}  {1:5s}  {2:25s}  {3:8s}'
          .format('=======', ' =============','===========================', ' ========'))
    for i in itemList:
        print('{0:8s}  {1:13s}  {2:28s}  {3:1s}'.format(i[0],i[1],i[2],i[3]))
    print('\n\n')

# The next function "buildDict" takes the list of lists and converts it into
# a dictionary. However, this is a reverse dictionary, which takes the second
# value of the list (in this case, the category) and assigns that as the key,
# with the values being the item code, description, and price. The dictionary
# is sorted in alphabetical order, starting with the key.

def buildDict(itemList):
    itemDict = {}
    itemList.sort()
    for i in itemList:
        if i[1] not in itemDict:
            itemDict[i[1]] = [[i[0], i[2], i[3]]]
        else:
            itemDict[i[1]].append([i[0], i[2], i[3]])
    return itemDict

# The fourth and final function "writeFile" takes the contents of the
# dictionary and essentially reverts it to the original format similar
# to the A1input.txt file. Each line is appended to a log variable which
# is written to an output file. This file contains the elements of the
# dictionary, but formatted with category, item code, description, and
# price separated by commas. The program then prompts the user to press
# 'Enter' to exit the program.

def writeFile(DS):
    e = open('C:/Users/Aiden Vosoghi/Desktop/Important Files/GMU/Fall 2020/IT 209/Assignments/vosoghiaA1output.txt','w')
    log = ''
    for b in DS:
        for a in DS.get(b):
            log = (b+","+",".join(a) + '\n')
            print(log.strip('\n'))
            e.write(log)
    e.close()
    print('\n\n')
    input('Press "Enter" to exit the program')

# In the main body of the program, 4 lines of code are executed, with
# each line containing a specific function as listed above.

itemList = loadItems()
displayItems(itemList)
DS = buildDict(itemList)
writeFile(DS)
