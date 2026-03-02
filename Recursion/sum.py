'''
Write a recursive programme to find sum of 1st n positive numbers
'''
def summ(n):
    if n==0:
        return 0
    return n+summ(n-1)
print(summ(10))