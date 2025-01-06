''' read and write elements in an array using recursion
n=int(input("Enter no of elements : ))
l=[]
def write(n):
    if(len(l)<n):
        l.append(int(input()))
        write(n)
write(n)
print(l)
'''

'''l=[1,2,3,4,5]
print(min(l),max(l))'''

''' Ascending and descenoding order and small and large
l=[20,60,12,45]
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]<l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
for i in range(0,len(l)):
    for j in range(i,len(l)):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print(l)
print(l[0],l[len(l)-1])'''

'''
l=[3,46,8,9,5,3,6,7,4,7,3]
print(sorted(l))'''


''''#second largest element in an array.
a=[1,4,5,3,2,4,2,3,9]
l=sorted(a)
res=[]
for i in l:
    if i not in res:
        res.append(i)
print(res)
print(res[len(res)-2]) '''


'''to copy all elements from an array to another array.
l=[1,7,4,9,2]
j=[]
for i in l:
    j.append(i)
print(j)
print(sorted(j))'''

'''insert and delete
l=[1,2,3,4,5]
l.append(10)
l.insert(2,10)
print(l)
l.pop()
l.remove(10)
print(l)
'''

'''
#all unique elements in the array.
a=input()
b=a.split(" ")
c=list(map(int,b))
print(c)
d=set(c)
print(list(d))'''

'''negative Count
l=[1,-1,-2,-3,-4,-5,1,3,5,6,9,0]
j=[]
nc=0
for i in l:
    if i<0:
        j.append(i)
        nc=nc+1
print(j)
print("negative count: ",nc)'''

'''total number of even and odd elements in an array.
l=list(map(int,input().split(" ")))
ec=0
oc=0
el=[]
ol=[]
for i in l:
    if(i%2==0):
        ec=ec+1
        el.append(i)
    else:
        oc=oc+1
        ol.append(i)
print(f"even count : {ec} odd count : {oc} evn list : {el} odd list : {ol}")'''

'''
#count total number of duplicate elements in an array.
l=[1,2,3,4,5,6,1,2,3,4,5,6,2,3,4,5,1,2,3,4]
act=[]
dup=set()
for i in l:
    if i not in act:
        act.append(i)
    else:
        dup.add(i)
print(list(dup))
print(len(dup))'''

'''
#count the frequency
l=[1,2,3,4,5,1,2,6,7,1,2]
key=1
count=0
for i in l:
    if(key==i):
        count=count+1
print(count)
'''

'''Reverse
l=[1,5,6,4,30]
print(l[::-1])
'''

'''Merge two lists
l1=[1,2,3,4,5]
l2=[6,7,8,5,4]
for i in l2:
    l1.append(i)
print(l1)'''





