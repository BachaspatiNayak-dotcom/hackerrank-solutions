'''
innitialize a list perform some operations on it based on user requirement
'''





if __name__ == '__main__':
    N = int(input('no.of operations you want to perform:'))
    lst = []

    for _ in range(N):
        command = input().split()

        if command[0] == "insert":
            lst.insert(int(command[1]), int(command[2]))

        elif command[0] == "print":
            print(lst)

        elif command[0] == "remove":
            lst.remove(int(command[1]))

        elif command[0] == "append":
            lst.append(int(command[1]))

        elif command[0] == "sort":
            lst.sort()

        elif command[0] == "pop":
            lst.pop()

        elif command[0] == "reverse":
            lst.reverse()