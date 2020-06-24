# Functions

Providing repeating tasks or calculation in functions is an effective way of code-reuse ("write-once-use-many").
This is a brief introduction of Python functions, not covering all possible variations of function-definitions. More on this can be found in the official Python docs <https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions>.
Function itself are Python objects, as such they can e.g be assigned, passed as parameters to or returned from functions, more on that later.

## Function Definition ##

In Python user-defined functions are defined using the `def`-statement. A function definition is made up
a function-header (defining the function-name and the call-signature)  and a function-body (the implementation of the task/calculation as a sequence of code statements ending up with an optional return-statement).


Python allows different ways of function-definitions as described in the following subsections.

***Note:***
Often the term "argument" and "parameter" are used interchangeable, but this is a little bit diffuse. More precise are the terms "actual parameter" for "argument" for variables or values in function-calls and "formal parameter" for parameter-names in function-definitions. Here the term "argument" is used for the variable/values in function-calls, the term "parameter is used for parameter-names in function-definitions. 


## Function with simple parameters ##

***function-definition example***

``` python
>>> def increment(a,stride):  # function-header
...    ''' Purpose: Increment a with stride '''   # optional doc-string
...    # function-body
...    c = a + stride
...    return c
...
>>>
```

A function-call is done simply writing the function-name following a `tuple` of positional call-arguments

***function-call example***

``` python
>>> result = increment(1,2)
>>> print(result)
3
>>>
```

***Note:***
The number of parameters equal the number of call-arguments. 
Also the order of the call-parameter must match the order of function-parameters: During the function-call the 1.st call-argument is mapped to the 1.st function-parameter, the 2.nd call-argument is mapped to the 2.nd function-parameter, i.e a position-based mapping from the call-arguments to the function-parameters (call-arguments here are ***positional arguments***)

Let's give it a try

--8<--
lessons/palindroms.md
--8<--

## Function with optional parameters ##

Optional parameters are parameters with assigned default values in the function-definition. Those optional parameters may be omitted during the function-call.

***function-definition example - utilizing default-paramater value***

``` python
>>> def increment(a,stride=1):  # function-header with default-argument
...    ''' Purpose: Increment a with stride '''   # optional doc-string
...    # function-body
...    c = a + stride
...    return c
...
>>>
```

***function-call example (1) - omitting optional parameter***
  
``` python  
>>> result = increment(1)
>>> print(result)
2
>>> 
```
  
***function-call example (2) - overwriting default-value of optional-parameter***
 
``` python
>>> result = increment(1,5)
>>> print(result)
6
>>> 
```
  
***Note 1:***
Function-call can be made using only with arguments for parameters, where no default-agument are defined
  
***Note 2:***
Optional-parameters must be defined at the end of the function-parameter-list. Otherhwise a SyntaxError is raised, e.g.

``` python
>>> def a(a,b=1,c):
...     return (a+b+c)
... 
  File "<stdin>", line 1
SyntaxError: non-default argument follows default argument
```
  
  
## Function with variable parameter list (variadic parameter) ##

A function can be defined having a variable-parameter-list. This is specified in preceding the last parameter with an asterisk-character `*` in the function definition.

***function-definition***

```python
>>> def print_info(header,footer,*args):    # 2 normal parameter & variable-length-parameter
...     print(header)
...     for elem in args: print(elem)
...     print(footer)
... 
>>>
```


***varargs-function-call (1)***

```python
>>> print_info('-->', '<--', 'Hello', 'World')  # last 2 arguments are mapped as a tuple into the *-parameter
-->
Hello
World
<--
>>>
```
    
***varargs-function-call (2)***

``` python
>>> print_info('-->', '<--', 'Tic', 'Tac', 'Toe')  # last 3 arguments are mapped as a tuple into the *-parameter
-->
Tic
Tac
Toe
<--
>>>
```


## Keyword Arguments ##

In the above sections the functions are called with ***positional arguments***, see ***Note*** above.
In addition function can also be called using named arguments (keyword arguments).

To demonstrate this, we use the `increment`-function-definition from above.

***function-definition ***
  
``` python
>>> def increment(a,stride=1):  # function-header
...    ''' Purpose: Increment a with stride '''   # optional doc-string
...    # function-body
...    c = a + stride
...    return c
...
>>>
```

***function-call using keyword parameter (1)***

``` python
>>> increment(a=1)
2
>>>
```

***function-call using keyword parameter (2)***

``` python
>>> increment(stride=3, a=1)
4
>>>
```

***Note***
Using keyword-arguments the position of the call-argument doesn't matter


## Function with additional keyword parameter ##

Additionally Python allows function-definitions with arbitray additional keyword-paramaters. This is specified in preceeding the last parmeter with double-asterisk character `**`. Additional kewyword-arguments are mapped during the function-call into a dictionary for the keyword-parameter of the function definition

***function-definition with keyword-parameters***
  
``` python  
>>> def print_info(header,footer,*args, **kwargs):
...     print(header)
...     for elem in args: print(elem)
...     for elem in kwargs.keys(): print('%s: %s' % (elem, kwargs[elem]))
...     print(footer)
... 
>>> 
``` 

***function-call***

``` python
>>> print_info('-->', '<--', 'Madrid', 'Berlin', 'Paris', capitols_of='European Countries', belonging_to='EU')
-->
Madrid
Berlin
Paris
capitols_of: European Countries
belonging_to: EU
<--
>>>
```

## Function Return Value ##

Python allows the return of mutiple values.

``` python
>>> def divide(number,div):
...     '''Division returning truncated division and modulo'''
...     d = number // div
...     m = number % div
...     return d,m
... 
>>> d, m = divide(9,4)
>>> d
2
>>> m
1
>>>
```

## Inner functions

Functions can be defined at every place, at module-level, inside classes (methods), but also inside functions.

***function definition***

``` python
>>> def outer_func(inner_func):
...     ''' function which defines inner functions'''
...     def x():
...         print(x.__name__)
...     def y():
...         print(y.__name__)
...     # return an inner function, simply by its name
...     if inner_func == 1:
...         return x
...     else:
...         return y
... 
>>>
```

***function-call***

``` python
>>> a_func = outer_func(1)    # assign a function
>>> a_func()                  # call the function
x
>>> b_func = outer_func(2)    # assign a function
>>> b_func()                  # call the function
y
>>>
```

***Note:***
As can be seen, functions are like ordinary Python objects that can be returned and assigned.

## Functions Annotations

[Function Annotations](https://docs.python.org/3/tutorial/controlflow.html#function-annotations) allow programmers to associate meta-information to a function-header. One kind of interesting mata-information are so called 'type-hints', which can provide 'type-information' about the function-paramertes and return-value.

Function annotations are stored in the `__annotations__` attribute of a function object.

***Function Annotation example***

``` python
>>> def concatenate(string_1: str, string_2: str) -> str:
...     return string_1 + string_2
... 
>>> concate('foo', 'bar')
'foobar'
>>> concate.__annotations__
{'string_1': <class 'str'>, 'string_2': <class 'str'>, 'return': <class 'str'>}
>>> 
```

For a more detailed inforamtions please refer to [PEP 3107 -- Function Annotations](https://www.python.org/dev/peps/pep-3107/) and [PEP 484 -- Type Hints ](https://www.python.org/dev/peps/pep-0484/)

***Note 1:***
Function annotations are optional, they are just informations. They are neither evaluated nor their compliance is enforced by the interpreter itself. It's provided in the language, helping other libraries do some type-checking.

***Note 2:***
'Type Hints'-support is implemented in the Python standard library [`typing`](https://docs.python.org/3/library/typing.html).

***Note 3:***
PEP - Python Enhancement Proposal - is the official process of suggesting enhancements to the Python language, please read [PEP 001 -- PEP Purpose and Guidelines](https://www.python.org/dev/peps/pep-0001/).


## Pythons Function Call Semantics ##

Function-call arguments are suggested in PEP variables in the scope of the caller.

Traditional function call semantics are:

1. call-by-value: 
  - the value of the argument-variable is copied to the call-parameter of the function
  - changing the value inside the function doesn't effect the caller
2. call-by-reference: 
  - a reference of the caller's variable is passed to the call-parameter of the function
  - as a consequence, changes to variable inside the function will affect the callers variable (side-effect from callee back to the caller) 
  - alongside the function return value, this provides additional communication-channels between caller and callee

Python function call semantics instead are controlled by the mutability/immutability of the Python objects of the caller's function-call arguments.

1. argument variable refering an immutable object: Will work without side-effects to the callee even, when the functions is changing the value, this is due to the copy-on-write behaviour 
2. argument variable refering a mutable object may have side-effects to the callee, when the variable is changed inside the function

***function-call with immutable call-argument***

``` python
>>> a = 1
>>> id(1)             # (1)
139752035048832
>>> def increment(a): 
...     print(id(a))  # (2) refers to the same object as the callers variable (1)
...     a += 1        # (3) copy-on-write creates new object
...     print(id(a))  # (4) new object dur to (3)
...     return a
... 
>>> b = increment(a)
139752035048832
139752035048864
>>> a
1    
>>> id(a)            # (4) refers to the same object as in (1)
139752035048832
>>>
```

***Note:***
Immutable objects of the caller are not effected by changes in the callee
  
***function-call with mmutable call-argument***

``` python
>>> d1 = {'a':1, 'b':2}
>>> id(d1)           # (1)
139752035393824
>>> def change_callee_object(d):
...     print(id(d))  # (2) refers to the same object as the callers variable (1)
...     for elem in d.keys(): d[elem] += 1  # (3) no copy is made, changes apply to origin object
...     print(id(d))  # (4) refers to the origin object (1), (2)
...     return d
... 
>>> d2 = change_callee_object(d1)
139752035393824
139752035393824
>>> d1 # site-effect caused by function-call with mutable argument
{'a': 2, 'b': 3}
>>> id(d1)
139752035393824
>>> d2
{'a': 2, 'b': 3}
>>> id(d2)
139752035393824
>>> 
```

***Note:***
Function-calls with mutable objects may have site-effect to the callee
  

