# nuke.splinewarp.Stroke
_class _nuke.splinewarp.Stroke

Bases:
A paint stroke, which may be animated.
A paint stroke is represented as a sequence of AnimControlPoint objects. You can find out how many control points there are in the stroke using python’s built-in len() function; and you can access individual control points using the array-style syntax (e.g. stroke[0] returns the first control point, stroke[-1] returns the last control point, etc.).
Methods
`append`  Add a new control point to the stroke.---
`clone`
`evaluate`  Bake out a curve for the path of this stroke at the specified time.
`getAttributes`  Gets the collection of attributes for this stroke.
`getFlag`  Check whether a particular flag is set or not.
`getTransform`  Gets the transform for this shape.
`getVisible`  Get the value of the visible attribute at a particular time.
`insert`  Insert a new control point in the stroke before the given index.
`remove`  Remove the control point at the given index.
`serialise`  Returns a string representation of the given element.
`setFlag`  Set a particular flag.
`setVisible`  Set the value of the visible attribute at a particular time.

Attributes
`locked`  Whether this element is locked.---
`name`  The name for this element.

append(_controlPoint_)  None

Add a new control point to the stroke. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.
clone()  elementCreate clone of element

evaluate(_time_ , _viewName ='default'_)

Bake out a curve for the path of this stroke at the specified time. :param time: The (floating point) frame number to bake the curve from. :param viewName: Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.
getAttributes()

Gets the collection of attributes for this stroke.
getFlag(_flag_)  bool

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.
getTransform()

Gets the transform for this shape.
getVisible(_time_)  bool

Get the value of the visible attribute at a particular time.
insert(_index_ , _controlPoint_)  None

Insert a new control point in the stroke before the given index. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.
locked

Whether this element is locked.
name

The name for this element.
remove(_index_)  None

Remove the control point at the given index. If the index is out of bounds, an IndexError will be raised.
serialise()  string

Returns a string representation of the given element.
setFlag(_flag_ , _value_)  None

Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.
setVisible(_time_ , _value_)  None

Set the value of the visible attribute at a particular time. value must be a bool.