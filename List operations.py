"""Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types
listed above. Iterate through each command in order and perform the corresponding operation on your list.

Example
N=4
append 1
append 2
insert 3 1
print
append 1: Append  to the list, .
append 2: Append  to the list, .
insert 3 1: Insert  at index , .
print: Print the array.
Output:
[1, 3, 2]
"""


if __name__ == '__main__':
    N = int(input())
    L=[]
    for i in range(0,N):
        a=input()
        x=a.split()
        if x[0]=='insert':
            L.insert(int(x[1]),int(x[2]))
        elif x[0]=='append':
            L.append(int(x[1]))
        elif x[0]=='pop':
            L.pop()
        elif x[0]=='remove':
            L.remove(int(x[1]))
        elif x[0]=='sort':
            L.sort()
        elif x[0]=='reverse':
            L.reverse()
        elif x[0]=='print':
            print(L)
