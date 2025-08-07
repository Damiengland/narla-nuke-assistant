# nukescripts.scripteditorknob.Qt
_class _nukescripts.scripteditorknob.Qt

Bases: `Shiboken.Object`
Methods
`beginPropertyUpdateGroup` ---
`bin`
`bom`
`center`
`dec`
`endPropertyUpdateGroup`
`endl`
`fixed`
`flush`
`forcepoint`
`forcesign`
`hex`
`left`
`lowercasebase`
`lowercasedigits`
`noforcepoint`
`noforcesign`
`noshowbase`
`oct`
`reset`
`right`
`scientific`
`showbase`
`uppercasebase`
`uppercasedigits`
`ws`

_class _AlignmentFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _AnchorPoint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ApplicationAttribute(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ApplicationState(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _ArrowType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _AspectRatioMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _Axis(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _BGMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _BrushStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _CaseSensitivity(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _CheckState(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ChecksumType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ClipOperation(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ColorScheme(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ConnectionType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ContextMenuPolicy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _CoordinateSystem(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _Corner(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _CursorMoveStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _CursorShape(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _DateFormat(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _DayOfWeek(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _DockWidgetArea(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _DockWidgetAreaSizes(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _DropAction(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _Edge(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _EnterKeyType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _EventPriority(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _FillRule(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _FindChildOption(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _FocusPolicy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _FocusReason(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _GestureFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _GestureState(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _GestureType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _GlobalColor(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _HighDpiScaleFactorRoundingPolicy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _HitTestAccuracy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ImageConversionFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _InputMethodHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _InputMethodQuery(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _ItemDataRole(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _ItemFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _ItemSelectionMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ItemSelectionOperation(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _Key(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _KeyboardModifier(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _LayoutDirection(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _MaskMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _MatchFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _Modifier(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _MouseButton(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _MouseEventFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _MouseEventSource(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _NativeGestureType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _NavigationMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _Orientation(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _PenCapStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _PenJoinStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _PenStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _PermissionStatus(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ReturnByValueConstant(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ScreenOrientation(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _ScrollBarPolicy(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ScrollPhase(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ShortcutContext(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _SizeHint(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _SizeMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _SortOrder(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _SplitBehaviorFlags(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _TabFocusBehavior(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TextElideMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TextFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_class _TextFormat(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TextInteractionFlag(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _TileRule(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TimeSpec(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TimerType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ToolBarArea(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _ToolBarAreaSizes(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _ToolButtonStyle(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _TouchPointState(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _TransformationMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _UIEffect(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _WhiteSpaceMode(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _WidgetAttribute(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _WindowFrameSection(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _WindowModality(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Enum`
_class _WindowState(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

Bases: `enum.Flag`
_class _WindowType(_value_ , _names =None_, _*_ , _module =None_, _qualname =None_, _type =None_, _start =1_, _boundary =None_)

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
_static _beginPropertyUpdateGroup()  None

_static _bin(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _bom(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _center(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _dec(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _endPropertyUpdateGroup()  None

_static _endl(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _fixed(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _flush(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _forcepoint(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _forcesign(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _hex(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _left(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _lowercasebase(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _lowercasedigits(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _noforcepoint(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _noforcesign(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _noshowbase(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _oct(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _reset(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _right(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _scientific(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _showbase(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _uppercasebase(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _uppercasedigits(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream

_static _ws(_s : PySide6.QtCore.QTextStream_)  PySide6.QtCore.QTextStream