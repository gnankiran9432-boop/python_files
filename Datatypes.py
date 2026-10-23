Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#datatypes
a=10
type(a)
<class 'int'>
b=11.4
type(b)
<class 'float'>
c="kiran"
type(c)
<class 'str'>
d=30+11j
type(d)
<class 'complex'>
a=true
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    a=true
NameError: name 'true' is not defined. Did you mean: 'True'?
type(a)
<class 'int'>
a=True
type(a)
<class 'bool'>
b=False
type(b)
<class 'bool'>
#DATATYPE CONVERSIONS
#INT
int(2.9)
2

int(2)
2
int("kiran")
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    int("kiran")
ValueError: invalid literal for int() with base 10: 'kiran'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
#FLOAT
float(8)
8.0
float(8.9)
8.9
float("hi")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    float("hi")
ValueError: could not convert string to float: 'hi'
float(3+9j)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    float(3+9j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
#STRING
str(1)
'1'
str(9.2)
'9.2'
str("hello")
'hello'
str(True)
'True'
str(False)
'False'
str(2+4j)
'(2+4j)'
#COMPLEX
complex(2)
(2+0j)
complex(4.2)
(4.2+0j)
complex("kiran")
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    complex("kiran")
ValueError: complex() arg is a malformed string
complex(True)
(1+0j)
complex(False)
0j
#BOOLEAN
bool(1)
True
bool(5.7)
True
>>> bool("kiran")
True
>>> bool(3+7j)
True
>>> bool(True)
True
>>> bool(False)
False
>>> int(True)
1
>>> True+True
2
>>> bool(0)
False
>>> bool("")
False
>>> x=5
>>> del x
>>> delx
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    delx
NameError: name 'delx' is not defined
>>> a,b=5,10
>>> a,b=b,a
>>> a
10
>>> del a
>>> bool([])
False
