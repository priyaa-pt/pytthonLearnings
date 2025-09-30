def calculateGmean(a,b):
    mean = (a*b)/(a+b)
    print (mean)

def isgreater(a,b):
    if(a>b):
     print (' First number is greater')
    else :
     print (' Second number is greater or equal')

def islesser (a,b) :
   pass 
a = 2
b = 5
isgreater(a,b)
calculateGmean(a, b)


def average (a,b):
   print ("the average number is ",(a+b)/2) 
average(4,5)

def average (a = 2,b = 5):# required arguments
   print ("the average value of" ,(a+b)/2)
average (1,3)

#default arguments
def name (fname,nname = "jhon",lname = "marry"):
  print("hello", fname,nname,lname)

name("any","baby","marry") # provide a default value while creating a function 

#keyword arguments
def name(a,b,c):
   print("fruits",a,b,c)
name(b = "apple",c = "cherry",a = "mango")# arguments are passed with key = value, in which order of arguments is passed dosent matters.

#required arguments 
def name (fname,nname,lname):
   print("hello", fname,nname,lname)

name ("any","baby","marry")


#? ENUMERATE FUNCTIONS

marks = [2,4,5,8,9,4,7,3]
for index, mark in enumerate(marks):
   print(mark)
   if(index == 3):
    print( "got 5 marks")




