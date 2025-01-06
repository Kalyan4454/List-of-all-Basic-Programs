Programming Languages 
----------------------

 a.statically typed -->variables and Data types are linked together(PL : c ,c++ ,java;)
compiler based
syntax:
       datatype varname=value;
eg:
    int a=20;
    string name="java";
  
 b.Dynamically Typed --> Python ,JavaScript ,R
interpreter based
syntax:
       varname=value
eg:
       age=20
       name="Kalyan"
based on the value given ,dataytype will automatically allocated/identified



Concepts
---------------------------------------------------------

1. Comments

   Symbol: #
   non executable statement ignores by the intrepreter and written for the beenfit of improving programmers's understandability of the code
   Multiline comments / Block Comments are not supported in python

-----------------------------------------------------------------------------------
2. Keywords

   Also known as reserved words
   Building blocks of a code
   Depending on version of python 3.12 --> has 36 keywords
   3.10 --> have only 35 keywords

   import keyword
   print(keyword.kwlist)
   print(len(keyword.kwlist))
   
   Module : keyword
   Pre-defined variable: kwlist
   Stores a list of all the available keywords in the particular version of python
   Use the Variable syntax- Syntax : Modulename.VariableName
   len()--> it will return the number of values stored in the specified variables

-------------------------------------------------------------------------------------
3. Identifiers

   Programmer defined names: variable; Function ; Method ; class ; Object;.......
 1.Starts with an alphabet/underscore(_)
   subsequent characters can be a combination of alphabets,digits,underscore 
   a=10
   _=23
   _x=16 this are valid
   10a=24 (not valid)

 2.Keywords are not used as an identifier
   if=20 -->error
 
 3.other than underscore - No other special characters can be used with in  a value

 4.Blank spaces in between names is not alowed
   eg= first name = "Kalyan" -->error
       firstName = "Kalyan" -->Valid
       first_name = "Kalyan" -->Valid

 5.Length of a name --> no limit
  akjgfjwgguyoifyrgi=10
  print(akjgfjwgguyoifyrgi)  --> o/p=10

----------------------------------------------------------------------------------------
4. Variables

Containers - used to store values temporary
Syntax:
Variable_name=value
Python comes under Dynamically Typed Programming Language / Type Infer Programming Language

type() ==>specifies the datatype of value
id() ==> specifies the memory location of value 

eg:
a=14
b=456.36
c=False
d=20+20j
e="Kalyan'
print(a,type(a),id(a))
print(b,type(b),id(b))
print(c,type(c),id(c))
print(d,type(d),id(d))
print(e,type(e),id(e))

o/p:
14 <class 'int'> 140729209775304
456.36 <class 'float'> 2656378505968
False <class 'bool'> 140729208249224
(20+20j) <class 'complex'> 2656378506992
Kalyan <class 'str'> 2656384604720

String : Group of characters (alphabets ,digits ,specified characters
Strings can be created in 3 ways
a. Single Quatation ==> 'String value'
b. Double Quatation ==> "String value"
c. Triple Quatation ==> '''String value''' / """String value"""  ==>used for Multi-Line strings

ex:
 
s1= 'C'
s2= "C"
s3= '''C'''
s4=""""C"""
print(s1,type(s1),id(s1))
print(s2,type(s2),id(s2))
print(s3,type(s3),id(s3))
print(s4,type(s4),id(s4))

o/p:
C <class 'str'> 
C <class 'str'> 
C <class 'str'> 
C <class 'str'> 

example:
print('My email id is : srinivasakalyan2004@gamil.com')  
print("My brother's name is Santhosh")
adress='''
kalyan
7/4/14 c building
lawyerpeta
ongole
'''
print(address)
-----------------------------------------------------------------------------------------------
5. Data Types [Inbuilt datatypes]

int,float,string,complex,boolean
list,tuple,set,dict,frozenset;
range,None,bytes,bytesarray;

classified into two data types
a.Mutable datatypes --> can be modified
list, set, dictionary, bytearray
b.Immutable datatypes--> cannot be modified/fixed
all the data types (int,float,str,complex,bool,tuple,frozenset)

ex: immuatable datatype
a=10
print(a,id(a))
a=20
print(a,id(a))          #address is changed
10 140715066516552
20 140715066516872

Mutable datatype
a=[10,20,30,40]
print(a,id(a))
#add a value to the end of list
a.append(85)
print(a,id(a))
#modify a value
a[0]="Python"
print(a,id(a))                          #address remains change
[10, 20, 30, 40] 1856726613056
[10, 20, 30, 40, 85] 1856726613056
['Python', 20, 30, 40, 85] 1856726613056

int
----
#int  limit doesn't matter
a=10864965283658652706260
print(a)
a=a+1
print(a)
10864965283658652706260
10864965283658652706261

Number system --> all the values of these number system belong to the int datatype

a.Decimal --> Base 10 :0 to 9
b.binary --> Base 2 :0 and 1 ;prefix=0b
c.octal --> Base 8 :0 to 7 ; prefix=0o
d.Hexadecimal --> Base 16 :0-9 and A to F ;prefix=0x

default Number system :decimal 

ex:
#creating a variable
a=11 #decimal
b=0b1010 #binary
c=0o45   #octal
d=0x8    #hexadecimal
#printing the value
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
o/p:-
11 <class 'int'>
10 <class 'int'>
37 <class 'int'>
8 <class 'int'>

Type Conversions functions : bin(), ocr(), hex()

#decimal int value
x=100
print(f"{bin(x)} is binary")
print(f"{oct(x)} is octal")
print(f"{hex(x)} is hexadecimal")

#binary int value
y=0b11001
print(f"decimal = {y}")
print(f"oct = {oct(y)}")
print(f"hex = {hex(x)}")

0b1100100 is binary
0o144 is octal
0x64 is hexadecimal
decimal = 25
oct = 0o31
hex = 0x64

Type conversion Functions :ord(),chr()
ASCII Functions
American Standard Code for Information Interchange.
English language --> Number representation

Alphabets -->
 Uppercase : A to Z --> 65 to 90
 Lowercase : a to z --> 97 to 122
 Digits : 0 to 9 --> 48 to 57

Type Conversion ASCII Functions:ord(),chr()
ord('character') : This function takes a single character as value and returns the ASCII number of that character 
ex:
print(ord("D"))
print(ord('d'))
print(ord('8'))
print(ord('@'))
print(ord(';'))
print(ord(' '))
print(ord('10')) #error ord() takes only  single charcter

68
100
56
64
59
32

chr(number) : This function takes an int as its value and returns the ASCILL character of that number
ex:
print(chr(64))
print(chr(34))
print(chr(100))
print(chr(60))

@
"
d
<

float
------
# Real numbers --> values with decimal or fractions
# c,c++,java,c# : float. double
# in python : supports ONLY float

ex:
a=100000000000.3546
print(a,type(a))

100000000000.3546 <class 'float'>

boolean
--------
# boolean --> bool : True or False
# Number representation --> True=1; False=0 
a=True
b=False
print(f"value of a is : {a} and datatype of a is :{type(a)}")
print(f"value of b is : {b} and datatype of b is :{type(b)}")
print(f"{a}+{b} : {a+b}")
print(f"{a}-{b} : {a-b}")
print(f"{a}*{b} : {a*b}")
print(f"{a}+{a} : {a+a}")
print(f"{a}/{a} : {a/a}")

value of a is : True and datatype of a is :<class 'bool'>
value of b is : False and datatype of b is :<class 'bool'>
True+False : 1
True-False : 1
True*False : 0
True+True : 2
True/True : 1.0

complex
--------
# complex : (real + img)
# for imaginary number - represent with the letter j/J
# num.real --> return the real value
# num.imag -->return the img value
ex;
c=45+2j
print(f"value of c is : {c} and datatype of a is :{type(c)}")
print(f"real number is {c.real}")
print(f"imaginary number is {c.imag}")

value of c is : (45+2j) and datatype of a is :<class 'complex'>
real number is 45.0
imaginary number is 2.0

Collection Datatype: 
---------------------
storing multiple values under a single variable
Also known as Iterables(can be iterated/looped over)
-->list, tuple, set, dict, frozenset

LIST
------
1.created using [] square brackets
2.inside the [] multiple values are stored where each value is seperated by comma
eg:l=[1,2,3,4,5]
3.it can store  Homogeneous(belongs to the same datatupe)  or Heterogenous(different datatypes) values
eg : l=[1,2,3,4,5] --> Homogennous
     g=["k",1,2.5,45+5j,True] --> Heterogenous
4.Allows DUPLICATE values
5.Mutable datatype -- Add, Update, delete
6.Ordered  (indexes are available)

TUPLE
------
1.created using () parenthesis
2.inside the () multiple values are stored where each value is seperated by comma
eg:l=(1,2,3,4,5)
3.it can store  Homogeneous(belongs to the same datatupe)  or Heterogenous(different datatypes) values
eg : l=(1,2,3,4,5) --> Homogennous
     g=("k",1,2.5,45+5j,True) --> Heterogenous
4.Allows DUPLICATE values
5.Immutable datatype -- Add, Update, delete cannot be perform(once you create cannot change)
6.Ordered  (indexes are available)

SET
-----
1.created using {} curly braces
2.inside the {} multiple values are stored where each value is seperated by comma
eg:l={1,2,3,4,5}
3.can store  Homogeneous(belongs to the same datatupe)  or Heterogenous(different datatypes) values
4.Mutable datatype -- Add, Update, delete
5.set allows only UNIQUE values
s={10,10,36,45,45,36,76,87}
print(s)                       {36, 87, 10, 76, 45}     --> does not allow duplicates
print(type(s))
6.Unordered (NO INDEX)
l={10,45,36,76,87}
print(l)                       {36, 87, 10, 76, 45}      --> Unordered 
print(type(l))


FROZENSET
----------

1.set is Mutable
2.Frozen set IMMUTABLE

DICTIONARY
------------
1.created using {} curly braces
2. Key:Value pairs of data is stored with in a dictionary
ex:
  Email_id - Password
  Student_id - Student details
  lat+lon - city
  IP address - Domain Name
3.Key is always UNIQUE value ; Values can have DUPLICATES
4.Mutable datatype -- Add, Update, delete
5.ordered (Based on Keys)
6.Homogeneous & hetereogenous values

ex:
student_info={
    'Name':'Kalyan',
    'REgNo':'228a1a4454',
    'Pno':'9347273490',
    'Email_id':'srinivasakalyan2004.gmail.com',
    'Sem':'5',
    'Marks':[96,95,99,98]
    }
print(student_info,type(student_info))

{'Name': 'Kalyan', 'REgNo': '228a1a4454', 'Pno': '9347273490', 'Email_id': 'srinivasakalyan2004.gmail.com', 'Sem': '5', 'Marks': [96, 95, 99, 98]} <class 'dict'>

Range()
-------
==>Used to generate a sequence of Numbers
Syntax:
range(start,end,step)
start --> starting value of sequence
end --> ending value(it is not included)(end=end-1)
step --> decides the next number that should come with in the sequence (negative step value is allowed)
next number = current number + step
Function : list(val) --> Converts the value into the list
x=list(range(1,5,1))
print(x)
1 2 3 4

x=list(range(1,5,1))
print(x)
y=list(range(1,11,1))
print(y)
x=list(range(5,50,5))
print(z)

[1, 2, 3, 4]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
[5, 10, 15, 20, 25, 30, 35, 40, 45]

Default value :
default start = 0
deault step value = 1
end is madataory

s=list(range(20))
print(s)
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

f=list(range(20,0,-1))
print(f)
[20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

g=list(range(20,0))
print(g)
[]

---------------------------------------------------------------------------------------------
6. Output Function : print()

# String : group of characters
name="Kalyan"
# integer (int) :Whole numbers
age=20
# Real number (float) : decimal/fractional values
per=8.68
# boolean (bool):True/False
sem_cleared=True
# complex :Real+imaginary numbers
x=21+29j

# printing the values
print(name)
print(age)
print(per)
print(sem_cleared)
print(x)

# printing the values with messages

# output : Kalyan is 20yrs Old and his Cgpa is 8.68

# Method 1: + operator - Concatenation: Strings
# Type Conversion:Converting of One datatype to Another Datatype
# Any datatype conerting to a strinf --> str(value)
# Convert int to string -->str(integer)
# Convert float into string -->str(float)
print(name+" is "+str(age)+"yrs Old and his Cgpa is "+str(per))

# Method 2: ','(comma) opertaor - Concatenation
# while joining this comma opeartor adds the single space
# ',' operator works with all datatypes no need of Type Conversion
print(name,"is",age,"yrs Old and his Cgpa is",per)

# Method 3: Format Specifiers
# int : %d
# float : %f
# Strings : %s
print("%s is %dyrs Old and his Cgpa is %.2f%%" %(name,age,per))

# Method 4:F-String(Formatted String)
# Prefix the string with  f or F
# Print a value:{variable name}
print(f"{name} is {age}yrs Old and his Cgpa is {per}")
marks=[96,98,95,94,93]
print(F"My semester marks are : {marks}")

# Method 5:format() Function
# {}--> Place holder
print("{} is {}yrs Old and his Cgpa is {}".format(name,age,per))

# end --> Represents the Cursor Position
# every print statements gets printed in a new line
# end='\n' (Escape Sequence : Newline)
# Multiple print statements given but u want the output in a single line

print("Welcome")
print("to")
print("Python")

print()

print("Welcome",end=" ")
print("to",end=" ")
print("Python")

# sep --> Seperator
# In as single print Statement when we are printing multiple values ,sep is used to show the difference between the values
# Default Seperator Value in python is :Single Space seperator
a=45
b=96
c=72
print(a,b,c)

#changing the Sep value
print(a,b,c,sep=',')
print(a,b,c,sep='*')
print(a,b,c,sep='$')
print(a,b,c,sep='')

--------------------------------------------------------------------------------------------------------------------------
7. Input Function : input()

Reqading the value of a varaible from the user at  runtime(during the execution of the progress) --> Dynamic inputs


syntax:
var = input("Message")

ex:
a=input("enter NAme :")
print(a)

o/p:
enter NAMe : kalyan
kalyan
---------------------------------------------------------------------------------------------------------------
8. Type Conversion

Q)Program : Employee details

a=input("Enter the Name : ")
b=input("Enter the Email ID : ")
c=int(input("Enter the Mobile Number : "))
d=int(input("Enter the AGE : "))
e=input("Designation : ")
f=float(input("Enter salary "))
hike=(20/100)*f
print("**************************")
print("Employee details")
print(f"NAME : {a}")
print(f"EMAIL_ID : {b}")
print(f"MOBILE NUMBER : {c}")
print(f"AGE : {d}")
print(f"DESIGNATION : {e}")
print(f"ACTUAL SALARY : {f}")
print(f"SALARY AFTER HIKE : {f+hike}")

o/p:

Enter the Name : Kalyan
Enter the Email ID : srinivasakalyan2004@gmail.com
Enter the Mobile Number : 9347273490
Enter the AGE : 20
Designation : Data Scientist
Enter salary 60000
**************************
Employee details
NAME : Kalyan
EMAIL_ID : srinivasakalyan2004@gmail.com
MOBILE NUMBER : 9347273490
AGE : 20
DESIGNATION : Data Scientist
ACTUAL SALARY : 60000.0
SALARY AFTER HIKE : 72000.0


# additon of 2 int numbers

n1=int(input("enter 1 st number"))
n2=int(input("enter 2nd number"))
print(f"total is :{n1+n2}")

# additon of 2 float numbers

x1=float(input("enter 1 st number"))
x2=float(input("enter 2nd number"))
print(f"total is :{x1+x2}")

# additon of 2 complex numbers

c1=complex(input("enter 1 st number"))
c2=complex(input("enter 2nd number"))
print(f"total is :{c1+c2}")

Q)Program: Reading Multiple values using a single input statement

split()
-------

*String function
*Cut the string into multiple pieces
*syntax:
   str.split() 
   str.split('delimeter')
*By default : space a delimeter
*result of the split() function a list of string values

#split()
#based on space
x=input("Enter the number ")
s=x.split()
print(s)

#based on the specific deleimeter comma
y=input("Enter the number ")
f=y.split(',')
print(f)

o/p:
Enter the number 10 20 30 40 50 60 70 80 90
['10', '20', '30', '40', '50', '60', '70', '80', '90']
Enter the number 10,20,30,40,50,60,70,80,90
['10', '20', '30', '40', '50', '60', '70', '80', '90']

Q) Program :sum of multiple values using single input()

#sum of multiple values using single input()

#reading Multiple values using single input()
x=input("enter the numbers :")

#spliiting the string and creating a list of values

a=x.split()
print(a)

#converting the list of string values into a list of integers 

a=list(map(int,a))
print(a)

#find the sum

tot=sum(a)
print(f"sum : {tot}")

o/p:

enter the numbers :10 20 30 40 50 60 70 80 90 100
['10', '20', '30', '40', '50', '60', '70', '80', '90', '100']
[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum : 550

#same logic in a single line

print(sum(list(map(int,input("enter the numbers :").split()))))

o/p:

enter the numbers : 10 20 30 40 50 60 70 80 90 100
550

map()
-------
converting the list of string values into a list of integers 

syntax:

list(map(datatype,var_name))

sum()
--------

give the sum of all the values in a list

syntax:

sum(var_listname)

Q)program: write a python program from the user and print only the first three digits.if more than 3 digits is given ignore the rest

input :12
output:12
input=123
output=123
input=12343456767
ouput=123

a=input("enter a number ")
b=a[:3]
print(b)

--------------------------------------------------------------------------------------------------------------------------------------------
9. Operators

1.Assignment --> used to assign a value to variable
Symbol : '='
eg:
a=10
b=a
c=a+b*10/4

2.Arithmetic --> Mathematical Calculations
Symbols : 
+ Addition
- Subtraction 
* Multiplication
/ Division(float)
% Modulo(remainder)
// Floor Division(int)
** Exponent(Power of)

eg:

10/3
3.3333333333333335
10//3
3
10%3
1

3.Arithmetic Assignment (Short Hand Operators) --> writing an expression in shorter way
a=10
Symbols : 
+=   a+=20 --> a=a+20
-=   a-=10 --> a=a-10
*=
/=
//=
%=
**=

4.Relational --> comparision of values
Reault : BOOLEAN -> True/False
Symbols:
> < >= <= == !=
Equality operators  : == !=

5.Logical --> Combining two or more conditions together to form a SINGLE expression
other Programming languages : && || !
In Python  NO Symbol Rpresentations


and --> When all the combining conditions must be TRUE the result is TRUE otherwise FALSE

10>5 and 15>5 and 16<46
True
10>5 and 10<5 and 75<100
False

or --> If any one of the combining condtion is TRUE then the result is TRUE
If all the condition are FALSE then the result is FALSE

not --> Inverse/Flip
Conditon is TRUE ==> Result is FALSE
Condition is FALSE ==> Result is TRUE

In Python ++ and -- Operators are Not available 
__________________________________________________

6.Conditional (Ternary) --> One line code for the if-else Statement
 Other Programming Language -> ?:

Syntax :
var_name=true_statement if condition else false_statement

ex:
n=int(input("enter the number : "))
if n%2 == 0:
      print("even")
else:
    print("odd")

#using conditional Operator

var="Even" if n%2==0 else "odd"
print(var)

a=10
b=20
a if a>b else b
20

7.Membership --> To perform a SEARCHING operation
Result is a BOOLEAN value - True/False
Searching is Case Sensitive (Upper/Lower)
will work only on Collection types
Collection : Multiple value stores in a single value

in -> If the searching value is present it will return True otherwise False
not in -> If the searching value is not there with in the collection it will return True otherwise False

ex:

a=[10,20,30,40]
10 in a
True
50 not in a
True
50 in a
False

s="programming"
"r" in s
True
'x' in s
False
'x' not in s
True
'gram' in s
True
'P' in s
False

8.Identity Operators --> Performs Comparison 
Result is a BOOLEAN value - True/False
Comparision of address 

is : if the comparing address is same then it return True otherwise False
is not :if the comparing address is not same  it return True otherwise False


*****  Memory Allocation in Python *****
 In c language, c++, JAVA :
      int a = 10
      int b = 20
For every variable creates a sepearte memory address gets allocated  inside which the value is stored

#include <stdio.h>
int main()
{
    int a=10;
    int b=20;
    printf("a=%d address=%u\n",a,&a);
    printf("b=%d address=%u\n",b,&b);

    return 0;
}

a=10 address=2072934272
b=20 address=2072934276

 In Python :-
 Memory allocation is different for mutable and immutable datatypes

 Mutable Datatypes : list, set, dict, bytearray
 For each variable separate memory will is created

 ex;
l1=[10,20,30]
l2=[10,20,30]
print(l1,id(l1))
[10, 20, 30] 2239642826816
print(l2,id(l2))
[10, 20, 30] 2239643024064

#seperate memory will be allocated for each list 









                         CONTROL STATEMENTS
                      ------------------------
--> Conditional Statements (or) Decision Making
--> Iteration (or) Looping Statements
--> Jump Statements

Conditional Statements

- if statement
- if-else statement
- if-elif-else statements
- Nested if-else statements
- Matcher Statements

==> if statement --> when the cidition is True, the statements will get executed
syntax :

if condition:
	Statements

ex:

#reading the age form the user 
age=int(input("age :"))
#checking if the age is less than 18
if (age<18):
    print("Sorrry you are not eligible")
    diff=18-age
    print(f"you have to wait until {diff} years")
    exit()
#if the age is greater than 18
print("you are eligible to vote")
print("choose wisely")

O/P:
age :15
Sorrry you are not eligible
you have to wait until 3 years


==> if-else statement -->  if the condition is True, then the statement within the if will get executed.and if the cindition is False,the statement within the else block will get executed.
syntax:

if condition:
   statements - True
else:
   statements - False
 
* odd or even
* postive or negative
* Age validation

eg:

#odd or even
a=int(input("enter a number :"))
if(a&1==0):
    print("even")
else:
    print("odd")
print()

#Positive or negative
x=int(input("enter a number :"))
if x>0:
    print("postive")
else:
    print("negative")
print()

#age validation
age=int(input("age :"))
if (age<18):
    print("Sorrry you are not eligible")
    diff=18-age
    print(f"you have to wait until {diff} years")
else:
    print("you are eligible to vote")
    print("choose wisely")

O/P:
enter a number :10
even

enter a number :6
postive

age :12
Sorrry you are not eligible
you have to wait until 6 years

=================== 
enter a number :5
odd

enter a number :-10
negative

age :25
you are eligible to vote
choose wisely

#zero division error
num=int(input("enter numerator : "))
den=int(input("enter denominator : "))
if den==0:
    print("devision by zero not possible")
else:
    print(f"{num}/{den} = {num/den}")

O/P:

enter numerator : 5
enter denominator : 0
devision by zero not possible

=================== 
enter numerator : 6
enter denominator : 3
6/3 = 2.0

==> if-elif-else statements --> whenever we have multiple conditions to handle ,we will use this option.else statement is optional.

syntax:

if condition_1:
    Statements -True
elif condition_2:
    Statements -True
elif condition_3:
    Statements -True
elif condition_4:
    Statements -True
    ....
    ....
    ....
elif condition_N:
    Statements -True
else:
    Statements -when all conditions are False   


ex:
#greatest of two numbers
a=int(input("a :"))
b=int(input("b : "))
if a>b:
    print(f"{a} is greater than {b} ")
elif a==b:
    print(f"{a} and {b} both are equal")
else:
    print(f"{b} is greater than {a} ")


O/P:
a : 10
b : 20
20 is greater than 10 

=================== 
a : 10
b : 10
10 and 10 both are equal

=================== 
a : 52
b : 12
52 is greater than 12 

#prize for coming as topper
'''DAD --> options
>90: New Bike
>80: New Laptop
>70: New Mobile
>60: Rs.5000 cash
>50:Increase my pocket Money for rs.250
Fail : Waste Fellow'''
name=input("enter the student name : ")
m1=int(input("enter 1st subject : "))
eng=int(input("enter 2nd subject : "))
ppsc=int(input("enter 3rd subject : "))
ac=int(input("enter 4rth subject : "))
avg=(m1+eng+ppsc+ac)//4
print(f"{avg} is the percenatge")
if avg>=90 and avg<=100 :
    print(f"{name} going to get a New Bike")
elif avg>=80 and avg<90:
    print(f"{name} going to get a new laptop")
elif avg>=70 and avg<80:
    print(f"{name} going to get a new mobile phone")
elif avg>=60 and avg<60:
    print(f"{name} going to get a rs.5000 cash prize")
elif avg>=50 and avg<50:
    print(f"{name} going to get increase in pocket money")
else:
    print(f"{name} is a waste fellow")

O/P:
enter the student name : Kalyan
enter 1st subject : 99
enter 2nd subject : 95
enter 3rd subject : 93
enter 4rth subject : 91
94 is the percenatge
Kalyan going to get a New Bike

a=input("enter a character :")
if (a>='a' and a<='z'):
    print("lower case")
elif (a>="A" and a<="Z"):
    print("uppercase letter")
elif (a>='0' and a<='9'):
    print("digit")
else:
    print("special character")

x=input("enetr a chjaracter :")
if x.isalpha():
    if x.isupper():
        print("uppercase letter")
    else:
        print("lower case")
elif x.isdigit():
    print("digit")
else:
    print("special character")

'''var_name.isalpha()--> checks it is a alphabet
'''var_name.isdigit()--> checks it is a digit 

enter a character :5
digit


=================== 
enetr a chjaracter : A
special character

=================== 
enetr a chjaracter :A
uppercase letter


a=input("enter a character :")
if ((a>='a' and a<='z') or (a>="A" and a<="Z")):
    if(a=='a' or a=='e' or a=='e' or a=='i' or a=='u' or a=='A' or a=='E' or a=='I' or a=='O' or a=='U'):
        print("vowel")
    else:
        print("consonant")
elif (a>='0' and a<='9'):
    print("digit")
else:
    print("special character")

O/P;
enter a character :B
consonant


Looping Statements
- Simple for loop
- for Loop with range()
- for loop with enumerate()
- while loop

Looping in Python 
-------------------
repeat the code again and again until specific number of times or until a specific number of times or until a condiion is satisified(True).
loops can be used on uterables /collections (string ,List, Set,Dictionary)
break and continue -can be used ONLY inside a loop
Loops can be written with else part 
wheb the loop condition becomes Falsethe else block is executed
a.while loop
b.for loop
    1.simple for loop
    2.for loop with range()
    3.for loop with enumerate()
    4.for loop with zip()

Loop : while

syntax:
  while condition :
    Statements that needs to be repeated

3 Parts :if these are not properly defined,
Loop will become INFINTE(never ending Loop)
1.Initialisation --> a variable's starting value
2.Condition
3.Iteration  --> Increement / decreement of the variable 

Program:
==>'Welcome to python' 100 times
count=1
while(count<=100):
    print(f"{count}.Welcome to python")
    count=count+1

o/p:
1.Welcome to python
2.Welcome to python
3.Welcome to python
4.Welcome to python
5.Welcome to python
6.Welcome to python
7.Welcome to python
8.Welcome to python
9.Welcome to python
10.Welcome to python
11.Welcome to python
12.Welcome to python
13.Welcome to python
14.Welcome to python
15.Welcome to python
16.Welcome to python
17.Welcome to python
18.Welcome to python
19.Welcome to python
"
"
"
"

==>print all the even numbers b/w in the range
a=int(input("Enter the starting value : "))
b=int(input("Enter the ending value : "))
count=0
while(a<=b):
    if(a%2==0):
        print(a,end=" ")
        count=count+1
    a=a+1
print("\n")
print(f"{count} are the evne numbers with in the range")

O/P:

Enter the starting value : 1
Enter the ending value : 10
2
4
6
8
10

5 are the evne numbers with in the range

ex2:

'''Program: Print all the even numbers between the given range and also give a count.'''

start = int(input("Enter the Starting value: "))
end = int(input("Enter the Ending value: "))
count = 0
temp = start
while start <= end:
    if start % 2 == 0:
        count = count + 1
        print(start , end =" ")
    start = start + 1

print(F"\nThere are {count} even Numbers between {temp} to {end}")

output:
Enter the Starting value: 100
Enter the Ending value: 150
100 102 104 106 108 110 112 114 116 118 120 122 124 126 128 130 132 134 136 138 140 142 144 146 148 150 
There are 26 even Numbers between 100 to 150



exp 3:

'''#multiplication table
2
1
10

2x1=2
2x2=4
2x3=6
-
-
2x10=20'''

num = int(input("Enter the Table Number: "))
start = int(input("Enter the Starting value: "))
end = int(input("Enter the Ending value: "))

while start <= end:
    print(F"{num}x{start}={num*start}")
    start=start+1

output:
Enter the Table Number: 10
Enter the Starting value: 1
Enter the Ending value: 5
10x1=10
10x2=20
10x3=30
10x4=40
10x5=50



example: Random Number

Random set of numbers
#To generate a Random Number in python: randint(start, end)
#This pre-defined function is present inside a python file called: random

a. Import the random Module
b. Use the funtion to generate a random number:
c. ModuleName.FuntionName()'''

program:

import  random
x = random.randint(0,9)
print("Random Number=", x)

output:
Random Number= 4

================================================================== RESTART: E:/228A1A4440/while loops.py =================================================================
Random Number= 5

================================================================== RESTART: E:/228A1A4440/while loops.py =================================================================
Random Number= 4


program: OTP number program

exp:
import random
n = int(input("Enter the Number of Digits: "))
i = 1
print("OTP Number is", end=" ")
while i<=n:
    print(random.randint(0,9), end="")
    i = i + 1

output:
Enter the Number of Digits: 6
OTP Number is 919169

--------------------------------------------------------------------------

Collection: String. List & Tuple

All these 3 data types are based on Index.
s='java'

Every element of the collection will occupy one index position
Index is used a indivudual index positions in python

2 types of Indexes are avaliable-
a.positive Index Position: Moving in forward direction (Left to Right)

start = 0
end = N-1
N = number of elements
b. Negative Index Position: Moving in backward direction (Right To Left)
Example:
# String
s = 'java'
print(s)   --> java
print(s[0])--> j
print(s[-4])-->j

Internal Memory:
0     1     2     3
j     a     v     a
-4    -3    -2    -1

# List
L = [45, 85, 10, 5, 70]
print(L) --->[45, 85, 10, 5, 70]
print(L[-4] --> 85


Internal Memory
 0      1     2     3     4
45     85    10    5     70
-5     -4    -3   -2     -1
----------------------------------------------------------------------------

# while loop with Strings
----------------------------------
s="python"
print("String value=",s)
print()

output:
String value= python


st = input("Enter a String : ")
#FETCHING THE NUMBER OF CHARACTER PRESENT WITHIN THE STRING

n=len(s)
# variable i is used to maintain the index position
i=0 # starting position

while i < n:
  print(st[i])
  i+=1

OUTPUT:
Enter a String : kalyan
k
a
l
y
a
n

# print the ASCII value of your Name and total
# Hint: ord() - it return the ASCII number equival

program:

name = input("Enter Name: ")
n = len(name)
i = 0
total = 0
print(F"Char ASCII")
while i<n:
    print(F"{name[i]}\t{ord(name[i])}")
    total = total + ord(name[i])
    i+=1
print("ASCII Total =", total)

output:

Enter Name: kalyan
Char ASCII
k	107
a	97
l	108
y	121
a	97
n	110
ASCII Total = 640

#List
example:
L=["Python", 45, 78.3, False, 49+8j]
n = len(L)
i = 0
while i<n:
    print(F"{i}\t{L[i]}")
    i+=1
print()

output:
0	Python
1	45
2	78.3
3	False
4	(49+8j)


#Tuple
T = ('C', 'C++', 'Python', 'Java', 'R', 'HTML', 'CSS', 'JavaScript')
n = len(T)
i = 0
print("Tuple Values are: ")
while i<n:
    print(F"{i}\t{T[i]}")
    i+=1
print()

output:
Tuple Values are: 
0	C
1	C++
2	Python
3	Java
4	R
5	HTML
6	CSS
7	JavaScript


===================================================================================================================


b.for loop
--------------
It is type of entry controlled loop
keep executing the statements with in the body of the loop until the condition turns false.once the condition becomes false,the loop will terminate
keywords : for,in
collection : Strings, Lists, Tuples, Sets, dictionaries
1.simple for loop
Syntax:
     for varName in collection:
         code to execute
Note: 
 It is Value based loop --> every time the loop executes,one value from the collection is fetched and gets stored inside varName 
 There is no start(OR) end value given;the loop will automatically start from the beginning of the collection and iterate till the end.
 Traversal is always in Forward direction

program:
working on simple for loop program 

#collections
s=input()
print("String = ",s)
print("Using Simple for LOOP to print String values")
print(f"letter\tAscii")
for var in s:
    print(f"{var}\t{ord(var)}")
print()
l=[10,20,30,40,50]
print("Using for loop to print list")
for ele in l:
    print(ele)
print()
t=('Apple','Orange','Banana','Grapes')
print("Using for loop to print tuple")
for v in t:
    print(v)
print()
st={'Black','White','Blue','Green','Red','Yellow'}
print("using for loop to print sets")
for se in st:
    print(se)
print()
d={1:'ONE',2:'TWO',3:'THREE'}
#data gest stored based on keys : no index
#only keys will retrieved
print("using for loop to print dictionaries")
for e in d:
    print(e)
print()
  
O/P:

Kalyan
String =  Kalyan
Using Simple for LOOP to print String values
letter	Ascii
K	75
a	97
l	108
y	121
a	97
n	110

Using for loop to print list
10
20
30
40
50

Using for loop to print tuple
Apple
Orange
Banana
Grapes

using for loop to print sets
White
Red
Yellow
Blue
Green
Black

using for loop to print dictionaries
1
2
3

==============================================================
    
2.for loop with range()
syntax:
for varName in range(start, stop, step):
    code to execute

range() -->One of the data type in pythin
to generate a sequence of numbers
Syntax:
range(start ,stop, step)

start-->represents the starting number of series.
stop -->represents the ending number of sequence.
is excluded(end=end-1)
step=it is used to generate the next number number within the sequence 
next=current+step


Default values : when you do not mention a value,then the inmtrepreter will consider the default values
start=0;step=1
start & step =optional
stop=mandatory


example:
range(1,10,2) --> start=1,stop=9,step=2 : 1 3 5 7 9
range(10)     --> start=0,stop=9;step=1 : 0 1 2 3 4 5 6 7 8 9

NOTE :
This is an index based loop with collections
yhis type of loop can be used only with list,string,tuples


Program : for loop working with string 

l=[20,30,59,43,22]
print("List : ",l)
for i in range(0,len(l),1):
    print(f"index {i} : {l[i]}")
    
o/p:

List :  [20, 30, 59, 43, 22]
index 0 : 20
index 1 : 30
index 2 : 59
index 3 : 43
index 4 : 22

append() --> insert element at the end of the list
program : to insert uppercase letters in list 

l=[]
for i in range(65,91,1):
    l.append(chr(i))
print(l)

O/p:

['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

program : to insert lowercase letters in list 


l=[]
for i in range(97,123,1):
    l.append(chr(i))
print(l)

o/p:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

program : to insert digits in list 

l=[]
for i in range(48,58,1):
    l.append(chr(i))
print(l)

o/p:

['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



program : to insert multiples of 5

l=[]
for i in range(5,101,5):
    l.append(i)
print(l)

o/p:

[5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]


program : for loop working with string 

s=input()
print("index\tuppercase")
for i in range(0,len(s),1):
    print(f"{i}\t{s[i].upper()}")


o/p:

kalyan
index	uppercase
0	K
1	A
2	L
3	Y
4	A
5	N


program : find upper,lower,special character,digit in a string

s=input()
for i in range(len(s)):
    if s[i].isupper():
        print(f"{s[i]}\tUPPER")
    elif s[i].islower():
        print(f"{s[i]}\tlower")
    elif s[i].isdigit():
        print(f"{s[i]}\tdigit")
    else:
        print(f"{s[i]}\tspecial character")


O/P:

Kalyan@123
K	UPPER
a	lower
l	lower
y	lower
a	lower
n	lower
@	special character
1	digit
2	digit
3	digit


=====================================================================

3.for loop with enumerate()
syntax:

for varName in enumerate(collection):
    code to execute

It will fetch the index,value both together as a tupke in each iteration from the collection.


program

s="kalyan"
l=[10,20,30,40,50]
t=('Apple','Orange','Banana','Grapes')
st={'Black','White','Blue','Green','Red','Yellow'}
d={1:'ONE',2:'TWO',3:'THREE'}

#strings -(index,value)
print("strings -(index,value)")
for x in enumerate(s):
    print(x)
print()
for i,j in enumerate(s):
    print(f"{i}\t{j}")
print()
print("list")
for k in enumerate(l):
    print(k)
print()
for k,m in enumerate(l):
    print(f"{k}\t{m}")
print()
print("sets")
for k in enumerate(st):
    print(k)
print()
for k,m in enumerate(st):
    print(f"{k}\t{m}")
print()
print("tuples")
for k in enumerate(t):
    print(k)
print()
for k,m in enumerate(t):
    print(f"{k}\t{m}")
print()
print("dictionaries")
for x in enumerate(d):
    print(d)
print()
for i,v in enumerate(d):
    print(f"{v}\t{d[v]}")
print()

O/P:

strings -(index,value)
(0, 'k')
(1, 'a')
(2, 'l')
(3, 'y')
(4, 'a')
(5, 'n')

0	k
1	a
2	l
3	y
4	a
5	n

list
(0, 10)
(1, 20)
(2, 30)
(3, 40)
(4, 50)

0	10
1	20
2	30
3	40
4	50

sets
(0, 'Yellow')
(1, 'Blue')
(2, 'Black')
(3, 'Green')
(4, 'White')
(5, 'Red')

0	Yellow
1	Blue
2	Black
3	Green
4	White
5	Red

tuples
(0, 'Apple')
(1, 'Orange')
(2, 'Banana')
(3, 'Grapes')

0	Apple
1	Orange
2	Banana
3	Grapes

dictionaries
{1: 'ONE', 2: 'TWO', 3: 'THREE'}
{1: 'ONE', 2: 'TWO', 3: 'THREE'}
{1: 'ONE', 2: 'TWO', 3: 'THREE'}

1	ONE
2	TWO
3	THREE

==================================================================================================

4.for loop with zip()

Syntax:
for varName in zip(collection,..........,collection):
     code to execute

rno=[4454,4449,4440]
names=['Kalyan','Naveen','Vishnu']
marks=[100,100,100]

'''output
   4454  Kalyan 100
   4449  Naveen 100
   4440  Vishnu 100
   '''
for i,j,k in zip(rno,names,marks):
    print(f"{i}\t{j}\t{k}")
print()


o/p:

4454	Kalyan	100
4449	Naveen	100
4440	Vishnu	100


In Python : Loops can have else statements
when the loops condition becomes False,the else part will get execute 

Example:
using for 
for i in range(5):
    print("Good morning")
else:
    print("Welcome")

O/P;-

Good morning
Good morning
Good morning
Good morning
Good morning
Welcome

using while
i=1
while(i<=5):
    print("Good morning")
    i=i+1
else:
    print("Welcome")

O/P:
Good morning
Good morning
Good morning
Good morning
Good morning
Welcome
=========================================================================================================
Jump Statements : It is used inside the loop statements

--> break:

==>This keyword is used to come out of loop.
   It is used inside the loop statements

for i in range(1,101):
    print(i,end=" ")
    if(i==10):
        break
print("Loop ended")

O/P:
1 2 3 4 5 6 7 8 9 10 Loop ended

'''program:
write a Python program to keep on reading a number from the user util they enter zero'''

while(True):
    m=int(input("enter the number : "))
    if(m==0):
        break
print("The user enter 0")

o/p:
enter the number : 45
enter the number : 5
enter the number : 4
enter the number : 8
enter the number : 85
enter the number : 8
enter the number : 0
The user enter 0


'''program:
write a Python program to keep on reading a number from the user util they enter zero find count and sum'''
coun=0
sum=0
avg=0
while(True):
    m=int(input("enter the number : "))
    if(m==0):
        break
    coun+=1
    sum=sum+m
print("The user enter 0")
print(f"count: {coun} sum: {sum} avg: {sum/coun}")

O/P:

enter the number : 45
enter the number : 6456
enter the number : 485
enter the number : 48454
enter the number : 85485485
enter the number : 85485
enter the number : 454850
enter the number : 0
The user enter 0
count: 7 sum: 86081260 avg: 12297322.857142856

NOTE:
If the loop is terminated using the break keyword;else part of code wil not get executed.


for i in range(5):
    print("Goood Morning")
    if(i==4):
        break  
else:
    print("Welcome")
    
Goood Morning
Goood Morning
Goood Morning
Goood Morning
Goood Morning

------------------------------------------------------------------------------------------------
--> continue

It is used to skip the current iteration and proceed to the next in the sequence

Q)print all numbers below 10 skip 3 and 7

for i in range(1,11,1):
    if(i==3 or i==7):
        continue
    print(i,end=" ")

1 2 4 5 6 8 9 10 

q)read 10 numbers from the user and find the sum.
Condition:If there are any negative numbers dont take consideration

sum=0
for i in range(10):
    a=int(input("enter a number : "))
    if(a<0):
        continue
    sum=sum+a
print(f"Sum : {sum}")

enter a number : 1
enter a number : 1
enter a number : 1
enter a number : 1
enter a number : 1
enter a number : 1
enter a number : -1
enter a number : -1
enter a number : -1
enter a number : -1
Sum : 6

----------------------------------------------------------------------------------
- pass : Do nothing

for i in range(21):
    if(i%2==0):
        print(i,end=" ")
    else:
        pass

0 2 4 6 8 10 12 14 16 18 20 
------------------------------------------------------------------------------------

- return

===========================================================================================


LISTS AND LISTS MANUPULATIONS IN PYTHON
---------------------------------------

Key Features of List 

1. List is a Collection – We can store multiple values under a single variable.

2. We can create a List by placing elements inside a square bracket [ ] where each element will be separated from the other with using a comma.
Examples:
L1 = [25,96,85,15,37,90,47]
L2 = ['C++', 'Python', 'JavaScript', 'PHP', 'CSS']

3. Lists in Python are Homogenous (or) Heterogeneous.
A List can contain data of the same type --> Homogenous
Example:
L3 = ['Ruby', 'R', 'HTML', 'CSS', 'C++'] --> A list of Strings

A single list may contain types like Integers, Floating point, Strings, Complex, Boolean as well as other Objects --> Heterogeneous
Example:
L3 = [10, 25.63, True, 'Python', 45+6j] --> A list having different types

4. The list is an Ordered sequence collection.
The elements get stored in the same order in which elements gets added into the List.
Example:
L4 = [10, 25.63, Tru4, 'Python', 45+6j]
print(L4)
Output:
[10, 25.63, Tru4, 'Python', 45+6j]
   
5. List elements can be accessed using Indexes.
We have both Positive and Negative indexes for the list.
Positive Index:
Index is labelled from starting of the List and goes till the end (Forward Direction).
The starting index value is 0 and the index value is always incremented by 1.
And the ending index is always N-1, where N is the length of the list.
Negative Index:
It starts from the ending of the List and goes on to the start (Backward Direction).
The Index value begins from -1 and ends with -N. The index value is always decremented by 1.
Index value can never be anything other than an integer.
Slicing operation is possible on the List as they are index based.
Random Access of elements is possible due to the indexing.

6. Dynamic in Nature: List is internally a dynamic array which can grow and shrink in size as and when the elements are added or removed from the list respectively.

7. List permits to store Duplicate values.
Example:
L4 = [10, 25, 96, 10, 25, 10, 96, 10]

8. List is a mutable sequence  Data can be inserted, updated, and deleted.
------------------------------------------------------------------------------------------------------------------------------------------------------------
Similarities: Arrays & Lists

Ordered sequence
Individual element can be accesses using Index
Allows duplicate elements
Mutable - add, delete, update

Differences: Arrays & Lists

1. Arrays: Homogenous
     int a[] = {10,52,63,89}; 
     double d[] = {45.3, 59.8, 78.2}

     Lists: Homogenous (or) Heterogeneous
     L3 = ['Ruby', 'R', 'HTML', 'CSS', 'C++']
     L3 = [10, 25.63, True, 'Python', 45+6j]

2. Arrays: Only Positive Index is available
    Lists: Positive & Negative Indexes

3. Arrays: Fixed size - size cannot grow or shrink
    int a[10];
    double d[20];
    
    Lists: Dynamic
    No need to mention the size. when we add element, size automatically increases and when we delete an element, size automatically     
    decreases.


1.What are the different ways to create a list?

A.Direct Intialisation
l=[78,56,456,5,748,4,'False',"good"]

B.Empty List
l1=[]
l2=list()

C.Dynamic : Input:eval() Function
input() will read the data and eval() will convert the data into appropriate data type

eval("5<7<9")
True
eval("1023+123")
1146
eval("3>5>9<5")
False

->Write a Python program to print the even index postions values with in a list
Input:l=[78,56,456,5,748,4,'False',"good"]
Output:
78
456
748
False

l=eval(input("enter a list : "))
for i in range(0,len(l),2):
    print(l[i])

O/P:
enter a list : [78,56,456,5,748,4,'False',"good"]
78
456
748
False

l=eval(input(""))
print(l)
print(type(l))

O/P:

45j
45j
<class 'complex'>

{10,20,30,40}
{40, 10, 20, 30}
<class 'set'>

D.Dynamic Input -Using Loops

#empty list
l=[]
#ask the user -how many data in insert into the list?
n=int(input("Enetr the number of elements : "))
#Loop - to read N values and store it into the list
for i in range(n):
    #reading the element
    e=eval(input("enter the element : "))
    #Inserting the element into list
    l.append(e)
#print the liist
print("List =",l)

O/P:

Enetr the number of elements : 8
enter the element : 79
enter the element : 45.2
enter the element : False
enter the element : 45j
enter the element : [78,25]
enter the element : 'Python'
enter the element : {'c','c++'}
enter the element : (15,25)
List = [79, 45.2, False, 45j, [78, 25], 'Python', {'c++', 'c'}, (15, 25)]


#while loop
#empty list
l=[]
#ask the user -how many data in insert into the list?
n=int(input("Enetr the number of elements : "))
#Loop - to read N values and store it into the list
i=0
while(i<n):
    #reading the element
    e=eval(input("enter the element : "))
    #Inserting the element into list
    l.append(e)
    i=i+1
#print the liist
print("List =",l)

O/P:
Enetr the number of elements : 8
enter the element : 4
enter the element : 5.2
enter the element : 8j
enter the element : True
enter the element : [10,20]
enter the element : 'c'
enter the element : {20,30}
enter the element : (30,40)
List = [4, 5.2, 8j, True, [10, 20], 'c', {20, 30}, (30, 40)]

E.Using the split() function we are going to create a list
Syntax:
string.split()           -->split the data based on empty space
string.split('delimeter')-->split the data based on delimeter in the quotes
After splitting the string this function returns the value inside the list in a string format.

x=input("Enter Data")
t=x.split()
print(t)

Enter Data10 20 30 40 50
['10', '20', '30', '40', '50']

Enter Datawelcome to programming
['welcome', 'to', 'programming']

x=input("Enter Data: ")
t=x.split('#')
print(t)

Enter Data: 10#20#30
['10', '20', '30']

x=input("Enter Data: ")
t=x.split('o')
print(t)

Enter Data: welcome to Python
['welc', 'me t', ' Pyth', 'n']

F.Using the list() Function
==>list() - convert the data passed to it as a parameter into the list 

x=list(range(1,11))
print(x)
l=list(map(chr,range(97,123)))
# chr(int)==>ASCII character equivalent of the number
# range()==> generates a sequence of numbers
# map(datatype/function,iterables/variable)--> it will apply the specify the function on each and every valuewith in the iterable.
print(l)

O/P:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

s=input("Enter the numbers : ")
t=s.split()
print("list : ",t)
x=list(map(int,t))
print("list: ",x)

Enter the numbers : 10 20 30 40 50 60 70 80 90 20 30 40 50 60
list :  ['10', '20', '30', '40', '50', '60', '70', '80', '90', '20', '30', '40', '50', '60']
list:  [10, 20, 30, 40, 50, 60, 70, 80, 90, 20, 30, 40, 50, 60]


#creating a list from an exixting sequence

#string
s="java"
l=list(s)
print(l)

#tuple
t=(45,67,89,79)
print(list(t))
      
#set
st={'R','PHP','RUBY'}
print(list(st))
      
#Dictionary
d={'name':"Kalyan",'age':20}
print(list(d))

o/p:
['j', 'a', 'v', 'a']
[45, 67, 89, 79]
['R', 'RUBY', 'PHP']
['name', 'age']




G.List Comprehension

syntax:
list=[expression for item in list/range() if condition if condition ......]
general way==>
for item in list/range():
      if condition:
          if condition:
     (both are same)




#even number from 1-50 -create a list
l=[]
for i in range(1,51):
    if(i%2==0):
        l.append(i)
print(l)

print()
print()

l=[i for i in range(1,51)if i%2==0]
print(l)

O/P:

[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]


[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50]

#creating a alphabet list
l=[chr(i) for i in range(97,123)]
print(l)

O/P:

['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#create a square of a number list
l=[x*x for x in range(1,11)]
print(l)

O/P:

[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#odd number list
l=[i for i in range(1,51) if i%2!=0]
print(l)

O/P:
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]

#creating 2 to the power of number list
l=[2**j for j in range(1,6)]
print(l)

O/P:
[2, 4, 8, 16, 32]


#filtering the list for even numbers
l=[10,20,30,40,50,25,35,45,55,65,75]
l1=[i for i in l if(i%2==0)]
print(l1)

O/P:
[10, 20, 30, 40, 50]

#multiple if conditions in list comprehension
l=[i for i in range(20) if i%2==0 if i%3==0]
print(l)


print()

s=[]
for i in range(20):
    if i%2==0:
        if i%3==0:
            s.append(i)
print(s)

O/P:

[0, 6, 12, 18]

[0, 6, 12, 18]


==> How to check whether the list is empty or not?
------------------------------------------------------

l1=[45,96,12,10,3,6]
l2=[]

==> 1st method : len() function

#len(): len() returns an integer value which represents the total number of elements present in the list if the list is empty it returns the value zero

syntax:
 len(collection)


n=len(l1)
if n==0:
    print("list is empty")
else:
    print("list contains values")

print()
n=len(l1)
#any non zero value is considers as True Zero means false
if n:
    print("list contains values")
else:
    print("list is empty")

print()
#if the collection is empty it says false if the collection contains any values then it is true
if l2:
    print("list contain value")
else:
    print("list is empty")

o/p:

list contains values

list contains values

list is empty



==> 2nd method : bool() function
# bool() --> if the collection is empty it says false if the collection contains any values then it is true
# syntax:
#    bool(collection)

l1=[45,96,12,10,3,6]
l2=[]

if bool(l1):
    print("list contains values")
else:
    print("list is empty")

print()
if bool(l2):
    print("list contains values")
else:
    print("list is empty")

O/P:

list contains values

list is empty

-------------------------------------------------------------------------------------------------------------

==>Indexing

The individual elements of the list can be accessed using the indices. 
In Python, we have both Positive and Negative Indexes.
Whenever we try to access an invalid index position – Error is thrown: IndexError: list index out of range

NOTE:
Strings, Lists and Tuples are all Index based sequences.

Example 1:
L1 = [ 10, 56, 45.25, 89.3,'A', 'C', "Python", "Java", 10+2j, True ]
# Printing theentire List
print(f"List -{L1}")
 
# Accessing Individual elements within the List
print(L1[0])
print(L1[-1])
print(L1[4])
print(L1[-4])
print(L1[-2])
 
List -[10, 56, 45.25, 89.3, 'A', 'C', 'Python', 'Java', (10+2j), True]
10
True
A
Python
(10+2j)


# When accessed beyond the Index range
print(L1[25])

Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 174, in <module>
    print(L1[25])
IndexError: list index out of range
Example 2:
List1 = [10, "Anu", 10.50, True, [100,200,300], (1,2,3), {10.5,20.5,30.5}]



# Accessing Individual List element
print("List -",List1)
print(List1[0])
print(List1[4])
print(List1[5])
print(List1[6])
print()

# Accessing Individual element of a sequence within the List
print(List1[1])
print(List1[1][2])
print(List1[4])
print(List1[4][1])
print(List1[5])
print(List1[5][0])


List - [10, 'Anu', 10.5, True, [100, 200, 300], (1, 2, 3), {10.5, 20.5, 30.5}]
10
[100, 200, 300]
(1, 2, 3)
{10.5, 20.5, 30.5}

Anu
u
[100, 200, 300]
200
(1, 2, 3)
1


==> Double indexing
-> possible for only list,string,tuple

l=[10,"kalyan",10.5,True,[100,200,300],(1,2,3),{10.5,20.5,30.5}]
print(l[1][2])
print(l[4][-1])
print(l[5][-3])
print(l[4][0])

l
300
1
100


==>Slicing

syntax:
object[start : end : step]

start = starting index position from where the slicing has to begin 
end = ending index position; where to stop the slicing.  end is always excluded (end = end - 1)
step = decides the next index position within the  sequence.

start , end, step --> all are Optional : object[ : : ]

• If the start value is not given: starts from the beginning of the list
• If the end value is not given: goes till the end of the list
• If the step value is not given: default step value is 1

The direction of slicing is decided based on the step value given.


• step value positive: slicing from Left to Right (Forward direction) --> Object[ : : 1] (or) Object[ : : ]
• step value negative:     slicing from Right to Left (Backward direction) --> Object[ : : -1]



# having 0-8 indexes - positive indexes
# having -1 t0 -9 negative index range

l=[10,"kalyan",10.5,True,[100,200,300],(1,2,3),{10.5,20.5,30.5},40+5j,{5:'Five',10:'ten'}]
#output : [True, [100, 200, 300], (1, 2, 3)]
x=l[3:6]
print(x)
print()
# when you slice alist the result will be list

#output : [10.5, True, [100, 200, 300], (1, 2, 3), {10.5, 20.5, 30.5}]
x=l[-7:-2]
print(x)
print()

# reverse a list ==> [::-1]
x=l[::-1]
print(x)
print()

#output: Complete list will be taken - forward direction
#default step value --> 1
x=l[::]
print(x)
print()

#output: Complete list will be taken - reverse direction
#default step value --> -1 slicing will occur from right hand to left hand direction
x=l[::-1]
print(x)
print()

#output:[]
#No slicing will takes place
x=l[-2:-7]
print(x)
print()

#output: [(40+5j), {10.5, 20.5, 30.5}, (1, 2, 3), [100, 200, 300], True]
x=l[-2:-7:-1]
print(x)
print()

O/P:

[True, [100, 200, 300], (1, 2, 3)]

[10.5, True, [100, 200, 300], (1, 2, 3), {10.5, 20.5, 30.5}]

[{5: 'Five', 10: 'ten'}, (40+5j), {10.5, 20.5, 30.5}, (1, 2, 3), [100, 200, 300], True, 10.5, 'kalyan', 10]

[10, 'kalyan', 10.5, True, [100, 200, 300], (1, 2, 3), {10.5, 20.5, 30.5}, (40+5j), {5: 'Five', 10: 'ten'}]

[{5: 'Five', 10: 'ten'}, (40+5j), {10.5, 20.5, 30.5}, (1, 2, 3), [100, 200, 300], True, 10.5, 'kalyan', 10]

[]

[(40+5j), {10.5, 20.5, 30.5}, (1, 2, 3), [100, 200, 300], True]


Inserting Values into the list
--------------------------------
a.append() : inserting the data to the end of the list.
This function can insert only one data  at the time.
syntax:
    list_name.append(item)

Example:

l=[(45,35,67),{100,200,300}]
print("List :",l)
l.append(1)
l.append(2.3)
l.append(True)
l.append("Kalyan")
l.append([80,90,100])
print("Modified list :",l)

List : [(45, 35, 67), {100, 300, 200}]
Modified list : [(45, 35, 67), {100, 300, 200}, 1, 2.3, True, 'Kalyan', [80, 90, 100]]


b.insert() : This function is used to insert data at the desired position.
Shifting of index position will occur.
syntax:
    list_name.insert(index,item)

EXAMPLE:
l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.insert(0,"Python")
l.insert(5,"C")
print("Modified List :",l)

# invalid index positions

# Positive index :data will inserted at the end of list .

l.insert(100,"java")
print("Modified List :",l)

# Positive index :data will inserted at the starting of list.

l.insert(-50,"C++")
print("Modified List :",l)

List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : ['Python', 45, 96, 78, 45, 'C', 6, 7, 89, 355, 89]
Modified List : ['Python', 45, 96, 78, 45, 'C', 6, 7, 89, 355, 89, 'java']
Modified List : ['C++', 'Python', 45, 96, 78, 45, 'C', 6, 7, 89, 355, 89, 'java']



c.extend() : This function add data to the end of the list.
This  function can add multiple data into the list at the same time.
It can insert ONLY Collection type

Syntax:
    list_name.extend(iterable)

EXAMPLE:

l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.extend([10,20,30,40])
l.extend("java")
print("Modified List :",l)


List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 96, 78, 45, 6, 7, 89, 355, 89, 10, 20, 30, 40, 'j', 'a', 'v', 'a']


l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.extend(10)

List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 233, in <module>
    l.extend(10)
TypeError: 'int' object is not iterable

==> Differnece between append() and extend()

l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.extend([10,20,30,40])
l.extend("java")
print("Modified List :",l)


l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.append([10,20,30,40])
l.append("java")
print("Modified List :",l)


List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 96, 78, 45, 6, 7, 89, 355, 89, 10, 20, 30, 40, 'j', 'a', 'v', 'a']
List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 96, 78, 45, 6, 7, 89, 355, 89, [10, 20, 30, 40], 'java']



Deleting Values from the list
------------------------------

a. remove() : value based deletion
If the element occurs multiple times it will remove only first occurance .In case of a string it is case sensitive
If the given value not present you will get ValueError
Syntax:
      list_name.remove(item)

l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.remove(89)
print("Modified List :",l)

List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 96, 78, 45, 6, 7, 355, 89]



l=['Bob','Alice','Tony','Thor']
l.remove('Bob')
print("Modified List :",l)
l.remove('tony')
print("Modified List :",l)

Modified List : ['Alice', 'Tony', 'Thor']
Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 239, in <module>
    l.remove('tony')
ValueError: list.remove(x): x not in list


b.pop()   : Index based deletion 
If the specified index not present it will get IndexError
Syntax:
       list_name.pop(Index)


l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
l.pop(1)
l.pop(5)
l.pop(2)
print("Modified List :",l)
l.pop(6)
print("Modified List :",l)

List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 78, 6, 7, 355, 89]
Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 249, in <module>
    l.pop(6)
IndexError: pop index out of range


c.pop() : it deleted last inserted value
If pop is given on an empty list 

Syntax:
          list_name.pop()

l=[45,96,78,45]
print("List :",l)
l.pop()
l.pop()
l.pop()
l.pop()
print("Modified List :",l)
l.pop()

List : [45, 96, 78, 45]
Modified List : []
Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 265, in <module>
    l.pop()
IndexError: pop from empty list

d.del :  deletes the element at certain index.
Syntax:
        del list_name[index]

l=[45,96,78,45,6,7,89,355,89]
print("List :",l)
del l[2]
del l[3]
print("Modified List :",l)
del l[100]

List : [45, 96, 78, 45, 6, 7, 89, 355, 89]
Modified List : [45, 96, 45, 7, 89, 355, 89]
Traceback (most recent call last):
  File "E:/228a1a4454/list example.py", line 257, in <module>
    del l[100]
IndexError: list assignment index out of range


Deleting Entire list
----------------------

a. del: It will delete the specified Object from Memory. Once deleted that object cannot be used again, If used - ERROR: NameError
Syntax:
    del list_name
   
Example:
L = [10,45,10,96]
print("List: ", L)
del L
print("List: ", L)


List:  [10, 45, 10, 96]
Traceback (most recent call last):
  File "C:\Users\Santhosh\Downloads\list example.py", line 273, in <module>
    print("List: ", L)
NameError: name 'L' is not defined



b. clear(): it will empty the list; deletes the content of the list, not the list itself.
Syntax:
    list_name.clear()

Example:
L = [10,45,10,96]
print("List: ", L)
L.clear()
print("List: ", L)
L.append('C++')
L.append('R')
print("List: ", L)


List:  [10, 45, 10, 96]
List:  []
List:  ['C++', 'R']


Sorting a List
---------------------

a. sort(): It is used to sort the list. Default Sorting - Ascending Order. It will change the positions of the elements within the list.
Changes will reflect on the Original List
Syntax:
    list_name.sort()
    This is used to sort the list in ascending order.

    list_name.sort(reverse=True)
    This is used to sort the list in descending order.
   
Example: Ascending Order
L = [45,10,5,78,100,54]
print("Before Sorting: " , L)
L.sort()
print("After Sorting: " , L)
print()

L = ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python']
print("Before Sorting: " , L)
L.sort()
print("After Sorting: " , L)
print()


Before Sorting:  [45, 10, 5, 78, 100, 54]
After Sorting:  [5, 10, 45, 54, 78, 100]

Before Sorting:  ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python']
After Sorting:  ['C', 'Java', 'Javascript', 'MYSQL', 'PHP', 'Python', 'R']


Example: Descending Order
L = [45,10,5,78,100,54]
print("Before Sorting: " , L)
L.sort(reverse = True)
print("After Sorting: " , L)
print()

L = ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python', 'Zebra']
print("Before Sorting: " , L)
L.sort(reverse = True)
print("After Sorting: " , L)
print()


Before Sorting:  [45, 10, 5, 78, 100, 54]
After Sorting:  [100, 78, 54, 45, 10, 5]

Before Sorting:  ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python', 'Zebra']
After Sorting:  ['Zebra', 'R', 'Python', 'PHP', 'MYSQL', 'Javascript', 'Java', 'C']



b. sorted(): It is used to sort the list and creates a new list as the result. Default Sorting - Ascending Order. Original List is not affected.
Syntax:
    sorted(list_name)
   
Example:
L = [45,10,5,78,100,54]
print("Before Sorting: " , L)
t = sorted(L)
print("Original List: " , L)
print("After Sorting: " , t)
print()

Before Sorting:  [45, 10, 5, 78, 100, 54]
Original List:  [45, 10, 5, 78, 100, 54]
After Sorting:  [5, 10, 45, 54, 78, 100]


L = ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python', 'Zebra']
print("Before Sorting: " , L)
t = sorted(L, reverse=True)
print("Original List: " , L)
print("After Sorting: " , t)
print()

Before Sorting:  ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python', 'Zebra']
Original List:  ['Java', 'C', 'R', 'PHP', 'MYSQL', 'Javascript', 'Python', 'Zebra']
After Sorting:  ['Zebra', 'R', 'Python', 'PHP', 'MYSQL', 'Javascript', 'Java', 'C']

Reversing a List
-----------------------

a. Slicing
Syntax:  list_name[::-1]
   
b. reverse()
Syntax:  list_name.reverse()

Example:
L = [45,10,5,78,100,54]
print("Original List: " , L)
L.reverse()
print("Reversed List: " , L)
print()

L = [45,10,5,78,100,54]
print("Original List: " , L)
print("Reversed List: " , L[::-1])


Original List:  [45, 10, 5, 78, 100, 54]
Reversed List:  [54, 100, 78, 5, 10, 45]

Original List:  [45, 10, 5, 78, 100, 54]
Reversed List:  [54, 100, 78, 5, 10, 45]


Copying a List
------------------

a. Slicing
Syntax: list_name = list_name[::]

b. copy()
Syntax: list_name.copy()
   
Example:
L1 = [45,10,5,78,100,54]
print("Original List: " , L1)
L2 = L1.copy()
print("Copied List: " , L2)
L3 = L1[ : : ]
print("Copied List: " , L3)

Original List:  [45, 10, 5, 78, 100, 54]
Copied List:  [45, 10, 5, 78, 100, 54]
Copied List:  [45, 10, 5, 78, 100, 54]
------------------------------------------------------------------------------------------------------------------------------------------------------------
Counting the Occurrence of an element

count(): It returns the number of times an element occurs within the List. It the specified element is not present = 0. Case Sensitive.
Syntax:
    list_name.count(element)
   
Example:
L = [45, 40.23, False, 'C', 45, True, 'c', True, 'java']
print("Original List: " , L)
print("True =" , L.count(True))
print("False =", L.count(False))
print("C =", L.count('C'))
print("Java =", L.count('Java'))

Original List:  [45, 40.23, False, 'C', 45, True, 'c', True, 'java']
True = 2
False = 1
C = 1
Java = 0
------------------------------------------------------------------------------------------------------------------------------------------------------------
Finding the Index Position of an element

index(): It returns the index position of the specified element. If multiple times the element is present - 1st Occurrence index value
Case sensitive. If the specified element is not present: ERROR
Syntax:
    list_name.index(element, start, end)

Example:
L = [40, 20, 55, 96, 40, 74, 16, 40, 0, -5]
print("L = ", L)
print("Index of 40 =" , L.index(40))
print("Index of 0 =" , L.index(0))
print("Index of -5 =" , L.index(-5))
print("Index of 40 [5:]=" , L.index(40,5,len(L)))


L =  [40, 20, 55, 96, 40, 74, 16, 40, 0, -5]
Index of 40 = 0
Index of 0 = 8
Index of -5 = 9
Index of 40 [5:]= 7
------------------------------------------------------------------------------------------------------------------------------------------------------------
Other Functions

1. len()  -->  Return the number of elements present within the list.
2. max()  -->  Returns the maximum value present within the list.
3. min()  -->  Returns the minimum value present within the list.
4. sum()  -->  Returns the sum of all the elements present within the list.
5. any()  -->  Returns True if any element within the list is True (Logical OR)
6. all()  -->  Returns True if all the elements within the list is True.(Logical AND)

Example:
L = [78, 20, 55, 96, 74, 16, 40, 0, -5]
print("L = ", L)
print("Length of the List = ", len(L))
print("Total = ", sum(L))
print("Smallest Number = ", min(L))
print("Biggest Number = ", max(L))
print("ANY = ", any(L))
print("ALL = ", all(L))

L =  [78, 20, 55, 96, 74, 16, 40, 0, -5]
Length of the List =  9
Total =  374
Smallest Number =  -5
Biggest Number =  96
ANY =  True 
ALL =  False

======================================================================================================

Data Structures :Tuples
------------------------

Key Points:
------------
a.Pre-defined Ds,collection,Itetable Type
b.Created using() with comma seperated values
c.Ordered:The way in which data is inserted the same way it gets internally stored.
d.It is index bases: RAndom Access possible; Slicing is possible
e.Dynamic in nature: No Fixed Size
f.can contain both homogeneous and heterogeneous elements
g.Allows Duplicate Values
h.Immutable: Data Cannot be inserted ,updated or deleted

Pre-defined Functions supported by Tuple
-----------------------------------------
1.len()
2.sum()
3.min()
4.max()
5.count()
6.index()
7.clear()
8.del keyword

# Creating Tuple – Direct Initialization
t1 = ('C', 'Java', 'Python', 10, 45.89, "M", 74)
print("Tuple 1:",t1)


Tuple 1: ('C', 'Java', 'Python', 10, 45.89, 'M', 74)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating Tuple – Direct Initialization: without using the Parenthesis
t2 = 10, 20, 30
print("Tuple 2:",t2)

t3 = "Java", "Python", "C"
print("Tuple 3:",t3) 


Tuple 2: (10, 20, 30)
Tuple 3: ('Java', 'Python', 'C')
-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating a Single value Tuple
t4 = (10,)
print("Tuple 4",t4)
print("Data Type:",type(t4))

Tuple 4 (10,)
Data Type: <class 'tuple'>
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dynamic Input: eval() Function
t5 = eval(input("Enter a Tuple: "))
print("Tuple 5:",t5)

Enter a Tuple: 10,20,30,40
Tuple 5: (10, 20, 30, 40)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dynamic Input: tuple() Function - Type Conversion
L = []
n = int(input("How many elements?: "))
for i in range(n):
    e = eval(input("Enter the element: "))
    L.append(e)

# Convert the List into a Tuple
t6 = tuple(L)
print("Tuple 6:",t6)


How many elements?: 5
Enter the element: 10,20,30,40,50
Enter the element: 50
Enter the element: 20
Enter the element: 30
Enter the element: 40
Tuple 6: ((10, 20, 30, 40, 50), 50, 20, 30, 40)

------------------------------------------------------------------------------------------------------------------------------------------------------------
# tuple() Function
D1 = {'Name':'Anu', 'Desig':'Trainer'}
S1 = {56,96,74,85,91,20,36}

# Converting a Dict into a Tuple - Only Keys will get Coonverted
t7 = tuple(D1)
print("Tuple 7:",t7)

# Converting a Set into a Tuple
t8= tuple(S1)
print("Tuple 8:",t8)

Tuple 7: ('Name', 'Desig')
Tuple 8: (96, 36, 20, 85, 56, 74, 91)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Creating an Empty Tuple
t9 = ()
print("Tuple 9:",t9)

Tuple 9: ()
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tuple Comprehension : NOT Supported - Immutable
t10 = (x**2 for x in range(1,6))
print(type(t10))
for x in t10:
    print(x)

<class 'generator'>
1
4
9
16
25
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Heterogeneous Tuple -
anu_info = (
("Anushya", "Srikanth"),
"Trainer",
("Chennai", "Tamil Nadu"),
[("NRI", "Vijayawada"),
("MITS", "Madanapalli"),
("SANK", "Gudur"),
("QIS", "Ongole"),
("Geetanjali", "Nellore"),
("PVKK", "Ananthapur")] )
print("Anu's Personal Information -")
print(anu_info)

Anu's Personal Information -
(('Anushya', 'Srikanth'), 'Trainer', ('Chennai', 'Tamil Nadu'), [('NRI', 'Vijayawada'), ('MITS', 'Madanapalli'), ('SANK', 'Gudur'), ('QIS', 'Ongole'), ('Geetanjali', 'Nellore'), ('PVKK', 'Ananthapur')])
------------------------------------------------------------------------------------------------------------------------------------------------------------
# + Operator performs the Tuple Concatenation
t1  = ('Python','Java','C')
t2 = ('C++','Ruby','Python','MySQL','Java')
print("Tuple 1:",t1)
print("Tuple 2:",t2)
# Tuple Concatenation
print('Concatenation of Tuples:\n',t1+t2)

Tuple 1: ('Python', 'Java', 'C')
Tuple 2: ('C++', 'Ruby', 'Python', 'MySQL', 'Java')
Concatenation of Tuples:
 ('Python', 'Java', 'C', 'C++', 'Ruby', 'Python', 'MySQL', 'Java')
------------------------------------------------------------------------------------------------------------------------------------------------------------
# * Operator performs the Tuple Repetation
t1  = ('Python','Java','C')
print("Tuple 1:",t1)
# Tuple Repetation
print('Tuple repeated 2 times:\n',t1*2)

Tuple 1: ('Python', 'Java', 'C')
Tuple repeated 2 times:
 ('Python', 'Java', 'C', 'Python', 'Java', 'C')
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Accessing Typle Elements through Indexes
t = ('C', 40, ('Python', 'C++'),['C#','Javascript','Ruby'],
     'Pearl',20.36,{'Admin':'admin@123'})
print("Tuple Contents are :\n " , t)
print()

Tuple Contents are :
  ('C', 40, ('Python', 'C++'), ['C#', 'Javascript', 'Ruby'], 'Pearl', 20.36, {'Admin': 'admin@123'})

# Individual Element
print("Index 0:",t[0])
print("Index -1:",t[-1])
print("Index 2:",t[2])
print("Index 3:",t[3])

# Index of Index
print("Index [3][2]:",t[3][2])
print("Index [2][1]:",t[2][1])
print("Index [3][2][2]:",t[3][2][2])

Tuple Contents are :
  ('C', 40, ('Python', 'C++'), ['C#', 'Javascript', 'Ruby'], 'Pearl', 20.36, {'Admin': 'admin@123'})

Index 0: C
Index -1: {'Admin': 'admin@123'}
Index 2: ('Python', 'C++')
Index 3: ['C#', 'Javascript', 'Ruby']
Index [3][2]: Ruby
Index [2][1]: C++
Index [3][2][2]: b
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Slicing
t = ("C", "C++", "Java", "Python", "HTML")
print("Tuple Contains - \n" ,t)
print()

# Slicing
print("Slicing [0:3] -",t[0:3])
print("Slicing [0:-2] -",t[0:-2])
print("Slicing [::-1] -",t[::-1])
print("Slicing [0::2] -",t[0::2])

Tuple Contains - 
 ('C', 'C++', 'Java', 'Python', 'HTML')

Slicing [0:3] - ('C', 'C++', 'Java')
Slicing [0:-2] - ('C', 'C++', 'Java')
Slicing [::-1] - ('HTML', 'Python', 'Java', 'C++', 'C')
Slicing [0::2] - ('C', 'Java', 'HTML')
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Iterating Over a Tuple

t = ('C', 40, ('Python', 'C++'),['C#','Javascript','Ruby'],'Pearl',20.36,{'Admin':'admin@123'});
print("Tuple Contents are :\n " , t)

print()

# SImple for Loop
for i in t:
    print(i)
print()

# for Loop with range()
n = len(t)
for x in range(n):
    print (x,t[x])
print()

# for Loop with enumerate
for x in enumerate(t):
    print(x)
print()

# Using while Loop
n = len(t)
i = 0
while i< n:
    print(t[i])
    i += 1


Tuple Contents are :
  ('C', 40, ('Python', 'C++'), ['C#', 'Javascript', 'Ruby'], 'Pearl', 20.36, {'Admin': 'admin@123'})

C
40
('Python', 'C++')
['C#', 'Javascript', 'Ruby']
Pearl
20.36
{'Admin': 'admin@123'}

0 C
1 40
2 ('Python', 'C++')
3 ['C#', 'Javascript', 'Ruby']
4 Pearl
5 20.36
6 {'Admin': 'admin@123'}

(0, 'C')
(1, 40)
(2, ('Python', 'C++'))
(3, ['C#', 'Javascript', 'Ruby'])
(4, 'Pearl')
(5, 20.36)
(6, {'Admin': 'admin@123'})

C
40
('Python', 'C++')
['C#', 'Javascript', 'Ruby']
Pearl
20.36
{'Admin': 'admin@123'}

------------------------------------------------------------------------------------------------------------------------------------------------------------
# Packing & Unpacking a Tuple

Example 1:
# Packing
person_detail = ("Srikanth RK", 34, "India", "AP")
# unpacking
name, age, country, state = person_detail
# printing results
print("Name:", name)
print("Age:", age)
print("Country:", country)
print("State:", state)

Name: Srikanth RK
Age: 34
Country: India
State: AP


Example 2:
# Packing
person_detail = ("Srikanth RK", 34, "India", "AP")
# unpacking
name, _, country, _ = person_detail
# printing results
print("Name:", name)
print("Country:", country)


Name: Srikanth RK
Country: India


Example 3:
# Packing
person_detail = ("Srikanth RK", 34, "India", "AP", "Vijayawada")
# Unpacking
name,*_, state = person_detail
# printing results
print("Name:", name)
print("State:", state)    

Name: Srikanth RK
State: Vijayawada


Example 4:
# Packing - tuple having 5 elements
tup = (78,96,35,15,100)
print("Tuple:", tup)

# Unpacking - ERROR
# Number of values within the tuple and number of variables does not match
a,b,c,d = tup
print(F"a={a}, b={b}, c={c}, d={d}")

# Unpacking - ERROR
# Number of values within the tuple and number of variables does not match
a,b,c,d,e,f = tup
print(F"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}")

Example 5:
# Function Definition
def result(x, y):
    return x * y
# Function Calling
print("Function Returns:",result(10, 100))

Function Returns: 1000


# A tuple is created
z = (10, 10)
# Tuple is passed to Function as argumentb by unpacked them
print("Function Returns:",result(*z))


Function Returns: 1000
Function Returns: 100


Example 6:
a, *b = 1, 2, 3
print(F"a={a}, b={b}")

*a, b = 1, 2, 3
print(F"a={a}, b={b}")

*a, b, c = 1, 2, 3
print(F"a={a}, b={b}, c={c}")

*a, b, c, d = 1, 2, 3
print(F"a={a}, b={b}, c={c}, d={d}")

seq = [1, 2, 3, 4, 5, 6]
a,*b,c = seq
print(F"a={a}, b={b}, c={c}")


a=1, b=[2, 3]
a=[1, 2], b=3
a=[1], b=2, c=3
a=[], b=1, c=2, d=3
a=1, b=[2, 3, 4, 5], c=6

# Error
# Correct Way: *r, = range(10)
*r = range(10)
print(F"r={r}")
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Tuple Comparision
t1 = (5,6,7,8,9)
t2 = (1,4,5,8,6,10)
t3 = (5,6,7,8,9)

print("Tuple 1:",t1)
print("Tuple 2:",t2)
print("Tuple 3:",t3)

print()

print("t1 == t3:",t1==t3)
print("t1 != t2:",t1!=t2)
print("t1 > t2:",t1>t2)
print("t1 < t2:",t1<t2)
print("t2 >= t1:",t2>=t1)
print("t1 >= t3:",t1>=t3)



Tuple 1: (5, 6, 7, 8, 9)
Tuple 2: (1, 4, 5, 8, 6, 10)
Tuple 3: (5, 6, 7, 8, 9)

t1 == t3: True
t1 != t2: True
t1 > t2: True
t1 < t2: False
t2 >= t1: False
t1 >= t3: True
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Function returning more than one value - Tuple type

import math

# Function Definition
def F(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * math.pi * r
    a = math.pi * r * r
    return (c, a)

# Function calling
# Returned value is unpacked and assigned to the 2 variables
area,circum = F(5)
print("Area =",round(area,2))
print("Circumference =",round(circum,2))
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Inserting an element into a Tuple

# Tuple
t = (45,69,87,96)

# Inserting an new element at the end of the Tuple
print(F"Tuple: {t}")
temp = list(t)
temp.append(800)
t = tuple(temp)
print(F"Modified Tuple: {t}")
print()

# Inserting element at Index 1
print(F"Tuple: {t}")
temp = list(t)
temp.insert(1,800)
t = tuple(temp)
print(F"Modified Tuple: {t}")


Tuple: (45, 69, 87, 96)
Modified Tuple: (45, 69, 87, 96, 800)

Tuple: (45, 69, 87, 96, 800)
Modified Tuple: (45, 800, 69, 87, 96, 800)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Removing element from a Tuple

# Tuple
t = (45,69,87,96,10,56,20,30)

# Removing the value at Index position 2
print(F"Tuple: {t}")
temp = list(t)
temp.pop(2)
t = tuple(temp)
print(F"Modified Tuple: {t}")
print()

# Removing the value 45
print(F"Tuple: {t}")
temp = list(t)
temp.remove(45)
t = tuple(temp)
print(F"Modified Tuple: {t}")
print()

# Removing the value at Index 2 usng Slicing
t = t[:2] + t[3:]
print(F"Modified Tuple: {t}")

Tuple: (45, 69, 87, 96, 10, 56, 20, 30)
Modified Tuple: (45, 69, 96, 10, 56, 20, 30)

Tuple: (45, 69, 96, 10, 56, 20, 30)
Modified Tuple: (69, 96, 10, 56, 20, 30)

Modified Tuple: (69, 96, 56, 20, 30)

------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deleting the entire Tuple

# Tuple
t = (45,69,87,96,10,56,20,30)
print(F"Tuple: {t}")

# Deleting the Tuple
del t

print(F"Tuple: {t}")

Tuple: (45, 69, 87, 96, 10, 56, 20, 30)
Traceback (most recent call last):
  File "E:/228a1a4454/tuple ex.py", line 264, in <module>
    print(F"Tuple: {t}")
NameError: name 't' is not defined
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sorting a Tuple

Example 1:
t = (45,69,87,96,10,56,20,30)
print(F"Tuple: {t}")
# Sorting the Tuple
t = tuple(sorted(t))
print(F"Tuple after Sorting: {t}")

Tuple: (45, 69, 87, 96, 10, 56, 20, 30)
Tuple after Sorting: (10, 20, 30, 45, 56, 69, 87, 96)

Example 2:
t = (45,69,87,96,10,56,20,30)
print(F"Tuple: {t}")
# Sorting
temp = list(t)
temp.sort()
t = tuple(temp)
print(F"Tuple after Sorting: {t}")

Tuple: (45, 69, 87, 96, 10, 56, 20, 30)
Tuple after Sorting: (10, 20, 30, 45, 56, 69, 87, 96)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Membership Operator

t1 = ('C', 'Java','Ruby','Python')
print("Tuple1 Content:" , t1)
print("Is 'C' present in the Tuple ? ", 'C' in t1)
print("'C++' not present in the Tuple ? ", 'C++' not in t1)

Tuple1 Content: ('C', 'Java', 'Ruby', 'Python')
Is 'C' present in the Tuple ?  True
'C++' not present in the Tuple ?  True
------------------------------------------------------------------------------------------------------------------------------------------------------------
# len()
t1 = ('C', 'Java', 'Python', 'C++','C#')
print("Tuple 1 : " , t1)
print("Tuple1 Length is",len(t1))

Tuple 1 :  ('C', 'Java', 'Python', 'C++', 'C#')
Tuple1 Length is 5
------------------------------------------------------------------------------------------------------------------------------------------------------------
# count()
tup = (1, 3, 5, 8, 7, 5, 4, 6, 8, 5)
print("Tuple Content",tup)
x = tup.count(5)
print("5 occurs",x,"times")

Tuple Content (1, 3, 5, 8, 7, 5, 4, 6, 8, 5)
5 occurs 3 times
------------------------------------------------------------------------------------------------------------------------------------------------------------
# index(element,startPos, endPos)
t = (1,3,8,5,8,1,7,8,7,5,4,6,5,8,12,56,44,5)
print("Tuple Content",tup)

x = t.index(8)
print("1st Occurrence Index Position of 8 is:",x)

x = t.index(8,6)
print("1st Occurrence of 8 starting from Index 6:",x)

x = t.index(8,7,12)
print("1st Occurrence of 8 between the range 7 to 12 indexes:",x)

# If element not Present
x = t.index(1500)
print("Index Position of 1500 =",x)

Tuple Content (1, 3, 8, 5, 8, 1, 7, 8, 7, 5, 4, 6, 5, 8, 12, 56, 44, 5)
1st Occurrence Index Position of 8 is: 2
1st Occurrence of 8 starting from Index 6: 7
1st Occurrence of 8 between the range 7 to 12 indexes: 7
Traceback (most recent call last):
  File "E:/228a1a4454/tuple ex.py", line 310, in <module>
    x = t.index(1500)
ValueError: tuple.index(x): x not in tuple
------------------------------------------------------------------------------------------------------------------------------------------------------------
# min(), max() and sum()

t1 = (10,5,4,100,25,69,45,1)
print("Tuple:",t1)
print("Max Value:",max(t1))
print("Min Value:",min(t1))
print("Sum of Tuple:",sum(t1))


Tuple: (10, 5, 4, 100, 25, 69, 45, 1)
Max Value: 100
Min Value: 1
Sum of Tuple: 259
------------------------------------------------------------------------------------------------------------------------------------------------------------
Modules in Python
--------------------


Module:
Python File that consist of Functions / Variables.
File Extension: .py
This file can be imported and shared across multiple users.

File: P1.py
print("Welcome to Python Programming Language")
print("IT is the most easiest of the programming languages")
print("All the best learning it!")

File: P2.py
import P1

<No other code inside this File>

output:
Welcome to Python Programming Language
IT is the most easiest of the programming languages
All the best learning it!
------------------------------------------------------------------------------------------------------------------------------------------------------------
Importing a Module into a Program

a. import <Module Name>
The complete file will get imported.
Use:
    Module_Name.Function_Name()

b. from <Module Name> import <Function Name> , ....
Only the Function name mentioned will get imported into our code
Use:
    Function_Name()
Module Name: random

Errors:
ModuleNotFoundError : when the given Module name is not available
ImportError:When the Function name with the Module is given incorrectle
------------------------------------------------------------------------------------------------------------------------------------------------------------
pre-defined Modules

1. os (Operating System)
2. sys (System-Specific Parameters and Functions)
3. math (Mathematical Functions)
4. datetime (Dates and Times)
5. random (Generate Random Numbers)
6. re (Regular Expressions)
7. collections (High-Performance Container Datatypes)
8. itertools (Functions Creating Iterators for Efficient Looping)
9. functools (Higher-Order Functions and Operations on Callable Objects)
------------------------------------------------------------------------------------------------------------------------------------------------------------
Module Name: random

It is used to generate a Random value.


Functions within the Module -
a. randrange()
b. randint()
c. random()
d. uniform()
e. choice()
f. sample()
g. shuffle()
------------------------------------------------------------------------------------------------------------------------------------------------------------
Random Integer Functions

Function: randrange()
It is used to select a random integer number from the generated sequence.
start value is included; stop value is excluded.

Syntax:
    randrange(start, stop, step)

Examples:
import random

x = random.randrange(5,500,5)
print(F"Random Number = {x}")
print()
x = random.randrange(1,50000)
print(F"Random Number = {x}")
print()
Random Number = 390

Random Number = 1728
============================= 
Random Number = 190

Random Number = 30789

---------------------------------------

Function: randint()
This function will select a random integer number from the specified range.
Both start & stop is inclusive.
Syntax:
    randint(start, stop)

Examples:
import random

x = random.randint(1,5)
print(F"Random Number = {x}")

x = random.randint(500,1000)
print(F"Random Number = {x}")

print(F"Random Number = ",end= ' ')
for i in range(6):
    x = random.randint(1,5)
    print(x, end='')


Random Number = 3
Random Number = 719
Random Number =  234552

------------------------------------------------------------------------------------------------------------------------------------------------------------
Random Float Functions

Function: random()
This function will always generate a Floating-point random number between the range of 0 to 1
It takes no parameters.
Syntax:
    random()
   
Function: uniform()
This function will select a random floating-point number from the specified range.
Syntax:
    uniform(start, stop)

Examples:
import random

print(F"Random Float Number between 0 to 1: {random.random()}")
print(F"Random Float Number between 0 to 1: {random.random()}")
print(F"Random Float Number between 0 to 1: {random.random()}")
print()
print(F"Random Float Number between 1 to 10: {random.uniform(1,10)}")
print(F"Random Float Number between 1000 to 10,000: {random.uniform(1000,100000)}")

Random Float Number between 0 to 1: 0.40032562101644653
Random Float Number between 0 to 1: 0.845740352935644
Random Float Number between 0 to 1: 0.14937547797870454

Random Float Number between 1 to 10: 2.482560384261104
Random Float Number between 1000 to 10,000: 67192.19884780532
------------------------------------------------------------------------------------------------------------------------------------------------------------
Random Collection Functions

Iterables: String, List, Tuple (Index Based)
It will not work with : Set &Dictionary
   
Function: choice()
It is used to select ONE random value from the given iterable.
Syntax:
    choice(Iterable_Name)
   
Examples:
import random

s = "programming"
l = [45, 63, 'C', 'Apples', 'Javascript', 'R', 'Oranges', 78, 90, 120]
t = (10,20,30,40,50)
st = {45,50,55,60}
d = {'Name':'Anu', 'Desig':'Trainer'}

# String
x = random.choice(s)
print(F"From the String: Random character = {x}")
# List
x = random.choice(l)
print(F"From the List: Random element = {x}")
# Tuple
x = random.choice(t)
print(F"From the Tuple: Random element = {x}")

# Both the below Types will generate ERROR
# Set
x = random.choice(st)
print(F"From the Set: Random element = {x}")
# Dictionary
x = random.choice(d)
print(F"From the Dict: Random element = {x}")


From the String: Random character = g
From the List: Random element = R
From the Tuple: Random element = 40
Traceback (most recent call last):
  File "E:/228a1a4454/random.py", line 136, in <module>
    x = random.choice(st)
  File "C:\Users\Rise\AppData\Local\Programs\Python\Python311\Lib\random.py", line 374, in choice
    return seq[self._randbelow(len(seq))]
TypeError: 'set' object is not subscriptable

-------------------------------------------------------
Function: sample()
It is used to select multiple random value from the given iterable.
It returns the result in form a List.
Syntax:
    sample(Iterable_Name, count)

Examples:
import random

s = "programming"
l = [45, 63, 'C', 'Apples', 'Javascript', 'R', 'Oranges', 78, 90, 120]
t = (10,20,30,40,50)

# String
x = random.sample(s, 3)
print(F"From the String: Random characters = {x}")
# List
x = random.sample(l, 4)
print(F"From the List: Random elements = {x}")
# Tuple
x = random.sample(t, 2)
print(F"From the Tuple: Random elements = {x}")


From the String: Random characters = ['m', 'g', 'o']
From the List: Random elements = [78, 'Apples', 45, 120]
From the Tuple: Random elements = [20, 30]

--------------------------------------------------------
Function: shuffle()
It works Only on Lists; Because Tuples & Strings are immutable, hence values cannot be modified.
It will randomly change the order of the elements present within the List.
Syntax:
    shuffle(List_Name)

Example:
import random

L = [45, 63, 'C', 'Apples', 'Javascript', 'R', 'Oranges', 78, 90, 120]
print(F"Original List = {L}")
random.shuffle(L)
print(F"Shuffled List 1= {L}")
random.shuffle(L)
print(F"Shuffled List 2= {L}")
random.shuffle(L)
print(F"Shuffled List 3= {L}")

Original List = [45, 63, 'C', 'Apples', 'Javascript', 'R', 'Oranges', 78, 90, 120]
Shuffled List 1= ['C', 45, 'R', 'Oranges', 90, 'Javascript', 63, 120, 'Apples', 78]
Shuffled List 2= [78, 120, 63, 'R', 'Apples', 90, 45, 'C', 'Oranges', 'Javascript']
Shuffled List 3= [120, 'R', 45, 'Javascript', 'C', 63, 78, 'Oranges', 90, 'Apples']

------------------------------------------


EXAMPLE:



from random import randrange,randint,random,uniform

#int numbers --> randrange,randint

x=randrange(5,100,5)
print(f"random Number : {x}")

x=randrange(0,100,2)
print(f"random Number : {x}")


x=randint(1,10)
print(f"random Number : {x}")

#float numbers --> random,unifrom

x=random() #always generate a number b/w 0 to 1
print(f"random Number : {x}")

x=uniform(50,100)
print(f"random Number : {x}")


random Number : 70
random Number : 96
random Number : 6
random Number : 0.4301617184725185
random Number : 57.969214502855095

---------------------------------------------------------------------------

random Number : 30
random Number : 78
random Number : 8
random Number : 0.6087113052669744
random Number : 77.75165949495701

-----------------------------------------------------------------------

# Collection /Iterable : List, Tuple, Set, Dictionary, String
# Index Based : List, String, Tuple --> choice(),sample(),shuffle()
# Functions are applied only on the index based

from random import choice,sample,shuffle

s="Kalyan"
l=[10,20,34,45,3,2,4,5,6,78,90]
t=(2,3,5,6,8,9,23,44,656,56,78)

# choice()--> used to select one random value from my collection

x=choice(s)
print(f"Random character from the string : {x}")

x=choice(l)
print(f"Random character from the list : {x}")

x=choice(t)
print(f"Random character from the tuple : {x}")

print()
print()


#sample() --> used to pick multiple values


x=sample(s,5)
print(f"Random character from the string : {x}")

x=sample(l,6)
print(f"Random character from the list : {x}")

x=sample(t,7)
print(f"Random character from the tuple : {x}")

print()
print()

#shuffle() --> changing the order ; Can work ONLY on mutable datatype : List


print("Original List : ",l)
shuffle(l)
print("Shuffled List : ",l)
shuffle(l)
print("Shuffled List : ",l)
shuffle(l)
print("Shuffled List : ",l)


Random character from the string : a
Random character from the list : 45
Random character from the tuple : 44


Random character from the string : ['K', 'a', 'l', 'a', 'y']
Random character from the list : [90, 34, 78, 2, 4, 5]
Random character from the tuple : [44, 9, 56, 78, 2, 5, 23]


Original List :  [10, 20, 34, 45, 3, 2, 4, 5, 6, 78, 90]
Shuffled List :  [3, 20, 78, 4, 2, 90, 34, 45, 10, 6, 5]
Shuffled List :  [20, 45, 3, 4, 34, 5, 2, 90, 6, 10, 78]
Shuffled List :  [90, 34, 45, 2, 3, 5, 6, 20, 10, 78, 4]

-----------------------------------------------------------------

Random character from the string : y
Random character from the list : 5
Random character from the tuple : 3


Random character from the string : ['a', 'K', 'y', 'a', 'n']
Random character from the list : [5, 90, 4, 34, 45, 6]
Random character from the tuple : [8, 56, 23, 656, 2, 3, 44]


Original List :  [10, 20, 34, 45, 3, 2, 4, 5, 6, 78, 90]
Shuffled List :  [78, 6, 20, 2, 10, 5, 45, 34, 4, 90, 3]
Shuffled List :  [34, 3, 5, 45, 20, 2, 90, 10, 6, 4, 78]
Shuffled List :  [2, 34, 6, 90, 4, 20, 45, 3, 5, 10, 78]


===========================================================================================================================================================

STRING & STRING MANIPULATIONS IN PYTHON
-------------------------------------------------------------------------------
C Language:         char na[50] = "Anushya S";
Java Language:   String na = "Anushya S";

What is a String?
String is a group of characters (alphabets both uppercase & lowercase, digits, and special characters)
enclosed within quotations.

NOTE: There is no char data type in Python. So, even a single character is treated as a String.
Ex:                  language = 'C'  --> String
C      --> char language = 'C'; --> char type - 1 byte
Java --> char language = 'C'; --> char type - 2 byte

1. It can be created in 3 ways: Single, Double, Triple Quotes

Example:
# Single Quoted String
s1 = 'Python 3.12'
print("Type =", type(s1))
print("Value =", s1)
print()

# Double Quoted String
# Output: I am enjoying 'Java' very much!
s2 = "I am enjoying 'Java' very much!"
print("Type =", type(s2))
print("Value =", s2)
print()

# Triple Quoted String: Multiline Strings
s3 = '''    Python
                       Rocks    '''
print("Type =", type(s3))
print("Value =", s3)
print()

s4 = """     Python
            Rules!       """
print("Type =", type(s4))
print("Value =", s4)
print()

Output:
    Type = <class 'str'>
Value = Python 3.12

Type = <class 'str'>
Value = I am enjoying 'Java' very much!

Type = <class 'str'>
Value =     Python
                       Rocks    

Type = <class 'str'>
Value =      Python
            Rules!      
------------------------------------------------------------------------------------------------------------------------------------------------------------
2. Strings are IMMUTABLE -> cannot be modified
    In Python - MUTABLE TYPES are: list, dict, set

Example:
s = "C++"
print("String =" , s)
print("Address of String =", id(s))

s = "Java"
print("String =" , s)
print("Address of String =", id(s))

Output:
String = C++
Address of String = 2657202361120
String = Java
Address of String = 2657162934384

Example:
s = "java"
print("String =" , s)
print("Address of String =", id(s))
print()

# Converts the String into Uppercase and produces a string as a result
r = s.upper()

print("Orinignal String =" , s)
print("Address of String =", id(s))
print()
print("Modified String =" , r)
print("Address of String =", id(r))

Output:
String = java
Address of String = 2413110471360

Orinignal String = java
Address of String = 2413110471360

Modified String = JAVA
Address of String = 2413110310112
------------------------------------------------------------------------------------------------------------------------------------------------------------
3. It is an iterable - can be looped over
    All the type of loops can be used to iterate over a String --> while, variations of for

Example:
# Reading the Input from the user
s = input("Enter the String: ")

# Simple for Loop
print("Simple For Loop")
for ele in s:
    print(ele)
print()

# for Loop with range()
print("for Loop with range()")
for i in range(0, len(s), 1):
    print(i,s[i])
print()

# for Loop with enumerate()
print("for Loop with enumerate()")
for x in enumerate(s):
    print(x)
print()

for x,y in enumerate(s):
    print(x,y)
print()

# while Loop
print("while Loop")
i = 0
while i < len(s):
    print(i,s[i])
    i+=1
print()
------------------------------------------------------------------------------------------------------------------------------------------------------------
4. Data is stored internally based on indexes (Random Access)

NOTE: 3 types in Python are Index Based: Lists, Strings and Tuples

In Python we have 2 types of Indexes:
    N = length of the String;
    a. Positive Index:   Forward direction   --> 0 to N-1
    b. Negative Index: Backward direction --> -1 to -N
   
Example:
s = "welcome Anu!"

''' INTERNAL STORAGE
0        1         2        3      4      5       6       7        8       9       10     11
w        e         l        c      o      m       e                A       n       u       !
-12     -11       -10      -9     -8     -7      -6       -5       -4      -3      -2      -1  
'''

# Accessing Individual Elements
print(s[0])
print(s[-1])
print(s[3])
print(s[-6])

# Invalid Index will generate Error - IndexError: string index out of range
print(s[100])
print(s[-20])
------------------------------------------------------------------------------------------------------------------------------------------------------------
5. Slicing can be applied

Syntax:
    String [start: stop: step]

NOTE: When we slice a string, the result we get is also a string
            Direction is decided based on the STEP value

Example:
s = "welcome Anu!"

''' INTERNAL STORAGE
0        1         2        3      4      5       6       7         8      9        10     11
w        e         l        c      o      m       e                 A       n       u       !
-12     -11       -10      -9     -8     -7      -6      -5        -4      -3      -2      -1  
'''

# Default Step Value = 1 ; Forward direction - from start to end
print(s[ : : ]) # welcome Anu!

# Step Value = 1 ; Forward direction - from start to end
print(s[ : :1]) # welcome Anu!

# Step Value = -1 ; Backward direction - from start to end
# Printitng the String in Reverse Order
print(s[::-1])

# Every 3rd character from the String: Forward direction - start to end
print(s[::3])

# From index 2 to Index -3 the characters will be fetched: Forward direction
print(s[2:-2:1]) # lcomeAn

# Default Step Value = 1 ; Clash in direction - Empty String will be produced as a result
print(s[-2:0]) # ""

# Invalid index positions in slicing - NO IndexError will be generated
# Default Step Value = 1; starting from index 0 till the end of the string slicing will happen
print(s[0:500]) # welcome Anu!

# Invalid index positions in slicing - NO IndexError will be generated
# Default Step Value = 1; Starting from -N to index 4 slicing will happen
print(s[-400:5]) # welco
------------------------------------------------------------------------------------------------------------------------------------------------------------
Interview Questions

1. What will be the Output?
str = "programming"
print(str[0])
print(str[-1])
print(str[1:5])
print(str[5:-2])
print(str[::1])
print(str[::-1])

Original String: "programming"
0        1        2        3        4        5         6        7         8        9        10
p        r        o        g        r        a         m        m         i         n        g
-11      -10     -9       -8       -7       -6        -5        -4       -3      -2        -1
------------------------------------------------------------------------------------------------------------------------------------------------------------
2. What will be the Output?
s="Python"
print(s[::-5])
print(s[::-1][::-5])
print(s[0]+s[-1])
print(s[::5])
print(s[::-1][-1]+s[len(s)-1])

Original String: "Python"
0        1         2        3        4        5
P        y         t        h        o        n
-6      -5        -4       -3       -2       -1

Reversed String: "nohtyP"
0        1        2        3        4        5
n        o        h       t         y        P
-6     -5        -4      -3       -2       -1    
------------------------------------------------------------------------------------------------------------------------------------------------------------
3. What will be the Output?
 
s = "PYTHON PROGRAMMING"
print(s[::-2])
print(s[2:3])
print(s[2:3:-1])
print(s[-6:7:-2])
print(s[4:-8])
print(s[9:-10])
print(s[22::-6])
print(s[2:-22:-1])
print(s[7::-1])
------------------------------------------------------------------------------------------------------------------------------------------------------------
6. Operator '+' does the work of concatenation / joining

Example:
s1 = "Welcome"
s2 = "to"
s3 = "Python"

s = s1 + ' ' + s2 + ' ' + s3
print("Concatenated String:",s)

Output:
Concatenated String: Welcome to Python
------------------------------------------------------------------------------------------------------------------------------------------------------------
7. Operator '*' does the work of repetition

Example:
s = "Welcome"
newStr = s * 3
print("Repeated String:" , newStr)

Output:
Repeated String: WelcomeWelcomeWelcome
------------------------------------------------------------------------------------------------------------------------------------------------------------
8. Membership Operators: in, not in
Used for the purpose of searching whether the given sub-string exists within the specified string or not.
Boolean value is returned as the output. Case Sensitive

• in: Returns True if a character exists within the given string otherwise False.
• not in: Returns True if a character does not exist in the given string otherwise returns False.

Example:
str = "Program"

print(f"Is 'gram' not present in the String?:   {'gram' not in str}")
print(f"Is 'grams' not present in the String?: {'grams' not in str}")
print()
print(f"Is 'a' present in the String?: {'a' in str}")
print(f"Is 'z' present in the String?: {'z' in str}")

Output:
Is 'gram' not present in the String?: False
Is 'grams' not present in the String?: True

Is 'a' present in the String?: True
Is 'z' present in the String?: False

Example:
string = input("Enter the String: ")
search = input("Enter the string to search: ")

if search in string:
    print("Found")
else:
    print("Not Found")
------------------------------------------------------------------------------------------------------------------------------------------------------------
9. Raw string - It is used to supresses the effects of the escape sequences used within the string.

Example:
print("This is \ngood\texample")
print()
print(r"This is \ngood\texample")
print(R"This is \ngood\texample")

Output:
This is
good    example

This is \ngood\texample
This is \ngood\texample

NOTE:
The same Job can also be done using the repr() function. The difference is that the output will be within single quotation.

Example:
print(repr("I \nLove\tPython"))
Output:
'I \nLove \tPython'
------------------------------------------------------------------------------------------------------------------------------------------------------------
Built-In String Functions

String have a very wide range of pre-defined functions.
General Syntax:
    str.FunctionName()

1. len():
    Syntax --> len(string)
    returns the length of the string and if the string is empty it returns 0
   
2. upper():
    Syntax --> str.upper()
    converts the string into uppercase and returns a new string as the result
   
3. lower():
    Syntax --> str.lower()
    converts the string into lowercase and returns a new string as the result

Example:
s = input("Enter the String: ")
print(F"Length of the String = {len(s)}")
print(F"String in Uppercase = {s.upper()}")
print(F"String in Lowercase = {s.lower()}")
------------------------------------------------------------------------------------------------------------------------------------------------------------
4. capitalize():
    Syntax --> str.capitalize()
    converts the entire string into lowercase alphabets except the 1st character, which will be in uppercase.

Example:
s = "PYTHON Programming is SO Cool!"
print(F"String = {s}")
print(F"Capitalized String = {s.capitalize()}")
------------------------------------------------------------------------------------------------------------------------------------------------------------
5. center():
    Syntax --> str.center(width, character)
    character is Optional; If not mentioned the default value is a single space.
    Decoration Purpose

Example:
s = "PYTHON"
print(F"String = {s}")
print(s.center(50))
print(s.center(50, '*'))
------------------------------------------------------------------------------------------------------------------------------------------------------------
6. count():
    Syntax --> str.count(character, start, end)
    start and end are Optional values. They are used when we want to search within a specific range
    It will return the number of occurrences of the specified character within the given string.
    Case sensitive search is performed.
   
Example:
s = "Welcome to python programming. Python is such a cool language. python is so easy to learn"
print(F"String = {s}")
print()

print(F"Number of time 'o' occurs = {s.count('o')}")
print(F"Number of time 'z' occurs = {s.count('z')}")
print(F"Number of time 'python' occurs = {s.count('python')}")
print(F"Number of time 'python' occurs = {s.count('python', 25)}")
print(F"Number of time 'python' occurs = {s.count('python', 25, 35)}")
------------------------------------------------------------------------------------------------------------------------------------------------------------
7. startswith():
    Boolean Function
    Syntax --> str.startswith(starting_char, start, end)
    start and end are optional parameters; They are used when we want to search within a specific range
    It will check whether the given string starts with the specified characters.
    Case Sensitive
   
8. endswith()
    Boolean Function
    Syntax --> str.endswith(ending_char, start, end)
    start and end are optional parameters; They are used when we want to search within a specific range
    It will check whether the given string ends with the specified characters.
    Case Sensitive

Example:
s = "Welcome to python programming."
print(F"String = {s}")
print()
print(F"Starts with 'Wel' = {s.startswith('Wel')}")
print(F"Ends with 'ing' = {s.endswith('ing')}")
print(F"Ends with 'ing.' = {s.endswith('ing.')}")
print()
print(F"Starts with 'py' from Index 11 = {s.startswith('py', 11)}")
----------------------------------------------------------------------------------------------------------------------------------------------------------  
9. find() --> gives which index the character is present
string.find('charcter')

10. rfind() --> The rfind() method finds the last occurrence of the specified value.
The rfind() method returns -1 if the value is not found.
string.rfind('character')


11. index() --> The index() method finds the first occurrence of the specified value.
The index() method raises an exception if the value is not found.
The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found.
string.index('character')

12. rindex() --> The rindex() method finds the last occurrence of the specified value.
The rindex() method raises an exception if the value is not found.
The rindex() method is almost the same as the rfind()
string.rindex('character')

13. title()--> The title() method returns a string where the first character in every word is upper case. Like a header, or a title.
If the word contains a number or a symbol, the first letter after that will be converted to upper case.
string.title()

14. join() -->The join() method takes all items in an iterable and joins them into one string.
A string must be specified as the separator.
"character/string".join(iterable)

15. ljust()-->The ljust() method will left align the string, using a specified character (space is default) as the fill character.
string.ljust(length, character)

16. rjust() --> The rjust() method will right align the string, using a specified character (space is default) as the fill character.
string.rjust(length, character)

17. swapecase()  -> The swapcase() method returns a string where all the upper case letters are lower case and vice versa.
string.swapcase()

18. lstrip() -->The lstrip() method removes any leading characters (space is the default leading character to remove)
string.lstrip(characters)

19. rstrip() -->The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
string.rstrip(characters)

20. strip() -->The strip() method removes any leading, and trailing whitespaces.
Leading means at the beginning of the string, trailing means at the end.
You can specify which character(s) to remove, if not, any whitespaces will be removed.
string.strip(characters)

21. replace()--> The replace() method replaces a specified phrase with another specified phrase.
string.replace(oldvalue, newvalue, count)

22. split() --> The split() method splits a string into a list.
You can specify the separator, default separator is any whitespace.
string.split(separator, maxsplit)

23. rsplit() --> The rsplit() method splits a string into a list, starting from the right.
If no "max" is specified, this method will return the same as the split() method.
string.rsplit(separator, maxsplit)

24. max() -->max() is an inbuilt function in Python programming language that returns the maximum alphabetical character in a string.
max(string) 
25. min() -->min() is an inbuilt function in Python programming language that returns the minimum alphabetical character in a string.
min(string) 

NOTE: All the functions starting with 'is' are Boolean - result will be either True (or) False

26. isalpha() --> The isalpha() method returns True if all the characters are alphabet letters (a-z).
Example of characters that are not alphabet letters: (space)!#%&? etc.
string.isalpha()


27. isdigit() -->The isdigit() method returns True if all the characters are digits, otherwise False.
Exponents, like ², are also considered to be a digit.
string.isdigit()

28. isnumeric()-->The isnumeric() method returns True if all the characters are numeric (0-9), otherwise False.
Exponents, like ² and ¾ are also considered to be numeric values.
"-1" and "1.5" are NOT considered numeric values, because all the characters in the string must be numeric, and the - and the . are not.
string.isnumeric()

29. isdecimal() -->The isdecimal() method returns True if all the characters are decimals (0-9).
string.isdecimal()

30. isidentifier() -->The isidentifier() method returns True if the string is a valid identifier, otherwise False.
A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
string.isidentifier()

31. isprintable() -->The isprintable() method returns True if all the characters are printable, otherwise False.
string.isprintable()

32. isspace() -->The isspace() method returns True if all the characters in a string are whitespaces, otherwise False.
string.isspace()

33. istitle() -->The istitle() method returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.
Symbols and numbers are ignored.
string.istitle()

34. isupper() -->The isupper() method returns True if all the characters are in upper case, otherwise False.
Numbers, symbols and spaces are not checked, only alphabet characters.
string.isupper()

35. islower() -->The islower() method returns True if all the characters are in lower case, otherwise False.
Numbers, symbols and spaces are not checked, only alphabet characters.
string.islower()

----------------------------------------------------------------------------------

Note:

***Difference between find() and index() Functions
The `find()` and `index()` functions in Python are both used to locate the position of a substring within a string, but they have some important differences in their behavior:

### 1. **Return Value**
- **`find(substring)`**: Returns the lowest index of the substring if found. If the substring is not found, it returns **`-1`**.
  
- **`index(substring)`**: Returns the lowest index of the substring if found. If the substring is not found, it raises a **`ValueError`**.

### 2. **Error Handling**
- **`find()`**: Does not raise an error if the substring is not found; it simply returns `-1`.
  
- **`index()`**: Raises a `ValueError` if the substring is not found, which can be caught using a try-except block if desired.

### 3. **Use Cases**
- Use **`find()`** when you want to check if a substring exists without raising an error.
- Use **`index()`** when you are certain the substring exists and want to get its position; if it doesn't exist, you want to be notified of the error.

### Example Code

Here's an example demonstrating both functions:

```python
text = "Hello, welcome to Python programming."

# Using find()
position = text.find("Python")
print(position)  # Output: 18

not_found_position = text.find("Java")
print(not_found_position)  # Output: -1

# Using index()
position_index = text.index("Python")
print(position_index)  # Output: 18

try:
    not_found_index = text.index("Java")
except ValueError as e:
    print(e)  # Output: substring not found
```

### Summary
- **`find()`**: returns `-1` when not found, no error.
- **`index()`**: raises `ValueError` when not found, must handle errors if you're unsure of the substring's presence.

Choosing between these functions depends on how you want to handle situations where the substring is not found.
    
***Difference between title() and capitalize() Functions
The `title()` and `capitalize()` methods in Python are both used to modify the case of strings, but they behave differently. Here’s a detailed comparison:

### 1. **Functionality**

- **`capitalize()`**:
  - Converts the first character of the entire string to uppercase.
  - Converts all other characters in the string to lowercase.
  
  **Example**:
  ```python
  text = "hello world"
  result = text.capitalize()
  print(result)  # Output: "Hello world"
  ```

- **`title()`**:
  - Converts the first character of each word in the string to uppercase.
  - Converts all other characters in each word to lowercase.
  
  **Example**:
  ```python
  text = "hello world"
  result = text.title()
  print(result)  # Output: "Hello World"
  ```

### 2. **Return Value**
- Both methods return a new string with the changes applied and do not modify the original string (strings in Python are immutable).

### 3. **Behavior with Different Inputs**

- **`capitalize()`**:
  - Affects only the first character of the string.
  
  **Example**:
  ```python
  text = "hElLo WoRlD"
  result = text.capitalize()
  print(result)  # Output: "Hello world"
  ```

- **`title()`**:
  - Affects every word in the string. Words are defined as sequences of characters separated by whitespace.
  
  **Example**:
  ```python
  text = "hElLo WoRlD"
  result = text.title()
  print(result)  # Output: "Hello World"
  ```

### 4. **Handling of Edge Cases**
- **`capitalize()`**:
  - Only the first character is capitalized; the rest are lowercased, regardless of their original case.
  
- **`title()`**:
  - Capitalizes the first letter of each word, but it may not handle special cases like contractions or words with apostrophes correctly.
  
  **Example**:
  ```python
  text = "it's a nice day"
  print(text.title())  # Output: "It'S A Nice Day"
  ```

### Summary
- **`capitalize()`**:
  - Use this method when you want to ensure that only the first letter of the entire string is uppercase, with all subsequent letters in lowercase.
  
- **`title()`**:
  - Use this method when you want each word in a string to start with an uppercase letter, but be aware of its limitations with certain punctuation and special characters.

By understanding these differences, you can choose the appropriate method based on your specific formatting needs!

***Difference between isdigit(), isnumeric() and isdecimal()
In Python, `isdigit()`, `isnumeric()`, and `isdecimal()` are string methods used to check whether the characters in a string represent numeric values. While they may seem similar, they have distinct differences in terms of the types of characters they recognize as numeric. Here’s a detailed comparison of these methods:

### 1. **Functionality**

- **`isdigit()`**:
  - Returns `True` if all characters in the string are digits (0-9).
  - This method recognizes digit characters from different numeral systems, including superscripts and fractions.
  
  **Example**:
  ```python
  s1 = "12345"
  s2 = "Ⅻ"  # Roman numeral for 12
  print(s1.isdigit())  # Output: True
  print(s2.isdigit())  # Output: True
  ```

- **`isnumeric()`**:
  - Returns `True` if all characters in the string are numeric characters.
  - This includes digit characters, fractions, Roman numerals, and other numeric types.
  
  **Example**:
  ```python
  s1 = "12345"
  s2 = "Ⅻ"  # Roman numeral for 12
  s3 = "1/2"  # Fraction
  print(s1.isnumeric())  # Output: True
  print(s2.isnumeric())  # Output: True
  print(s3.isnumeric())  # Output: True
  ```

- **`isdecimal()`**:
  - Returns `True` if all characters in the string are decimal characters (0-9).
  - This method is stricter than `isdigit()` and `isnumeric()`, as it does not recognize characters like fractions or Roman numerals.
  
  **Example**:
  ```python
  s1 = "12345"
  s2 = "Ⅻ"  # Roman numeral for 12
  s3 = "1.5"  # Decimal point is not allowed
  print(s1.isdecimal())  # Output: True
  print(s2.isdecimal())  # Output: False
  print(s3.isdecimal())  # Output: False
  ```

### 2. **Summary of Differences**

| Method      | Definition                      | Accepts             | Example Input | Output     |
|-------------|---------------------------------|---------------------|---------------|------------|
| `isdigit()` | True for digits and numeric     | Digits, Roman numerals, fractions | `"123"`, `"Ⅻ"` | True      |
| `isnumeric()` | True for all numeric characters | Digits, Roman numerals, fractions, etc. | `"123"`, `"Ⅻ"`, `"1/2"` | True |
| `isdecimal()` | True for decimal characters only| Only digits (0-9)  | `"123"`        | True      |

### 3. **Use Cases**
- Use **`isdigit()`** when you want to check if a string consists of digits, including numeric characters from different numeral systems.
- Use **`isnumeric()`** when you want a broader check that includes fractions and Roman numerals.
- Use **`isdecimal()`** when you need to ensure that the string contains only standard decimal digits.

### Examples for Clarity

```python
# isdigit()
print("12345".isdigit())  # True
print("Ⅻ".isdigit())      # True (Roman numeral)
print("12.34".isdigit())  # False (contains a decimal point)

# isnumeric()
print("12345".isnumeric())  # True
print("Ⅻ".isnumeric())      # True (Roman numeral)
print("1/2".isnumeric())    # True (fraction)

# isdecimal()
print("12345".isdecimal())  # True
print("Ⅻ".isdecimal())      # False (not a decimal digit)
print("12.34".isdecimal())  # False (contains a decimal point)
```

### Summary
- **`isdigit()`**: Checks for any digit character (0-9) and recognizes broader numeric characters.
- **`isnumeric()`**: Checks for any numeric character, including fractions and Roman numerals.
- **`isdecimal()`**: Checks for decimal digits (0-9) only, the strictest of the three.

Choosing the right method depends on the specific criteria for numeric validation in your application!

======================================================================================================================

DICTIONARY
----------------
An Introduction to Dictionary

• Dictionary is a Collection – We can store multiple values under a single variable.
• They are also known as Maps (or) Associative arrays.
• We can create a Dictionary by placing elements inside a curly brace { } where each element will be separated from the other with using a comma.
• They are used to store the data as a Key-Value pairs.

Examples :
User Ids - Passwords
IP Address - Domain Name
Employee ID - Name
City Name - Population
IME Number - Mobile Model

Syntax:
dictionary_Name = {key:value, key:value, key:value, …. , key_N:value}

Example:
d1={'Name':'Anushya', 'ID':1001, 'Dept':'IT' , 'Designation':'Trainer'} 


• Here 'Name' , 'ID' , 'Dept' , and 'Designation' are KEYS whereas 'Anushya' , 1001 , 'IT' , 'Trainer' are VALUES

NOTE:


• Keys must be UNIQUE and must be of a Immutable type
• Values can be duplicated and can be of Mutable / Immutable type
• Dictionaries can be Heterogeneous : A single Dictionary may contain types like Integers, Floating point, Strings, Complex, Boolean as well as other Objects.
• Dictionary are Ordered: The elements get stored in the same order in which they get added into the Dictionary. However, elements are not accessed using the position but using the Key.
• Dictionaries do not have INDEXES – hence Slicing is not possible.
• Dictionaries are Mutable : values can be modified - we can add, delete, update the values according to our requirement.
• Dynamic in Nature – No Fixed Size
• Random Access is possible: Individually elements of the dictionary can be accessed with their keys.

------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dynamic Input - Loop : Using eval() Function for Inputs
d = {}
n = int(input("Enter the Number of Items: "))
for i in range(n):
    k = eval(input("Enter the Key: "))
    v = eval(input("Enter the Value: "))
    d[k] = v

print(d)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Dict - Mutable
data= {
    'Stud_ID' : 1005,
    'Name' :'Anushya',
    'Dept' : 'CSE',
    'Sem' : 4,
    'Marks' : [96,78,95,87,90],
    'mbno' : 9381817369 ,
    'email' : 'anushya.trainer@gmail.com'
}
print("Original Dictionary Values:")
print(data)
print()

Insertion, Deletion, Updations are Possible

# Adding a Key-Value Pair --> Using Key Name, update() Function

# 1. Using Key Name
data['Fees'] = 85000
print("Modified Dictionary Values:")
print(data)
print()

# 2. update() Function
# Single data
data.update({'Location': 'Chennai'})
# Multiple data
data.update({"Qualify" :"B.Tech", 'Cname': 'RISE'})
print("Modified Dictionary Values:")
print(data)
print()

# Inserting Multiple data
d = {}
d.update(Desig='Trainer', Location='Chennai', Salary = 58000)
print(d)
print()

# Mergering Dict
A={'oct':"october",'nov':"november",'dec':"december"}
B={'jan':"january",'feb':"february"}
print("Dic1 -",A)
print("Dic2 -",B)
# Merging dict_2 with dict_1
A.update(B)
print("Dic1 Updated -",A)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Updating a Key-Value Pair --> Using the Key Name , update() Function

# 1. Using the Key Name
data['Name'] = "Anushya S"
print("Modified Dictionary Values:")
print(data)
print()

# 2. update() Function
data.update({'Name': "Anushya Srikanth"})
print("Modified Dictionary Values:")
print(data)
print()

# If the key is not present within the dict, it will get inserted as a new Key-Value pair
data.update({'ID':15005})
print("Modified Dictionary Values:")
print(data)
print()
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Deleting a Key-Value Pair --> del, clear(), pop(), potitem()

# pop() Function: deletes the specified key along with its value from the dict
# Syntax:    pop(del_key, msg) - It returns the deleted key's value

mb = data.pop('mbno' )
print(F"{mb} is deleted from the dictionary")

addr = data.pop('address' , 'Key is not available')
print(F"Deleted Info: {addr}")

print("Modified Dictionary Values:")
print(data)
print()

# popitem() Function: deletes the last inserted key-value pair
# Syntax: dict.popitem()
data.popitem()
data.popitem()
print("Modified Dictionary Values:")
print(data)
print()

# clear() : It will empty the dict; earse all the content
data.clear()
print("Modified Dictionary Values:")
print(data)
print()

# Keyword: del --> Used in 2 ways
# Delete a Key-Value pair
del data['Sem']
print("Modified Dictionary Values:")
print(data)
print()

# Delete the entire Dictionary - it will get deleted from the memory
del data
print("Modified Dictionary Values:")
# After deleting use the 'del' - we cannot access the dict again: NameError
print(data)
print()
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Accessing the Key-Value Pair --> Using Key Name, get()

# 1. Using Key Name
department = data['Dept']
print(F"I belong to {department} dept")
M = data['Marks']
print(F"My Semester Marks are: {M}")

# If the Key is not present: KeyError
fee = data['Fees']
print(F"I have paid Rs.{fee} as college Fees")
print()

# Avoid the error if the key is not present
key = input("Enter the Key: ")
if key in data:
    fee = data['Fees']
    print(F"I have paid Rs.{fee} as college Fees")
else:
    print('<Data Not Available>')
   
# 2. get() Function
department = data.get('Dept')
print(F"I belong to {department} dept")
M = data.get('Marks')
print(F"My Semester Marks are: {M}")
# If the Key is not present: Customised Message can be given
fee = data.get('Fees' , '<Data Not Available>')
print(F"I have paid Rs.{fee} as college Fees")
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Duplicate Keys: Overriding the key's value (last updated value will be considered)
d1 = { "color":"pink", "shape":"square", "color":"blue" }
print("Dictionary -",d1)

# Keys are Case Sensitive
d1 = { "color":"pink", "shape":"square", "Color":"blue" }
print("Dictionary -",d1)

# Values can be duplicated
D = { "color":"pink", "shape":"square", "fav_color":"pink" }
print(F"Dict: {D}")

# Keys - Immutable Data Type : TypeError
# Mutable: List, Set, Dict
d = {["a","b","c"]: "alpha", "o": "omega", "g": "gamma"}
print(F"Dict: {d}")
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Functions: keys(), values(), items()

data={'Name':'Anushya','ID':'E001','Dept':'IT'}
print("Dict -",data)
# Fetching all the Keys within the dict
k = list(data.keys())
# Fetching all the values of the keys within the dict
v = list(data.values())
# Fetching both the Key+Value present within the dict
kv = list(data.items())
# Printing
print("Keys =",k)
print("Values =",v)
print("Key and Value =",kv)
------------------------------------------------------------------------------------------------------------------------------------------------------------
# Iterating over a Dictionary

# Using simple for loop
data = {
    'Name':'Anushya',
    'ID':'E001',
    'Dept':'IT',
    'Desig':'Trainer',
    'Salary':35000
    }
for i in data:
    print(F"Key{[i]}: {data[i]}")

# Using simple for loop and items() function
statesAndCapitals = {
    'Gujarat': 'Gandhinagar',
    'Maharashtra': 'Mumbai',
    'Rajasthan': 'Jaipur',
    'Bihar': 'Patna'
}
for state, capital in statesAndCapitals.items():
    print(state, ":", capital)

# Using simple for loop with: keys(), values() and enumerate() functions
data = {
    'Name':'Anushya',
    'ID':'E001',
    'Dept':'IT',
    'Desig':'Trainer',
    'Salary':35000
    }

# Iterate over the Keys
print("Dictionary Keys: ")
print("--------------------")
for k in data.keys():
    print(k)
print()

# Iterate over the Values
print("Dictionary Values: ")
print("----------------------")
for k in data.values():
    print(k)
print()

# Using for loop with enumerate()
print("Keys\tValues")
print("------\t--------")
for i,(k,v) in enumerate(data.items()):
    print(F"{k}\t{v}")
print()
------------------------------------------------------------------------------------------------------------------------------------------------------------
3 Important Functions --> keys(), values(), items()
keys(): will return all the keys that are present within the dictionary
values(): will return all the values that are present within the dictionary
items(): returns the key-value pairs

# Example 1:
data={'Name':'Anushya','ID':'E001','Dept':'IT'}
print("Dict:",data)
print()

# Fetching all the Keys within the dict
k = list(data.keys())
# Fetching all the values of the keys within the dict
v = list(data.values())
# Fetching both the Key+Value present within the dict
kv = list(data.items())

# Printing
print("Keys =",k)
print("Values =",v)
print("Key and Value =",kv)
----------------------------------------------------------------------------------------------------
# Example 2: Using the keys()
data={'Name':'Anushya','ID':'E001','Dept':'IT'}
print("Dict:",data)

# Printing all the Keys within the Dict
keys = data.keys()
print("Keys of the Dict:",keys)

# Fetching the 2nd key of the Dict
print("2nd key of the Dict:", list(data.keys())[1])

# Adding new Key/Value pair
data['Desig'] = "Trainer"
print('After dictionary is updated:', keys)
----------------------------------------------------------------------------------------------------
# Example 3: Using the values()
emp_sal = {
    'E001': 32000,
    'E002': 45250,
    'E003': 75210,
    'E004': 25000,
    'E005': 31500}
print("Dict:",emp_sal)

# stores the salaries only
L = emp_sal.values()
# prints the sum of all salaries
print(F"Total Salary Given Every Month = Rs.{sum(L)}")  
----------------------------------------------------------------------------------------------------
# Example 4: Using the items()
op = {'milk': 10, 'coffee': 15, 'bread': 25}
hike = 5
np = {item: value+hike for (item, value) in op.items()}
print(np)
----------------------------------------------------------------------------------------------------
# Example 5: Using the items()
stud = {'Jack': 98, 'Michael': 85, 'Guido': 91, 'John': 83, 'James': 89}
A = {k: v for (k, v) in stud.items() if v>90}
print(A)
------------------------------------------------------------------------------------------------------------------------------------------------------------
Dictionary Comparison

# Example 1: Using the == Equality Operator

dict1 = {'Name': 'Arun', 'Age': 5}
dict2 = {'Name': 'Priya', 'Age': 78}
dict3 = {'Name': 'Arun', 'Age': 5}
dict4 = { 'Age': 5, 'Name': 'Arun'}

# Comparing the 2 dictionaries - dict1 & dict2
print("Dict 1:" , dict1)
print("Dict 2:" , dict2)
if dict1 == dict2:
    print("dict1 is equal to dict2")
else:
    print("dict1 is not equal to dict2")
print()

# Comparing the 2 dictionaries - dict1 & dict3
print("Dict 1:" , dict1)
print("Dict 3:" , dict3)
if dict1 == dict3:
    print("dict1 is equal to dict3")
else:
    print("dict1 is not equal to dict3")
print()

# Comparing the 2 dictionaries - dict1 & dict4
# Order of the dict does not matter; Key & value must match
print("Dict 1:" , dict1)
print("Dict 4:" , dict4)
if dict1 == dict4:
    print("dict1 is equal to dict4")
else:
    print("dict1 is not equal to dict4")
----------------------------------------------------------------------------------------------------
# Example 2: Using Loops

dict1 = {'Name': 'Arun', 'Age': 5}
dict2 = {'Name': 'Priya', 'Age': 78}
dict3 = {'Name': 'Arun', 'Age': 5}

# Looping Over a dictionary and compare its values
if len(dict1)!=len(dict2):
    print("Not equal")
else:
    flag=0
    for i in dict1:
        if dict1.get(i)!=dict2.get(i):
            flag=1
            break
       
    if flag==0:
        print("Equal")
    else:
        print("Not equal")
------------------------------------------------------------------------------------------------------------------------------------------------------------
Dictionary Sorting

sorted() Function --> It will sort the data by default in ascending order
It will not modify the original object, it will return the sorted data as a LIST.
Syntax: sorted(Object)
If descending order sorting: sorted(Object, reverse=True)

Example:
L = [56,85,10,47,96,34,72,20,25]
print("Unsorted List =", L)

t = sorted(L, reverse=True)
print("Sorted List =", t)

print("Original List =", L)


Example 1: sorted() Function
d = {1:'One', 3:'Three', 5:'Five', 2:'Two', 4:'Four'}
print("Original Dict:",d)

# Sorting a Dictionary - Keys
dsort = sorted(d)
print("Sorted Dict Keys:",dsort)

# Looping over the Sorted Keys to get its value
print("Dictionary in Sorted Order: ")
print("Key         Value")
for i in dsort:
    print(F"{i}\t{d[i]}")

Example 2: sort() Function
Boys = {'Raghav':'S001','Chandu':'S002','Rahul':'S003'}

#Converting the Dict Keys into a List
Students = list(Boys.keys())

# Sorting the Dict
Students.sort()

# Looping over the Sorted Keys
print("Student List is Alphabetical Order")
for S in Students:
      print(" : ".join((S,str(Boys[S]))))
------------------------------------------------------------------------------------------------------------------------------------------------------------
Dictionary Copy


• Shallow Copy
• Deep Copy

Example 1: copy() Function
dict1 = {"key1": "V1", "key2": "V2"}

# Creating a Shallow copy of dict1
dict2 = dict1.copy()

# Printing both the dictionaries
print("Dict 1 -",dict1)
print("Dict 2 -",dict2)

# Making Modifications
dict2['key2'] = 'Modified V2'
dict1['key1'] = 'Modified V1'

# Printing both the dictionaries after changes
print("Dict 1 -",dict1)
print("Dict 2 -",dict2)

Example 2: Shallow Copy
original_dict = {
    'name': 'John',
    'info': {'age': 30, 'address': {'city': 'Anytown','state': 'CA'}}
    }

# Creating a deep copy of the original dictionary
copied_dict = original_dict.copy()

# Printing the dictionary
print('Original Dictionary before Modification - ')
print(original_dict)
print('Copied Dictionary before Modification - ')
print(copied_dict)
print()

# Modifying the original dictionary
original_dict['info']['age'] = 31
original_dict['info']['address']['city'] = 'New City'

# Modifying the copied dictionary
copied_dict['info']['age'] = 101

# Original dictionary has changed
print('Original Dictionary after Modification - ')
print(original_dict)

# Copied dictionary remains unchanged
print('Copied Dictionary after Modification - ')
print(copied_dict)


Example 3: Deep Copy
import copy

original_dict = {
    'name': 'John',
    'info': {'age': 30, 'address': {'city': 'Anytown', 'state': 'CA'}}
     }

# Creating a deep copy of the original dictionary
copied_dict = copy.deepcopy(original_dict)

# Printing the dictionary
print('Original Dictionary before Modification - ')
print(original_dict)
print('Copied Dictionary before Modification - ')
print(copied_dict)
print()

# Modifying the original dictionary
original_dict['info']['age'] = 31
original_dict['info']['address']['city'] = 'New City'

# Modifying the copied dictionary
copied_dict['info']['age'] = 101

# Original dictionary has changed
print('Original Dictionary after Modification - ')
print(original_dict)

# Copied dictionary remains unchanged
print('Copied Dictionary after Modification - ')
print(copied_dict)
------------------------------------------------------------------------------------------------------------------------------------------------------------
Converting different Data Types into Dictionary

#Creating a Tuple
t = (("Name","Anushya"),("Profession","Trainer"))
print(t)
print(type(t))

# Tuple to Dictionary
d1 = dict(t)
print("Dictionary 1", d1)    
print("Type", type(d1))


#Creating a List
l = [["Dept","CSE/IT"],["Exp","10+"]]
print(l)
print(type(l))

# List to Dictionary
d2 = dict(l)
print("Dictionary 2", d2)
print("Type", type(d2))

import json
# initializing string
s = '{"sachin" : 1, "Virat" : 2, "Dhoni" : 3}'
print(type(s))
print("The original string:",str(s))

# using json.loads() for conversion
res = json.loads(s)
print(type(res))
print("The converted dictionary:",res)
------------------------------------------------------------------------------------------------------------------------------------------------------------
16-12-2024

Functions:
-----------------
Def: A block of code that performs a particular operation
        another name is module.
Advantages:
1.code optimization
2.reusability
3.modular programming

Classification:
---------------------
1.predefined function or Built in functions
the functions that are already defined present in modules or packages.
ex: print(),max(),min(),sum(),len()

2.user defined functions
the functions that are developed by the user

syntax:
def function-name(formal parameters):           
               "function-doc"                        
               executable statements
               return expression

function header:

def function-name(formal parameters): 

function body :  

              "function-doc"                        
               executable statements
               return expression

def -->keyword for defines the function
def,function-name,executable statements are compulsory

Terminology:

Actual parameters ==> present in the calling function
Formal parameters ==>present in the function definition(called function)
calling function
function definition

always the def should be above of calling function

Based on parameters and return values functions are classifies as:
--------------------------------------------------------------------------------------------------

parameter    return value
--------------    ------------------
0                         0
0                         1
1                         0
1                         1

0-absent
1-present



1.function with no parameter and no return value

def a00():   #function def
    a,b=map(int,input().split())
    c=a+b
    print(c)
a00() #calling fun
----------------------
print("hello")
print("Worls")
def a00():   #function def
    a,b=map(int,input().split())
    c=a+b
    print(c)
a00() #calling fun
-------------------------
def a00():   #function def
    a=int(input("a:"))
    b=int(input("b:"))
    c=a+b
    print(c)
a00() #calling fun
-----------------------------
def a00():   #function def
    a,b=int(input()),int(input())
    c=a+b
    print(c)
a00() #calling fun
-----------------------------------------

2.function with no parameter but return value

def a01():   #function def
    a,b=int(input()),int(input())
    c=a+b
    return c

s=a01() #calling fun
print(s)
--------------------------------------------------------
def a01():   #function def
    a,b=int(input()),int(input())
    c=a+b
    return c
print(a01()) #calling fun
-----------------------------------------------------------

3.function with parameters but no return value

def a10(x,y):   #function def   x,y--> formal parameters
    print(x+y)

a,b=int(input()),int(input())
a10(a,b)   #fun call a,b--> actual parameters
--------------------------------------------------------------------
def a10(a,b):   #function def   a,b--> formal parameters
    print(a+b)

a,b=int(input()),int(input())
a10(a,b)   #fun call a,b--> actual parameters

formal parameters can be same as actual parameters
-----------------------------------------------------------------------

4.function with parameters and return values

def a11(a,b):   #function def   a,b--> formal parameters
    return(a+b)

a,b=int(input()),int(input())
print(a11(a,b))  #fun call a,b--> actual parameters
------------------------------------------------------------
def a11(a,b):   #function def   a,b--> formal parameters
    return(a+b)

a,b=int(input()),int(input())
x=a11(a,b)  #fun call a,b--> actual parameters
print(x)
-------------------------------------------------

5.function that return multiple values

def frmv():
    a,b=int(input()),int(input())
    c=a+b
    d=a-b
    return c,d
a,b=frmv()
print(a)
print(b)



-------------------------------------------------------------------------------------------------------
============================================================

def frmv():
    a,b=int(input()),int(input())
    c=a+b
    d=a-b
    return c,d
a=frmv()
print(a)
print(type(a))

10
20
(30, -10)
<class 'tuple'>

----------------------------------

def frmv():
    a,b=int(input()),int(input())
    c=a+b
    d=a-b
    return [c,d]
a=frmv()
print(a)
print(type(a))

10
20
[30, -10]
<class 'list'>
-----------------------------------------

def frmv():
    a,b=int(input()),int(input())
    c=a+b
    d=a-b
    return {c,d}
a=frmv()
print(a)
print(type(a))

10
20
{30, -10}
<class 'set'>

----------------------------------------------

def frmv():
    d={}
    d['name']='rise'
    d['branch']='DS'
    return d
a=frmv()
print(a)

{'name': 'rise', 'branch': 'DS'}
<class 'dict'>

--------------------------------------------

import operator
x=operator.add(12,13)
y=operator.sub(12,13)
print(x,y)

---------------------------------------------


Parameter passing mechanisms:
-----------------------------

def a(s1,s2):
    print(s1)
    x=b(s2)
    print(x)

def b(st2):
    return st2.upper()

a("aiml","ds")

the way how the parameters are passing from calling function to called function
1.call by value or pass by value
2.call by reference or pass by reference == two copies of data


mutable     - call by reference
immutable   - call by value    


call by reference  :
--------------------

def cbrf(b):
    print(b)
    print(id(b))
    b.append("aiml")
    print(b)
    print(id(b))

a=["ds"]
print(a)
print(id(a))
cbrf(a)
print(a)
print(id(a))
     
['ds']
1791636949312
['ds']
1791636949312
['ds', 'aiml']
1791636949312
['ds', 'aiml']
1791636949312


call by value:
--------------

def cbv(a):
    print(a)
    print(id(a))
    a=a*2
    print(a)
    print(id(a))

a=5
print(a)
print(id(a))
cbv(a)
print(a)
print(id(a))


5
140735705506728
5
140735705506728
10
140735705506888
5
140735705506728



classification of function based on formal arguments:
-----------------------------------------------------------------------------
a.Required arguments == actual parameters count same as formal parameters count 

def ra(n,a,g):
    print(n,a,g)
name="Kalyan"
age=20
gender="M"
ra(name,age,gender)

Kalyan 20 M


b.keyword arguments == from the calling function which we passing parameters with data
formal and actual parameter names should be same
same order is not naccessary

def ka(age,gender,name):
    print(name,age,gender)
ka(name="Kalyan",age=20,gender="M")

Kalyan 20 M

c.Default arguments == same as the keyword arguments in the definition if a parameter is return with a value in the last position then that is called default parameter


def da(age,gender,name="pskalyan"):
    print(name,age,gender)
da(name="Kalyan",age=20,gender="M")

Kalyan 20 M


def da(age,gender,name="pskalyan"):
    print(name,age,gender)
da(name="Kalyan",age=20,gender="M")
da(age=21,gender="M")

Kalyan 20 M
pskalyan 21 M



d.variable length arguments == there is no fixed length parameter


def vla(x,*y):
    print(x)
    print(y)
    
# * more than one value
vla(5,10,15,20,25)
vla(2,4,6)


5
(10, 15, 20, 25)
2
(4, 6)

def vla(x,*y):
    print(x)
    print(y)
    
# * more than one value
vla(5)

5
()

def vla(*y):
    print(y)
    
# * more than one value
vla(5,10,15,2,4,5,5)

(5,10,15,2,4,5,5)


e.variable length keyword arguments == combination of keyword and variable length arguments 

def vlka(**y):
    print(y)
vlka(name="Kalyan",gender="M",age=20)
vlka(a=1,b=2,c=3,d=4)

{'name': 'Kalyan', 'gender': 'M', 'age': 20}
{'a': 1, 'b': 2, 'c': 3, 'd': 4}


Lambda functions:
--------------------------

1.Lambda functions are also called as anonymous functions because lambda functions do not have a name
ANONYMOUS - NAME LESS FUNCTIONS
2.the differences between lambda functions and normal functions are 
a.Normal functons are defined with the keyword def
a1.lambda functions are defined with the keyword lambda

b.Normal functions can be written in print()
b1.Lambda functions should not be written in print()

c.Lambda forms can take any number of arguments but return just one value in the form of an expression
They cannot contain commands or multiple expressions

Lambda definitions are useful when the definiton is small.


syntax:
-------

lambda arg1,arg2.........argn:expression with arguments

expression with arguments ===> function definition

ex-1:

add=lambda x1,x2:x1+x2
x=add(10,5)
print(x)

15

ex-2:

add=lambda x1,x2:x1+x2
print(add(10,5))

15

ex-3:

add=lambda x1,x2:print(x1+x2)
add(10,5)

15

ex-4:

add=lambda x1,x2:print(x1+x2)
a=int(input())
b=int(input())
add(a,b)

ex-5:

big=lambda x,y: x if(x>y) else y
a=int(input())
b=int(input())
ans=big(a,b)
print(ans)

10
0
10


big=lambda x,y: x if(x>y) else y
a=int(input())
b=int(input())
print(big(a,b))


big=lambda x,y: print(x) if(x>y) else print(y)
a=int(input())
b=int(input())
big(a,b)

'''wrie a program to verify whether the given string is palindrome or not using lambda function'''

a=input()
c=a[::-1]
pal=lambda a,c:print('pal') if(a==c) else print("not pal")
pal(a,c)

madam
pal

---------------------------------------------------------------------------------------------------------------------------



First class functions:
-----------------------------
Properties:
-----------------

1.A function is an instance of object type.
2.you can store the function in a variable
3.you can pass a function as a parameter to another function
4.you can return a function from another function
5.you can store them in data structures like list,tuple,ets.

Property 1 & 2 :

def add(x,y):
    return x+y

a,b=int(input()),int(input())
print(add(a,b))
x=add
print(x(a,b))


Property 3 & 4:

def aiml(ds):
    x=ds("rise")
    print(x)

def ds(s1):
    return s1.upper()

aiml(ds) #function call of aiml

RISE


Fruitful function & void function :
-----------------------------------------------

a function that returns a value is called fruitful function


void function:
---------------------
a function that does not return any value  is called void function


Scope of variable:
--------------------------
A variable which is used upto or how much time can be used is called scope

a.Local variable:

1.The variable that is present under a particular block is called as local variable.
2.The scope of local variable is only within the block.


def aiml():
    a=5 #Local variable
    print(a)
    print(id(a))

def ds():
    a=10 #Local variable
    print(a)
    print(id(a))

def rise():
    a=15 #Local variable
    print(a)
    print(id(a))
aiml()
ds()
rise()


5
140732451316648
10
140732451316808
15
140732451316968


b.Global variable:

1.The variable that is not present under any block is called as global variable
2.The scope of global variables is throughout the program


def aiml():
    print(a)
    print(id(a))

def ds():
    print(a)
    print(id(a))

def rise():
    print(a)
    print(id(a))

a=20 #global variable
aiml()
ds()
rise()

20
140732451317128
20
140732451317128
20
140732451317128

Both Gloabl and Local :

def aiml():
    a=5 #Local variable
    print(a)
    print(id(a))

def ds():
    a=10 #Local variable
    print(a)
    print(id(a))

def rise():
    a=15 #Local variable
    print(a)
    print(id(a))

a=2 #Global variable
aiml()
ds()
rise()
print(a)
print(id(a))

5
140732451316648
10
140732451316808
15
140732451316968
2
140732451316552


Global Keyword :
---------------------------

global keyword is used to take the permission to change the data in the certain function of a local variable
It is keyword  allows the user to modify a variable outside of the current scope

# Global Keyword
def aiml():
    global a
    a=a*2
    print(a)
    print(id(a))

a=5
print(a)
print(id(a))
aiml()
print(a)
print(id(a))


5
140732451316648
10
140732451316808
10
140732451316808

Yield Keyword:
----------------------
1.yield is a keyword in python that is used to return from a function without destroying the states of its local variable and when the function is called.
2.The execution starts from the last yield statement.
3.Any function that contains a yield keyword is termed as generator .Hence yield is what makes a generator


# yield keyword

def print_even(test_list):
    for i in test_list:
        if i%2==0:
            yield i

test_list=[1,4,5,6,7]

print(test_list)

print("The even numbers in list are : ",end=" ")
for j in print_even(test_list):
    print(j)


[1, 4, 5, 6, 7]
The even numbers in list are :  4
6



Recursive Functions:
---------------------------------
A function calling itself is called recursion.

Adv:
1.Complex problems  can be solved easily with the help of recursion
2.Reusability

disadv:
1.Recursive programs consumes more processor time and occupies more space
2.Recursive programs execution is slow when compared with iteration

Recursive programs are base don stack data structure

Q1)
# write a program to print the numbers from a to b where a=low value b=high value using recursion

def rlh(x,y):
    if(x<=y):
        print(x)
        x+=1
        rlh(x,y)

a,b=int(input()),int(input())
rlh(a,b) # calling 

10
20
10
11
12
13
14
15
16
17
18
19
20

Q2)
# write a program to print the numbers from a to b where a= high value b=low value using recursion

def rhl(x,y):
    if(x>=y):
        print(x)
        x-=1
        rhl(x,y)
a,b=int(input()),int(input())
rhl(a,b)

20
10
20
19
18
17
16
15
14
13
12
11
10

# towers of hanoi using recusion

def toh(n,s,d,h):  #s=source,d=destination,h=helper
    if n==1:
        print ("Move disk 1 from source",s,"to destination",d)
        return
    toh(n-1, s, h, d)
    print ("Move disk",n,"from source",s,"to destination",d)
    toh(n-1, h, d, s)
n = 4 # Driver code
toh(n,'A','B','C') # A, C, B are the name of rods

Move disk 1 from source A to destination C
Move disk 2 from source A to destination B
Move disk 1 from source C to destination B
Move disk 3 from source A to destination C
Move disk 1 from source B to destination A
Move disk 2 from source B to destination C
Move disk 1 from source A to destination C
Move disk 4 from source A to destination B
Move disk 1 from source C to destination B
Move disk 2 from source C to destination A
Move disk 1 from source B to destination A
Move disk 3 from source C to destination B
Move disk 1 from source A to destination C
Move disk 2 from source A to destination B
Move disk 1 from source C to destination B

# write a program to fibd the factorial of number using recursion

n=int(input("Enter a Number : "))
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact(n-1)
print(fact(n))

Enter a Number : 5
120

Note:

1.Recursion works based on stack (LIFO -> Last in First Out) data structure.
2.Last item stored in the data structure will be processed first.
3.First item stored in the data structure will be processed first.


import sys
sys.setrecursionlimit(50)

def ds():
    global i
    print(i)
    i=i+1
    ds()
i=1
print(ds())

RecursionError: maximum recursion depth exceeded while pickling an object                                          

==============================================================================

Object Oriented Programming:
--------------------------------------------
C-Language:
-------------------
syntax:

struct structure-name
{
//structure elements
}

class is same as structure in c programming

OOP:
---------
1.An object paradigm is designing the program using classes and objects
2.Reusability

Major priciples of object oriented programming:
----------------------------------------------------------------------
1.Class
2.Object
3.Method
4.Constructor
5.Inheritance
6.Abstraction
7.Encapsulation
8.polymorphism

1.python - class:
-------------------------

1.class is a logically entity that has some attributes and methods
2.class is a blue print or model for creating the objects

syntax:
------------

class class_name:
    instance variables  ==> The variables connected with objects.
    static variables(class variables) ==> The variables that are associated with class.
    constructors  ==>  is also a method
    static methods
    abstract methods
    normal methods


2.Object:
-------------    

1.Object is an instance of a class
2.using object class attributes and methodss are used
3.Everything in python is an object and is associated with some attributes and methods

syntax for object creation:
----------------------------------------

object_name=class_name()

Accessing data of class using the object syntax:
----------------------------------------------------------------------

object_name.variable
object_name.method
				
Accessing data of a class using class_name:
-----------------------------------------------------------------

classname.variable
classname.method
The concept is static

ex:1

class person:
    age=36

p1=person()
print(p1.age)
print(person.age)

36
36

ex:2

class student:
    name="Kalyan"
    age=20
    branch="CSD"
s1=student()
print(f"Student Name : {s1.name} Age : {s1.age} Branch : {s1.branch}")
print(f"Student Name : {student.name} Age : {student.age} Branch : {student.branch}")

Student Name : Kalyan Age : 20 Branch : CSD
Student Name : Kalyan Age : 20 Branch : CSD


3.Constructor:
----------------------

1.Every class a function called def __init__() called constructor
2.The connstructor will execute automatically everytime when the class is being used to create an object
3.The constructor initializes the data to the object of a class using self parameter

The self parameter:
----------------------------
1.It is a reference to the current instance of the class and is being used to initialize the object
2.Every function first parameter should be self
3.The name need not be self e can specify some other name

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

p1=Person("Kalyan",20)
p2=Person("Srinivasa",20)
print(p1.name,p1.age)
print(p2.name,p2.age)

Kalyan 20
Srinivasa 20

class Student:
    def __init__(self,Rollno,Name):
        self.Rollno=Rollno
        self.Name=Name

s1=Student("228A1A4454","Kalyan")
print(s1.Rollno,s1.Name)

228A1A4454 Kalyan

*Instance variable:
-------------------------
Variables that are unique to each object.They are created inside methods(typically __init__())

*class variables(static variables):
----------------------------------------------
Variables shared among all instances of a class.They are defined within the class,outside any methods.

#constructor with the static variable
class person:
    static_count=0
    def __init__(sel):
        person.static_count+=1
        print(person.static_count)
p1=person()
p2=person()
p3=person()

1
2
3

**Deletion Operation:
------------------------------
Two cases:

1.deleting object of particular attribue data
2.delete complete object


4.Methods:
-----------------
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)

p1=Person("Kalyan",20)
p2=Person("Srinivasa",20)
p1.show()
p2.show()

Kalyan 20
Srinivasa 20

#check whether minor or not minor
class minor:
    def __init__(self,age):
        self.age=age
    def decide(self):
        if(self.age>18):
            print("Minor")
        else:
            print("Not Minor")
n=int(input())
m=minor(n)
m.decide()

45
Minor

5
Not Minor

class add:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def addition(sel): #instead of self we can write any thing 
        print(sel.a+sel.b)
i=add(5,10)
i.addition()

15


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print(self.name,self.age)
    def decide(self):
        if(self.age>18):
            print("Minor")
        else:
            print("Not Minor")

p1=Person("Kalyan",20)
p2=Person("Srinivasa",20)
p1.show()
p2.show()
p1.decide()
p2.decide()

Kalyan 20
Srinivasa 20
Minor
Minor



**Types of Constructors :
-------------------------------------
a.Parameterized constructor
b.Non parameterized constructor
c.Default Constructor

a.Parameterized constructor:

The constructor if its contains parameters other than self.
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

b.Non parameterized constructor:

The constructor that contains only self parameter.
class person:
    static_count=0
    def __init__(sel):
        person.static_count+=1
        print(person.static_count)

c.Default Constructor:

whether you may write constructor or not there is always a constructor is called constructor.
class person:
    age=36

p1=person()
print(p1.age)
print(person.age)

**Multiple constructors in a Class:
------------------------------------------------
class person:
    def __init__(self):
        print("This is first Constructor ")
    def __init__(self):
        print("This is Second Constructor")
p1=person()

This is Second Constructor


**Three Imp Methods:
------------------------------
getattr(),setattr(),hasattr() -- Functions
__________________________________

getattr(): read operation of an object particular attribute
syntax:
getattr(objectname,attributename) #p1.name

setattr():write operation of an attribue of an object
syntax:
setattr(objectname,attribue name,value) #p1.name="Kalyan"

hasattr(): is for checking whether the object is so and so attribue
syntax:
hasattr(objectname,attributename)

The hasattr() verifies whether the object is associated with the specified given attribue or not
The output is boolean output that is either True or False.


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=Person('Kalyan',20)
print(getattr(p1,'name'))
print(getattr(p1,'age'))
setattr(p1,'age',21)
print(getattr(p1,'age'))
print(hasattr(p1,"age"))
print(hasattr(p1,'id'))

Kalyan
20
21
True
False


==============================================================================

5.Inheritance:
------------------------
Def : Creating a newclass by making use of the existing class or classes is called inheritance

Adv:
The main adv of Inheritance is reusability

A child class object can use the data in parent class and also the class
when you erite constructor in a another constructor intendation dose not require
Types of Inheritance:-
-----------------------------------
1.Single level inheritance
2.Multi level inheritance
3.Multiple inheritance
4.Hierarchical inheritance
5.Hybrid inheritance

Syntax for deriving a class or writing a child class:
-------------------------------------------------------------------------

class child_class_name/derived_class_name(p1,p2,...........pn):
          class body
p1=parent class 1
p2=parent class 2
    ............
    ............
    ............
pn=parent class n



*1.Single level inheritance:
---------------------------------------
Deriving a class by making use of exactly one class

               A  ==> Parent class/Base Class
               ||
               v
               B  ==> Child class/Sub Class/Derived Class

class Father:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)

class Son(Father):
    def __init__(self,name):
        self.name=name
    def show1(self):
        print(self.name)

x=Father("Prasad Rao")
x.show() #Normal
y=Son("Srinivasa Rao")
y.show1()
y.show()

Prasad Rao
Srinivasa Rao
Srinivasa Rao

class Base:
    def __init__(self):
        self._a=21
class Derived(Base):
    def __init__(self):
        Base.__init__(self)#invoking the base class constructor
        print(self._a)
d1=Derived()

21

Access specifiers are 3 in number in python
1.public
2.private(__)
3.protected(_)
The public and protected data of a class is asseeible in the class where it is present in the derived classesand in the rest of the program
The private data of a class is accessible only with in the class.

class Base:
    def __init__(self):
        self._a=21 #protected data(_)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)#invoking the base class constructor
        print(self._a)
d1=Derived()
b1=Base()
print(b1._a)

21
21



*2.Multi level inheritance:
-----------------------------------
Deriving a class from a derived class

                A   --> Parent class
                ||
                v
                B   -->Child class
                ||
                v
                C  -->Derived class

class Base:
    def __init__(self):
        self.a=21 
        print(self.a)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)#invoking the base class constructor
        print(self.a+2)
class Derived1(Derived):
    def __init__(self):
        Derived.__init__(self)
        print(self.a+3)
d1=Derived1()

21
23
24

class Base:
    def __init__(self):
        self.a=21 
        print(self.a)
class Derived(Base):
    def __init__(self):
        Base.__init__(self)#invoking the base class constructor
        print(self.a+2)
class Derived1(Derived):
    def __init__(self):
        Base.__init__(self)
        print(self.a+3)
d1=Derived1()

21
24


*3.Multiple inheritance:
---------------------------------
If a class is created by using more than one base class


A                    B
 |                   |
 |                   |
 l------->C<---------l

class Father:
    fathername=''
    def father(self):
        print(self.fathername)
        
class Mother:
    mothername=''
    def mother(self):
        print(self.mothername)
        
class Son1(Father,Mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)

s1=Son1()
s1.name="Kalyan"
s1.fathername="Prasad Rao"
s1.mothername="Hymavathi"
s1.show()

Prasad Rao
Hymavathi
Kalyan

class Father:
    fathername=''
    def father(self):
        print(self.fathername)
        
class Mother:
    mothername=''
    def mother(self):
        print(self.mothername)
        
class Son1(Father,Mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)

s1=Son1()
s1.name="Kalyan"
s1.fathername="Prasad Rao"
s1.mothername="Hymavathi"
s1.show()
s1.father()
s1.mother()

Prasad Rao
Hymavathi
Kalyan
Prasad Rao
Hymavathi


*4.Hierarchical inheritance:
----------------------------------------
Deriving more than one class from one particular base class


     _________ A____________
    |          |            |
   B           C            D


class Father:
    fathername=''
    def father(self):
        print(self.fathername)
        
class Son1(Father):
    name=''
    def show(self):
        print(self.fathername)
        print(self.name)

class Son2(Father):
    name=''
    def show1(self):
        print(self.fathername)
        print(self.name)
s1=Son1()
s2=Son2()
s1.name='Lava'
s1.fathername='Ram'
s2.name='Kusha'
s2.fathername='Ram'
s1.show()
s2.show1()
s1.father()
s2.father()

Ram
Lava
Ram
Kusha
Ram
Ram


*5.Hybrid inheritance:
-------------------------------

Combination of any two types of inheritances

     _________ A__________
    |          |          |
   B           C          D
    |
   E

class Father:
    fathername=''
    def father(self):
        print(self.fathername)
        
class Mother:
    mothername=''
    def mother(self):
        print(self.mothername)
        
class Son1(Father,Mother):
    name=''
    def show(self):
        print(self.fathername)
        print(self.mothername)
        print(self.name)
class Son2(Father):
    name=''
    def show1(self):
        print(self.fathername)
        print(self.name)
s2=Son2()
s1=Son1()
s2.name='Kusha'
s2.fathername='Ram'
s2.show1()
s2.father()
s1.name="Kalyan"
s1.fathername="Prasad Rao"
s1.mothername="Hymavathi"
s1.show()
s1.father()
s1.mother()

Ram
Kusha
Ram
Prasad Rao
Hymavathi
Kalyan
Prasad Rao
Hymavathi

              Father                  Mother
              |  |                         |
              |  |                         |
       Son2---l  l----------Son1-----------l
   


--------------------------------------------------------------------------------------------------------------

The issubclass(sub,sup) method :
------------------------------------------------
syntax:
issubclass()

issubclass(sub,sup) methos is used to check the relatioonship b/w the specified classes.It returns true if the first class is the subclass of the second class and false otherwise

class Calculation1:
    def sum(self,a,b):
        return a+b
class Calculation2:
    def mul(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d=Derived()
print(issubclass(Derived,Calculation1))
print(issubclass(Derived,Calculation2))
print(issubclass(Calculation1,Calculation2))

True
True
False


The isinstance(obj,class)
------------------------------------
syntax:
isinstance(obj,class)

The isinstance() method is used to  check the relationship b/w the objects and classes.It returns true if the first parameter i.e obj is instance of the class otherwise false

class Calculation1:
    def sum(self,a,b):
        return a+b
class Calculation2:
    def mul(self,a,b):
        return a*b
class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b
d=Derived()
print(isinstance(d,Derived))
print(isinstance(d,Calculation1))
print(isinstance(d,Calculation2))

True
True
True

================================================================================================================================================

6.Polymorphism:
------------------------

The word polymorphism means having many forms.
polymorphism is of two types:
a.static polymorphism(Compile time polymorphism)
b.Dynamic polymorphism(Run time polymorphism)

Compile time polymorphism:
-----------------------------------------

In polymorphism means the same function name(but different signature) being used for different types is called method overloading

Operator overloading:
-------------------------------
same operator performing multiple operations having multiple names

"""operator overloading"""

#addition of two numbers
print(1+2)

#concatenate two strings
print("Geeks"+"For")

#product of two numbers
print(3*4)

#Repeat the String
print("Geeks"*4)

3
GeeksFor
12
GeeksGeeksGeeksGeeks


Function overloading:
-------------------------------

"""Function overloading"""

#python program to demonstate in-built polymorphic functions
#len() being used for string
print(len("geeks"))

#len() being used for a list
print(len([10,20,30]))


class A:
    def __init__(self,a):
        self.a=a

    #adding two objects
    def __add__(self,o):
        return self.a+o.a

ob1=A(1)
ob2=A(2)
print(ob1+ob2)
ob3=A("Geeks")
ob4=A("For")
print(ob3+ob4)

3
GeeksFor


5
3

Python magic methods or special functions for operator overloading:
----------------------------------------------------------------------------------------------------

Binary Operators:
-------------------------
Operator	     Magic Method
+	__add__(self, other)
–	__sub__(self, other)
*	__mul__(self, other)
/	__truediv__(self, other)
//	__floordiv__(self, other)
%	__mod__(self, other)
**	__pow__(self, other)
>>	__rshift__(self, other)
<<	__lshift__(self, other)
&	__and__(self, other)
|	__or__(self, other)
^	__xor__(self, other)

Comparison Operators:
----------------------------------
Operator	    Magic Method
<	__lt__(self, other)
>	__gt__(self, other)
<=	__le__(self, other)
>=	__ge__(self, other)
==	__eq__(self, other)
!=	__ne__(self, other)

Assignment Operators:
----------------------------------
Operator	Magic Method
-=	__isub__(self, other)
+=	__iadd__(self, other)
*=	__imul__(self, other)
/=	__idiv__(self, other)
//=	__ifloordiv__(self, other)
%=	__imod__(self, other)
**=	__ipow__(self, other)
>>=	__irshift__(self, other)
<<=	__ilshift__(self, other)
&=	__iand__(self, other)
|=	__ior__(self, other)
^=	__ixor__(self, other)

Unary Operators:
-------------------------
Operator	Magic Method
–	__neg__(self)
+	__pos__(self)
~	__invert__(self)

____________________________________________________________________________________

Method overriding:
---------------------------
When the parent class method is defined in the child class then the concept is called overriding.

# Method Overriding

class bank:
    def getroi(self):
        return 10
class sbi(bank):
    def getroi(self):
        return 9
class icici(bank):
    def getroi(self):
        return 8

b1=bank()
s1=sbi()
i1=icici()
print(b1.getroi())
print(s1.getroi())
print(i1.getroi())


10
9
8

Dynamic binding:
-------------------------
Based on the object corresponding or related method present in tthe class executed the concept is called dynamic binding.

Method Resolution Order:(MRO)
----------------------------------------------
1.Method resolution order is assosiated with multilevel and multiple inheritance.
2.Method resolution order describes the search path of the class which Python uses to get the appropriate method in classes that contain the multi-inheritance
3.MRO stands for Method Resolution Order. It is the order in which Python looks for a method in a hierarchy of classes. MRO follows a specific sequence to determine which method to invoke when it encounters multiple classes with the same method name.

# Method resolution Order

class A:
    def myname(self):
        print("I am a class A")
class B(A):
    def myname(self):
        print("I am a class B")
class c(A):
    def myname(self):
        print("I am a class c")

class D(c,B):       # Empty class
    pass    
d=D()
d.myname()

I am a class c

Python follows a depth-first lookup order and hence ends up calling the method from class A. By following the method resolution order, the lookup order as follows. 
Class D -> Class C -> Class B -> Class A 
Python follows depth-first order to resolve the methods and attributes. So in the above example, it executes the method in class c. 

class A:
    def myname(self):
        print("I am a class A")
class B(A):
    def myname(self):
        print("I am a class B")
class c(A):
    def myname(self):
        print("I am a class c")

class D(B,c):
    pass

print(D.__mro__)   #tuple
print(c.mro())  #list

(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.c'>, <class '__main__.A'>, <class 'object'>)
[<class '__main__.c'>, <class '__main__.A'>, <class 'object'>]

Static method;
---------------------
Can be created in 2 ways:
a.using static method
b.using decorator @staticmethod

static topics:
1.static varaible
2.static method

# Static method 1

class maths:
    def add(x,y):
        return x+y

maths.add=staticmethod(maths.add)
print(maths.add(6,12))

18

class maths:
    def add(x,y):
        return x+y

x=staticmethod(maths.add)
print(x(6,12))

18

#static method 2 (decorator(@))

class maths:
    @staticmethod
    def add(x,y):
        return x+y

print(maths.add(12,4))

16

class maths:
    @staticmethod
    def add(x,y):
        return x+y
x=maths.add
print(x(12,4))

16

Decorator:
---------------
It is a very powerful and useful tool in python since it allows programmers to modify the behaviour of function or class

==============================================================================================================

7.Abstraction and Encapsulation:
------------------------------------------------
1.Data abstraction and encapsulation in python are related to each other.
2.Data abstarction is only possible through encapsulation

class base:
    def __init__(self):
        self.__a="aimlds"
        print(self.__a)

class derived(base):
    def __init__(self):
        base.__init__(self)
        print(self.__a)

#d1=derived()
b1=base()

aimlds

**Every class is a encapsulated class when there is a method in class and the method have some data then it is called encapsulated class

3.Data abstarction means to hide internal functionalities that are performing on the application using codes and to show only essential information(class attributes)

==> Making use of the functionality withput knowing of there information is called abstarction.
ex: we all use smart phone and very much familiar with its functions such as camera,voice,record,call dialing etc but we don,t know how these operations are happening in the background

Abstract class in python:
------------------------------------
1.A class that consists of one or more abstarct methods is called abstract class
2.Abstarct methods don't contain their implemantation.Abstract method can be inherited by abstract method gets its definition in the subclass
3.Abstract classes allow us to define methods that must be implemented by subclasses, ensuring a consistent interface while still allowing the subclasses to provide specific implementations.
4.An abstract class can be helpful when we are designing large functions and abstaract class is also helpful to provide the standard interface for different implementations of components.
5..Python provides abc module to use the abstarction in the python program

syntax:
----------
from abc import ABC
class classname(ABC):
we import the ABC class from the abc module

from abc import ABC, abstractmethod
class BaseClass(ABC):
    @abstractmethod
    def method_1(self):
         #empty body
         pass

from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def milage(self):
        psss

class suzuki(car):
    def milage(self):
        print("The milage is 20kmph")

class tesla(car):
    def milage(self):
        print("The milage is 30kmph")
s1=suzuki()
t1=tesla()
s1.milage()
t1.milage()

Super function:
-----------------------
Python also has a super() function that will the child class inherit all the methods and properties from its parent
By using the super() function,you do not have to use the name of the parent element it will automatically inherit the methods and properties from its parent


# super()
class Base:
    def __init__(self):
        self.a=21 
        print(self.a)
class Derived(Base):
    def __init__(self):
        super().__init__()
        print(self.a+2)
class Derived1(Derived):
    def __init__(self):
        super().__init__()
        print(self.a+3)
d1=Derived1()

21
23
24

Encapsulation:
----------------------
Encapsulation is the process of hiding the internal state of an object and requiring all interactions to be performed through an object’s methods

    -----------------------------------------------------
    |    Methods         |         Variables            |
    |                    |                              |   
    -----------------------------------------------------
                              Class

The wrapping up of data and methods into a single unit is called encapsulation
How Encapsulation Works :
Data Hiding: The variables (attributes) are kept private or protected, meaning they are not accessible directly from outside the class. Instead, they can only be accessed or modified through the methods.
Access through Methods: Methods act as the interface through which external code interacts with the data stored in the variables. For instance, getters and setters are common methods used to retrieve and update the value of a private variable.
Control and Security: By encapsulating the variables and only allowing their manipulation via methods, the class can enforce rules on how the variables are accessed or modified, thus maintaining control and security over the data.

Public Members
--------------------------

class Public:
    def __init__(self):
        self.name = "Kalyan"  # Public attribute

    def display_name(self):
        print(self.name)  # Public method

obj = Public()
obj.display_name()  # Accessible
print(obj.name)  # Accessible

Kalyan
Kalyan

Protected members
-----------------------------

class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

30

Private members:
--------------------------
class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError

50000 

Encapsulation is an Object-Oriented Programming (OOP) principle that involves bundling the data (attributes) and methods (functions) that operate on the data into a single unit, called a class. This concept helps hide the internal state of an object from the outside world, providing a controlled interface for interacting with the object’s data and methods.

Encapsulation in Python is implemented using access specifiers to control access to class members:

Public Members: By default, attributes and methods are public and can be accessed from outside the class.
Protected Members: Use a single underscore (_) prefix to indicate that an attribute or method is intended for internal use within the class and its subclasses.
Private Members: Use double underscores (__) prefix to make an attribute or method private. This leads to name mangling, making it more challenging to access from outside the class.


====================================================================================================================

*****FILES******

File Handling:
-------------------
Def:
A file is a place on the disk where a group of related data is stored

Classification:
a.Text files
b.Binary files

Advantages:
Huge amount of data can be handled easily

Basic operations of file:
1.Creating or opening a file
2.Read/write operation on the file
3.Closing the file

Different File Mode in Python
Below are the different types of file modes in Python along with their description:

Mode            Description

‘r’	Open text file for reading. Raises an I/O error if the file does not exist.
‘r+’	Open the file for reading and writing. Raises an I/O error if the file does not exist.
‘w’	Open the file for writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘w+’	Open the file for reading and writing. Truncates the file if it already exists. Creates a new file if it does not exist.
‘a’	Open the file for writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘a+’	Open the file for reading and writing. The data being written will be inserted at the end of the file. Creates a new file if it does not exist.
‘rb’	Open the file for reading in binary format. Raises an I/O error if the file does not exist.
‘rb+’	Open the file for reading and writing in binary format. Raises an I/O error if the file does not exist.
‘wb’	Open the file for writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘wb+’	Open the file for reading and writing in binary format. Truncates the file if it already exists. Creates a new file if it does not exist.
‘ab’	Open the file for appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.
‘ab+’	Open the file for reading and appending in binary format. Inserts data at the end of the file. Creates a new file if it does not exist.

open():
---------
Syntax:

fileptrobject=open("filename","mode")

1.The open() is used for creating a new file and as well as is used for opening a file already present in the system
2.When the mode specified is 'w' and if the file is already present then that file data get losses
3.When the mode specified is 'w' and if the file is not present then new file get creates

Mode:

The mode specifies the intention of the user in opening the file
r-read mode
w-write mode
a-append mode
b-binary mode

close():
----------
Syntax:

fileptrobject.close()
It breaks the connection from the file

write():
---------
Syntax:

fileobject.write("Data to store into the file")

x=open("DS.txt","w")
x.write('''Hi Kalyan!
Pyhton files topic
started today''')
x.close()

Read Operation:
-----------------------

1.read()-method : reads the complete data of the file
------------------------

syntax:
fileobject.read()

x=open("DS.txt","r")
content=x.read()
print(content)
x.close()

Hi Kalyan!
Pyhton files topic
started today


2.read(n)-method :reads first n characters from the file
-----------------------

x=open("DS.txt","r")
content=x.read(2)  #reads first 2 characters from the file
print(content)
x.close()

Hi 

3.readline() -method: reads the first line of the file
--------------------------
Syntax:
fileobject.readline()

x=open("DS.txt","r")
content=x.readline() 
print(content)
x.close()

Hi Kalyan!

x=open("DS.txt","r")
content=x.readline(9) # readline with parameter to read characters
print(content)
x.close()


4.readlines()-method:
----------------------------
1.reads the total lines of the data from the file
2.The output of readlines() is a list where each line of the file is one element

syntax:
fileobject.readlines()

x=open("DS.txt","r")
content=x.readlines() 
print(content)
print(type(content))
print(len(content))
x.close()

['Hi Kalyan!\n', 'Pyhton files topic\n', 'started today']
<class 'list'>
3

**readlines with number parameter return only first line whatever the number is
----------------------------------

x=open("DS.txt","r")
content=x.readlines(2) 
print(content)
print(type(content))
print(len(content))
x.close()

x=open("DS.txt","r")
content=x.readlines(10) 
print(content)
print(type(content))
print(len(content))
x.close()

['Hi Kalyan!\n']
<class 'list'>
1
['Hi Kalyan!\n']
<class 'list'>
1

**To read  file using for loop
---------------------------------------

#read file using for loop

x=open("DS.txt","r")
c=0
for i in x:
    print(i)
    c=c+1
print(c)
x.close()

Hi Kalyan!

Pyhton files topic

started today
3



append():used for adding extra data to the file already present
-------------
syntax:
fileobject=open("filename",'a')

1.If the file name is not present in the system,then a newfile get creates and data stores into it.
2.If the file is present then the data attaches at last of the existing file.

# append() ==> method

x=open("DS.txt",'a')
x.write("Good morning Kalyan.Happy to see you")
print("Appending  done succesfully")
x.close()

Appending  done succesfully


Modifying file pointer positions:
---------------------------------------------
tell() - method:
--------------------
syntax:
fileobject.tell()

Description:
Gives the current position of the file pointer in the file.
By default the file pointer position is index 0


# tell() ==> method

x=open("DS.txt","r")
a=x.tell()
print(a)
x.close()

0

seek() - method:
-----------------------
In python,seek() function is used to change the position of the file handle to a given specific postion

syntax:
fileobject.seek(offset,fromwhere)

offset: number of position to move
fromwhere : it defines the point of reference
It accepts three values:
0-beginning of the file
1-present postion of the file
2-end of the file

0-default value

x=open("DS.txt","r")
x.seek(5,0)
a=x.read()
print(a)
x.close()
print()

lyan!
Pyhton files topic
started todayGood morning Kalyan.Happy to see you

x=open("DS.txt","r")
x.seek(3,0)
a=x.read()
print(a)
x.close()
print()

Kalyan!
Pyhton files topic
started todayGood morning Kalyan.Happy to see you

x=open("DS.txt","r")
x.seek(3)
a=x.read()
print(a)
x.close()
print()

Kalyan!
Pyhton files topic
started todayGood morning Kalyan.Happy to see you

#if you want to change the multiple times the file pointer position use the  'rb' mode
x=open("DS.txt","rb")
x.seek(3)
x.seek(2,1)
a=x.read()
print(a)
x.close()
print()

b'lyan!\r\nPyhton files topic\r\nstarted todayGood morning Kalyan.Happy to see you'

x=open("DS.txt","rb")
x.seek(-10,2)
a=x.read()
print(a)
x.close()
print()

b'to see you'


with keyword:
-------------------
syntax:
with open("filename","mode") as fileobject:

With keyword guarntees the closing of files

# with keyword :

with open("DS.txt","rb") as x:
    x.seek(-10,2)
    a=x.read()
    print(a)

b'to see you'

Files with command line parameters:
-----------------------------------------------------

# command line parameters

Srinivasa Kalyan
   1              2

0 index : File name

import sys
print(sys.argv[0])
x=sys.argv[1]
y=sys.argv[2]
print(x*3)
print(y*4)

E:\228a1a4454\files.py
SrinivasaSrinivasaSrinivasa
KalyanKalyanKalyanKalyan


DS.txt  crt.txt
 1            2 
DS.txt copied to crt.txt


import sys
inf=open(sys.argv[1],"r")
ouf=open(sys.argv[2],"w")
r=inf.read()
while r:
    ouf.write(r)
    r=inf.read()
print("File copied Succesfully")
inf.close()
ouf.close()

File copied Succesfully


import sys
inf=open(sys.argv[1],"r")
ouf=open(sys.argv[2],"w")
r=inf.read()
print(r)
while r:
    ouf.write(r)
    r=inf.read()
print("File copied Succesfully")
inf.close()

Hi Kalyan!
Pyhton files topic
started todayGood morning Kalyan.Happy to see you
File copied Succesfully

Execution : Run -> configuration per file -> command line parameters


File Zipping and Unzipping:
---------------------------------------
The files should be in the present working directory to perform zip and unzip operations

# ZIPPING NAD UNZIPPING

from zipfile import *
p=ZipFile("sk.zip",'w',ZIP_DEFLATED)
p.write('Kalyan.docx')
p.close()

here sk.zip is the zip file creted and Kalyan.docx is the file created in same directory to zip

#Unzpping

from zipfile import *
p=ZipFile("sk.zip","r",ZIP_STORED)
a=p.namelist()  namelist()--> display the total files in the zip file
for x in a:
    print(x)
p.close()

Kalyan.docx


Operating System module:
--------------------------------------

rename():
--------------
syntax:
os.rename("oldfilename","newfilename")
rename() is used for changing the name of the file

import os
os.rename("Kalyan.docx","sk.docx")

mkdir():
-----------
syntax:
os.mkdir("name of the directory")

import os
os.mkdir("Kalyan")

getcwd():
-------------
syntax:
os.getcwd()
cwd stands for current working directory

import os
print(os.getcwd())

rmdir():
----------
syntax:
os.rmdir()
rmdir stands for removing the directory

import os
os.rmdir("Kalyan")

Sr.No.	Methods & Description

1	os.access(path, mode)
Use the real uid/gid to test for access to path.

2	os.chdir(path)
Change the current working directory to path

3	os.chflags(path, flags)
Set the flags of path to the numeric flags.

4	os.chmod(path, mode)
Change the mode of path to the numeric mode.

5	os.chown(path, uid, gid)
Change the owner and group id of path to the numeric uid and gid.

6	os.chroot(path)
Change the root directory of the current process to path.

7	os.close(fd)
Close file descriptor fd.

8	os.closerange(fd_low, fd_high)
Close all file descriptors from fd_low (inclusive) to fd_high (exclusive), ignoring errors.

9	os.dup(fd)
Return a duplicate of file descriptor fd.

10	os.dup2(fd, fd2)
Duplicate file descriptor fd to fd2, closing the latter first if necessary.

11	os.fchdir(fd)
Change the current working directory to the directory represented by the file descriptor fd.

12	os.fchmod(fd, mode)
Change the mode of the file given by fd to the numeric mode.

13	os.fchown(fd, uid, gid)
Change the owner and group id of the file given by fd to the numeric uid and gid.

14	os.fdatasync(fd)
Force write of file with filedescriptor fd to disk.

15	os.fdopen(fd[, mode[, bufsize]])
Return an open file object connected to the file descriptor fd.

16	os.fpathconf(fd, name)
Return system configuration information relevant to an open file. name specifies the configuration value to retrieve.

17	os.fstat(fd)
Return status for file descriptor fd, like stat().

18	os.fstatvfs(fd)
Return information about the filesystem containing the file associated with file descriptor fd, like statvfs().

19	os.fsync(fd)
Force write of file with filedescriptor fd to disk.

20	os.ftruncate(fd, length)
Truncate the file corresponding to file descriptor fd, so that it is at most length bytes in size.

21	os.getcwd()
Return a string representing the current working directory.

22	os.getcwdu()
Return a Unicode object representing the current working directory.

23	os.isatty(fd)
Return True if the file descriptor fd is open and connected to a tty(-like) device, else False.

24	os.lchflags(path, flags)
Set the flags of path to the numeric flags, like chflags(), but do not follow symbolic links.

25	os.lchmod(path, mode)
Change the mode of path to the numeric mode.

26	os.lchown(path, uid, gid)
Change the owner and group id of path to the numeric uid and gid. This function will not follow symbolic links.

27	os.link(src, dst)
Create a hard link pointing to src named dst.

28	os.listdir(path)
Return a list containing the names of the entries in the directory given by path.

29	os.lseek(fd, pos, how)
Set the current position of file descriptor fd to position pos, modified by how.

30	os.lstat(path)
Like stat(), but do not follow symbolic links.

31	os.major(device)
Extract the device major number from a raw device number.

32	os.makedev(major, minor)
Compose a raw device number from the major and minor device numbers.

33	os.makedirs(path[, mode])
Recursive directory creation function.

34	os.minor(device)
Extract the device minor number from a raw device number.

35	os.mkdir(path[, mode])
Create a directory named path with numeric mode mode.

36	os.mkfifo(path[, mode])
Create a FIFO (a named pipe) named path with numeric mode mode. The default mode is 0666 (octal).

37	os.mknod(filename[, mode=0600, device])
Create a filesystem node (file, device special file or named pipe) named filename.

38	os.open(file, flags[, mode])
Open the file file and set various flags according to flags and possibly its mode according to mode.

39	os.openpty()
Open a new pseudo-terminal pair. Return a pair of file descriptors (master, slave) for the pty and the tty, respectively.

40	os.pathconf(path, name)
Return system configuration information relevant to a named file.

41	os.pipe()
Create a pipe. Return a pair of file descriptors (r, w) usable for reading and writing, respectively.

42	os.popen(command[, mode[, bufsize]])
Open a pipe to or from command.

43	os.read(fd, n)
Read at most n bytes from file descriptor fd. Return a string containing the bytes read. If the end of the file referred to by fd has been reached, an empty string is returned.

44	os.readlink(path)
Return a string representing the path to which the symbolic link points.

45	os.remove(path)
Remove the file path.

46	os.removedirs(path)
Remove directories recursively.

47	os.rename(src, dst)
Rename the file or directory src to dst.

48	os.renames(old, new)
Recursive directory or file renaming function.

49	os.rmdir(path)
Remove the directory path

50	os.stat(path)
Perform a stat system call on the given path.

51	os.stat_float_times([newvalue])
Determine whether stat_result represents time stamps as float objects.

52	os.statvfs(path)
Perform a statvfs system call on the given path.

53	os.symlink(src, dst)
Create a symbolic link pointing to src named dst.

54	os.tcgetpgrp(fd)
Return the process group associated with the terminal given by fd (an open file descriptor as returned by open()).

55	os.tcsetpgrp(fd, pg)
Set the process group associated with the terminal given by fd (an open file descriptor as returned by open()) to pg.

56	os.tempnam([dir[, prefix]])
Return a unique path name that is reasonable for creating a temporary file.

57	os.tmpfile()
Return a new file object opened in update mode (w+b).

58	os.tmpnam()
Return a unique path name that is reasonable for creating a temporary file.

59	os.ttyname(fd)
Return a string which specifies the terminal device associated with file descriptor fd. If fd is not associated with a terminal device, an exception is raised.

60	os.unlink(path)
Remove the file path.

61	os.utime(path, times)
Set the access and modified times of the file specified by path.

62	os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
Generate the file names in a directory tree by walking the tree either top-down or bottom-up.

63	os.write(fd, str)
Write the string str to file descriptor fd. Return the number of bytes actually written.


***The os.path is another Python module, which also provides a big range of useful methods to manipulate files and directories. Most of the useful methods are listed here −


Sr.No.	Methods with Description

1	os.path.abspath(path)
Returns a normalized absolutized version of the pathname path.

2	os.path.basename(path)
Returns the base name of pathname path.

3	os.path.commonprefix(list)
Returns the longest path prefix (taken character-by-character) that is a prefix of all paths in list.

4	os.path.dirname(path)
Returns the directory name of pathname path.

5	os.path.exists(path)
Returns True if path refers to an existing path. Returns False for broken symbolic links.

6	os.path.lexists(path)
Returns True if path refers to an existing path. Returns True for broken symbolic links.

7	os.path.expanduser(path)
On Unix and Windows, returns the argument with an initial component of ~ or ~user replaced by that user's home directory.

8	os.path.expandvars(path)
Returns the argument with environment variables expanded.

9	os.path.getatime(path)
Returns the time of last access of path.

10	os.path.getmtime(path)
Returns the time of last modification of path.

11	os.path.getctime(path)
Returns the system's ctime, which on some systems (like Unix) is the time of the last change, and, on others (like Windows), is the creation time for path.

12	os.path.getsize(path)
Returns the size, in bytes, of path.

13	os.path.isabs(path)
Returns True if path is an absolute pathname.

14	os.path.isfile(path)
Returns True if path is an existing regular file.

15	os.path.isdir(path)
Returns True if path is an existing directory.

16	os.path.islink(path)
Returns True if path refers to a directory entry that is a symbolic link.

17	os.path.ismount(path)
Returns True if pathname path is a mount point: a point in a file system where a different file system has been mounted.

18	os.path.join(path1[, path2[, ...]])
Joins one or more path components intelligently.

19	os.path.normcase(path)
Normalizes the case of a pathname.

20	os.path.normpath(path)
Normalizes a pathname.

21	os.path.realpath(path)
Returns the canonical path of the specified filename, eliminating any symbolic links encountered in the path

22	os.path.relpath(path[, start])
Returns a relative filepath to path either from the current directory or from an optional start point.

23	os.path.samefile(path1, path2)
Returns True if both pathname arguments refer to the same file or directory

24	os.path.sameopenfile(fp1, fp2)
Returns True if the file descriptors fp1 and fp2 refer to the same file.

25	os.path.samestat(stat1, stat2)
Returns True if the stat tuples stat1 and stat2 refer to the same file.

26	os.path.split(path)
Splits the pathname path into a pair, (head, tail) where tail is the last pathname component and head is everything leading up to that.

27	os.path.splitdrive(path)
Splits the pathname path into a pair (drive, tail) where drive is either a drive specification or the empty string.

28	os.path.splitext(path)
Splits the pathname path into a pair (root, ext) such that root + ext == path, and ext is empty or begins with a period and contains at most one period.

29	os.path.walk(path, visit, arg)
Calls the function visit with arguments (arg, dirname, names) for each directory in the directory tree rooted at path (including path itself, if it is a directory).

===============================================================================================================================

*************Exception Handling********************

Programming errors are classified into two types
a.compile time eroors
b.Run time errors
Run time errors are called exception
(or)
unusual condition in a program resulting in the interruption of the program execution

Exception Handling
----------------------------
Handling runtime errors is called exception handling

If a exception is not handled:
------------------------------------------
The program execution stops at the point of exception and the next part of the program execution does not takes place

Sr.No. Name of the Exception
Description of the Exception
1 Exception
All exceptions of Python have a base class.
2 StopIteration
If the next() method returns null for an iterator, this exception is raised.
3 SystemExit
The sys.exit() procedure raises this value.
4 StandardError
Excluding the StopIteration and SystemExit, this is the base class for all Python built-in exceptions.
5 ArithmeticError
All mathematical computation errors belong to this base class.
6 OverflowError
This exception is raised when a computation surpasses the numeric data type's maximum limit.
7 FloatingPointError
If a floating-point operation fails, this exception is raised.
8 ZeroDivisionError
For all numeric data types, its value is raised whenever a number is attempted to be divided by zero.
9 AssertionError
If the Assert statement fails, this exception is raised.
10 AttributeError
This exception is raised if a variable reference or assigning a value fails.
11 EOFError
When the endpoint of the file is approached, and the interpreter didn't get any input value by raw_input() or input() functions, this exception is raised.
12 ImportError
This exception is raised if using the import keyword to import a module fails.
13 KeyboardInterrupt
If the user interrupts the execution of a program, generally by hitting Ctrl+C, this exception is raised.
14 LookupError
LookupErrorBase is the base class for all search errors.
15 IndexError
This exception is raised when the index attempted to be accessed is not found.
16 KeyError
When the given key is not found in the dictionary to be found in, this exception is raised.
17 NameError
This exception is raised when a variable isn't located in either local or global namespace.
18 UnboundLocalError
This exception is raised when we try to access a local variable inside a function, and the variable has not been assigned any value.
19 EnvironmentError
All exceptions that arise beyond the Python environment have this base class.
20 IOError
If an input or output action fails, like when using the print command or the open() function to access a file that does not exist, this exception is raised.
22 SyntaxError
This exception is raised whenever a syntax error occurs in our program.
23 IndentationError
This exception was raised when we made an improper indentation.
24 SystemExit
This exception is raised when the sys.exit() method is used to terminate the Python interpreter. The parser exits if the situation is not addressed within the code.
25 TypeError
This exception is raised whenever a data type-incompatible action or function is tried to be executed.
26 ValueError
This exception is raised if the parameters for a built-in method for a particular data type are of the correct type but have been given the wrong values.
27 RuntimeError
This exception is raised when an error that occurred during the program's execution cannot be classified.
28 NotImplementedError
If an abstract function that the user must define in an inherited class is not defined, this exception is raised.
29 SystemError
Raised when the interpreter finds an internal problem, but when this error is encountered the Python interpreter does not exit.

Common exceptions:
-------------------------------
Python provides the number of built-in exceptions
A list of common exceptions that can be thrown from a standard python program is given below
1.ZeroDivisionError : Occurs when a number is divided by zero
2.NameError: It occurs when the name is not found.It may be local or global.
3.IndentationError : If incorrect indentation is given
4.IOError : It occurs when input and Output operation fails
5.EOFError : It occurs when the end of the file is reached,and yet operations are being performed

a=int(input())
b=int(input())
c=a/b
print("a/b = %d"%c)
print("Hi i am other part of program")

10
0
Traceback (most recent call last):
  File "E:/228a1a4454/Exception handiling.py", line 3, in <module>
    c=a/b
ZeroDivisionError: division by zero

Exception handling- 1
-------------------------------
The try-except statement
-------------------------------------
try:
possibility of error occuring statements are suppose to written un try bloack

except:
The code to execute if an exception occurs

try:
    a=int(input())
    b=int(input())
    c=a/b
    print(c)
except:
    print("can't divide with zero")
print("hi")


10
0
can't divide with zero
hi

Exception handling- 2
--------------------------------
syntax:

try:
           #block of code

except Exception1:
           #block of code

else:
       #this code executes if no except block is executed.

try:
    a=int(input())
    b=int(input())
    c=a/b
    print("a/b = %d"%c)

except Exception:
    print("cant't divide by zero")
    print(Exception)
else:
    print("I am else block")


10
0
cant't divide by zero
<class 'Exception'>      

10
5
a/b = 2
I am else block

Except with exception class object:
---------------------------------------------------
try:
    a=int(input())
    b=int(input())
    c=a/b
    print("a/b = %d"%c)

except Exception as e:
    print("cant't divide by zero")
    print(e)
else:
    print("I am else block")

10
0
cant't divide by zero
division by zero


try:
    a=int(input())
    b=int(input())
    c=a/b
    print("a/b = %d"%c)

except Exception:
    print("2 chances are left to give crct input")
    counter=2
    while(counter):
        a=int(input())
        b=int(input())
        if(a==0 or b==0):
            counter-=1
            if(counter==0):
                print("Chances Over")
                break
            print("%d Chance left give correct input" %counter)
            continue
        else:
            c=a/b;
            print(c)
            break


10
0
2 chances are left to give crct input
10
0
1 Chance left give correct input
10
0
Chances Over


Declaring multiple exceptions:
--------------------------------------------
syntax:

try:
    #block of code

except (<Exception1>,<Exception1>,<Exception1>,<Exception1>,..........,<Exception1>):
    #block of code
else:
    #block of code

try:
    a=10/0
except(ArithmeticError,IOError):
    print("Arithmetic Exception")
    print(ArithmeticError)
else:
    print("Successfully Done")

Arithmetic Exception
<class 'ArithmeticError'>


Exception Handling -3
-------------------------------
syntax:

try:
    #block of code
    #this may throw an exception
finally:
    #block of code
    #this will be always executed

Finally:
----------
The code to execute compulsory

try:
    fileptr=open("kalyan.txt","r")
    fileptr.write("Hi i am good")
except:
    print("Wrong operation")
else:
    print("Mode of the file is read")
finally:
    print("File closed")
    print("Error")

Wrong operation
File closed
Error

Raising Exceptions:
----------------------------
Syntax:
raise Exception_class,<value>

try:
    age=int(input("Enter the age:"))
    if(age<18):
        raise ValueError
    else:
        print("The age is Valid")
except ValueError:
    print("The age is not valid")

Enter the age:12
The age is not valid

