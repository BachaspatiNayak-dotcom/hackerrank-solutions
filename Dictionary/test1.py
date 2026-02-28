'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''




if __name__ == '__main__':
    n = int(input('enter no.of students:'))
    student_marks = {}

    for _ in range(n):
        data = input('enter details:').split()
        name = data[0]
        scores = list(map(float, data[1:]))
        student_marks[name] = scores

    query_name = input('enter student name:').strip()

    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"average mark of {query_name} is {avg:.2f}")