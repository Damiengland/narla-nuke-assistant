# nuke.nukemath.Matrix3
_class _nuke.nukemath.Matrix3(_* args_, _** kwargs_)

Bases: `pybind11_builtins.pybind11_object`
Overloaded function.
  1. __init__(self: nukemath.Matrix3) -> None
  2. __init__(self: nukemath.Matrix3, arg0: float, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float, arg7: float, arg8: float) -> None
  3. __init__(self: nukemath.Matrix3, arg0: nukemath.Matrix3) -> None
Methods
`determinant` ---
`identity`
`inverse`
`makeIdentity`
`rotate`  Overloaded function.
`rotateX`
`rotateY`
`rotateZ`
`rotation`  Overloaded function.
`rotationX`
`rotationY`
`rotationZ`
`scale`  Overloaded function.
`scaling`  Overloaded function.
`set`
`skew`
`transform`

__add__(_self : nukemath.Matrix3_, _arg0 : nukemath.Matrix3_)  nukemath.Matrix3

__mul__(_* args_, _** kwargs_)

Overloaded function.
  1. __mul__(self: nukemath.Matrix3, arg0: float) -> nukemath.Matrix3
  2. __mul__(self: nukemath.Matrix3, arg0: nukemath.Vector3) -> nukemath.Vector3
  3. __mul__(self: nukemath.Matrix3, arg0: nukemath.Matrix3) -> nukemath.Matrix3
determinant(_self : nukemath.Matrix3_)  float

identity()  nukemath.Matrix3

inverse(_self : nukemath.Matrix3_)  nukemath.Matrix3

makeIdentity(_self : nukemath.Matrix3_)  None

rotate(_* args_, _** kwargs_)

Overloaded function.
  1. rotate(self: nukemath.Matrix3, arg0: float, arg1: float, arg2: float, arg3: float) -> None
  2. rotate(self: nukemath.Matrix3, arg0: float, arg1: nukemath.Vector3) -> None
rotateX(_self : nukemath.Matrix3_, _arg0 : float_)  None

rotateY(_self : nukemath.Matrix3_, _arg0 : float_)  None

rotateZ(_self : nukemath.Matrix3_, _arg0 : float_)  None

rotation(_* args_, _** kwargs_)

Overloaded function.
  1. rotation(self: nukemath.Matrix3, arg0: float, arg1: float, arg2: float, arg3: float) -> None
  2. rotation(self: nukemath.Matrix3, arg0: float, arg1: nukemath.Vector3) -> None
rotationX(_self : nukemath.Matrix3_, _arg0 : float_)  None

rotationY(_self : nukemath.Matrix3_, _arg0 : float_)  None

rotationZ(_self : nukemath.Matrix3_, _arg0 : float_)  None

scale(_* args_, _** kwargs_)

Overloaded function.
  1. scale(self: nukemath.Matrix3, arg0: float) -> None
  2. scale(self: nukemath.Matrix3, arg0: float, arg1: float, arg2: float) -> None
scaling(_* args_, _** kwargs_)

Overloaded function.
  1. scaling(self: nukemath.Matrix3, arg0: float) -> None
  2. scaling(self: nukemath.Matrix3, arg0: float, arg1: float, arg2: float) -> None
  3. scaling(self: nukemath.Matrix3, arg0: nukemath.Vector3) -> None
set(_self : nukemath.Matrix3_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_, _arg4 : float_, _arg5 : float_, _arg6 : float_, _arg7 : float_, _arg8 : float_)  None

skew(_self : nukemath.Matrix3_, _arg0 : float_)  None

transform(_self : nukemath.Matrix3_, _arg0 :_)