# nukescripts.toolbars.IntEnum
_class _nukescripts.toolbars.IntEnum(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `int`, `enum.ReprEnum`
Enum where members are also (and must be) ints
Methods
`as_integer_ratio`  Return integer ratio.---
`bit_count`  Number of ones in the binary representation of the absolute value of self.
`bit_length`  Number of bits necessary to represent self in binary.
`conjugate`  Returns self, the complex conjugate of any int.
`from_bytes`  Return the integer represented by the given array of bytes.
`to_bytes`  Return an array of bytes representing an integer.

Attributes
`denominator`  the denominator of a rational number in lowest terms---
`imag`  the imaginary part of a complex number
`numerator`  the numerator of a rational number in lowest terms
`real`  the real part of a complex number

__add__(_value_ , _/_)

Return self+value.
__mul__(_value_ , _/_)

Return self*value.
as_integer_ratio()

Return integer ratio.
Return a pair of integers, whose ratio is exactly equal to the original int and with a positive denominator.


    ```python
    >>> (10).as_integer_ratio()
    (10, 1)
    >>> (-10).as_integer_ratio()
    (-10, 1)
    >>> (0).as_integer_ratio()
    (0, 1)
    ```
bit_count()

Number of ones in the binary representation of the absolute value of self.
Also known as the population count.


    ```python
    >>> bin(13)
    '0b1101'
    >>> (13).bit_count()
    3
    ```
bit_length()

Number of bits necessary to represent self in binary.


    ```python
    >>> bin(37)
    '0b100101'
    >>> (37).bit_length()
    6
    ```
conjugate()

Returns self, the complex conjugate of any int.
denominator

the denominator of a rational number in lowest terms
from_bytes(_byteorder ='big'_, _*_ , _signed =False_)

Return the integer represented by the given array of bytes.
bytes

Holds the array of bytes to convert. The argument must either support the buffer protocol or be an iterable object producing bytes. Bytes and bytearray are examples of built-in objects that support the buffer protocol.
byteorder

The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use `sys.byteorder’ as the byte order value. Default is to use ‘big’.
signed

Indicates whether two’s complement is used to represent the integer.
imag

the imaginary part of a complex number
numerator

the numerator of a rational number in lowest terms
real

the real part of a complex number
to_bytes(_length =1_, _byteorder ='big'_, _*_ , _signed =False_)

Return an array of bytes representing an integer.
length

Length of bytes object to use. An OverflowError is raised if the integer is not representable with the given number of bytes. Default is length 1.
byteorder

The byte order used to represent the integer. If byteorder is ‘big’, the most significant byte is at the beginning of the byte array. If byteorder is ‘little’, the most significant byte is at the end of the byte array. To request the native byte order of the host system, use `sys.byteorder’ as the byte order value. Default is to use ‘big’.
signed

Determines whether two’s complement is used to represent the integer. If signed is False and a negative integer is given, an OverflowError is raised.