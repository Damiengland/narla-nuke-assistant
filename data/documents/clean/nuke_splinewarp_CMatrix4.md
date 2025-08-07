# nuke.splinewarp.CMatrix4
_class _nuke.splinewarp.CMatrix4

Bases: `object`
A 4x4 matrix with methods for affine transformations.
Methods
`makeIdentity`  Set this matrix to be the identity matrix.---
`rotateX`  Post-multiply this matrix by a rotation around the X axis.
`rotateY`  Post-multiply this matrix by a rotation around the Y axis.
`rotateZ`  self.rotateY(angleInRadians) -> None Post-multiply this matrix by a rotation around the Z axis.
`scale`  Post-multiply this matrix by a scale transformation.
`skew`  Post-multiply this matrix with a skew transformation.
`translate`  Post-multiply this matrix by a translation matrix.
`translation`  Set this matrix to be a translation matrix, replacing any existing values.
`transpose`  Transpose the matrix in-place.

__add__(_value_ , _/_)

Return self+value.
__mul__(_value_ , _/_)

Return self*value.
makeIdentity()  None

Set this matrix to be the identity matrix.
rotateX(_angleInRadians_)  None

Post-multiply this matrix by a rotation around the X axis.
rotateY(_angleInRadians_)  None

Post-multiply this matrix by a rotation around the Y axis.
rotateZ()

self.rotateY(angleInRadians) -> None Post-multiply this matrix by a rotation around the Z axis.
scale(_x_ , _y_ , _z_)  None

Post-multiply this matrix by a scale transformation. The y and z parameters may be left out; if so the scale is uniform along all three axes.
skew(_x_ , _y_ , _z_)  None

Post-multiply this matrix with a skew transformation. The y and z parameters may be left out; if so, the skew is in the X direction only.
translate(_x_ , _y_ , _z_)  None

Post-multiply this matrix by a translation matrix.
translation(_x_ , _y_ , _z_)  None

Set this matrix to be a translation matrix, replacing any existing values.
This is different from other methods in this class as it replaces, rather than multiplying by, the existing values in the matrix.
transpose()  None

Transpose the matrix in-place.