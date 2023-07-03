#카드정렬하기
import sys
from heapq import heappush,heappop,heapify

input = sys.stdin.readline

N = int(input().rstrip())

arr = [int(input().rstrip()) for _ in range(N)]


arr.sort(reverse=True)


result = (N-1)*sum(arr)
for i in range(N-2):
    result-=(N-2-i)*arr[i]

print(result)