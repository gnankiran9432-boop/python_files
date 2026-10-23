Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#variables
a=10
print(a)
10
A=20
print(a)
10
B=40
print(b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(b)
NameError: name 'b' is not defined. Did you mean: 'B'?
#always give the variable what gave to store a value
#RULES
#RULES
#a-z,A-Z,0-9
#it dont allow  special characters
_a=50
print(_a)
50
_=40
print(_)
40
@=40
SyntaxError: invalid syntax
&=30
SyntaxError: invalid syntax
#
#3.dont give spaces between words
first name="gnan"
SyntaxError: invalid syntax
first_name="gnan"
firstname="gnan"
#dont give comma between two variables
a=5,b=5
SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
a=5;b=5#instead give semicolan
print(a+b)
10
a,b=5,5
print(a+b)
10
a=4,5,6,7,8
print(a)
(4, 5, 6, 7, 8)
a,b,c=4,5,6
print(a+b+c)
15
#if we give one side 4 variables and gave 3 values only it will give error
#w can access by using strings also
name="kiran"
print(name)
kiran
print("name")    #if we give any  string with  double quotes then it give name  only
name
>>> #unpacking the variables
>>> a,b,c=(8,9,7)
>>> print(a,b,c)
8 9 7
>>> #python is  a case sensitive coz what we assign the variable to the value always  give the variable name when we print
>>> name="kiran"
>>> print(Name)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    print(Name)
NameError: name 'Name' is not defined. Did you mean: 'name'?
>>> print(a)
8
>>> print(name)
kiran
>>> a=5
>>> prin(a)
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    prin(a)
NameError: name 'prin' is not defined. Did you mean: 'print'?
>>> print(a)
5
>>> del a
>>> print(a)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    print(a)
NameError: name 'a' is not defined. Did you mean: 'A'?
#coz a is deleted
#DATA TYPES
#INTEGER->1,2,3
#FLOAT->4.8,9.0
#STRING->"KIRAN",'KIRAN','''KIRAN'''
#COMPLEX->5+9J
#BOOLEAN->TRUE,FALSE






