# nuke.nukemath.Matrix4
_class _nuke.nukemath.Matrix4(_* args_, _** kwargs_)

Bases: `pybind11_builtins.pybind11_object`
Overloaded function.
  1. __init__(self: nukemath.Matrix4) -> None
  2. __init__(self: nukemath.Matrix4, arg0: nukemath.Matrix4) -> None
Methods
`determinant` ---
`identity`
`inverse`
`makeIdentity`
`mapQuadToUnitSquare`
`mapUnitSquareToQuad`
`ntransform`
`projection`
`rotate`  Overloaded function.
`rotateX`
`rotateY`
`rotateZ`
`rotation`  Overloaded function.
`rotationOnly`
`rotationX`
`rotationY`
`rotationZ`
`rotationsXYZ`
`rotationsXZY`
`rotationsYXZ`
`rotationsYZX`
`rotationsZXY`
`rotationsZYX`
`scale`  Overloaded function.
`scaleAndRotationOnly`
`scaleOnly`
`scaling`  Overloaded function.
`skew`
`skewXY`
`transform`  Overloaded function.
`translate`  Overloaded function.
`translation`  Overloaded function.
`translationOnly`
`transpose`
`vtransform`
`xAxis`
`yAxis`
`zAxis`

__add__(_self : nukemath.Matrix4_, _arg0 : nukemath.Matrix4_)  nukemath.Matrix4

__mul__(_* args_, _** kwargs_)

Overloaded function.
  1. __mul__(self: nukemath.Matrix4, arg0: float) -> nukemath.Matrix4
  2. __mul__(self: nukemath.Matrix4, arg0: nukemath.Vector4) -> nukemath.Vector4
  3. __mul__(self: nukemath.Matrix4, arg0: nukemath.Matrix4) -> nukemath.Matrix4
determinant(_self : nukemath.Matrix4_)  float

identity()  nukemath.Matrix4

inverse(_self : nukemath.Matrix4_)  nukemath.Matrix4

makeIdentity(_self : nukemath.Matrix4_)  None

mapQuadToUnitSquare(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_, _arg4 : float_, _arg5 : float_, _arg6 : float_, _arg7 : float_)  None

mapUnitSquareToQuad(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_, _arg4 : float_, _arg5 : float_, _arg6 : float_, _arg7 : float_)  None

ntransform(_self : nukemath.Matrix4_, _arg0 :_)

projection(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : bool_)  None

rotate(_* args_, _** kwargs_)

Overloaded function.
  1. rotate(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
  2. rotate(self: nukemath.Matrix4, arg0: float, arg1: nukemath.Vector3) -> None
rotateX(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotateY(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotateZ(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotation(_* args_, _** kwargs_)

Overloaded function.
  1. rotation(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float, arg3: float) -> None
  2. rotation(self: nukemath.Matrix4, arg0: float, arg1: nukemath.Vector3) -> None
rotationOnly(_self : nukemath.Matrix4_)  None

rotationX(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotationY(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotationZ(_self : nukemath.Matrix4_, _arg0 : float_)  None

rotationsXYZ(_self : nukemath.Matrix4_)  tuple

rotationsXZY(_self : nukemath.Matrix4_)  tuple

rotationsYXZ(_self : nukemath.Matrix4_)  tuple

rotationsYZX(_self : nukemath.Matrix4_)  tuple

rotationsZXY(_self : nukemath.Matrix4_)  tuple

rotationsZYX(_self : nukemath.Matrix4_)  tuple

scale(_* args_, _** kwargs_)

Overloaded function.
  1. scale(self: nukemath.Matrix4, arg0: float) -> None
  2. scale(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None
scaleAndRotationOnly(_self : nukemath.Matrix4_)  None

scaleOnly(_self : nukemath.Matrix4_)  None

scaling(_* args_, _** kwargs_)

Overloaded function.
  1. scaling(self: nukemath.Matrix4, arg0: float) -> None
  2. scaling(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None
  3. scaling(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None
skew(_self : nukemath.Matrix4_, _arg0 : float_)  None

skewXY(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_)  None

transform(_* args_, _** kwargs_)

Overloaded function.
  1. transform(self: nukemath.Matrix4, arg0: nukemath.Vector4) -> nukemath.Vector4
  2. transform(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> nukemath.Vector3
translate(_* args_, _** kwargs_)

Overloaded function.
  1. translate(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None
  2. translate(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None
translation(_* args_, _** kwargs_)

Overloaded function.
  1. translation(self: nukemath.Matrix4) -> tuple
  2. translation(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None
  3. translation(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None
translationOnly(_self : nukemath.Matrix4_)  None

transpose(_self : nukemath.Matrix4_)  None

vtransform(_self : nukemath.Matrix4_, _arg0 :_)

xAxis(_self : nukemath.Matrix4_)

yAxis(_self : nukemath.Matrix4_)

zAxis(_self : nukemath.Matrix4_)