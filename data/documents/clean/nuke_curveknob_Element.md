# nuke.curveknob.Element
_class _nuke.curveknob.Element

Bases: `object`
The base class for the different types of elements you can create in the RotoPaint node.
Methods
`clone` ---
`getVisible`  Get the value of the visible attribute at a particular time.
`serialise`  Returns a string representation of the given element.
`setVisible`  Set the value of the visible attribute at a particular time.

Attributes
`locked`  Whether this element is locked.---
`name`  The name for this element.

clone()  elementCreate clone of element

getVisible(_time_)  bool

Get the value of the visible attribute at a particular time.
locked

Whether this element is locked.
name

The name for this element.
serialise()  string

Returns a string representation of the given element.
setVisible(_time_ , _value_)  None

Set the value of the visible attribute at a particular time. value must be a bool.