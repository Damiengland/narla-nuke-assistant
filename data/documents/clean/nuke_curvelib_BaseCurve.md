# nuke.curvelib.BaseCurve
_class _nuke.curvelib.BaseCurve

Bases:
A base class for animated curves.
You shouldn’t be using this class directly, it only exists for other classes in this module to inherit from.
Methods
`getFlag`  Gets the specified flag.---
`setFlag`  Set or clear the specified flag.

Attributes
`curveTension`  The tension type for this curve.---
`curveType`  The type of curve to treat this as.
`kDefaultCurveFlag`
`kDefaultCurveTension`
`kDefaultCurveType`
`name`  The name for this curve.

curveTension

The tension type for this curve.
curveType

The type of curve to treat this as.
getFlag(_flag_)  bool

Gets the specified flag. The parameter should be one of the FlagType constants.
name

The name for this curve.
setFlag(_flag_ , _value_)  None

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.