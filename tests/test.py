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

raise Exception from ex

yield from

lambda x: x.test

def functionname
class Classname
def функция
class Класс

@test
def something()

@test.test
def something

test(arg1=1, arg2=int)

_long    = concretization_function_error(long)
_complex = concretization_function_error(complex)
_hex     = concretization_function_error(hex)
_oct     = concretization_function_error(oct)
test(hash=hash)
test(help=help)
test(int=int)
test(__import__)
test(__import__=int)
test(print)
test(memoryview)
test(type)
test(chr)
test(slice)


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

# builtin method
__new__ __init__ __del__ __repr__ __str__ __bytes__
__format__ __le__ __lt__ __eq__ __ne__ __gt__ __ge__
__hash__ __bool__ __getattr__ __setattr__ __delattr__
__dir__ __get__ __set__ __delete__ __set_name__ __slots__
__init_subclass__ __prepare__ __instancecheck__ __subclasscheck__
__class_getitem__ __call__ __len__ __length_hint__ __getitem__
__missing__ __setitem__ __delitem__ __iter__ __reversed__
__contains__ __add__ __sub__ __mul__ __matmul__ __truediv__
__floordiv__ __mod__ __divmod__ __pow__ __lshift__ __rshift__
__and__ __xor__ __or__ __radd__ __rsub__ __rmul__ __rmatmul__
__rtruediv__ __rfloordiv__ __rmod__ __rdivmod__ __rpow__ __rlshift__
__rrshift__ __rand__ __rxor__ __ror__ __iadd__ __isub__ __imul__
__imatmul__ __itruediv__ __ifloordiv__ __imod__ __ipow__ __ilshift__
__irshift__ __iand__ __ixor__ __ior__ __neg__ __pos__ __abs__ __invert__
__complex__ __int__ __float__ __index__ __round__ __trunc__ __floor__
__ceil__ __enter__ __exit__ __await__ __aiter__ __anext__ __aenter__
__aexit__

# Keywords: Python 2

exec
# wontfix
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

# slice & memoryview should be italic, type & chr should be non-italic
__import__ abs all any bin bool bytearray callable chr classmethod
compile complex delattr dict dir divmod enumerate eval filter float
format frozenset getattr globals hasattr hash help hex id input int
isinstance issubclass iter len list locals map max memoryview min next
object oct open ord pow property range repr reversed round set setattr
slice sorted staticmethod str sum super tuple type vars zip

__import__() abs() all() any() bin() bool() bytearray() callable() chr()
classmethod() compile() complex() delattr() dict() dir() divmod() enumerate()
eval() filter() float() format() frozenset() getattr() globals() hasattr()
hash() help() hex() id() input() int() isinstance() issubclass() iter() len()
list() locals() map() max() memoryview() min() next() object() oct() open()
ord() pow() property() range() repr() reversed() round() set() setattr()
slice() sorted() staticmethod() str() sum() super() tuple() type() vars() zip()

# Builtin functions: Python 2

apply() basestring() buffer() cmp() coerce() execfile() file() intern()
long() raw_input() reduce() reload() unichr() unicode() xrange() print()

# Builtin functions: Python 3

ascii() bytes() exec() print()

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
