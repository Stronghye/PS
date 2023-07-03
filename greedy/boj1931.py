import sys

input = sys.stdin.readline

N= int(input())
list = [tuple(map(int,input().split())) for _ in range(N)]

list.sort(key = lambda x:(x[1],x[0]))

ans= [list.pop(0)]

for i in list:
    if(ans[-1][1]<=i[0]):
        ans.append(i)

print(len(ans))