
#? sets (unorderd collection of data)
set1 = {"car",1,True,"car",1,2.3,"baby","yes"}
print(set1)

priya = set()
print(type(set()))

for value in set1:
 print(value , end = '')


#set methods

# unioun() and update()

s1 = {1,2,3,4,5,6}
s2 = {1,2,}
print(s1.union(s2))
s1.update(s2)
print (s1,s2)

# intersection() and intersection_update()
s1 = {1,2,3,4,5,6}
s2 = {1,2,}
print(s1.intersection(s2))
s1.intersection_update(s2)
print (s1,s2)

#symmetric_diffrence and symmetric_diffrence_update()
s1 = {1,2,3,4,5,6}
s2 = {1,2,}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print (s1,s2)

#diffrence() and diffrence_update()
s1 = {1,2,3,4,5,6}
s2 = {1,2,}
print(s1.difference(s2))
s1.difference_update(s2)
print (s1,s2)