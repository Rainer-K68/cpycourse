# Context is Key: Context Managers

Certain Python objects that follow the so-called "context manager protocol" can
be used with Python's `with` statement:

``` python
>>> with open("myfile.txt", "w") as myfile:
...     myfile.write("Hello!")
... 
6
>>> with open("myfile.txt", "r") as myfile:
...     myfile.readlines()
... 
['Hello!']
>>> 
>> myfile
<_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
>>> myfile.closed
True
>>> 
```

A context manager object gets *entered* through the `with` statement and
*exits* when the `with` code block ends.

This is a very useful mechanism for closing resources (that shouldn't be left
open). Prominent examples for such resources are

 - files
 - network connections
 - database connections

Context managers can be implemented by providing an object with the context
manager protocol methods:

``` python
class MyContextManager:
    def __enter__(self):
        # resource acquisition goes here
        # ...

    def __exit__(self, exc_type, exc_value, traceback):
        # resource closing/cleanup goes here
        # ...

```

Useful tools for easily creating context managers are in the
[stdlib `contextlib`](https://docs.python.org/3/library/contextlib.html).
