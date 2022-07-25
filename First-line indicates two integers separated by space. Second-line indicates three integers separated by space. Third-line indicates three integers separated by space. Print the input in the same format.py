"""
Write a code to get the input in the given format and print the output in the given format

Input Description:
First-line indicates two integers separated by space. Second-line indicates three integers separated by space. Third-line indicates three integers separated by space

Output Description:
Print the input in the same format.

Sample Input :
2 5
2 5 6
2 4 5
Sample Output :
2 5
2 5 6
2 4 5
"""



L1=list(map(int,input().split()))
L2=list(map(int,input().split()))
L3=list(map(int,input().split()))
print(*L1,sep=' ')
print(*L2,sep=' ')
print(*L3,sep=' ')
