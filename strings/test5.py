'''
I/P format-->'3a2b4c3d'
O/P format-->'aaabbbbddd'
'''

def modify(S):
    i = 0
    result = ''
    while i < len(S):
        num = ''
        # collect number
        while i < len(S) and S[i].isdigit():
            num += S[i]
            i += 1
        char = S[i]
        i += 1
        result += char * int(num)
    return result

print(modify('10a2b4c3d'))
       

