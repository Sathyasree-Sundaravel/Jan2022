"""
Write a code to get the input in the given format and print the output in the given format.

Input Description:
First-line indicates two integers which are the size of array and 'K' value. Second-line indicates an integer contains elements of an array.

Output Description:
Print the taken input in the same format.

Sample Input :
5 3
1 2 3 4 5
Sample Output :
5 3
1 2 3 4 5
"""



n,k=input().split()
x=list(map(int,input().split()))
value=0
print(n,end=" ")
print(k)
for value in range(len(x)-1):
    print(x[value],end=" ")
    value=value+1
print(x[-1])
