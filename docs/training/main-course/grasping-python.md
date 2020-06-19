# You gotta understand: Important things for grasping Python

## Syntax

Just the basic rules to be able to understand Python code, informally.


### Indentation

Python uses **indentation** to denote blocks of code (as opposed to e.g. {}
braces in many other languages). Many love it, some don't care all that much,
a few hate it. We believe that this is one reason why Python is so inherently 
readable.

Indentation must be consistent:
``` python
>>> if True:
...     print('True!')
...       print('Still true.')
  File "<stdin>", line 3
    print('Still true.')
    ^
    IndentationError: unexpected indent
```

Always use 4 spaces for one level of indentation.[^indentation]

[^indentation]: While this is not mandatory and enforced just do it :wink:.

### Comments

A comment starts with a "#":

``` python
>>> # a comment
... print('something')  # an inline comment
something
```

### Literals

#### Numeric literals

``` python
>>> 12345  # integer
12345
>>> 123.45  # floating-point number
123.45
>>> 1 + 3j  # complex number with real and imaginary part
(1+3j)
>>> 1.1 + 3.1J  # another complex number with real and imaginary part
(1.1+3.1j)
```

You can optionally separate big numbers for easier human reading:

``` python
>>> 1000_000_000  # not peanuts
1000000000
```


#### String literals

All these are valid string literals i.e. text or "sequences of characters":

``` python
>>> """text"""
'text'
>>> '''text'''
'text'
>>> "text"
'text'
>>> 'text'
'text'
```

You can use the different variations to avoid escaping. I.e. instead of
``` python
>>> 'Guido\'s time machine'
"Guido's time machine"
```

simply use

``` python
>>> "Guido's time machine"
"Guido's time machine"
>>> 
```

### Docstrings
A string literal as 1st statement in a module, a function or a class
definition will become the so-called "documentation string" of this object, 
which is accessible as the object's `__doc__` attribute:

A documented function:

``` python
>>> def noop(x):
...     """noop does nothing, really."""
...     return x
... 
>>> noop.__doc__
'noop does nothing, really.'
```

A documented class:

``` python
>>> class Animal:
...     """I'm a beast.
...     """
... 
>>> Animal.__doc__
"I'm a beast.\n    "
>>> 
```

A documented module:

``` python
$ cat mymodule.py 

"""This is my module's docstring.
"""

import os

print(os)
$ python3 -q
>>> import mymodule
<module 'os' from '/opt/subtools/current/lib/python3.6/os.py'>
>>> mymodule.__doc__
"This is my module's docstring.\n"
>>>
```

If for some reason you can't put this docstring as the first module statement
you may alternatively just set `__doc__` (as a module-global variable):

``` python
$ cat mymodule2.py 
import os  # for some reason we want to do this first

__doc__ = """This is my module's docstring.
"""

print(os)
$ python3 -q
>>> import mymodule2
<module 'os' from '/opt/subtools/current/lib/python3.6/os.py'>
>>> mymodule2.__doc__
"This is my module's docstring.\n"
>>> 
```

### Valid Identifiers & Reserved words

Identifiers are the names you are allowed to use e.g. for variable, function or
class names.

You can find out all there is to know about identifiers here:
https://docs.python.org/3/reference/lexical_analysis.html#identifiers

As a basic rule of thumb identifiers consist of letters A to Z (uppercase and
lowercase), the underscore _ and digits 0 to 9. Identifiers must not start with
a digit.[^identifiers]

[^identifiers]:
    Since Python 3.0 you can actually use other unicode characters in
    identifiers though in international codebases, the ASCII range characters
    prevail.

Identifiers are case-sensitive.

Reserved words are the language keywords which are not allowed for use as a 
name:
```
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### Source code encoding

Source code is text data. The binary representation of text data (e.g. when
stored in a file) is called an "encoding". It is important to know the encoding
of a text file since

 - different encodings are capable of representing different characters and
 - interpret the binary data as different characters (e.g. the ISO-8859-1
   encoding does not contain the € (EUR) sign (but the ¤ "general currency
   sign"), whereas the ISO-8859-15 encoding does; the byte `A4` is thus
   interpreted differently by these encodings)

A [special comment on the 1st or 2nd
line](https://docs.python.org/3/reference/lexical_analysis.html#encoding-declarations)

``` python
# -*- coding: <encoding-name> -*-
```

explicitly denotes the source code file encding.

The default Python source code encoding is
[UTF-8](https://en.wikipedia.org/wiki/UTF-8).

### Line continuation

Usually a statement ends with a newline. If long statements need to be
formatted to span multiple lines for readability the line continuation
character "\" can be used. This is called explicit line joining:

``` python
x = (operand1 + operand2) * \
    (operand1 - operand2)
```


As code enclosed in parentheses (...) (and brackets [...], braces {...} and
triple quotes) can span multiple line the line continuation character is often unnecessary:

``` python
"""A long docstring comment on this example.

Triple-quoted strings can span
multiple lines.
"""


if (condition_a
        and condition_b
        and condition_c):
    do_this()


german_month_names = [
    # comments are allowed
    'Januar', 'Februar', 'März',       # Q1
    'April', 'Mai', 'Juni',            # Q2
    'Juli', 'August', 'September',     # Q3
    'Oktober', 'November', 'Dezember'  # Q4
    ]

# dictionaries more often than not span lines
german_months = { 
    1: 'Januar',
    2: 'Februar',
    3: 'März',
    4: 'April',
    5: 'Mai',
    6: 'Juni',
    7: 'Juli',
    8: 'August',
    9: 'September',
    10: 'Oktober',
    11: 'November',
    12: 'Dezember'
    } 
```

This is called implicit line joining.

Tip: This and Python's *implicit string concatenation* can be used to format
lines:
``` python
>>> "12" "34"   "56"  # implicit string concatenation
'123456'
>>> hash("12"
...      "34"
...      "56")
239865887022063660
>>> hash("123456")
239865887022063660
```

This can be handy e.g. for formatting function calls with longer string
parameters (i.e. not so short as in this example...).


## Names and Objects

Python variables are names for objects. An object can have many names:

``` python
>>> x = 1
>>> y = x
>>> x
1
>>> y
1
>>> l1 = [1, 2, 3]
>>> l2 = l1
>>> l1
[1, 2, 3]
>>> l2
[1, 2, 3]
```

But it is still the same object:

``` python
>>> x is y  # is checks for object identity
True
>>> l1 is l2
True
>>> id(x), id(y)  # id() returns an object's unique id
(140700697906560, 140700697906560)
>>> id(l1), id(l2)
(140700698907784, 140700698907784)
```

Compare that to the meaning of variables in other languages, e.g. C.

In C (or C++) a variable is basically the in-program name for a "memory cell"
(a memory location that can hold a value of the type declared for that variable
). Thus, assignment in C/C++ means writing a value of the proper type into that
"memory cell".

Whereas a variable in Python is rather one "label" (of potentially many) for an
object in a sense more analogous to a C++ reference or a C pointer: a name for
an object.

Consequently, assignment in Python means "pinning" a new name to an object; it 
*never* copies data.[^c-assignment]

[^c-assignment]: Whereas in C/C++ assignment usually copies data.

Deleting a name doesn't affect object existence:
``` python
>>> del x
>>> y
1
```
(as long as there is still a name *referencing* that object)

Further reading: A great in-depth explanation can be found
[here](https://nedbatchelder.com/text/names1.html).


## Style guide

Python has a widely accepted
[style guide](https://www.python.org/dev/peps/pep-0008/). Follow it.

## Be pythonic
Python programmers often strive to write code that is said to be "pythonic",
which means it has a certain quality of beauty (as in being working, functional, elegant yet maintainable and readable).

While "pythonic" can understandably not be a very well-defined term the
[Zen of Python](https://www.python.org/dev/peps/pep-0020/) is a collection of
Python's language design guiding principles which can also be put to good use
in your quest to write "pythonic" code.
