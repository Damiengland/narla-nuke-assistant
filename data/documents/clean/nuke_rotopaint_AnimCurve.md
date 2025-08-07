# nuke.rotopaint.AnimCurve
_class _nuke.rotopaint.AnimCurve

Bases:
An animated curve. The curve is described as a series of key values (instances of the AnimCurveKey class) which say what value it should have a particular time. For any time in between keys, the neighbouring key values are interpolated based on a curve type and interpolation settings specified at each key.
Each curve can only represent a single floating point value over time.
Methods
`addKey`  Add a new key to this curve.---
`evaluate`  Calculate the value of the curve at a specific time, the pass that in to the expression for the curve.
`evaluateY`  Calculates the value of the curve at a specific time.
`getFlag`  Gets the specified flag.
`getKey`  Returns one of the keys on this curve.
`getNumberOfKeys`  Returns the number of keys along this curve.
`isDefault`  Check whether this curve has been modified away from its default values.
`removeAllKeys`  Removes all keys from this curve.
`removeKey`  Remove an existing key from this curve.
`reset`  Reset this object to its default values.
`setFlag`  Set or clear the specified flag.

Attributes
`constantValue`  The constant (not-animated) value for this curve, if any.---
`curveTension`  The tension type for this curve.
`curveType`  The type of curve to treat this as.
`expressionString`  The expression string for the this curve, if any.
`kDefaultConstantValue`
`kDefaultCurveFlag`
`kDefaultCurveTension`
`kDefaultCurveType`
`name`  The name for this curve.
`useExpression`  Whether or not to use the expression string to calculate a value for this curve.

addKey(_time_ , _value_)  None
addKey(_keyObj_)  None

Add a new key to this curve. You can pass in either a time and value pair (the value parameter is optional), or an AnimCurveKey object you’ve created yourself. In the former case, a new AnimCurveKey object will be created and added to the curve; in the latter case, the key you pass in will be added directly.
constantValue

The constant (not-animated) value for this curve, if any.
curveTension

The tension type for this curve.
curveType

The type of curve to treat this as.
evaluate(_time_)  float

Calculate the value of the curve at a specific time, the pass that in to the expression for the curve. The return value is the result of the expression.
evaluateY(_time_)  float

Calculates the value of the curve at a specific time.
expressionString

The expression string for the this curve, if any.
getFlag(_flag_)  bool

Gets the specified flag. The parameter should be one of the FlagType constants.
getKey(_index_)

Returns one of the keys on this curve.
getNumberOfKeys()  int

Returns the number of keys along this curve.
isDefault()  bool

Check whether this curve has been modified away from its default values.
name

The name for this curve.
removeAllKeys()  None

Removes all keys from this curve.
removeKey(_timeOrHash_)  None

Remove an existing key from this curve. The key is identified by either the time it occurs at, or its hash (as returned by the key’s getHash() method.
reset()  None

Reset this object to its default values.
setFlag(_flag_ , _value_)  None

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.
useExpression

Whether or not to use the expression string to calculate a value for this curve.