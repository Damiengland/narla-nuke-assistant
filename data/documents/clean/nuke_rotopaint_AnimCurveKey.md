# nuke.rotopaint.AnimCurveKey
_class _nuke.rotopaint.AnimCurveKey

Bases:
A key value in a parametric curve represented as a value at a particular time.
Methods
`getFlag`  Gets the specified flag.---
`reset`  Reset this key to its default values.
`setFlag`  Set or clear the specified flag.

Attributes
`interpolationType`  The interpolation type to use for this key.---
`kDefaultAnimCurveKeyInterpolation`
`kDefaultAnimCurveKeyTime`
`kDefaultAnimCurveKeyValue`
`la`  The left bicubic value for this key.
`lslope`  The left derivative for this key.
`ra`  The right bicubic value for this key.
`rslope`  The right derivative for this key.
`time`  The time this key is set at.
`value`  The value for this key.

getFlag(_flag_)  bool

Gets the specified flag. The parameter should be one of the FlagType constants.
interpolationType

The interpolation type to use for this key.
la

The left bicubic value for this key.
lslope

The left derivative for this key.
ra

The right bicubic value for this key.
reset()  None

Reset this key to its default values.
rslope

The right derivative for this key.
setFlag(_flag_ , _value_)  None

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.
time

The time this key is set at.
value

The value for this key.