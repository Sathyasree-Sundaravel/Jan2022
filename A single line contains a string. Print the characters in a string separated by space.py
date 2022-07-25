"""
Write a code to get the input in the given format and print the output in the given format

Input Description:
A single line contains a string.

Output Description:
Print the characters in a string separated by space.

Sample Input :
guvi
Sample Output :
g u v i
"""


a=str(input())
for i in range(len(a)-1):
    print(a[i],end=' ')
print(a[-1])
