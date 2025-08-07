# nuke.rotopaint.CTransform
_class _nuke.rotopaint.CTransform

Bases: `object`
A transform at a single point in time.
This is the result of evaluating an AnimTransform for a particular time.
Methods
`getInverseMatrix`  Gets the inverse transform matrix, which can be used for undoing the effects of this transform.---
`getMatrix`  Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.
`getTransposeMatrix`  Returns a transposed copy of the matrix representing this transform.
`isDefault`  Returns True if this transform matches the default settings, False if not.
`reset`  Return this transform to its default settings.
`setIdentity`  Set this transform to the identity transform (the transform which doesn't change the object at all).

Attributes
`name`  The name for this transform.---
`pivotPoint`  The location of the pivot point, represented as a CVec3 object.
`rotation`  The rotation amounts, represented as a CVec3 object.
`rotationOrder`  Indicates which order to apply the rotations in.
`scale`  The scale factors, represented as a CVec3 object.
`skew`  The skew amounts, represented as a CVec3 object.
`transformOrder`  Indicates which order to apply the transformations in.
`translation`  The translation amounts, represented as a CVec3 object.

getInverseMatrix()

Gets the inverse transform matrix, which can be used for undoing the effects of this transform.
getMatrix()

Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.
getTransposeMatrix()

Returns a transposed copy of the matrix representing this transform.
isDefault()  bool

Returns True if this transform matches the default settings, False if not.
name

The name for this transform.
pivotPoint

The location of the pivot point, represented as a CVec3 object.
reset()  None

Return this transform to its default settings.
rotation

The rotation amounts, represented as a CVec3 object.
rotationOrder

Indicates which order to apply the rotations in. The value will be one of the constants from the RotationOrder class.
scale

The scale factors, represented as a CVec3 object.
setIdentity()  None

Set this transform to the identity transform (the transform which doesn’t change the object at all).
skew

The skew amounts, represented as a CVec3 object.
transformOrder

Indicates which order to apply the transformations in. The value will be one of the constants from the TransformOrder class.
translation

The translation amounts, represented as a CVec3 object.