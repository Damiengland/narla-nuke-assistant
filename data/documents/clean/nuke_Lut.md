# nuke.Lut
_class _nuke.Lut

Bases: `object`
Methods
`fromByte`  Converts byte values in the range 0-255 to floating point.---
`fromByteSingle`  self.fromByte(float) -> float.
`fromFloat`  Convert a sequence of floating-point values to from_byte(x*255).
`isLinear`
`isZero`
`toByte`  Converts floating point values to byte values in the range 0-255.
`toByteSingle`  self.toByte(float) -> float.
`toFloat`  Convert a sequence of floating-point values to to_byte(x)/255.

fromByte(_float_)  float.

Converts byte values in the range 0-255 to floating point.
fromByteSingle()

self.fromByte(float) -> float.
Converts byte values in the range 0-255 to floating point.
fromFloat(_src_ , _alpha_)  float list.

Convert a sequence of floating-point values to from_byte(x*255). Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.
isLinear()  True if toByte(x) appears to return x*255, False otherwise.

isZero()  True if toByte(0) returns a value <= 0, False otherwise.

toByte(_float_)  float.

Converts floating point values to byte values in the range 0-255.
toByteSingle()

self.toByte(float) -> float.
Converts floating point values to byte values in the range 0-255.
toFloat(_src_ , _alpha_)  float list.

Convert a sequence of floating-point values to to_byte(x)/255. Alpha is an optional argument and if present unpremultiply by alpha, convert, and then multiply back.