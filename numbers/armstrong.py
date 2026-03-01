'''
WAP to check if  a given number is armstrong number or not.
An Armstrong number is a positive integer equal to the sum of its own digits, each raised to the power of the total number of digits
'''
def armstrong(n):
    summ=0
    dummy=n
    p=len(str(n))
    while dummy>0:
        rem=dummy%10
        summ+=rem**p
        dummy//=10
    if summ==n:
        return 'it is a armstrong number'
    else:
        return 'it is not a armstrong number'
print(armstrong(153))
print(armstrong(678))