Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#operators
#arithmetic operator->+,-,*,**,//,/,%
a=5
b=10
print(a+b)
15
print(a-b)
-5
print(a*b)
50
print(a**b)
9765625
print(a//b)
0
print(a/b)
0.5
print(a%b)
5
#assignment operators
->+=,-=,*=,**=,//=,/=,%=
SyntaxError: invalid syntax
a=2
b=4
a+=1
a
3
a-=2
a
1
a*=1
a
1
a**=2
a
1
a//=2
a
0
a/=
SyntaxError: invalid syntax
a/=2
a
0.0
a%=2
a
0.0
#comparision operators
#==,!=,>,<,>=,<=
a=2
b=4
a==b
False
a!=b
True
a>b
False
a<b
True
b<a
False
b>a
True
a>=
SyntaxError: invalid syntax
a>=b
False
b<=a
False
a<=b
True
#logical operators
#->and,or,not
a=2
b=5
a<b and b>a
True
a>b and b<a
False
b>a and a>b
False
b>a or a>b
True
a<b not b>a
SyntaxError: invalid syntax
not a>b
True
not b>a
False
#membership operators
#in,not in
a=1,4,5,6,7,8
4 in a
True
9 in a
False
10 not in a
True
10 in a
False
#identity operators
#->is is not
a=1,2,3,4
b=2,46,7,8
a is b
False
a=1,2,3,4
b=a
b=1,2,3,4
a is b
False
a is c
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    a is c
NameError: name 'c' is not defined
>>> c=1,2,3,4
>>> a is b
False
>>> a is c
False
>>> a is not b
True
>>> a in not c
SyntaxError: invalid syntax
>>> a is not c
True
>>> #bitwise operators
>>> #->and(&),|(or),^,~,<<,>>
>>> a=5
>>> b=3
>>> a&b
1
>>> a|b
7
>>> a^b
6
>>> a~b
SyntaxError: invalid syntax
>>> a<<b
40
>>> a>>b
0
