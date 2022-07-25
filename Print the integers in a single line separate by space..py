"""
Write a code to get the input in the given format and print the output in the given format

Input Description:
Three integers are given in line by line.

Output Description:
Print the integers in a single line separate by space.

Sample Input :
2
4
5
Sample Output :
2 4 5
"""


a=int(input())
b=int(input())
c=int(input())
L=[]
L.append(a)
L.append(b)
L.append(c)
print(*L,sep=' ')
