'''
Extracting even numbers from a iterable
'''
print(list(filter(lambda x:x%2==0,[10,22,11,33,44,55,66])))

'''
Extracting values based on boolean result of function
'''
print(tuple(filter(lambda n:n-11,[23,12,45,11,24])))