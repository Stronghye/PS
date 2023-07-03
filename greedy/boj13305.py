import sys

input= sys.stdin.readline

N = int(input())
weight = list(map(int,input().split()))
vertex = list(map(int,input().split()))

i =0
sum = 0
while i<len(vertex)-1:
    j = i+1
    while vertex[i]<vertex[j] and j<len(vertex)-1:
        j+=1
    for k in range(i,j):
        sum += vertex[i]*weight[k]
    i = j

print(sum)
