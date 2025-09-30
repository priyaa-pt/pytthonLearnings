
#? OPEN,READ ND CLOSE FILE
f = ("file_name", "mode")

#? READ

f = open("demo.txt","r")
data = f.read()
print(data)
print(type(data))
f.close()

#? READLINE

f = open("demo.txt","r")
data = f.readline()
print(data)
f.close()

#? WRITE

f = open("demo.txt","w")
f.write("heey iam feeling good")   #overwrites the entire file)
f.close()

#? APPEND

f = open("demo.txt","a")
f.write ("and iam happy")   #adds at the end of the file)
f.close()

#? DELETING A FILE

import os
os.remove("demo.txt")


#? seek()

with open('file.txt','r') as f:
    f.seek(10) # move to the 1oth byte of file
# read the next 5 bytes
data = f.read(5)

#? tell()

with open('file.txt','r') as f:
    data = f.read(5) # read the next 5 bytes
# save the current position
current_position = f.tell()

#seeked to the saved position
f.seek(current_position)

#? truncate()


with open('file.txt','w') as f:
    f.write("hello world")
    f.truncate(5)
    
with open('file.txt','r') as f:
    print(f.read())
