# nuke.curveknob.CurveWidget
_class _nuke.curveknob.CurveWidget

Bases:
The Curve Widget displayed in the Roto panel. This should only be used for test harness functionality.
IMPORTANT:

  1. may be None as it is not guaranteed that the widget is accessible
  2. the lifetime of the underlying object is undefined, DO NOT STORE!
Methods
`add`  Add a new group layer under the selected item's parent---
`clone`
`getSelectedItems`
`getVisible`  Get the value of the visible attribute at a particular time.
`remove`  Remove the selected items in the CurveTreeList
`serialise`  Returns a string representation of the given element.
`setVisible`  Set the value of the visible attribute at a particular time.

Attributes
`locked`  Whether this element is locked.---
`name`  The name for this element.

add()  None

Add a new group layer under the selected item’s parent
clone()  elementCreate clone of element

getSelectedItems()  List of strings of selected item namesGets a list of the selected items in the CurveTreeWidget

getVisible(_time_)  bool

Get the value of the visible attribute at a particular time.
locked

Whether this element is locked.
name

The name for this element.
remove()  None

Remove the selected items in the CurveTreeList
serialise()  string

Returns a string representation of the given element.
setVisible(_time_ , _value_)  None

Set the value of the visible attribute at a particular time. value must be a bool.