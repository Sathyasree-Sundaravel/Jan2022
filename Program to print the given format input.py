#Program to print the given format input
x=list(map(int,input().split()))
value=0
for value in range(len(x)):
    print(x[value],end=" ")
    value=value+1
