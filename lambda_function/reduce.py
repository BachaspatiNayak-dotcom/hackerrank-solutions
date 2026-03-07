'''
Sum of integers of a given list using reduce function
'''
from functools import reduce
print(reduce(lambda x,y:x+y,[10,20,30]))
