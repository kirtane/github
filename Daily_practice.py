# = it is single line comment
# ctrl + / => multiple line comments
## ctrl + k + c  => 
## ctrl + k + c  => 
 #""" ...... """  => multiple lines

# =================================================
#Developed By : Innovant batch 01
#Date : 11/01/2023
#Purpose : Just program

print("hello")                    #hello
print("5+4")                      # 5+4
print(5+4)                        # 9

import math              # inbuilt module for mathematical calculation
print(math.pi)


from math import pi
print(pi)

# to print folder path of current working directory
import os
print(os.getcwd())

### To use enternal modules
#use pip - from pip we can download any  
#----------------------------------------------------------------------------------------------
                                         # # VARIABLES
a = 10
print(10)            #10
print(a)             #10

a = 20               # variable value is change
print(10)            #10
print(a)             #20

my_text = ""         #here in string we pass nothing
print(my_text)
print('')            # it will print null value o/p is blank

gofwater = 3
gofwater=gofwater+1
print(gofwater)      #o/p is 4
#----------------------------------------------------------------------------------------------
                                      # DATA TYPE
a = 10                #Integer
a = -10               #Integer

a = 10.20             #float
a = -10.20            #Float

a = '10'              #String
a = "hello"           #String
a = '''hello how r u
        thank you'''    #String
print(a)

a = True              #Boolean type, boolean can contain true or false only            
b = False             #Boolean type

a = None              #None type #No specific meaning none only

a = 10
print(a)
type(a)                # type() will accept input and provide type of that value
print(type(a))         # class 'int'>
temptype = type(a)
print(temptype)        #class 'int'>

#-----------------------------------------------------------------------------
                                   #TYPECASTING
print(10 + 10)         #20
print("10" + "10")     #1010
print("10" + 10)       # type error unsuported 

aValue = 10
bValue = 20
print(aValue + bValue)   #20

aValue = 10
bValue = "20"
print(aValue + bValue)   #type error

aValue = 10
bValue = "20"
print(aValue + int(bValue))   #20

aValue = 10
bValue = "20"
print(str(aValue) + bValue)   #here we convert avlue to string so o/p is 1020
aValue = str(aValue)          # here we convert int to string value and store in variable and print it
print(aValue + bValue)

aValue = 10.50
bValue = 20
print((aValue) +float(bValue))   # here for addition bvalue should be float so convert it into flat and then add
print(float(aValue) + bValue)

avalue= 'true'
print(type(avalue))
print(bool(avalue))              # o/p true

avalue= 'false'
print(type(avalue))
print(bool(avalue))            #it always show o/p of any string is true 

avalue= ''
print(type(avalue))
print(bool(avalue))             #empty string value of bool is false
#----------------------------------------------------------------------------------

avalue= 'True'
print(type(avalue))
print(eval(avalue))              # o/p true

avalue= 'False'
print(type(avalue))
print(eval(avalue))            # o/p is false

avalue= ''
print(type(avalue))
print(eval(avalue))             #empty string value of bool is false
#----------------------------------------------------------------------------------------------
# OPERATORS IN PYTHON

a = 10
b = 20
result = a+b
print(result)

a = 10
b = 20
a =  a+b             # ivaluation calculation is always done in right side
print("a=",a,"b=",b)

#2nd way to write assignment operator

a = 10
b = 20
a += b             # it will use assignment op.
print("a=",a,"b=",b)
#------------------------------------------------

a = 10
b = 20
print("a==b", a==b)       #comparison op output is alsway boolean o/p is false
print("a!=b", a!=b)       # o/p is boolean ture
print(a>b)                #o/p false

a=10
b=10
print(a>b)                # o/p is false
print(a>=b)               #o/p is true
#----------------------------------------------------------
#LOGICAL OPERATOR
#IT WORKS IN BOOLEAN

a= True
b= True
print("a and b", a and b)    # o/p is true

a= True
b= False
print("a and b", a and b)    # o/p is true
#---------------------------------------------------
               #AND
a=10
b=20
print("a<10 and b<20", a<10 and b<20)       #o/p false
print("a<10 and b<=20", a<10 and b<=20)     #o/p false
print("a<=10 and b<=20", a<=10 and b<=20)   #o/p true
#-----------------------------------------------------
                 #OR
a=10
b=20
print("a<10 or b<20", a<10 or b<20)       #o/p false
print("a<10 or b<=20", a<10 or b<=20)     #o/p true
print("a<=10 or b<=20", a<=10 or b<=20)   #o/p true
#--------------------------------------------------------
#Logical opertaor always consider any non false value as true
a=10
b=20
print("a and b", a and b)               #o/p 20
print("a or b", a or b)                 #o/p 20
#--------------------------------------------------------------------------------------
#INPUT FUNCTION
#input function always accept input value as string
#1st way
a = input("enter 1st no.=")
b = imput("enter 2nd no. =")
result = a+b
print(result)       # it shows o/p in concate of 2value not addition. becz input fun accepts only string value

a = input("Enter 1st no. =")
b = input("Enter 2nd no. =")
result = int(a) + int(b)
print( result)           #in o/p it shows addition of two inserted values

#2nd way
a = input("Enter 1st no. =")
b = input("Enter 2nd no. =")
print(int(a)+int(b))

#3rd way
print((int(input("enter 1st no. =")) + int(input("enter 2nd no.="))))

#=========================================================================================================
#                                STRING SLICING

avalue = "welcome"
print(avalue)
print(avalue[1])

#to find length of string use len function
strlen = len(avalue)
print(avalue[strlen-1])
print(avalue[0]+ avalue[1]+ avalue[2])    # simple method
print(avalue[0:2])                        #mentos life

#=========================================================================================================
#                              STRING FUNCTION
avalue ="welcome"
print("length of avalue is:" (len(avalue)))


result = avalue.startswith('w')
print(f"{avalue} stsrtwith'w': {result}")          # it will print true

result = avalue.endswith('Come')
print(f"{avalue} stsrtwith'come': {result}")       # it will print false because it is case sensetive

result = avalue.capitalize()
print(f"{avalue} capitalise: {result}")             # it will capital only 1st letter other one samall

result = avalue.upper()
print(f"{avalue} in upper is: {result}")            # all string is in upper case

result = avalue.lower()
print(f"{avalue} in lower is: {result}")             # all string is in lower case

avalue ="welcome"
print(f"length of avalue is: {len(avalue)}")
result = avalue.startswith('w')
print(f"{avalue} stsrtwith'w': {result}")          # it will print true

result = avalue.endswith('Come')
print(f"{avalue} stsrtwith'come': {result}")       # it will print false because it is case sensetive

result = avalue.capitalize()
print(f"{avalue} capitalise: {result}")             # it will capital only 1st letter other one samall

result = avalue.upper()
print(f"{avalue} in upper is: {result}")            # all string is in upper case

result = avalue.find("co")
print(f"index no of 'co' in{avalue}: {result}")       # it will show index no of substring 

result = avalue.find("Co")
print(f"index no of 'co' in{avalue}: {result}")       # it will return -1 in o/p because result not match c capital

result = avalue.find("Co",2,5)
print(f"index no of 'co' in{avalue}: {result}")       # it will return -1 in o/p because result not match c capital

result = avalue.find("e")                             # fiding e 
print(f"index no of 'e' in{avalue}: {result}")        # it will show 1st come e index

result = avalue.find("e",3)                             # fiding 2nd e in string 
print(f"index no of 'e' in{avalue}: {result}")        # it will show 2nd come e index

result = avalue.replace('come','done')                             # fiding 2nd e in string 
print(f" replace 'come' with 'done' in{avalue}: {result}") 

result = avalue.replace('come','done').replace('done','played').upper()   # here we have replay multiple time also convert it into upper case
print(f" replace 'come' with 'done' in{avalue}: {result}")

result = avalue.count(e)                           # fiding 2nd e in string 
print(f" count of 'e' {avalue}: {result}")
#=========================================================================================================
#                                  LISTS
a = 10
print(a,type(a))                 # class 'int

colors = ['Red','Green','Blue','Black','pink']
print(colors, type(colors))       # class 'colors
print(colors[0])                  # o/p is Red, it will accepts index value
print(colors[1])                  # o/p is green, it will accepts index value
print(colors[4])                  # o/p is pink, it will accepts index value
print(colors[-1])                  # o/p is pink, it will accepts index value
print(colors[0:3])                  # o/p is Red, it will accepts index value

#assignment = all operation we perform in string

colors = ['Red','Green','Blue','Black','pink']
newitem = 'White'                 # item assignment
item = colors[3]
colors[4] = 'yellow'               # item assignment
print(colors, type(colors))

avalue = 'welcome'
avalue[3] = 'd'                   #o/p will show error

#there are two data type
#1) mutable = changable / we can modify
#2)Immutable = non changable / cant modify

# String - Immutable          #item assignment is not allowed
#List - Mutable               # item assignment is allowed

#we can not change single or fer element from string
# however we can replace whole string
avalue = 'welcome'
print(avalue)             #o/p welcome
avalue = 'weldome'
print(avalue)             # o/p weldome
#------------------------------------------------------------
avalue = 'welcome'
print(avalue)             #o/p welcome
avalue.replace('c','d')   # in this it direcly not change value c to d because not store in any variable
result = avalue.replace('c','d')
print(result)
#---------------------------------------
#assignment
colors = ['Red','Green','Blue','Black','pink'] reverse the string

avalue = 'welcome'
print(avalue[::-1])
print(avalue[::1])
print(avalue[::-2])
print(avalue[::2])

colors = ['Red','Green','Blue','Black','pink'] reverse the string
print(colors[::-1])
print(colors[::1])
print(colors[::-2])
print(colors[::2])
#----------------------------------------------------------------------------------
                                   #LISTS FUNCTION:

colors = ['Red','Green','Blue','Black','pink'] 
print(len(colors))        # o/p 5 lenghts of lists
print(f"list before sort = {colors}")
result = colors.sort()
print(f"list after sort {colors} = {result}")      # by default it sort in assending order
result = colors.sort()     # for descending

print(f"list before sort = {colors}")
result = colors.reverse()
print(f"list after sort {colors} = {result}")        # it will reverse string

colors.append('voilet')      # it will add extra violet color at the end of string
print(colors)

colors.insert(2,'voilet')      # it will add extra violet color at the index value 2 string
print(colors)

colors.pop()                # it will delete given index value, if index not provide it will delete last index
print (colors)

colors.remove('voilet')    # here it will remove given value. if other than list value pass it will show error
print(colors)
#===================================================================================================
#                                Tuples
#tuples are immutable(cant change or modify) data. it stored multiple elements
avalue = [10, 30, 50, 20, 90]      #---- [] its lists
print(avalue, type(avalue))

avalue = (10, 30, 50, 20, 90)      #---- () its Tuples
print(avalue, type(avalue))

avalue = 10, 30, 50, 20, 90      #---- round bracket is not compulsary tuple identify by ',' its tuple
bvalue = str(avalue)
print(bvalue, type(bvalue))

avalue = (10)                       #--- its integers
print(avalue = type(avalue))
#---------------------------------------------------------
avalue = (10, 30, 50, 20, 90)
print(avalue[1])             # o/p 30
print(avalue[-1])            # o/p 90

avalue[4] = 0               # it will give error because tuple is immutable

#------------------------------------------------------------------------------------------------------
# TUPLE FUNCTIONS

avalue = (10, 30, 50, 20, 90, 10, 50, 10)      
print(f"avalue before count (10) {avalue}")
result = avalue.count(10)
print(f"avalue before count (10) {avalue} : result ={result}")   #o/p is 3 which is integer

result = avalue.index(10)
print(f"avalue before index (10) {avalue} : result ={result}")    # o/p is 0 because 10th index not available
#-------------------------
# Assignment get index of 3rd occurence
#==========================================================================================================
#                                DICTIONARY
employeelist = [
                [101, 'priya','1111'],
                [102, 'manoj', '2222'],
                [103, 'saurabh','3333'],
                [104, 'sawan', '4444'],
                [105, 'namrata', '5555'],
               ]
print(employeelist[2])           
print(employeelist[0][0]== 101)           # THIS TYPE OF INDEXING WE HAD DONE IN LIST BUT INDEXING IS NOT
print(employeelist[1][0]== 101)           # POSIBLE IN DICTIONARY    
print(employeelist[2][0]== 101)    
print(employeelist[3][0]== 101)    
print(employeelist[4][0]== 101)    
#---------------------------------------------------------------------

#Sample_dictionary ={'key' : 'value   1001 : 'pune'}

employeelist = {
                1 : [101, 'priya','1111'],
                2 : [102, 'manoj', '2222'],
                3 : [103, 'saurabh','3333'],
                4 : [104, 'sawan', '4444'],
                5 : [105, 'namrata', '5555'], 
               }
print(employeelist)  
print(employeelist[1]) 
print(employeelist)  
print(employeelist[1])   
print(employeelist [3])
employeelist [2][1] = 'ishwari'
print(employeelist[2])
employeelist [5] = [110, 'komal', '5555']
print(employeelist)           
#-------------------------------------------------------------------------
#UPDATE FUNCTION
result = {1  : [101, 'priya', '9999']}
employeelist.update(result)
employeelist.update({[1][2] : '9999'})      # ERROR ASK TO SIR
print(employeelist)

employeelist.update({6 : [106, 'snehal', '8888']})
print(employeelist)

employeelist.update({6 : [106, 'snehal', '8888'], 7 : [107,'aasha','7777']})    #ERROR ASK TO SIR

#----------------------------------------------------------------------------
#ITEMS FUNCTION

result = employeelist.items()
print(result)
#----------------------------------------------------------------------------
#KEYS FUNCTION

result =employeelist.keys()
print(result)
#---------------------------------------------------------------------------
#GET FUNCTION

result = employeelist.get(2)
print(result)                        #o/p show record of key value 2

result = employeelist.get("manoj")
print(result)                        #o/p returns none

#====================================================================================================
# CONDITIONAL STATEMENT:
#IF - WE CAN HAVE MULTIPLE IF STATEMENT
#ELIF - WE CAN HAVE MULTIPLE ELIF STATEMENT
#ELSE - WE CAN NOT HAVE MULTIPLE ELSE STATEMENT

#WE CAN HAVE SINGLE ALONE IF STSTEMENTS
#WE CAN NOT HAVE SINGLE ALONE ELSE STSTEMENTS

#if we combine if with elif or else then we can have only one if and else
#however elif can be multiple times
#============================================================================================
#                           LOOPS IN PYTHON
#a loops is a sequence of instruction that is continually repeated until a certain condition is reached
# there are two types of loops in python:
#1. while loop
#2. for loop
#--------------------------------------------------------------
# WHILE LOOP:
print("hello priya")
print("hello priya")
print("hello priya")
print("hello priya")
print("hello priya")

icounter = 5
while icounter > 0:
        print("hello priya")
        icounter = icounter - 1

icounter = 0
while icounter < 5:
        print("hello priya")
        icounter = icounter + 1        

alist = [10, 20, 30, 40, 50]
icounter = 0
while icounter <= 4:
    print(alist[icounter])
    icounter = icounter + 1 

icounter = 0
while icounter <= 4:
    if alist[icounter] == 20 or alist[icounter] == 50
            print(alist[icounter])
            icounter = icounter + 1     
#--------------------------------------------------------------------------------------
# assignment - 
# 1) take input from user and print number till given number            
# 2) take input from user and print even number till given number 
# 3) take input from user and print odd number till given number 

avalue= input("enter the number you wants to display =")
print(avalue)
#==========================================================================================================
#                                      FOR LOOP

alist = [10,45,30,60,25,55,20]
for item in alist:              # here alist muct me define variable, and item is any tem variable. instade of item we can use any thing
        print(item)

for item in alist:
        if item % 2 == 0:
                print("Even number : ", item)
        else:
                print("Odd number: ", item)

for index in range(10):      # here index is any temp variable and range is function. which generate sequense of number automatically
        print(index)         # o/p - 9 but in range it will print till value -1 

for index in range(10, 20,2):   # o/p 10, 12, 14, 16, 18 it will step number after 2, 10 is start index 20 is last index   
        print(index)

for index in range(10, 1, -1):
        print(index)                     # here it will print revers order value
#------------------------------------------------------------------------------------
# LOOP STATEMENT
# BREAK : it use to come out of the loop when encounterd. it instruct the program to exit

alist = [10,45,30,60,25,55,20]
for item in alist:              # here alist muct me define variable, and item is any tem variable. instade of item we can use any thing
        print(item, end=' ')    # here end is function in for it will print values in horizontal like 10, 45,30,et
#---------------------------------------------------------------------------------------

alist = [10,45,30,60,25,55,20]
for item in alist:              # here alist muct me define variable, and item is any tem variable. instade of item we can use any thing
        if item == 60:          # here it will print value till 60 after 60 it will break loop and came out
                break
        print(item, end=' ')     # o/p 10,45,30    
        

alist = [10,45,30,60,25,55,20]
for item in alist:              # here alist muct me define variable, and item is any tem variable. instade of item we can use any thing
        if item == 60:          # here it will print value till 60 after came to 60 it will skip that iterration and continue with next iterration
                continue
        print(item, end=' ')    # o/p 10,45,30,25,55,20

#pass is null ststement in python which do nothing just pass       
alist = [10,45,30,60,25,55,20]
for item in alist:  
        pass      # it will just pass for loop and dont print anything or do any change
#========================================================================================================
# ELSE : it will print after complete for loop exicution.
# in break condition else part will not display because it will not exicute complte for loop
#in continue else ststement will exicute. because it will exicute complete for loop
alist = [10,45,30,60,25,55,20]
for item in alist:              # here alist muct me define variable, and item is any tem variable. instade of item we can use any thing
        if item == 60:          # here it will print value till 60 after 60 it will break loop and came out
                break
        print(item, end=' ') 
else:
        print("Loop exicution completed")   # here else not print after break.      

#=======================================================================================================
#                                    FUNCTIONS
# we can define function once can use multiple times
def printInUpper():          #function defination   # printInUpper is function name
        print("hello innovant".upper())  #function body
#we can have multiple lines in function body       
# #--------------------------------------------------------------------
printInUpper()              # function call # trigger
printInUpper()              # function call # trigger
printInUpper()              # function call # trigger
printInUpper()              # function call # trigger
#====================================================================================================
# Functions with parameters

def printInUpper(inputstr):          #function defination   # printInUpper is function parameter inputstr is parameter name
        print(inputstr.upper())              #function body
printInUpper("hello")                     # it will print in upper case
print("hello")                           # it will print as it is 
#----------------------------------------------------------------------------------------------------

a = 10 
b = 20
result = a+b
print("addition :", result)
#-------------------------------------------------
def addition(a , b):
        result= a+b
        print(f" addition of {a} and {b} : {result}")
addition(10 , 20)        
addition(40 , 50)        
result = addition(10, 20)
print(result)
#==========================================================================================
#FACTORIAL:

counter = 5
result = 1
while counter > 1:
        result = result * counter
        counter= counter - 1
print("factorial of 5:", result)

factorialofnumber = int(input("Enter number") )
counter=2
result = 1
while counter <= factorialofnumber :
        result = result * counter
        counter= counter + 1
print(f"factorial of  {factorialofnumber}:", {result})
#=======================================================================================
# LIST REVERS PROGRAM

alist = [10, 20, "priya","sagar"]
lower = 0
upper = len(alist)-1
while lower<upper:
        alist[lower],alist[upper] = alist[upper],alist[lower]
        lower+=1
        upper-=1
print(alist)
#--------------------------------------------------------------------------------------------
# FILE I/O
#FILE READING OPERATION 

















