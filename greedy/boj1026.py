#보물

import sys
import heapq

input = sys.stdin.readline

N= int(input().rstrip())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

heapq.heapify(A)
bHeap=[]
for element in B:
    heapq.heappush(bHeap,(-element,element))

sum=0
for i in range(N):
    sum+= heapq.heappop(A) * heapq.heappop(bHeap)[1]

print(sum)