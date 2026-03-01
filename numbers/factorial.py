'''
WAP to find factorial of a given number
'''
def factorial(n):
    F=1
    for i in range(2,n+1):
        F*=i
    return F
print(factorial(15))
print(factorial(5))