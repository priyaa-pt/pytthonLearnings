 #?ef-else statement

appleprice = 220
budget = 200 

if (appleprice <= budget ):
    print("Alexa, add 1 kg apple to the cart.")
else :
    print("Alexa, do not add apples to the cart.")
          
# elif statement 

num = int(input("enter the value of num:"))
if ( num < 0 ):
    print ("Number is negetive")
elif ( num == 0):
    print ( " Number is zero ")
else :
    print (" Number is poitive")

# Nested if statement

num = 18 
if( num < 0):
    print ("Number is negetive")
elif (num > 0):
    if( num <= 10):
        print ("Number is between 1-10")
    elif ( num > 10 and num <= 20):
        print ("Number is between 11-20")
    else :
        print (" Number is greater than 20")
else:
    print ("Number is zero")

# match statement 

x = int(input ("enter the value of x:"))
# x is a variable to match 
match x:
    # if x is 0
    case 0:
        print( "x is zero")
     # case with if-condition
    case 4:
        print("case is 4")
    case _:
        print(x)  

                                               #*LOOPs
 
# for loop 
name = "priya"
for i in name:
    print(i)


# for loop(in lists)
colors = ["red","blue","green","blue"]
for color in colors:  
  print(color)
  for i in color:
      print(i)

# RANGE
for k in range (1,101) :
    print (k )
for k in range (1,10,2) :
    print (k )


# WHILE LOOP
i = int(input("enter the value of i :"))
while( i < 5):
    print(i)
print("done with the loop")

count = 5
while (count > 0): # reverse or decrement the loop
    print(count)
    count = count - 1
else :
    print("iam inside the else")

# finding a number 
i = 0 # initialization
num = (1,2,3,4,5,6,7,8,9)
x = 5
while i < len(num):
   if(num == x):
      print("found")
   i+=1 






# DO WHILE LOOP    
i = 0 
while True:
    print(i)
    i = i + 1
    if(i%100==0):
     break


#BREAK STATEMENT
for i in range(12):
 if(i==10):
    break # skips over a part of code
 print("5 x",i+1, "=",5*(i+1))
   
print("leave the loop")

#CONTINUE STATEMENT
for i in range(12):
 if(i==10):
  print("stop")
  continue # skips the iteration
 print("5 x",i, "=",5*i)
   