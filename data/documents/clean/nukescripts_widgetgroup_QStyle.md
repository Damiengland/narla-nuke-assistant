# nukescripts.widgetgroup.QStyle
_class _nukescripts.widgetgroup.QStyle(_self_)  None

Bases: `PySide6.QtCore.QObject`
__init__(self) -> None
Initialize self. See help(type(self)) for accurate signature.
Methods
`alignedRect` ---
`blockSignals`
`childEvent`
`children`
`combinedLayoutSpacing`
`connect`
`connectNotify`
`customEvent`
`deleteLater`
`disconnect`
`disconnectNotify`
`drawComplexControl`
`drawControl`
`drawItemPixmap`
`drawItemText`
`drawPrimitive`
`dumpObjectInfo`
`dumpObjectTree`
`dynamicPropertyNames`
`emit`
`event`
`eventFilter`
`findChild`
`findChildren`
`generatedIconPixmap`
`hitTestComplexControl`
`inherits`
`installEventFilter`
`isQuickItemType`
`isSignalConnected`
`isWidgetType`
`isWindowType`
`itemPixmapRect`
`itemTextRect`
`killTimer`
`layoutSpacing`
`metaObject`
`moveToThread`
`name`
`objectName`
`parent`
`pixelMetric`
`polish`
`property`
`proxy`
`receivers`
`removeEventFilter`
`sender`
`senderSignalIndex`
`setObjectName`
`setParent`
`setProperty`
`signalsBlocked`
`sizeFromContents`
`sliderPositionFromValue`
`sliderValueFromPosition`
`standardIcon`
`standardPalette`
`standardPixmap`
`startTimer`
`styleHint`
`subControlRect`
`subElementRect`
`thread`
`timerEvent`
`tr`
`unpolish`
`visualAlignment`
`visualPos`
`visualRect`

Attributes
`destroyed` ---
`objectNameChanged`
`staticMetaObject`

_class _ComplexControl(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _ContentsType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _ControlElement(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _PixelMetric(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _PrimitiveElement(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _RequestSoftwareInputPanel(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _StandardPixmap(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _StateFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _StyleHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_class _SubControl(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _SubElement(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases:
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
_static _alignedRect(_direction :_, _alignment :_, _size : PySide6.QtCore.QSize_, _rectangle : PySide6.QtCore.QRect_)  PySide6.QtCore.QRect

blockSignals(_self_ , _b : bool_)  bool

childEvent(_self_ , _event : PySide6.QtCore.QChildEvent_)  None

children(_self_)  List[PySide6.QtCore.QObject]

combinedLayoutSpacing(_self_ , _controls1 :_, _controls2 :_, _orientation :_, _option : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_)  int

_static _connect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _arg__1 : bytes_, _arg__2 : PySide6.QtCore.QObject_, _arg__3 : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_self_ , _sender : PySide6.QtCore.QObject_, _signal : bytes_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _method : PySide6.QtCore.QMetaMethod_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection
_static _connect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_, _type : = Instance(Qt.AutoConnection)_)  PySide6.QtCore.QMetaObject.Connection

connectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

customEvent(_self_ , _event : PySide6.QtCore.QEvent_)  None

deleteLater(_self_)  None

_static _disconnect(_arg__1 : PySide6.QtCore.QMetaObject.Connection_)  bool
_static _disconnect(_arg__1 : PySide6.QtCore.QObject_, _arg__2 : bytes_, _arg__3 : Callable_)  bool
_static _disconnect(_self_ , _arg__1 : bytes_, _arg__2 : Callable_)  bool
_static _disconnect(_self_ , _receiver : PySide6.QtCore.QObject_, _member : Optional[bytes] = None_)  bool
_static _disconnect(_self_ , _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : PySide6.QtCore.QMetaMethod_, _receiver : PySide6.QtCore.QObject_, _member : PySide6.QtCore.QMetaMethod_)  bool
_static _disconnect(_sender : PySide6.QtCore.QObject_, _signal : bytes_, _receiver : PySide6.QtCore.QObject_, _member : bytes_)  bool

disconnectNotify(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  None

drawComplexControl(_self_ , _cc : PySide6.QtWidgets.QStyle.ComplexControl_, _opt : PySide6.QtWidgets.QStyleOptionComplex_, _p :_, _widget : Optional] = None_)  None

drawControl(_self_ , _element : PySide6.QtWidgets.QStyle.ControlElement_, _opt : PySide6.QtWidgets.QStyleOption_, _p :_, _widget : Optional] = None_)  None

drawItemPixmap(_self_ , _painter :_, _rect : PySide6.QtCore.QRect_, _alignment : int_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  None

drawItemText(_self_ , _painter :_, _rect : PySide6.QtCore.QRect_, _flags : int_, _pal : Union,, PySide6.QtGui.QColor]_, _enabled : bool_, _text : str_, _textRole : = Instance(PySide6.QtGui.QPalette.NoRole)_)  None

drawPrimitive(_self_ , _pe : PySide6.QtWidgets.QStyle.PrimitiveElement_, _opt : PySide6.QtWidgets.QStyleOption_, _p :_, _widget : Optional] = None_)  None

dumpObjectInfo(_self_)  None

dumpObjectTree(_self_)  None

dynamicPropertyNames(_self_)  List[PySide6.QtCore.QByteArray]

emit(_self_ , _arg__1 : bytes_, _* args: None_)  bool

event(_self_ , _event : PySide6.QtCore.QEvent_)  bool

eventFilter(_self_ , _watched : PySide6.QtCore.QObject_, _event : PySide6.QtCore.QEvent_)  bool

findChild(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)  object

findChildren(_self_ , _type : type_, _name : str = {}_, _options : = Instance(Qt.FindChildrenRecursively)_)
findChildren(_self_ , _type : type_, _pattern : Union[PySide6.QtCore.QRegularExpression, str]_, _options : = Instance(Qt.FindChildrenRecursively)_)

generatedIconPixmap(_self_ , _iconMode : PySide6.QtGui.QIcon.Mode_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_, _opt : PySide6.QtWidgets.QStyleOption_)  PySide6.QtGui.QPixmap

hitTestComplexControl(_self_ , _cc : PySide6.QtWidgets.QStyle.ComplexControl_, _opt : PySide6.QtWidgets.QStyleOptionComplex_, _pt : PySide6.QtCore.QPoint_, _widget : Optional] = None_)  PySide6.QtWidgets.QStyle.SubControl

inherits(_self_ , _classname : bytes_)  bool

installEventFilter(_self_ , _filterObj : PySide6.QtCore.QObject_)  None

isQuickItemType(_self_)  bool

isSignalConnected(_self_ , _signal : PySide6.QtCore.QMetaMethod_)  bool

isWidgetType(_self_)  bool

isWindowType(_self_)  bool

itemPixmapRect(_self_ , _r : PySide6.QtCore.QRect_, _flags : int_, _pixmap : Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage, str]_)  PySide6.QtCore.QRect

itemTextRect(_self_ , _fm : PySide6.QtGui.QFontMetrics_, _r : PySide6.QtCore.QRect_, _flags : int_, _enabled : bool_, _text : str_)  PySide6.QtCore.QRect

killTimer(_self_ , _id : int_)  None

layoutSpacing(_self_ , _control1 :_, _control2 :_, _orientation :_, _option : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_)  int

metaObject(_self_)  PySide6.QtCore.QMetaObject

moveToThread(_self_ , _thread : PySide6.QtCore.QThread_)  None

name(_self_)  str

objectName(_self_)  str

parent(_self_)  PySide6.QtCore.QObject

pixelMetric(_self_ , _metric : PySide6.QtWidgets.QStyle.PixelMetric_, _option : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_)  int

polish(_self_ , _application :_)  None
polish(_self_ , _palette : Union,, PySide6.QtGui.QColor]_)  None
polish(_self_ , _widget :_)  None

property(_self_ , _name : str_)  Any

proxy(_self_)  PySide6.QtWidgets.QStyle

receivers(_self_ , _signal : bytes_)  int

removeEventFilter(_self_ , _obj : PySide6.QtCore.QObject_)  None

sender(_self_)  PySide6.QtCore.QObject

senderSignalIndex(_self_)  int

setObjectName(_self_ , _name : str_)  None

setParent(_self_ , _parent : Optional[PySide6.QtCore.QObject]_)  None

setProperty(_self_ , _name : str_, _value : Any_)  bool

signalsBlocked(_self_)  bool

sizeFromContents(_self_ , _ct : PySide6.QtWidgets.QStyle.ContentsType_, _opt : PySide6.QtWidgets.QStyleOption_, _contentsSize : PySide6.QtCore.QSize_, _w : Optional] = None_)  PySide6.QtCore.QSize

_static _sliderPositionFromValue(_min : int_, _max : int_, _val : int_, _space : int_, _upsideDown : bool = False_)  int

_static _sliderValueFromPosition(_min : int_, _max : int_, _pos : int_, _space : int_, _upsideDown : bool = False_)  int

standardIcon(_self_ , _standardIcon : PySide6.QtWidgets.QStyle.StandardPixmap_, _option : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_)  PySide6.QtGui.QIcon

standardPalette(_self_)

standardPixmap(_self_ , _standardPixmap : PySide6.QtWidgets.QStyle.StandardPixmap_, _opt : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_)  PySide6.QtGui.QPixmap

startTimer(_self_ , _interval : int_, _timerType : = Instance(Qt.CoarseTimer)_)  int

styleHint(_self_ , _stylehint : PySide6.QtWidgets.QStyle.StyleHint_, _opt : Optional[PySide6.QtWidgets.QStyleOption] = None_, _widget : Optional] = None_, _returnData : Optional[PySide6.QtWidgets.QStyleHintReturn] = None_)  int

subControlRect(_self_ , _cc : PySide6.QtWidgets.QStyle.ComplexControl_, _opt : PySide6.QtWidgets.QStyleOptionComplex_, _sc : PySide6.QtWidgets.QStyle.SubControl_, _widget : Optional] = None_)  PySide6.QtCore.QRect

subElementRect(_self_ , _subElement : PySide6.QtWidgets.QStyle.SubElement_, _option : PySide6.QtWidgets.QStyleOption_, _widget : Optional] = None_)  PySide6.QtCore.QRect

thread(_self_)  PySide6.QtCore.QThread

timerEvent(_self_ , _event : PySide6.QtCore.QTimerEvent_)  None

tr(_self_ , _sourceText : str_, _disambiguation : Optional[str]_, _n : int = - 1_)  str

unpolish(_self_ , _application :_)  None
unpolish(_self_ , _widget :_)  None

_static _visualAlignment(_direction :_, _alignment :_)

_static _visualPos(_direction :_, _boundingRect : PySide6.QtCore.QRect_, _logicalPos : PySide6.QtCore.QPoint_)  PySide6.QtCore.QPoint

_static _visualRect(_direction :_, _boundingRect : PySide6.QtCore.QRect_, _logicalRect : PySide6.QtCore.QRect_)  PySide6.QtCore.QRect