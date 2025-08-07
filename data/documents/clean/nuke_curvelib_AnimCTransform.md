# nuke.curvelib.AnimCTransform
_class _nuke.curvelib.AnimCTransform

Bases: `object`
An animated transform, where each part of the transform is represented as a curve over time.
Methods
`addPivotPointKey` ---
`addRotationKey`
`addScaleKey`
`addSkewXKey`
`addTransformKey`
`addTranslationKey`
`evaluate`
`getExtraMatrixAnimCurve`  Returns the AnimCurve object for the 4i+j element in the transform's extra matrix.The view parameter is optional.
`getNumberOfPivotPointKeys`  Get the number of keys for the pivotPoint attribute.
`getNumberOfRotationKeys`  Get the number of keys for the rotation attribute.
`getNumberOfScaleKeys`  Get the number of keys for the scale attribute.
`getNumberOfSkewXKeys`  Get the number of keys for the skewX attribute.
`getNumberOfTransformKeys`  Get the number of keys for all attributes of this transform.
`getNumberOfTranslationKeys`  Get the number of keys for the translation attribute.
`getPivotPointAnimCurve`
`getPivotPointKeyTime`  Get the time for a specific key on the pivotPoint attribute.
`getPivotPointKeyTimes`  Get the times for all keys on the pivotPoint attribute.
`getRotationAnimCurve`
`getRotationKeyTime`  Get the time for a specific key on the rotation attribute.
`getRotationKeyTimes`  Get the times for all keys on the rotation attribute.The view parameter is optional.
`getScaleAnimCurve`
`getScaleKeyTime`  Get the time for a specific key on the scale attribute.
`getScaleKeyTimes`  Get the times for all keys on the scale attribute.
`getSkewXAnimCurve`
`getSkewXKeyTime`  Get the time for a specific key on the skewX attribute.
`getSkewXKeyTimes`  Get the times for all keys on the skewX attribute.
`getTransformKeyTime`  Get the time for a specific key.
`getTransformKeyTimes`  Get the times for all keys, across all attributes of this transform.
`getTranslationAnimCurve`
`getTranslationKeyTime`  Get the time for a specific key on the translation attribute.
`getTranslationKeyTimes`  Get the times for all keys on the translation attribute.
`isDefault`  Check whether this transform has been modified away from the default values.
`removePivotPointKey`
`removeRotationKey`
`removeScaleKey`
`removeSkewXKey`
`removeTransformKey`
`removeTranslationKey`
`reset`
`setExtraMatrixAnimCurve`  Sets the AnimCurve object for the '4i+j'-th element of the extra matrix.The view parameter is optional
`setIdentity`
`setPivotPointAnimCurve`  Set the anim curve for the pivot point attribute of this transform.
`setRotationAnimCurve`  Set the anim curve for the rotation attribute of this transform.
`setScaleAnimCurve`  Set the anim curve for the scale attribute of this transform.
`setSkewXAnimCurve`  Set the anim curve for the skewX attribute of this transform.
`setTranslationAnimCurve`  Set the anim curve for the translation attribute of this transform.

Attributes
`name`  The name for this transform.---
`rotationOrder`  The order in which to perform rotations around the axes.
`transformOrder`  The order in which to perform the transformations.

addPivotPointKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_)  None

addRotationKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_)  None

addScaleKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_)  None

addSkewXKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_)  None

addTransformKey(_time_ , _view_)  None

addTranslationKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_)  None

evaluate(_time_ , _view_)  None

getExtraMatrixAnimCurve(_i_ , _j_ , _view_)

Returns the AnimCurve object for the 4i+j element in the transform’s extra matrix.The view parameter is optional.
getNumberOfPivotPointKeys(_view_)  int

Get the number of keys for the pivotPoint attribute. The view parameter is optional.
getNumberOfRotationKeys(_view_)  int

Get the number of keys for the rotation attribute. The view parameter is optional.
getNumberOfScaleKeys(_view_)  int

Get the number of keys for the scale attribute. The view parameter is optional.
getNumberOfSkewXKeys(_view_)  int

Get the number of keys for the skewX attribute. The view parameter is optional.
getNumberOfTransformKeys(_view_)  int

Get the number of keys for all attributes of this transform. The view parameter is optional.
getNumberOfTranslationKeys(_view_)  int

Get the number of keys for the translation attribute. The view parameter is optional.
getPivotPointAnimCurve(_index_ , _view_)

getPivotPointKeyTime(_index_ , _view_)  float

Get the time for a specific key on the pivotPoint attribute. index is the index of the key. The view parameter is optional.
getPivotPointKeyTimes(_view_)  list of floats

Get the times for all keys on the pivotPoint attribute. The view parameter is optional.
getRotationAnimCurve(_index_ , _view_)

getRotationKeyTime(_index_ , _view_)  float

Get the time for a specific key on the rotation attribute. index is the index of the key. The view parameter is optional.
getRotationKeyTimes(_view_)  list of floats

Get the times for all keys on the rotation attribute.The view parameter is optional.
getScaleAnimCurve(_index_ , _view_)

getScaleKeyTime(_index_ , _view_)  float

Get the time for a specific key on the scale attribute. index is the index of the key. The view parameter is optional.
getScaleKeyTimes(_view_)  list of floats

Get the times for all keys on the scale attribute. The view parameter is optional.
getSkewXAnimCurve(_index_ , _view_)

getSkewXKeyTime(_index_ , _view_)  float

Get the time for a specific key on the skewX attribute. index is the index of the key. The view parameter is optional.
getSkewXKeyTimes(_view_)  list of floats

Get the times for all keys on the skewX attribute. The view parameter is optional.
getTransformKeyTime(_index_ , _view_)  float

Get the time for a specific key. The view parameter is optional.
getTransformKeyTimes(_view_)  list of floats

Get the times for all keys, across all attributes of this transform. The view parameter is optional.
getTranslationAnimCurve(_index_ , _view_)

getTranslationKeyTime(_index_ , _view_)  float

Get the time for a specific key on the translation attribute. index is the index of the key. The view parameter is optional.
getTranslationKeyTimes(_view_)  list of floats

Get the times for all keys on the translation attribute. The view parameter is optional.
isDefault()  bool

Check whether this transform has been modified away from the default values.
name

The name for this transform.
removePivotPointKey(_time_ , _view_)  None

removeRotationKey(_time_ , _view_)  None

removeScaleKey(_time_ , _view_)  None

removeSkewXKey(_time_ , _view_)  None

removeTransformKey(_time_ , _view_)  None

removeTranslationKey(_time_ , _view_)  None

reset()  None

rotationOrder

The order in which to perform rotations around the axes.
setExtraMatrixAnimCurve(_i_ , _j_ , _animcurve_ , _view_)  None

Sets the AnimCurve object for the ‘4i+j’-th element of the extra matrix.The view parameter is optional
setIdentity(_view ='default'_)  None

setPivotPointAnimCurve(_index_ , _animCurve_ , _view_)  None

Set the anim curve for the pivot point attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
setRotationAnimCurve(_index_ , _animCurve_ , _view_)  None

Set the anim curve for the rotation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
setScaleAnimCurve(_index_ , _animCurve_ , _view_)  None

Set the anim curve for the scale attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
setSkewXAnimCurve(_index_ , _animCurve_ , _view_)  None

Set the anim curve for the skewX attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
setTranslationAnimCurve(_index_ , _animCurve_ , _view_)  None

Set the anim curve for the translation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.
transformOrder

The order in which to perform the transformations.