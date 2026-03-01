'''
I/P format-->'a3b2c5d2'
O/P format-->'aaabbcccccdd'
'''
def modify(S):
    result=''
    i=0
    while i<len(S):
        char=S[i]
        num=''
        i+=1
        while i<len(S) and S[i].isdigit():
            num+=S[i]
            i+=1
        result+=char*int(num)
    return result
    
print(modify('g7d4w3l9'))
print(modify('a10b10'))