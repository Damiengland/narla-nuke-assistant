# nuke.nukemath.Vector3
_class _nuke.nukemath.Vector3(_* args_, _** kwargs_)

Bases: `pybind11_builtins.pybind11_object`
Overloaded function.
  1. __init__(self: nukemath.Vector3) -> None
  2. __init__(self: nukemath.Vector3, arg0: float, arg1: float, arg2: float) -> None
  3. __init__(self: nukemath.Vector3, arg0: nukemath.Vector3) -> None
Methods
`cross` ---
`distanceBetween`
`distanceFromPlane`
`distanceSquared`
`dot`
`fast_normalize`
`length`
`lengthSquared`
`maximum`
`minimum`
`negate`
`normalize`
`reflect`
`set`

Attributes
`x` ---
`y`
`z`

__add__(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  nukemath.Vector3

__mul__(_* args_, _** kwargs_)

Overloaded function.
  1. __mul__(self: nukemath.Vector3, arg0: float) -> nukemath.Vector3
  2. __mul__(self: nukemath.Vector3, arg0: nukemath.Vector3) -> nukemath.Vector3
  3. __mul__(self: nukemath.Vector3, arg0: float) -> nukemath.Vector3
cross(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  nukemath.Vector3

distanceBetween(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  float

distanceFromPlane(_self : nukemath.Vector3_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_)  float

distanceSquared(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  float

dot(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  float

fast_normalize(_self : nukemath.Vector3_)  float

length(_self : nukemath.Vector3_)  float

lengthSquared(_self : nukemath.Vector3_)  float

maximum(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  nukemath.Vector3

minimum(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  nukemath.Vector3

negate(_self : nukemath.Vector3_)  None

normalize(_self : nukemath.Vector3_)  float

reflect(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_)  nukemath.Vector3

set(_self : nukemath.Vector3_, _arg0 : float_, _arg1 : float_, _arg2 : float_)  None