# print("Hello World")

'''this 
is  a 
multi line
comment'''

# line = '''multiline 
# string'''
# print(line)


    #Exercise 1 - Changing a given string's first letter to capital

# name = "himanshu"
# fLetter = name[0]
# fLetter = fLetter.upper()
# name = fLetter + name[1:]
# print(name)
# or
# print(name.capitalize()) #The above exercise can also be written like this 

    #String methods
# print(len((name)))
# print(name.strip())
# print(type(name))
# print(name.replace("himanshu", "tanvi"))

# a = 3
# print(float(a))
# print(type(a))


    #Just for practice
# inpnum = input()
# print (type(inpnum))
# inpnum = int(inpnum)
# print(type(inpnum))
# print(name[0:8:2])# This will print characters till the 7th letter(according to python) with skipping 1 letter
# print(name[::2])# It can also be written like this

    #Lists and its methods in python

# grocery  = ["Bhindi", "Lauki", "Parwal", 56] #This is a mixed list1
# print(grocery) #This will print the list
# print(grocery[2]) #This will print an item of the list
# print(grocery[9]) #This will throw an error


listofnum = [4, 354,6, 647, 7, 12, 67]
alphabets = ['a','c','j','h','a','b','t','h']
alphabets1 = ['o','s','w','q','z','v','x','s']
# listofnum.sort() #This will set the numbers of the list in ascending order
# listofnum.reverse() #This will set the numbers of the list in descending order
# print(listofnum) #This will print the list
# print(listofnum[::2]) #This is the same as string methods
# priint(len(listofnum)) #This will print the length of the list
# print(max(listofnum)) #This will print the greatest no. pf the list
# print(min(listofnum)) #This will print the smallest no. pf the list
# print(min(grocery)) #This will throw an error because the list contains a string

# listofnum.append(69) #This will add an item in the end of the list
# print(listofnum)

# listofnum.insert(2,5) #This will include a given item after the 2nd item
# print(listofnum)

# listofnum.pop() #This will remove the last item of the list
# print(listofnum)

# listofnum.remove(5) #This will remove 5 from the list
# print(listofnum)

# listofnum[0] = 8
# print(listofnum)

# newlist = listofnum #A list can be copied using the = operator. 
# print(newlist)

# newlist = listofnum.copy() #This will also copy the list
# print(newlist)

# newlist = listofnum[:] #This will also copy the list
# print(newlist)

# listofnum.clear() #This will clear the list
# print(listofnum)

# count = alphabets.count('h') #This will count the number of 'h' in the list
# print(count)

# alphabets.extend(alphabets1) #This will extend the list
# print(alphabets)

# alphabets += alphabets1 #This will also extend the list -->  a = a + b
# print(alphabets)

# index = alphabets.index('a') #This will give the place value where 'a' is i.e. 0 . If 'a' is not present in the list then this will throw an error
# print(index)

# tup = (1,1,2) # This is a tuple because it is enclosed in parenthesis



    # Swapping in Python
    
# a = 1
# b = 7

# temp = a
# a = b
# b = temp

# a, b = b, a   #Swapping can also be done like this in Python


    #Dictionaries in python

d1 = {"Ram Pyaare":"Roti",
"Mohan Pyaare":"Chawal",
"Pyaare Mohan":"Fish",
"Mohan":{"breakfast":"roti",
"lunch":"chawal",
"dinner":"fish"}} # This is a dictionary within another dictinary
# print(d1)

# print(type(d1)) #This line will prove that d1 s a dictionary

# d1 ["Ankit"] = "junk food" #This is used to update a dictionary
# d1.update({"anikt":"toffee"}) #This will also update the dictionary

# print(d1.keys()) #This will print all the keys present in the dictionary
# print (d1.items()) #This will print key-value pairs

# print(d1["Mohan Pyaare"]) #This will print Mohan Pyaare's value

# print(d1.get("Mohan Pyaare")) #This is also used to print the value of a key

# print(d1["Mohan"]) #This will print Mohan's value which is a dictionary

# print(d1["Mohan"]["breakfast"]) #This will print the value of "breakfast" which is present in Mohan's dictionary


del d1["Pyaare Mohan"] #This will delete "Pyaare Mohan" from the dictionary
# print(d1)

     # Difference between "=" and ".copy()" function

# d3 = d1 #If we change d3 then the contents of d1 will also be changed because d3 is a pointer which is pointing to d1
# d3 ["Himanshu"] = "Maggie"
# print("This is d1:",d1) #d1 is affected here
# print("This is d3:",d3) #And d3 is also affected

# d2 = d1.copy() #In this case, if we change d2, then d1 will not get changed
# d2 ["Anshu"] = "Daal"
# print("This is d1:",d1) #d1 is not affected here 
# print("This is d2:",d2) #Only d2 is affected


    # Sets in Python

    # Set is just like a list but if a duplicate data is present in the list then the duplicate one will not get printed

li = [1, 2, 3, 4, 5] #This is a list
s = set(li) #This is a set
# print(type(s)) #This line will prove  that this "s" is a set
# s.add(6) #This will add 6 in the set
# s.add(1) 
# print(s) #This will not print 1 two times because it is already present 
# s.remove(2) #This will remove 2 from the set
 

    # If-Else Ladder in Python
# print("Enter a number")
# in1 = int(input())
# if in1>100:
#     print("The number is too big")
# elif in1 in s:
#     print(in1, "is in the set")
# else:
#     print(in1, "is not in the set")
# print("")
# print("If-Else Ladder ended here")


    # Loops in Python
        # For Loop 

# list1 = ["Himanshu",  "Tanvi", "Ankit", "Anshu"]

# for item in list1: # Any variable name can be used in place of "item"
#     print("The name of the student is:",item) # This line will be executed until the list ends


# list2 = [["Himanshu", 1], ["Tanvi", 10], ["Ankit", 2],["Anshu", 4]]

# for item1, lollipop in list2: 
#     print("The name of the student is:", item1, "and lollipops eaten by the student is:",lollipop)


# list3 = [["Himanshu", 1], ["Tanvi", 10], ["Ankit", 2],["Anshu", 4]]
# dict1 = dict(list3)

# for item2, lollipop2 in dict1: 
#     print("The name of the student is:", item2, "and lollipops eaten by the student is:",lollipop2) 
#This loop will throw error 


# list3 = [["Himanshu", 1], ["Tanvi", 10], ["Ankit", 2],["Anshu", 4]]
# dict1 = dict(list3)
# print(dict1)

# for item2, lollipop2 in dict1.items(): 
#     print("The name of the student is:", item2, "and lollipops eaten by",item2,"is:",lollipop2) 
#This will not throw error because .items() function is used here

    # Quiz -- Create a list and print all the numbers present in the list which are bigger than 6 using For loop

# Sol-
# qlist = [int, float, "Himanshu", 5, 78, 675, 67, 92, 40, 2, 1]

# for variable in qlist:
#     if str(variable).isnumeric() and variable>6:
#         print(variable)


        # While Loop

# i = 0

# while(i<10):
#     print("The value of i is:",i)
#     i = i + 1

# while (True):
#     a = int(input("Enter your number ")) # This is an infinite loop

        # Break and Continue statements in Python
        # Break - Comes out of the loop 
        # Continue - Skips the current iteration and prints the next one 

# wha = 1
# while (True):
#     if wha < 10:
#         wha = wha + 1
#         continue
#     else:
#         wha = wha + 1
#         print(wha)
#         if wha == 50:
#             break


    # Python Game 
    # Guess the number game

# number = 18
# guessesLeft = 9
# while (guessesLeft > 0):
#     print("Enter your guess: ")
#     guess = int(input())
#     guessesLeft = guessesLeft - 1
#     if guess == number:
#         print("Congratulation! You won!!!")
#         print("No. of guesses taken: ",9-guessesLeft)
#         win = "You"
#         break
#     elif guess > number:
#         print("The correct number is smaller than your guess.")
#         print("Number of guesses left:",guessesLeft)
#         print("")
#         win = "none"
#         continue
#     elif guess < number:
#         print("The correct number is greater than your guess.")
#         print("Number of guesses left:",guessesLeft)
#         print("")
#         win = "none"
#         continue
#     else:
#         print("Unknown Error!")
#         win = "none"
#         break

# if guessesLeft == 0 and win == "none":
#     print("You Lost!!!")
# else:
#     print("")


    # Membership Operators

# memoper = [3, 3,2, 2,39, 33, 35,32] #This is a list
# print(32 in list) #This will return true because 32 is in the list
# print(32 not in list) #This will return false because 32 is in the list and the statement states that it is not
# print(325 in list) #This will return false because 325 is not in the list
# print(325 not in list) #This will return true 


    # If-Else short-hand
# print("Enter first number")
# frstnum = int(input())
# print("Enter second number")
# scndnum = int(input())

# print("First Number is bigger than the Second Number") if frstnum > scndnum else print("Second Number is bigger than the First Number") #This is If-Else short-hand


    # Functions in Python

# def func1():
#     print("Hello this is a function")

# func1() #This line will run the function

# def func2(am, are): #This function takes two values
#     print("Sum of am and are is: ", am + are)

# func2(2, 3) #This will pass 2 and 3 to func2 which will be stored in am and are

# def func3(u,v):
#     av = (u+v)/2
#     return av #This will return the value of av to gv 

# gv = func3(4, 8)
# print("The average is:",gv) #This will print the value of gv


    # Docstring in Python

# def func4(u,v):
#     """This is a dostring"""
#     bv = (u+v)/2
#     return bv 

# pv = func4(9, 5)
# print("The average is:",pv) 
# print(func4.__doc__) #This line will print the docstring present in func4


    # Try-Except exception handling in Python

# number1 = input("Enter the first number: ")
# number2 = input("Enter the second number: ")

# print("The sum is:",int(number1) +int(number2)) #This will print the sum but if the user enters string as the input then this line will throw error and the program will be terminated
# print("This is a very important line")
# To prevent this problem, we use try and except Exception


# number3 = input("Enter the first number: ")
# number4 = input("Enter the second number: ")

# try: #This statement will try to print the statement below. But if any error occurs then the except statement will be executed
#     print("The sum is:",int(number3) +int(number4)) 

# except Exception as error: #The error statement will be stored in the variable named "error" 
#     print(error)
#     error = "Please enter a valid input the next time"
#     print(error)
# print("This line is very important")


    # File IO basics

"""
"r" - The r mode is used to read a file.

"w" - The w mode is used to write something in the file and if the there is already   some data present in the file, then it overwrites it.

"x" - The x mode is used to create a file if it doesn't exists.

"a" - a means append (write in the end). It does the same as the w mode does. But it doesn't overwrites the file. It adds data in the end of the file.

"t" - t mode is used to open our file in text mode and only proper text files can be opened by it. It deals with the file data as a string

"b" - b means binary. This mode can only open binary files. The binary files include images, documents etc.

"+" - The + mode is used to read and write a file simultaneously.
""" 
        # Reading a file 
# f = open("python.txt", "rt")
# content = f.read()
# print(content)

# print(f.read(34)) #This will read the first 34 characters
# print(f.read(34)) #This will read the next 34 characters

# for anything in f: #Anything is a variable
#     print(anything,end="")

# print(f.readline()) #This will read the first line
# print(f.readline()) #This will read the second line
# print(f.readline()) #This will read the third line

# print(f.readlines()) #This will print all the lines in a list

# for anything in f: #anything is a variable
#     print(anything,end="")

# f.close()


        # Writing to a file

# fr = open("python.txt", "w")
# frin = input()
# fr.write(frin)
# fr.close()

        # Appending to a file
            # Python text editor software--->
# fr2 = open("python.txt", "a")
# print("Start Typing...\n")
# hj = 1
# while (True):
#     frin = input()
#     if frin == "#close":
#         break
#     else:
#         if hj == 1:
#             hj = 2
#             fr2.write(frin)
#         else:
#             fr2.write("\n")
#             fr2.write(frin)
# fr2.close()
# hj = 1
# print("Note written successfully")


        # Reading and writing simulatneously

# fr1 = open("python.txt", "r+")
# print(fr1.read())
# fr1.write("Himanshu is a good boy.")
# fr1.close()


    # Python Exercise

# noOfRow = int(input("Enter the no. of rows: "))
# boolVal = int(input("Enter 0 or 1: "))
# boolVal = bool(boolVal)
# if boolVal == True:
#     i = 1
#     while(i<=noOfRow):
#         print("*" * i)
#         i = i+1
# else:
#     i = noOfRow
#     noOfRow = 1
#     while(i>=noOfRow):
#         print("*" * i)
#         i = i-1


    # seek and tell functions in python

# f = open("python.txt", "r")

# print(f.tell()) #The tell function is used to know where the file handle is
# print(f.readline())

# print(f.tell()) 
# print(f.readline())

# f.seek(0) #The seek function is used to change the location of file handle
# print(f.tell())
# print(f.readline()) #The first line will be printed here because the location of file handle has been changed
# f.seek(0)
# f.close()


    # Using With Block to open file 

# with open("python.txt") as f: #If we use with block then there is no need to use close function
#     print(f.readlines())


    # Global and Local variables

# gl = 7 # This is a global variable as it is not inside any function
# gi = 8


# def function10():

    # gl = 8 # This is a local variable as it is inside a function 
    # gk = 9

    # print(gl) # This will print 8
    # print(gk) # gk could be printed here as it is the local variable of this function

    # print(gi) #This will print gi even if it is a global variable because global variables are read-only

    # gi = gi + 93 # This will throw error because gi is a global variable(Comment out this line to maintain the flow)

    #global gi # Now this function has the access to gi and can edit or change its value
    # gi = 98
    # print(gi)

# function10()
# print(gl) # This will print 7
# print(gk) # This line will throw error because gk is a local variable and it can only be accessed inside the function  


    # Lambda or Anonymous functions in Python

# Lambda - Lambda functions are one line functions. Example- 
# add = lambda numO, numT: numO + numT # This is a lambda function
# print(add(5,6)) 


    # Python Modules
# Random -

import random
from typing import Mapping
# randint = random.randint(0,9) #This will generate random 'integer' between 0 and 9
# print(randint)

# randi = [1,2,3,4,5,6]
# choice = random.choice(randi) #This will select any random thing from the given list
# print(choice)

# rand = random.random() * 100 #This will generate any random decimal number betwee 0 to 100
# print(rand)


    # F-string in Python

m = "Tripathi "
an = "Himanshu"

# a = "This is {} {}"
# b = a.format(an,m)

# a = "This is {1} {0}"
# b = a.format(an,m) 
# print(b)

# For editing the variable a, we have to use the format function. This makes the code look messy.
# But if we use f string then we can make the code look better.Ex->

# a = f"This is {an} {m} {4*5}"
# print(a)


    # *args and **kwargs in Python

# Syntax -->
#  def func(normalArguement, *args, **kwargs)
# func(n, *list, **dict)
# If this syntax is not followed then the program will throw error

# Example of *args and **kwargs -- 

# def func11(normalArguement, *li, **dict):

#     print(normalArguement)

#     for i in li:
#         print(i)

#     for key,values in dict.items():
#         print(f"Key: {key} Value: {values}")

# n = "This is a normal variable"
# tli = ["Himanshu", "School", "This"]
# tdict = {"Himanshu":"Human", "Someone":"NoOne"}

# func11(n, *tli, **tdict)


    # Time Module in Python

# import time
# execution = time.time()
# print(execution)


    # Enumerate function in Python 

l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]

# for index, item in enumerate(l1):
#     if index%2==0:
#         print(f"Jarvis please buy {item}")


    # if __name__ == "__main__" in Python 

def func13(a,b):
    return a+b

# print("This is a line") # If we import this file in another program, and use its func13, then this line will also get printed 

# but if we use if __name__ == "__main__", then the lines inside it will not be printed.

# To understand better, check out "Rough.py"
  
# if __name__ == "__main__":
#     print("This is also a line")


    # Join function in Python

li9 = ["Himanshu", "Ankit", "Anshu", "Other"]

# for item in li9:
#     print(f"{item} and ", end = "")

# To do the same task, we can also use join funtion
# a = " and ".join(li9)
# print(a)


    # Map, Filter and Reduce in Python

li = ["9", "8", "5", "2", "1"]

#  -- Map --

# If we want to apply a function to all the items of a list without using loop, then we can use map function

li = list(map(int, li)) #This will typecast all the items of the list to integer
# print (li)

# We can also use a function or Lambda function in map

# print(list(map(lambda x: x*x, li)))

# -- Filter --
# def grter(n):
#     return n>4

# The filter function tests a specific user-defined condition for a function and returns an iterable for the elements and values that satisfy the condition or, in other words, return true.
# greater = list(filter(grter,li))
# print(greater)

# -- Reduce --

# Reduce functions apply a function to every item of an iterable and gives back a single value as a resultant

# from functools import reduce
# m = reduce(lambda x,y: x*y, li)
# print(m)


    # Decorators in Python

# def caller(func16): #This is a function that takes the name of a function and then runs the function.
#     def runner():
#         print("This is a line")
#         func16()
#         print("Program Executed")
#     return runner

# @ caller #This is a decorator
# def this():
#     print("This is a function")

# this = caller(this) # Instead of doing this, we can use decorator
# a = this()

# We can use the above function called caller when we want to do the same thing for many functions. Ex -
# Printing some lines after or before a function (as shown above)


    # Object and Classes in Python

class student:
    fees = 2390 # This is a class variable and it is shared by everyone
    pass # This pass function is used when we want to leave something blank

himanshu = student()
rohan = student()

himanshu.name = "Himanshu Tripathi" # This is an instance variable(It is the property of this object only)
himanshu.standard = 8
himanshu.div = "D"

rohan.name = "Rohan Das"
rohan.standard = 8
rohan.div = "A"

# print(himanshu.name)

print(student.fees)
student.fees = 2000 # This will change the fees of every object in the class
print(student.fees)
rohan.fees = 1900 # This will change the fees of rohan only
print(rohan.fees)

print(rohan.__dict__) #This will print all the variables of rohan in the form of a dictionary