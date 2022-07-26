"""
Write a code to get the input in the given format and print the output in the given format

Input Description:
A single line contains integers separated by space

Output Description:
Print the integer list of integers separated by space

Sample Input :
2 3 4 5 6 7 8
Sample Output :
2 3 4 5 6 7 8
"""


L=list(map(int,input().split()))
for i in range(len(L)-1):
    print(L[i],end=' ')
print(L[-1])
