import sys
n_cases = int(input())
for _ in range(n_cases):
    # write your code starting here. replace these lines as needed:
    line = input().rstrip()
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")

    a = int(line[0])
    b = int(line[1])
    c = int(line[2])

    if a % 2 == 0:
        a = a + 1
    
    elif b % 2 == 0:
        b = b + 1

    elif c % 2 == 0:
        c = c + 1
    
    print(a, b, c)

    

    
    if a % 2 != 0:

        a = a + 2

    elif b % 2 != 0:
        b= b + 2

    elif c % 2 != 0:
        c = c + 2

    print(a, b, c)