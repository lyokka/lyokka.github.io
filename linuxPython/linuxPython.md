---
layout: single
author_profile: true
permalink: /linuxPython/
title: Python in Linux
---

Usually we write python code in linux like this:

```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: person.py

class Person:
  def __init__(self, name, job=None, pay=0):
    self.name = name
    self.job = job
    self.pay = pay

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job='dev', pay=100000)
  print bob.name, bob.pay
  print sue.name, sue.pay
```

Right now let's discuss why we need to write code like this.

- ## First line
```Python
#!/usr/bin/python
```
This line looks very magic, it is just like a comment. But actually, it chooses python interpreter.

Typically, we can execute a python script in terminal like this

![exc1](/assets/images/linuxPython/exc1.png)

But you cannot execute python like this

![exc1](/assets/images/linuxPython/exc2.png)

After changing the permission of this file to be executable we can run python in this way

![exc1](/assets/images/linuxPython/ex3.png)

Let's check the python interpreters we have.

![exc1](/assets/images/linuxPython/inter1.png)

Right now, let's change the interpreter to python3.5m
```Python
#!/usr/bin/python3.5m
# -*- coding: utf-8 -*-
# file: person.py

class Person:
  def __init__(self, name, job=None, pay=0):
    self.name = name
    self.job = job
    self.pay = pay

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job='dev', pay=100000)
  print bob.name, bob.pay
  print sue.name, sue.pay
```
That's what expected to get, since python2 and python3 have difference in print function.

![exc1](/assets/images/linuxPython/inter2.png)

- ## \_\_name\_\_

Let's change the code a little bit.

```Python
#!/usr/bin/python
# -*- coding: utf-8 -*-
# file: person.py

class Person:
  def __init__(self, name, job=None, pay=0):
    self.name = name
    self.job = job
    self.pay = pay

print "__name__ is " + __name__

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job='dev', pay=100000)
  print bob.name, bob.pay
  print sue.name, sue.pay
```
What we will get is

![exc1](/assets/images/linuxPython/name1.png)

This shows "\_\_name\_\_" is "\_\_main\_\_"

But what if we load this module in another file?
```Python
#!/usr/bin/Python
# -*- coding: utf-8 -*-
# file: main.py

from person import *

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job='dev', pay=100000)
  print bob.name, bob.pay
  print sue.name, sue.pay
```
This is what we get

![exc1](/assets/images/linuxPython/name2.png)

Right now, '\_\_name\_\_' in person.py changes to 'person'.
