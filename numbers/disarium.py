'''
WAP to check if  a given number is disarium number or not.
A Disarium number is an integer where the sum of its digits raised to the power of their respective positions (starting from 1) equals the number itself.
'''

def disarium(n):
    summ=0
    dummy=n
    p=len(str(n))
    while dummy>0:
        rem=dummy%10
        summ+=rem**p
        p-=1
        dummy//=10
    if summ==n:
        return 'it is a disarium number'
    else:
        return 'it is not a disarium number'
print(disarium(135))
print(disarium(518))