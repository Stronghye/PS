#잃어버린 괄호
import sys

string = sys.stdin.readline().split("-")


for i in range(len(string)):
    if "+" in string[i]:
        string[i] = sum(list(map(int,string[i].split("+"))))
    else:
        string[i]=int(string[i])

sum = string[0]
for i in range(1,len(string)):
    sum -= string[i]

print(sum)