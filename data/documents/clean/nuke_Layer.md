# nuke.Layer
_class _nuke.Layer

Bases: `object`
A layer is a set of channels.
Methods
`channels`  Get a list of the channels in this layer.---
`name`  Get the layer name.
`setName`  Set the name of this layer.
`visible`  Check whether the layer is visible.

channels()  [string, ...]

Get a list of the channels in this layer.
Returns

A list of strings, where each string is the name of a channel in this layer.
name()  str

Get the layer name.
Returns

The layer name, as a string.
setName(_newName_)  None

Set the name of this layer.
Parameters

**newName** – The new name for this layer.
visible()  bool

Check whether the layer is visible.
Returns

True if visible, False if not.