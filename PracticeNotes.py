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

# tup = (1,1,2) # This is a tuple as it is enclosed in parenthesis



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

# import random
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

# The filter function tests a specific user-defined condition for a function and returns an iterable for the 
# elements and values that satisfy the condition or, in other words, return true.
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

# class student:
#     fees = 2390 # This is a class variable and it is shared by everyone
#     pass # This pass function is used when we want to leave something blank

# himanshu = student()
# rohan = student()

# himanshu.name = "Himanshu Tripathi" # This is an instance variable(It is the property of this object only)
# himanshu.standard = 8
# himanshu.div = "D"

# rohan.name = "Rohan Das"
# rohan.standard = 8
# rohan.div = "A"

# print(himanshu.name)

# print(student.fees)
# student.fees = 2000 # This will change the fees of every object in the class
# print(student.fees)
# rohan.fees = 1900 # This will change the fees of rohan only
# print(rohan.fees)

# print(rohan.__dict__) #This will print all the variables of rohan in the form of a dictionary


    # Self and __init__() functions in Python 

# class Employee:

# self is the name of the object
#     def __init__(self, name, salary, age): # This will run automatically when the object is created 
#         self.name = name
#         self.salary = salary 
#         self.age = age

#     def printdetails(self):
#         return f"The name of the Employee is {self.name}. Salary is: {self.salary} and age is {self.age}."

# harry = Employee("Haris Ali Khan", 800000, 25) 
# print(harry.printdetails()) #This will run the function and pass the object automatically to the function because the function contains self 


    # Class Method and other methods in Python

class emp:
    leaves = 5
    
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age
    
    def printdetails(self):
        return f"The name is: {self.name}. The salary is: {self.salary} and the age is: {self.age}"

    @classmethod
    def change_leaves(cls, no): #cls here means class name
        cls.leaves = no 

    @classmethod
    def from_slash(cls,string): # Class Methods as alternative constructor
        return cls(*string.split("/"))

    @staticmethod # We use staticmethod when we want to make a function that neither takes self or cls 
    def printsome(stat):
        print(stat)
        

himanshu = emp("Himanshu", 99999, 13)

# himanshu.change_leaves(6) #This will change the number of leaves of the whole class 
# print(himanshu.leaves)
# print(emp.leaves)


    # Class method as alternative constructor

# See function named "from_salsh" in the previous section

RohanDas = emp.from_slash("Rohan Das/10000/15")
# print(RohanDas.name)
# print(RohanDas.salary)
# print(RohanDas.age)


    # Static Methods(Decorator) 
    
# RohanDas.printsome("Rohan is a good boy")


    # Single inheritance 

class programmer(emp): # This class inherits all the functions and properties of emp class

    def __init__(self, name, salary, age, progLang):
        self.name = name
        self.salary = salary
        self.age = age
        self.prolang = progLang

    def printprog(self):
        return f"Name: {self.name} \n Salary: {self.salary} \n Age: {self.age} \n Programming Languages: {self.prolang}"

anshu = programmer("Anshu", 1000000, 20, ["Python", "C++"])
# print(anshu.printprog())


    # Multiple inheritance 

class player:
    leaves = 6

    def __init__(self, name, game):
        self.name = name
        self.game = game 

    def printdetails(self):
        return f"The name of the player is {self.name} and game(s) is/are: {self.game}"


class progamer(emp, player): # Here the presidency for the constructor goes to the class inherited first, i.e. emp  
    leaves = 7 #This has the presidency even if this variable is present in other inherited class too

ankit = progamer("Ankit", 100000, 18)
# print(ankit.age)
# print(ankit.leaves)


    # Multilevel Inheritance 

class cricketer(progamer): # Constructor of emp class
    pass
# This class inherited the progamer class and as the progamer class inherited other classs, this class also inherited those classes

aniket = cricketer("Aniket", 20000, 16)
# print(aniket.leaves)
# print(aniket.printdetails())


    # Private, Public and Protected access specifiers 

# class Pri:
#     pub = 1 # This is a public variable
#     _pro = 2 # This is a protected variable which can be accessed only by the class itself and the classes derived from it
#     __pr = 3 # This is a private variable and it is only accessible by the class itself 

# rishabh = Pri()
# print(rishabh.pub) # Accessing the public variable of the class by its object
# print(rishabh._pro) # Accessing the protected variable of the class

# print(rishabh.__pr) # This will throw error. Python doesn't has functions like Java to protect its private variables, so python uses the concept of data mangling, i.e. stores the variable in a different name. 

# print(rishabh._Pri__pr) # Accessing the private variable of the class 


    # Overriding in Python

# class A:

#     classvar1 = "I am a class variable in class A"

#     def __init__(self):
#         self.var1 = "I am in class A's constructor"
        # self.special = "I am Special "
        # self.classvar1 = "I am the instance variable of A's object" # This will be the value of classvar1 if we make an object, but, when we comment out this line, then the class variable will be printed. This is function overriding.

# class B(A):

#     def __init__(self):
#         super().__init__() # This will run the constructor of class A
        # But, if we want to change some varibles then we can do that 
        # self.var1 = "I am in class B's constructor" 
        # self.var2 = "This is a new variable"

        # print(super().classvar1) # This will print the class variable of class A
        # print(self.classvar1) # But, this will print the instance variable of the object 

# ObjB = B()
# print(ObjB.var1)
# print(ObjB.var1)
# print(ObjB.special)


    # Diamond-Shape Problem 
# https://www.youtube.com/watch?v=mEF_vVNTPUY&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=67


    # Operators overloading and dunder methods in Python 
# Functions starting and ending with double underscore(__) are called dunder methods.
 
# class C:

#     def __init__(self, name, salary): # This is a dunder method
#         self.name = name
#         self.salary = salary

#     def __repr__(self): # If we comment out the function __str__, then this function will be used 
#         return "This is __repr__"

#     def __str__(self): 
#          return "This is __str__"

#     def __add__(self,other): # This is an example of operator overloading
#         return self.salary + other.salary 

# c1 = C("c1", 5000)
# c2 = C("c2", 10000)
# print(c1 + c2) # If we comment out the function __add__ then this will throw error
# print(c1) # By default, the  __str__ function will be used 
# print(repr(c1)) # Using the __repr__ function


    # Abstract Base Class & @abstractmethod

# from abc import ABC, abstractmethod

# @abstractmethod is a decorator that is used to ensure that the child class of a parent class has the given functions
# Ex - Shown Below 
# class abs(ABC):

#     @abstractmethod 
#     def printdetails():
#         pass

# class abs2(abs):
#     def __init__(self,name):
#         self.name = name 
    
#     def printdetails(): # This function must be present or the program will throw error
#         pass

# s = abs2("Abstract")


    # Setter and Property decorators in Python
# https://www.codewithharry.com/videos/python-tutorials-for-absolute-beginners-69

# class Employee:
#     def __init__(self, fname, lname):
#         self.fname = fname
#         self.lname = lname
#         # self.email = f"{fname}.{lname}@codewithharry.com"

#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"

#     @property
#     def email(self):
#         if self.fname==None or self.lname == None:
#             return "Email is not set. Please set it using setter"
#         return f"{self.fname}.{self.lname}@codewithharry.com"

#     @email.setter
#     def email(self, string):
#         print("Setting now...")
#         names = string.split("@")[0]
#         self.fname = names.split(".")[0]
#         self.lname = names.split(".")[1]

#     @email.deleter
#     def email(self):
#         self.fname = None
#         self.lname = None


# hindustani_supporter = Employee("Hindustani", "Supporter")
# nikhil_raj_pandey = Employee("Nikhil", "Raj")

# print(hindustani_supporter.email)

# hindustani_supporter.fname = "US"

# print(hindustani_supporter.email)
# hindustani_supporter.email = "this.that@codewithharry.com"
# print(hindustani_supporter.fname)

# del hindustani_supporter.email
# print(hindustani_supporter.email)
# hindustani_supporter.email = "Harry.Perry@codewithharry.com"
# print(hindustani_supporter.email)


    # Object Introspection in Python

# Introspection ---> Introspection means ability to recognize an object along with its properties

# Ways of introspection -
# We are just going to see three ways 

# print(type("This is a string")) # Way no. 1. . This will print the datatype of the string.
# print(id("This is id")) # Way no. 2 . This will print the id where the object is stored.
# print(dir("This is dir")) # Way no. 3 . This will print the attributes of the string. 


    # Generators in Python 
"""
Iterable - Which can be iterated. Functions defined - __iter__() or __getitem__() 
Iterator - Fuction defined - __next__() 
Iteration -
"""

# def iter(n):

    # for i in range(n):
        # yield i
        # print(i)

# g = iter(3) 
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__()) # This line will throw error

# for i in g:
#     print(i)


    # Comprehensions in Python 

# Comprehension -- Comprehension means compressing the code and making a four or five lines of code into a one-liner.

# List comprehension

# li10 = [ist for ist in range(10) if ist%2==0] # This is list comprehension where we have made a four to five lines of code into one-liner.
# print(li10)

# Dictionary comprehension  

# dic8 = {key:f"item {key}" for key in range(15) if key%3 == 0} # Dictionary comprehension
# print(dic8)

# dic9 = {value:key for key,value in dic8.items()} # Reversing the dictionary
# print(dic9)

# Set comprehensions 

# set1 = {ite for ite in ["Harry","Himanshu",
#                         "Harry","Himanshu"]} # Set comprehension
# print(type(set1))
# print(set1)

# Generator comprehension 

# gener = (insp for insp in range(20) if insp % 5 == 0) # Generator comprehension
# print(type(gener))
# print(gener.__next__())
# print(gener.__next__())
# for items in gener:
#     print(items)


    # Else with For loop in Python
# The else statement is executed in a for loop when the for loop ends normally i.e. without break statement

# for item in l1:
#     if item == "chopsticks":
#         print("Item Found")
#         break

# else:
#     print("Item not found") #If break statement executed, then this line will be printed


    # Function Caching in Python

# import time
# from functools import lru_cache

# @lru_cache(maxsize=3) # This will store the latest 3 calls of the function below
# def someTime(n):
#     time.sleep(n)

# print("Calling...")
# someTime(3) # This will be cached in the memory but will not take time when it is called again
# print("Done!")

# print("Calling again...")
# someTime(3) # This will not take time again as python stored or cached the last call 
# print("Done!!")


    # Else & Finally in Python

# try:
#     f = open("does.txt")

# except IOError as e:
#     print("IO error occured")

# except EOFError as e: # There could be more than one except statements
#     print("EOF error occured")

# else: # This will be executed if the except statement is not executed 
#     print("No except executed")

# finally: # This will be printed anyway i.e. either the except statement gets executed or not it doesn't matter
#     print("This will be printed anyway")

# print("Done")


    # Coroutines in Python
# Coroutines are used when we want a function to not to read data again and again which consumes time

# def cor():
#     text = "This is a big text which contains some words"
#     import time
#     time.sleep(2) # Just suppose that this is a task that takes 2 seconds

#     while True:
#         given = (yield)
#         if given in text:
#             print("Word found")
#         else:
#             print("Not found")

# corou = cor()
# corou.__next__()
# corou.send("big")
# input("Press any key")
# corou.send("This")
# corou.close()

# print("Program ended")

    # OS Module in Python

# import os

# print(dir(os))
# print(os.getcwd())
# os.chdir("C://")
# print(os.getcwd())
# f = open("harry.txt")
# print(os.listdir("C://"))
# os.makedirs("This/that")
# os.rename("harry.txt", "codewithharry.txt")
# print(os.environ.get('Path'))
# print(os.path.join("C:/", "/harry.txt"))

# print(os.path.exists("C://Program Files2"))
# print(os.path.isfile("C://Program Files"))


    # Request module for HTTP Requests

# import requests

# url = "www.somewebsite.com"
'''
data = {
    "emailaddress" : "email@email.com",
    "password" : "passwordHere"
}
'''
# req = requests.post(url=url, data=data)
# print(req.content)

# r = requests.get("http://codingwithhimanshu.epizy.com")
# print(r)
# print(r.text) # This will print all the code of the given web page
# print(r.status_code) # This will print the status code


    # Json module in Python - https://www.youtube.com/watch?v=9U4dHBOzmaE&list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME&index=83


    # Pickle module  in Python

# import pickle
# Pickling means preserving. We use the pickle module in Python for the same purpose.

# Pickling a file
# lis1 = ["Himanshu","Ankit","Anshu"]
# fil = "him.pkl"

# fileObj = open(fil,"wb")
# pickle.dump(lis1,fileObj)
# fileObj.close()

# # Unpickling a file
# file = "him.pkl"

# filObj = open(file,"rb")
# txt = pickle.load(filObj)
# print(txt)
# filObj.close()


    # Raise in Python 
# Raise - Raise is used when we want to raise an error and terminate the program 

# name = input("Enter your name ")
# if name == "Himanshu":
#     raise NameError("Himanshu is blocked") # This will raise an error 
