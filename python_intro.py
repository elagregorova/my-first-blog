def hi(name):
    print("Hey "+name+"?")

hi("jozo")
>>>  jozo
'jk'
>>>  len(jozo)
2
>>>  jozo="zmizni"
>>>  jozo
'zmizni'
>>>  jk="kokot"
>>>  jk
'kokot'
>>>  jozo + jk
'zmiznikokot'
>>>  jozo +  jk
'zmiznikokot'
>>>  jozo + ( jk)
'zmiznikokot'
>>>  jozo + (     jk)
'zmiznikokot'
>>>  jozo + (jk)
'zmiznikokot'
>>>  jk="kokot     "
>>>  jozo + (jk)
'zmiznikokot     '
>>>  print(jozo)
zmizni
>>>  del jozo
>>>  print(jozo)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'jozo' is not defined
>>>  []
[]
>>>  lotterz = [12,34,45]
>>>  lotterz
[12, 34, 45]
>>>  len(lotterz)
3
>>>  lottery = [12,34,45]
>>>  lottery
[12, 34, 45]
>>>  lottery.sort()
>>>  print(lottery)
[12, 34, 45]
>>>  lottery.reverse()
>>>  lottery
[45, 34, 12]
>>>  lottery.reverse
<built-in method reverse of list object at 0x000001CDFFF6F6C8>
>>>  lottery.reverse()
>>>  lottery
[12, 34, 45]
>>>  lottery.append(456)
>>>  lottery
[12, 34, 45, 456]
>>>  lottery.sort()
>>>  lottery
[12, 34, 45, 456]
>>>  lottery.reverse()
>>>  lottery
[456, 45, 34, 12]
>>>  lottery[2]
34
>>>  lotterz
[12, 34, 45]
>>>  lottery
[456, 45, 34, 12]
>>>  lottery.pop(2)
34
>>>  lottery
[456, 45, 12]
>>>  lottery.extend([56, 23])
>>>  lottery
[456, 45, 12, 56, 23]
>>>  lottery.pop(-1)
23
>>>  lottery
[456, 45, 12, 56]
>>>  lottery(-4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>>  lottery(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'list' object is not callable
>>>  lottery[-4]
456
>>>  lottery[0]
456
>>>  {}
{}
>>>  jozoskids ={"name":"Ola", "country":"Poland", "favorite_numbers":[7, 42, 92]}
>>>  name
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'name' is not defined
>>>  joyokids
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'joyokids' is not defined
>>>  jozoskids
{'name': 'Ola', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
>>>  jozoskids ={"name":"Ela", "country":"Poland", "favorite_numbers":[7, 42, 92]}
>>>  jozokids
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'jozokids' is not defined
>>>  jozoskids
{'name': 'Ela', 'country': 'Poland', 'favorite_numbers': [7, 42, 92]}
>>>  name = "jozo"
>>>  jozoskids ={"name":"Ela", "country":"Poland", "favorite_numbers":[7, 42, 92]}
>>>  name
'jozo'
>>>  favorite_numbers
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'favorite_numbers' is not defined
>>>  "favorite_numbers"
'favorite_numbers'
>>>  jozoskids("name")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dict' object is not callable
>>>  jozoskids["name"]
'Ela'
>>>  jozoskids["age"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'age'
>>>  jozoskids["favorite_language"]="zobni"
>>>  jozoskids
{'name': 'Ela', 'country': 'Poland', 'favorite_numbers': [7, 42, 92], 'favorite_language': 'zobni'}
>>>  len(jozoskids)
4
>>>  len(jozoskids)
4
>>>  jozoskids.pop("favorite_numbers")
[7, 42, 92]
>>>  jozoskids
{'name': 'Ela', 'country': 'Poland', 'favorite_language': 'zobni'}
>>>  jozoskids ={"name":"Ela", "country":"Czech", "favorite_language":"zobni"}
>>>  jozoskids
{'name': 'Ela', 'country': 'Czech', 'favorite_language': 'zobni'}
>>>  jozoskids["country"]=Poland
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Poland' is not defined
>>>  jozoskids["country"]="Poland"
>>>  jozoskids
{'name': 'Ela', 'country': 'Poland', 'favorite_language': 'zobni'}
>>>  jozoskids["country"]="Czech"
>>>  jozoskids
{'name': 'Ela', 'country': 'Czech', 'favorite_language': 'zobni'}
>>>  6>= 12/2
True
>>>  6== 12/2
True
>>>  1>"django"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'int' and 'str'
>>>  a=2>5
>>>  a
False
>>>  True and True
True
>>>  False and True
False
>>>  True or False
True
>>>  True or 1==1
True
>>>  exit()

C:\Users\Ela.G>cd djangogirls

C:\Users\Ela.G\djangogirls>python python_intro.py
Hello, Django girls!

C:\Users\Ela.G\djangogirls>python python_intro.py
  File "python_intro.py", line 4

    ^
SyntaxError: unexpected EOF while parsing

C:\Users\Ela.G\djangogirls>python python_intro.py
It works!

C:\Users\Ela.G\djangogirls>python python_intro.py
  File "python_intro.py", line 5
    print("Hey Sonja!")
        ^
IndentationError: expected an indented block

C:\Users\Ela.G\djangogirls>python python_intro.py
Hey Sonja!

C:\Users\Ela.G\djangogirls>python python_intro.py
Hey anonymous!

C:\Users\Ela.G\djangogirls>python python_intro.py
  File "python_intro.py", line 2
    if volume < 60:
    ^
IndentationError: unexpected indent

C:\Users\Ela.G\djangogirls>python python_intro.py
Je to dost potichu.

C:\Users\Ela.G\djangogirls>python python_intro.py
Je to dost potichu.
Skvělé, slyším všechny detaily.

C:\Users\Ela.G\djangogirls>python python_intro.py
Traceback (most recent call last):
  File "python_intro.py", line 5, in <module>
    hi()
NameError: name 'hi' is not defined

C:\Users\Ela.G\djangogirls>python python_intro.py
Zobni!
A zmizni!

C:\Users\Ela.G\djangogirls>python python_intro.py
Zobni!
A zmizni!
10

C:\Users\Ela.G\djangogirls>python python_intro.py
Zobni!
A zmizni!

C:\Users\Ela.G\djangogirls>python python_intro.py
  File "python_intro.py", line 3

        ^
SyntaxError: unexpected EOF while parsing

C:\Users\Ela.G\djangogirls>python python_intro.py
Traceback (most recent call last):
  File "python_intro.py", line 9, in <module>
    jozo()
TypeError: jozo() missing 1 required positional argument: 'name'

C:\Users\Ela.G\djangogirls>python python_intro.py
Traceback (most recent call last):
  File "python_intro.py", line 9, in <module>
    hi()
TypeError: hi() missing 1 required positional argument: 'name'

C:\Users\Ela.G\djangogirls>python python_intro.py
Hi Ola!

C:\Users\Ela.G\djangogirls>python python_intro.py
Hi anonymous!

C:\Users\Ela.G\djangogirls>python python_intro.py
  File "python_intro.py", line 2
    print('Hi " + name + "?")
                            ^
SyntaxError: EOL while scanning string literal

C:\Users\Ela.G\djangogirls>python python_intro.py
Hey jozo?

C:\Users\Ela.G\djangogirls>python python_intro.py
Hey jozo?

C:\Users\Ela.G\djangogirls>python python_intro.py
Hey jozo?

C:\Users\Ela.G\djangogirls>myvenv\Scripts\activate
(myvenv) C:\Users\Ela.G\djangogirls>django-admin.py startproject mysite .
CommandError: C:\Users\Ela.G\djangogirls\manage.py already exists, overlaying a project or app into an existing directory won't replace conflicting files

(myvenv) C:\Users\Ela.G\djangogirls>ls
manage.py  myvenv  python_intro.py

(myvenv) C:\Users\Ela.G\djangogirls>django-admin startproject mysite .
'django-admin' is not recognized as an internal or external command,
operable program or batch file.

(myvenv) C:\Users\Ela.G\djangogirls>pip freeze
Django==1.8

(myvenv) C:\Users\Ela.G\djangogirls>django-admin.py startproject mysite .
CommandError: C:\Users\Ela.G\djangogirls\manage.py already exists, overlaying a project or app into an existing directory won't replace conflicting files

(myvenv) C:\Users\Ela.G\djangogirls>rm manage.py

(myvenv) C:\Users\Ela.G\djangogirls>django-admin.py startproject mysite .
CommandError: C:\Users\Ela.G\djangogirls\manage.py already exists, overlaying a project or app into an existing directory won't replace conflicting files

(myvenv) C:\Users\Ela.G\djangogirls>ls
manage.py  myvenv  python_intro.py

(myvenv) C:\Users\Ela.G\djangogirls>