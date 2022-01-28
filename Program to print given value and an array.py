#Program to print given value and an array
n,k=input().split()
x=list(map(int,input().split()))
value=0
print(n,end=" ")
print(k)
for value in range(len(x)):
    print(x[value],end=" ")
    value=value+1
