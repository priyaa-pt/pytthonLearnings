
#? MAPS
# maps(functions , iterable)


def cube(x):
    return  x * x * x

#list of number

l = [1,3,5,7,9,10]
newl = list(map(cube,l))
print(newl)


#? FILTER 
# filter(predicate , iterable)  predicate argument is a function that returns boolean value.

def filter_function(x):
    return x > 5
      
l = [1,3,5,7,9,10]
NEWl = list(filter(filter_function , l))
print(NEWl) 


#? REDUCE 
# reduce( functions , iterable) takes 2 arguments and return single value.

from functools import reduce

l = [1,3,5,7,9,10]
newnewl = (reduce(lambda x,y: (x-y) , l))
print(newnewl)

