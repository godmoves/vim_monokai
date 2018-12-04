#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Above the run-comment and file encoding comment.

# Comments.

# TODO FIXME XXX

# Keywords.

with break continue del return pass raise global assert lambda yield
for while if elif else import as try except finally

from test import var as name
from . import test
from test.test import test
from .test import test
# error
from test.

raise Exception from ex

yield from

lambda x: x.test
lambda x: x.test()

def functionname
class Classname
def функция
class Класс

@test
def something()

@test.test
def something

# error
@test..test
def something

@.test
def something

@test.test()
def something

test(arg1=1, arg2=2)

test.__init__

def test(arg1=1, arg2=True, __init__)

class Model(torch.nn.Module):

    def __init__(self):
        """
        In the constructor we instantiate two nn.Linear module
        """
        super(Model, self).__init__()
        self.linear = torch.nn.Linear(1, 1)  # One in and one out

    def forward(self, x):
        """
        In the forward function we accept a Variable of input data and we must return
        a Variable of output data. We can use Modules defined in the constructor as
        well as arbitrary operators on Variables.
        """
        y_pred = self.linear(x)
        return y_pred

    def __str__(self):
        return "test"

    def __repr__(slef):
        return

    def __new__
    def __init__
    def __del__
    def __repr__
    def __str__
    def __bytes__
    def __format__
    def __le__
    def __lt__
    def __eq__
    def __ne__
    def __gt__
    def __ge__
    def __hash__
    def __bool__
    def __getattr__
    def __setattr__
    def __delattr__
    def __dir__
    def __get__
    def __set__
    def __delete__
    def __set_name__
    def __slots__
    def __init_subclass__
    def __prepare__
    def __instancecheck__
    def __subclasscheck__
    def __class_getitem__
    def __call__
    def __len__
    def __length_hint__
    def __getitem__
    def __missing__
    def __setitem__
    def __delitem__
    def __iter__
    def __reversed__
    def __contains__
    def __add__
    def __sub__
    def __mul__
    def __matmul__
    def __truediv__
    def __floordiv__
    def __mod__
    def __divmod__
    def __pow__
    def __lshift__
    def __rshift__
    def __and__
    def __xor__
    def __or__
    def __radd__
    def __rsub__
    def __rmul__
    def __rmatmul__
    def __rtruediv__
    def __rfloordiv__
    def __rmod__
    def __rdivmod__
    def __rpow__
    def __rlshift__
    def __rrshift__
    def __rand__
    def __rxor__
    def __ror__
    def __iadd__
    def __isub__
    def __imul__
    def __imatmul__
    def __itruediv__
    def __ifloordiv__
    def __imod__
    def __ipow__
    def __ilshift__
    def __irshift__
    def __iand__
    def __ixor__
    def __ior__
    def __neg__
    def __pos__
    def __abs__
    def __invert__
    def __complex__
    def __int__
    def __float__
    def __index__
    def __round__
    def __trunc__
    def __floor__
    def __ceil__
    def __enter__
    def __exit__
    def __await__
    def __aiter__
    def __anext__
    def __aenter__
    def __aexit__
    def send
    def throw
    def close

# Keywords: Python 2

exec
print

# Keywords: Python 3

await
async def Test
async with
async for

# Builtin objects.

True False Ellipsis None NotImplemented

# Bultin types

bool bytearray dict float frozenset int list object set str tuple

# Builtin functions
__import__
abs
all
any
bin
bool
bytearray
callable
chr
classmethod
compile
complex
delattr
dict
dir
divmod
enumerate
eval
filter
float
format
frozenset
getattr
globals
hasattr
hash
help
hex
id
input
int
isinstance
issubclass
iter
len
list
locals
map
max
memoryview
min
next
object
oct
open
ord
pow
property
range
repr
reversed
round
set
setattr
slice
sorted
staticmethod
str
sum
super
tuple
type
vars
zip

__import__()
abs()
all()
any()
bin()
bool()
bytearray()
callable()
chr()
classmethod()
compile()
complex()
delattr()
dict()
dir()
divmod()
enumerate()
eval()
filter()
float()
format()
frozenset()
getattr()
globals()
hasattr()
hash()
help()
hex()
id()
input()
int()
isinstance()
issubclass()
iter()
len()
list()
locals()
map()
max()
memoryview()
min()
next()
object()
oct()
open()
ord()
pow()
property()
range()
repr()
reversed()
round()
set()
setattr()
slice()
sorted()
staticmethod()
str()
sum()
super()
tuple()
type()
vars()
zip()

# Builtin functions: Python 2

apply()
basestring()
buffer()
cmp()
coerce()
execfile()
file()
intern()
long()
raw_input()
reduce()
reload()
unichr()
unicode()
xrange()

print()

# Builtin functions: Python 3

ascii()
bytes()
exec()
print()

# Builtin exceptions and warnings.

BaseException Exception StandardError ArithmeticError LookupError
EnvironmentError

AssertionError AttributeError EOFError FloatingPointError GeneratorExit IOError
ImportError IndexError KeyError KeyboardInterrupt MemoryError NameError
NotImplementedError OSError OverflowError ReferenceError RuntimeError
StopIteration SyntaxError IndentationError TabError SystemError SystemExit
TypeError UnboundLocalError UnicodeError UnicodeEncodeError UnicodeDecodeError
UnicodeTranslateError ValueError WindowsError ZeroDivisionError

Warning UserWarning DeprecationWarning PendingDeprecationWarning SyntaxWarning
RuntimeWarning FutureWarning ImportWarning UnicodeWarning

# Decorators.

@ decoratorname
@ object.__init__(arg1, arg2)
@ декоратор
@ декоратор.décorateur

# Operators

and or in is not

- + * ** **- **+ **~ @ / // %
& | ^ ~ << >>
< <= == != >= >

= =- =+ =~
-= += *= **= @= /= //= %=
&= |= ^= ~= <<= >>=

->

# Erroneous operators

$ ?
===
-- ++ *** @@ /// %%
&& || ^^ ~~ <<< >>>
<== !== !!= >==
%- +- -+

# Numbers

0 1 2 9 10 0x1f .3 12.34 0j 124j 34.2E-3 0b10 0o77 1023434 0x0
1_1 1_1.2_2 1_2j 0x_1f 0x1_f 34_56e-3 34_56e+3_1 0o7_7 1.23j 3e4j
.3j 23j 23_4j

# Erroneous numbers

077 100L 0xfffffffL 0L 08 0xk 0x 0b102 0o78 0o123LaB
0_ 0_1 0_x1f 0x1f_ 0_b77 0b77_ .2_ 1_j

# Strings

" test " ' test '
"test\
test"
'test\
test'

"""
  test
\""""
'''
  test
\''''

test = """ this is
a test string """

" \a\b\c\"\'\n\r \x34\077 \08 \xag"
r" \" \' "

"testтест"

test = b"test"
test = \
    b"test"

b"test"

b"test\r\n\xffff"

b"тестtest"

br"test"

br"\a\b\n\r"

ur""
rr""
uu""
ru""


# Formattings

" %f "
b" %f "

"{0.name!r:b} {0[n]} {name!s:  } {{test}} {{}} {} {.__len__:s}"
b"{0.name!r:b} {0[n]} {name!s:  } {{test}} {{}} {} {.__len__:s}"

"${test} ${test ${test}aname $$$ $test+nope"
b"${test} ${test ${test}aname $$$ $test+nope"

f"{var}...{arr[123]} normal {var['{'] // 0xff} \"xzcb\" 'xzcb' {var['}'] + 1} text"
f"{expr1 if True or False else expr2} wow {','.join(c.lower() for c in 'asdf')}"
f"hello {expr:.2f} yes {(lambda: 0b1)():#03x} lol {var!r}"
f'brackets: {{ 1 + 2 }} and {{{{ 3 + 4 }}}}'
fr'this {that}'

# Doctests.

"""
    Test:
    >>> a = 5
    >>> a
    5

    Test
"""

'''
    Test:
    >>> a = 5
    >>> a
    5

    Test
'''

# Erroneous variable names

6xav


# Indentation errors.

    	    break

# Trailing space errors.

    	
    break	    
"""  	
   	 
    test    	
"""  	
