'''
Write a programme to find no.of distinct vowels present in a given string
'''
def vowels(String):
    S=set()
    for ele in String:
        if ele in 'aeiou'.lower():
            S.add(ele)
    return len(S)

# print(vowels('aeiouaeiou'))
