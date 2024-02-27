import sys
n_cases = int(input())
for _ in range(n_cases):
    # write your code starting here. replace these lines as needed:
    line = input().rstrip()
    line = sys.stdin.readline().rstrip()
    line = line.split(" ")

    if int(line[0]) % 2 == 0 or int(line[1]) % 2 == 0 or int(line[2]) % 2 == 0:
        print(int(line[0]) + 1, int(line[1]) +1, int(line[2]) +1)

    else:
        print(int(line[0]) + 2, int(line[1]) + 2, int(line[2]) + 2)
