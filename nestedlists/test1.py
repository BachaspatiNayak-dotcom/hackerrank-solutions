'''
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''




if __name__ == '__main__':
    classdata=[]

    for _ in range(int(input('enter no.of students in class:'))):
        name = input('enter student name')
        score = float(input('enter his/her mark'))
        classdata.append([name, score])

    scores={student[1] for student in classdata}
    scores.remove(max(scores))
    second_highest=max(scores)

    names=[student[0] for student in classdata if student[1]==second_highest]

    for name in sorted(names):
        print(name,'got 2nd highest mark')