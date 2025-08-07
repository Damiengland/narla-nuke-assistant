# nukescripts.widgetgroup.QSizePolicy
_class _nukescripts.widgetgroup.QSizePolicy(_self_)  None
_class _nukescripts.widgetgroup.QSizePolicy(_self_ , _horizontal : PySide6.QtWidgets.QSizePolicy.Policy_, _vertical : PySide6.QtWidgets.QSizePolicy.Policy_, _type : PySide6.QtWidgets.QSizePolicy.ControlType = Instance(PySide6.QtWidgets.QSizePolicy.ControlType.DefaultType)_)  None

Bases: `Shiboken.Object`
__init__(self) -> None __init__(self, horizontal: PySide6.QtWidgets.QSizePolicy.Policy, vertical: PySide6.QtWidgets.QSizePolicy.Policy, type: PySide6.QtWidgets.QSizePolicy.ControlType = Instance(PySide6.QtWidgets.QSizePolicy.ControlType.DefaultType)) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`controlType` ---
`expandingDirections`
`hasHeightForWidth`
`hasWidthForHeight`
`horizontalPolicy`
`horizontalStretch`
`retainSizeWhenHidden`
`setControlType`
`setHeightForWidth`
`setHorizontalPolicy`
`setHorizontalStretch`
`setRetainSizeWhenHidden`
`setVerticalPolicy`
`setVerticalStretch`
`setWidthForHeight`
`transpose`
`transposed`
`verticalPolicy`
`verticalStretch`

_class _ControlType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _Policy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _PolicyFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.IntFlag`
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
controlType(_self_)  PySide6.QtWidgets.QSizePolicy.ControlType

expandingDirections(_self_)

hasHeightForWidth(_self_)  bool

hasWidthForHeight(_self_)  bool

horizontalPolicy(_self_)  PySide6.QtWidgets.QSizePolicy.Policy

horizontalStretch(_self_)  int

retainSizeWhenHidden(_self_)  bool

setControlType(_self_ , _type : PySide6.QtWidgets.QSizePolicy.ControlType_)  None

setHeightForWidth(_self_ , _b : bool_)  None

setHorizontalPolicy(_self_ , _d : PySide6.QtWidgets.QSizePolicy.Policy_)  None

setHorizontalStretch(_self_ , _stretchFactor : int_)  None

setRetainSizeWhenHidden(_self_ , _retainSize : bool_)  None

setVerticalPolicy(_self_ , _d : PySide6.QtWidgets.QSizePolicy.Policy_)  None

setVerticalStretch(_self_ , _stretchFactor : int_)  None

setWidthForHeight(_self_ , _b : bool_)  None

transpose(_self_)  None

transposed(_self_)  PySide6.QtWidgets.QSizePolicy

verticalPolicy(_self_)  PySide6.QtWidgets.QSizePolicy.Policy

verticalStretch(_self_)  int