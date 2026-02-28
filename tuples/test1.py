'''
Given an integer n, , and n space-separated integers as input, create a tuple, , of those integers. Then compute and print the result of hash(t) .
'''




n = int(input('enter no of elements:'))
numbers = tuple(map(int, input('enter elements:').split()))

print(hash(numbers))