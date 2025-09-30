# TUPLE
#? tuples are ordered collection of data items.
#? they store multiple items in a single data type.
#? tuples are immutable ( can'nt change after creation ).

tup = (1,2,3,4,"mom","dad")
print(type(tup),tup)
print(tup[5])

#checking wheter the item is present in the tuple or not
if "mom" in tup:
    print("yes mom is present in tuple")



#? METHODS IN TUPLE 
# As tuples are immmutable, hence if you wqant any modifications in items. then firstly you must convert tuple into list.

items = ("good","bad","positive","negative","happy","sad")
temp = list(items) # converts into list and stores in temp variable 
temp.append("hurray") # add item
temp.pop(5)       # remove item
temp[2]="verygood"     # change item 
item = tuple(temp)
print(temp)

#concatenate tuple

items1 = ("good","bad","positive","negative","happy","sad")
items2 =  ("sky", "water" ,"fire", "soil", "air")
k = items1 + items2
print(k)

#METHODS

#count()
A = (11,55,88,65,5,2,3,)
print(A.count(3)) # returns the count of the number of items.

#index()
B = [11,55,88,65,5,2,3,88]
print (B.index(88)) #returns the index of the first occurance of the list item{tuple.index(elemnt,start,end)}
