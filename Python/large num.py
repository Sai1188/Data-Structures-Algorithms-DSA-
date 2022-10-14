n=int(input())
lst=[]
for i in range(0,n):
    lst.append(int(input()))
lst.sort(reverse=True)
if lst[1]*2>=lst[0]:
    print(False)
elif lst[1]*2<lst[0]:
    print(True)
    