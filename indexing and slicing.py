Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
#Indexing->1.positive indexing,2.negative indexing
#+ve starts  from 0 and -ve starts from -1
a="vijayawada"
a[0]
'v'
a[0:7]
'vijayaw'
a[0:6]
'vijaya'
a[0]+a[1]+a[2]
'vij'
a="i am in class"
a[8]+a[9]+a[10]+a[11]+a[12]
'class'
a[1]
' '
a[5]
'i'
a[4]
' '
a[3]
'm'
a[1]+a[4]+a[7]
'   '
a="I am learning python fullstack"
a[2]+a[3]
'am'
a[5]+a[6]+a[7]+a[8]+a[9]
'learn'
a[14]+a[15]+a[16]+a[17]+a[18]
'pytho'
a[21]+a[22]+a[23]+a[24]
'full'
a="Time is precious"
a="Time is very precious"
a[-18]+a[-19]+a[-20]+a[-21]
'emiT'
a[-13]+a[-12]+a[-11]+a[-10]
'very'
a="vijayawada is a royal city"
a[-4]+a[-3]+a[-2]+a[-1]
'city'
a[-10]+a[-9]+a[-8]+a[-7]+a[-6]
'royal'
a[-26]+a[-25]+a[-24]+a[-23]+a[-22]+a[-21]+a[-20]+a[-19]+a[-18]+a[-17]+a[-16]
'vijayawada '
#SLICING
a="codegnan"
a[0:4]
'code'
a[4:8]
'gnan'
>>> a[:4]
'code'
>>> a[4:]
'gnan'
>>> a="codegnan it solutions"
>>> a[-17:-13]
'gnan'
>>> a[-12:-10]
'it'
>>> a[-9:-1]
'solution'
>>> b="vijayawada is royal city"
>>> b[-10:-5]
'royal'
>>> b[-1:-5]
''
>>> b[-5:-1]
' cit'
>>> b[-5:0]
''
>>> b[-26:-16]
'vijayawa'
>>> b[-26:-13]
'vijayawada '
>>> a[9:]
'it solutions'
>>> a[-9:]
'solutions'
>>> b[-4:]
'city'
