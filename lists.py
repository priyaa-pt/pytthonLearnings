# LIST
#? lists are ordered collection of data items.
#? they store multiple items in a single data type.
#? lists are mutable ( can change after creation ).

list1 = [ 1 , 3 , 5 , 7]
list2 = [ "sky", "water" ,"fire", "soil", "air"]
print(list1)
print(list2)
print(type(list2))
print(len(list2))

#list indexing

list1 = [ 1 , 3 , 5 , 7]
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])

# negetive indexing

list1 = [ 1 , 3 , 5 , 7, 6, 9, 3, 5, 0, 5]
print(list1[-1])
print(list1[len(list1)-1]) 

# check whether the item is present in the list or not 
if 2 in list1 :
    print("yes")
else :
    print("no")

# jump index
print(list1[0:5])
print(list1[1:2:1])

# list comprehension 
lst = [i for i in range(10)]
print(lst)




#? LIST METHODS 

#list sort()

list = [11,55,88,65,5,2,3,]
print (list)
list.sort()
print(list)

list = [11,55,88,65,5,2,3,]
print (list)
list.sort(reverse = True) # arrange the list in desending order
print(list)

#index()
list = [11,55,88,65,5,2,3,88]
print (list.index(88)) #returns the index of the first occurance of the list item.

#count()
list = [11,55,88,65,5,2,3,]
print(list.count(3)) # returns the count of the number of items.

#copy()
list = [11,55,88,65,5,2,3,]
print(list)
m = list.copy() # returns the copy of the list 
print(m)
m[3] = 0
print (m)
 
# append()
list = [11,55,88,65,5,2,3,]
print (list)
list.append(1)
print(list)

#insert()
list = [11,55,88,65,5,2,3,]
print (list)
list.insert(3,4) # insert the value at the given index.
print (list)

#extend()
list = [11,55,88,65,5,2,3,]
sets = ["green","blue","white"]
list.extend(sets)
print (list)

# concatenation of 2 lists
list = [11,55,88,65,5,2,3,]
sets = ["green","blue","white"]
k = list + sets
print(k)