# nuke.nukemath.Quaternion
_class _nuke.nukemath.Quaternion(_* args_, _** kwargs_)

Bases: `pybind11_builtins.pybind11_object`
Overloaded function.
  1. __init__(self: nukemath.Quaternion, arg0: float, arg1: float, arg2: float, arg3: float) -> None
  2. __init__(self: nukemath.Quaternion, arg0: float, arg1: nukemath.Vector3) -> None
  3. __init__(self: nukemath.Quaternion, arg0: nukemath.Quaternion) -> None
  4. __init__(self: nukemath.Quaternion, arg0: nukemath.Matrix4) -> None
  5. __init__(self: nukemath.Quaternion, arg0: nukemath.Vector3, arg1: nukemath.Vector3) -> None
Methods
`addInverse` ---
`conjugate`
`length`
`lengthSquared`
`magnitude`
`matrix`
`multInverse`
`set`
`slerp`

Attributes
`s` ---
`vx`
`vy`
`vz`

__add__(_self : nukemath.Quaternion_, _arg0 : nukemath.Quaternion_)  nukemath.Quaternion

__mul__(_* args_, _** kwargs_)

Overloaded function.
  1. __mul__(self: nukemath.Quaternion, arg0: float) -> nukemath.Quaternion
  2. __mul__(self: nukemath.Quaternion, arg0: nukemath.Quaternion) -> nukemath.Quaternion
addInverse(_self : nukemath.Quaternion_)  nukemath.Quaternion

conjugate(_self : nukemath.Quaternion_)  nukemath.Quaternion

length(_self : nukemath.Quaternion_)  float

lengthSquared(_self : nukemath.Quaternion_)  float

magnitude(_self : nukemath.Quaternion_)  float

matrix(_self : nukemath.Quaternion_)

multInverse(_self : nukemath.Quaternion_)  nukemath.Quaternion

set(_self : nukemath.Quaternion_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_)  None

slerp(_self : nukemath.Quaternion_, _arg0 : nukemath.Quaternion_, _arg1 : float_)  nukemath.Quaternion