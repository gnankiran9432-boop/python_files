Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#bitwise operator
#&(and)
a=2
b=4
a&b
0
a=4
b=6
a&b
4
#|(or)
a=4
b=8
a|b
12
a=5
b=7
a|b
7
#~(not)
a=3
~a
-4
-(a+1)
-4
a=-4
~a
3
-(a+1)
3
b=7
~b
-8
#^(xor)
a=3
b=6
a^b
5
bin(3)
'0b11'
bin(6)
'0b110'
>>> a=4
>>> b=7
>>> a^b
3
>>> a=12
>>> b=23
>>> a^b
27
>>> #<<(left shift)
>>> a=3
>>> a<<
SyntaxError: invalid syntax
>>> a<<2
12
>>> a=5
>>> a<<3
40
>>> #>>(right shift)
>>> a=3
>>> a>>2
0
>>> a=4
>>> a>>2
1
>>> a=6
>>> a>>3
0
>>> a=7
>>> a>>3
0
