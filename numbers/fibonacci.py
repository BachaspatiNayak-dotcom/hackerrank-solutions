'''
WAP to print fibonacci series upto n terms
'''
def fibo(n):
    count=0
    a,b=0,1
    while count<n:
       a,b=b,a+b
       print(a)
       count+=1
fibo(7)

