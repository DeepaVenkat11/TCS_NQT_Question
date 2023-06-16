from collections import Counter

n = int(input())

lst = map(int,(input().split()))

costomer = int(input())

income=0

for i in range(costomer):

    size,rate = map(int,input().split())

    if(lst[size]):

        income += rate

        lst[size]-=1

print(income)
