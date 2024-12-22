'''23 Write a  program to print all natural numbers from 1 to n. - using while loop
24 Write a  program to print all natural numbers in reverse (from n to 1). - using while loop
25 Write a  program to print all alphabets from a to z. - using while loop
26 Write a  program to print all even numbers between 1 to 100. - using while loop
27 Write a  program to print sum of all even numbers between 1 to n.
28 Write a  program to print sum of all odd numbers between 1 to n.
29 Write a  program to print table of any number.
30 Write a  program to find first and last digit of any number.
31 Write a  program to count number of digits in any number.
32 Write a  program to calculate sum of digits of any number.
33 Write a  program to calculate product of digits of any number.
34 Write a  program to swap first and last digits of any number.
35 Write a  program to enter any number and print its reverse.
36 Write a  program to enter any number and check whether the number is palindrome or not.
37 Write a  program to find frequency of each digit in a given integer.
38 Write a  program to enter any number and print it in words.
39 Write a  program to print all ASCII character with their values.
40 Write a  program to enter any number and print all factors of the number.
41 Write a  program to enter any number and calculate its factorial.
42 Write a  program to find HCF (GCD) of two numbers.
43 Write a  program to find LCM of two numbers.
44 Write a  program to check whether a number is Prime number or not.
45 Write a  program to check whether a number is Armstrong number or not.
46 Write a  program to check whether a number is Perfect number or not.
47 Write a  program to check whether a number is Strong number or not.
48 Write a  program to print Fibonacci series up to n terms.'''


'''i=1
n=int(input())
while(i<=n):
    print(i,end=" ")
    i=i+1'''
from tempfile import tempdir

'''n=int(input())
while(n>=1):
    print(n,end=" ")
    n=n-1'''

'''a=97
b=122
while(a<=b):
    print(chr(a),end=" ")
    a=a+1'''

'''i=1
n=int(input())
sum=0
while(i<=n):
    if(i%2==0):
        print(i,end=" ")
        sum=sum+i
    i=i+1
print()
print(sum)'''

'''n=int(input())
i=1
sum=0
while(i<=n):
    if(i%2!=0):
        print(i,end=" ")
        sum=sum+i
    i=i+1
print()
print(sum)'''

'''n=int(input())
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")'''

'''n=input()
m=list(n)
print(f"length : {len(m)}")
print(f"first digit {m[0]}")
print(f"last digit {m[len(m)-1]}")'''

'''n=int(input())
digit=0
while(n>0):
    digit=digit+1
    n=n//10
print(digit)'''

'''n=input()
m=list(map(int,list(n)))
print(m)
print(sum(m))'''

'''n=int(input())
prod=1
while(n>0):
    rem=n%10
    prod=prod*rem
    n=n//10
print(prod)

m=input()
k=list(map(int,list(m)))
prod=1
for i in k:
    prod=prod*i
print(prod)'''

'''n=input()
b=list(n)
print(b)
l=len(b)
print(l)
temp=b[0]
b[0]=b[l-1]
b[l-1]=temp
print(b)'''

'''n=input()
print(n[::-1])

a=int(input())
rev=0
while(a>0):
    rem=a%10
    rev=rev*10+rem
    a=a//10
print(rev)'''

'''n=input()
if(n==n[::-1]):
    print("pal")
else:
    print("not")'''

'''a=input()
b=list(map(int,list(a)))
count=0
fre_num=int(input())
for i in b:
        if(fre_num==i):
            count+=1
print(count)'''

'''l1=[1,2,3,4,5,6,7,8,9]
l2=['One','Two','Three','Four','five','six','Seven','eight','Nine']
n=input()
b=list(map(int,(list(n))))
print(b)
for i in b:
    for j in l1:
        if(i==j):
            print(l2[j-1],end=" ")'''

'''l1=[]
l2=[]
for i in range(65,91):
    l1.append(chr(i))
j=0
for i in range(65,91):
        print(f"{l1[j]} : {i},",end=" ")
        j=j+1
print()
for i in range(97,123):
    l2.append(chr(i))
j=0
for i in range(97,123):
        print(f"{l2[j]} : {i},",end=" ")
        j=j+1'''

'''l1=[]
l2=[]
for i in range(65,91):
    l1.append(chr(i))
    l2.append(i)
c=zip(l1,l2)
d=dict(c)
l3=[]
l4=[]
for i in range(97,123):
    l3.append(chr(i))
    l4.append(i)
e=zip(l3,l4)
f=dict(e)
d.update(f)
print(d)'''

'''n=int(input())
i=1
digit=0
while(i<=n):
    if(n%i==0):
        print(i)
        digit+=1
    i=i+1
print(digit)'''

'''import math
n=int(input())
print(math.factorial(n))

def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(n))'''

'''n1=int(input())
n2=int(input())
a=n1
b=n2
while(b!=0):
    temp=b
    b=a%b
    a=temp
hcf=a
lcm=(n1*n2)/hcf
print(f"{hcf} {lcm}")'''
'''def hcf(a,b):
    if(b==0):
        return a
    else:
        return hcf(b,a%b)
a=int(input())
b=int(input())
print(hcf(a,b))
x=a
y=b
lcm=(x*y)/hcf(a,b)
print(lcm)'''

'''
n=int(input())
c=0
i=1
while(i<=n):
    if(n%i==0):
        c=c+1
    i=i+1
if(c==2):
    print("prime")
else:
    print("Not prime")

start=int(input())
end=int(input())
while(start<=end):
    i=1
    count=0
    while(i<=start):
        if(start%i==0):
            count=count+1
        i=i+1
    if(count==2):
        print(start)
    start=start+1
'''

'''n=int(input())
temp=n
temp1=n
o=0
while(temp1>0):
    o=o+1
    temp1 = temp1// 10
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**o
    n=n//10
if(temp==sum):
    print("arm")
else:
    print("Not")'''

'''#perfect number ==> factors sum = number
n=int(input())
i=1
sum=0
while(i<n):
    if(n%i==0):
        sum=sum+i
    i=i+1
if(sum==n):
    print("Perfect")
else:
    print("no")'''

'''
#A strong number is a positive integer where the sum of the factorials of its digits is equal to the number itself
n=input()
b=list(map(int,list(n)))
sum=0
def fact(h):
    if(h==0 or h==1):
        return 1
    else:
        return h*fact(h-1)
for i in b:
    a=fact(i)
    sum=sum+a
c=str(sum)
if(n==c):
    print("strong")
else:
    print("Not")
'''

'''
n1=0
n2=1
n3=n1+n2
x=int(input())
print(n1,n2,end=" ")
i=1
while i<x-1:
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
    i=i+1
    
print()

n1=0
n2=1
x=int(input())
n3=n1+n2
print(n1,n2,end=" ")
while(n3<=x):
    print(n3,end=" ")
    n1=n2
    n2=n3
    n3=n1+n2
'''

