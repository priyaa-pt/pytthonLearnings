dic = {
    1 : "priya",
    2 : "riya",
    3 : "rishi",
    4 : "blue"
}

print(dic[1])

#accessing single value:
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info)
print(info['name'])
print(info.get('name'))

#accessing multiple value:
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info.values())

#accessing keys:
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info.keys())

#accessing key-values:
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info.items())

#? METHODS 
# update()
#accessing single value:
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info)
info.update({'name':'rishi'})
info.update({'age':'22'})
print(info)

#clear()
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
print(info.clear())
print(info)

#pop()
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
info.pop('age')
print(info)

#popitem()#removes lasth key-value pair
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
info.popitem()
print(info)

#del()
info = {'name': 'priya' , 'age': 21 , 'eligible' : True}
del info['age']
print(info)

#?for loop with else
for i in range(5):
 print (i)
else :
 print("soory no i")



#raising value error
a = int(input("enter the value between 5 and 9"))

if ( a<5 or a>9):
 raise valueError("value sghould be between 5 an 9")
 
