'''
WAP to print every 2nd prime number in a given range
'''
def primes2nd(LL,UL):
    count=0
    for num in range(LL,UL+1):
        if num>1:
           for i in range(2,int(num**0.5)+1):
              if num%i==0:
                break
           else:
            count+=1
            if count%2==0:
                print(num)
primes2nd(1,10)