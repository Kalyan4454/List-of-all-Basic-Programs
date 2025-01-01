https://prepinsta.com/pattern-programs-tutorial/#4

'''
n=5
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end=" ")
    print()

*
* *
* * *
* * * *
* * * * *
'''

'''
n=5
k=65
for i in range(0,n):
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
A 
B C 
D E F 
G H I J 
K L M N O '''

'''
n=5
for i in range(0,n):
    k=65
    for j in range(0,i+1):
        print(chr(k),end=" ")
        k=k+1
    print()
A 
A B 
A B C 
A B C D 
A B C D E 

'''
'''
n=5
k=1
for i in range(0,n):
    for j in range(0,i+1):
        print(k,end=" ")
        k=k+1
    print()

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15 
'''

'''
n=5
for i in range(0,n):
    for k in range(n-i-1):
        print(" ",end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    print()

        * 
      * * 
    * * * 
  * * * * 
* * * * * 
'''

'''
n=5
for i in  range(n,0,-1):
    for j in range(0,i):
        print("*",end=" ")
    print()

* * * * * 
* * * * 
* * * 
* * 
*
'''

'''
n=5
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

* * * * * 
  * * * * 
    * * * 
      * * 
        *
'''

'''
n=5
for i in range(0,n):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        print("*",end=" ")
    print()

        * 
      * * * 
    * * * * * 
  * * * * * * *
'''

'''
n=5
for i in range(n,0,-1):
    for k in range(n-i):
        print(" ",end=" ")
    for j in range(2*i-1):
        print("*",end=" ")
    print()
    
* * * * * * * * * 
  * * * * * * * 
    * * * * * 
      * * * 
        * 
        '''
