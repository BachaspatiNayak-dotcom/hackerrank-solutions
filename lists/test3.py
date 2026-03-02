'''
Given a list of positive integers, return the number of elements that are strictly greater than the average of all previous elements. Skip the first element.
'''
def count_greater(list):
    total=list[0]
    count=0

    for i in range(1,len(list)):
        avg=total/i
        if list[i]>avg:
            print(list[i])
            count+=1
        total+=list[i]
        return count

print(count_greater([11,22,33,44,55,10,4]))