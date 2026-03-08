def timedecorator(func):
    def inner(*args,**kwargs):
        import time
        IT=time.time()
        func(*args,**kwargs)
        FT=time.time()
        print('execution time of function:',FT-IT,'seconds')
    return inner
@timedecorator
def primes(LL,UL):
    for num in range(LL,UL+1):
        if num>1:
          for i in range(2,int(num**0.5)+1):
            if num%i==0:
                break
          else:
            print(num)
primes(1,100)