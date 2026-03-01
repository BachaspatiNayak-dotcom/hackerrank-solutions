'''
WAP to find if a number is perfect number or not.
A perfect number is a positive integer equal to the sum of its proper positive divisors (excluding the number itself)
'''
def isperfect(n):
    summ=0
    for i in range(1,n):
        if n%i==0:
            summ+=i
    if summ==n:
        return 'Perfect number'
    else:
        return 'not a perfect number'
print(isperfect(28))
print(isperfect(496))
