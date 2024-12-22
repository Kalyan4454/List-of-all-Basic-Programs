'''
1 Write a  program to enter two numbers and find their sum.
2 Write a  program to enter two numbers and perform all arithmetic operations.
3 Write a  program to enter length and breadth of a rectangle and find its perimeter.
4 Write a  program to enter length and breadth of a rectangle and find its area.
5 Write a  program to enter radius of a circle and find its diameter, circumference and area.
6 Write a  program to enter length in centimeter and convert it into meter and kilometer.
7 Write a  program to enter temperature in °Celsius and convert it into °Fahrenheit.
8 Write a  program to convert days into years, weeks and days.
9 Write a  program to find power of any number xy (x^y).
10 Write a  program to enter any number and calculate its square root.
11 Write a  program to enter two angles of a triangle and find the third angle.
12 Write a  program to enter base and height of a triangle and find its area.
13 Write a  program to calculate area of an equilateral triangle.
14 Write a  program to enter marks of five subjects and calculate total, average and percentage.
15 Write a  program to enter P, T, R and calculate Simple Interest.
'''

'''a=input("enter 2 numbers :")
b=list(map(int,a.split()))
print(sum(b))'''

'''a=int(input())
b=int(input())
print(f"{a+b} {a-b} {a*b} {a/b} {a//b} {a%b}")'''

'''l=float(input("length :"))
b=float(input("breadth :"))
h=float(input("heaight :"))
print(f"perimeter : {2*h*(l*b)}  area : {l*b}")'''

'''r=float(input("enter radius : "))
print(f"area {3.14*r*r} diameter : {2*r} circumference : {2*3.14*r}")'''

'''cm=float(input("enter centimeteres :"))
print(f"meters : {cm*0.01} kilometeres :{cm*0.00001}")'''

'''c=float(input("ce;cius :"))
print(f"farehnheit : {((c*9)/5)+32}")'''

'''d=int(input())
years=d//365
rd=d%365
we=rd//7
days=rd%7
print(f"{years} years {we} weeks {days} days")'''

'''import math
a,b=int(input()),int(input())
print(f"{math.pow(a,b)} is power {math.sqrt(a)} {math.sqrt(b)} is square root")'''

'''a1,a2=int(input()),int(input())
print(180-a1-a2)'''

'''b=int(input("base : "))
h=int(input("Heaight : "))
print("area :",0.5*b*h)'''

'''import math
side=int(input("Side :"))
print((math.sqrt(3)/4)*side**2)'''

'''a=input()
b=list(map(int,a.split()))
print(f"{sum(b)} {sum(b)/5}")
print(5/(sum(b)/5)*100)'''

'''p,t,r=float(input()),float(input()),float(input())
print((p*t*r)/100)'''
