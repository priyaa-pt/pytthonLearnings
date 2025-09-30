
#? TYPECASTING

# explicit typecasting

a = "7"
b = "2"
print (int(a)+(int(b)))


# implicit typecasting 

a = 2.2
b = 2
print (type(a))
print (type(b))
print (a + b)



#* USER INPUT
a = input("enter my name :")
print ("my name is", a ) 


x = input("enter value of a:" )
y = input("enter value o b :")
print (int(x) + int(y))



# SRINGS
name = "priya"

sky = '''todays whether is good
"we have a plan today" 
"we will celebrate it together'''

for character in sky:
 print(character) # indexing each character used for multiline code


print(sky)

print ("hello,"+ name )
print(name [0]) # used for single line code
print(name [1])
print(name [2])
print(name [3])
print(name [4])
print(name [5]) #throws an error

#* STRING SLICING 
# len()

fruit = "mango"
len = len(fruit)
print("mango is a" , len , "letter words")

names = "priya tiwari"
print(len(names))

# slicing
fruit = "cherry"
print (fruit[0:4]) # exclude 4th character(n-1) where n is the last character 

print (fruit[3:4])

print (fruit[1:-3]) # called as negative slicing where (len(fruit)-3)
print (fruit[-2:-3])

#*ALTER AND MODIFY STRINGS

# upper()
name = "wednesday"
print (name.upper())

# lower()
print (name.lower())

# strip()
name =" wednesday "
print(name.strip())

#rstrip()
name ="hello world@"
print(name.rstrip("@")) # strips all trailing characters like !@ 

#replace()
print(name.replace("world" , "hello")) # replace all occurances of world with hello

#list()
print(name.split(" "))

#capitalize()
print(name.capitalize()) # capitalize the first character and rest all are in small 

#center()
print(name.center(50))

#count()
print(name.count("hello")) #count the number of occurance

#endswith()
print(name.endswith("@")) # checks that the given strings is end with @ or not 

#find()
print(name.find("world")) # returns the index number where it is present 