# nuke.splinewarp.Layer
_class _nuke.splinewarp.Layer

Bases:
A layer, used to group other elements in the paint tree.
Layers can contain shapes, strokes and other layers. They can be transformed, which has the effect of transforming all contained objects by the same amount (in addition to any individual transforms on the contained objects).
Layers are represented as a sequence of Element objects. You can find out how many items the layer contains using the len() function, as for any python sequence. Likewise you can access the contained elements using python’s array-style syntax (e.g. layer[0] will return the first element inside the layer, layer[-1] will return the last element, etc.).
Methods
`append`  Add a new element inside this layer.---
`clone`
`getAttributes`  Gets the collection of attributes for this stroke.
`getFlag`  Check whether a particular flag is set or not.
`getTransform`  Gets the transform for this shape.
`getVisible`  Get the value of the visible attribute at a particular time.
`insert`  Insert a new element inside this layer at the given index.
`remove`  Remove the element at the given index from this layer.
`removeAll`  Remove all elements from this layer.
`serialise`  Returns a string representation of the given element.
`setFlag`  Set a particular flag.
`setTransform`  Replace the existing transform for this shape with a new one.
`setVisible`  Set the value of the visible attribute at a particular time.

Attributes
`locked`  Whether this element is locked.---
`name`  The name for this element.

append(_element_)  None

Add a new element inside this layer. The element must be an instance of either the Shape, Stroke or Layer classes. Note that an element cannot be in more than one place in the tree, so if you try to add an element that is already in the tree somewhere else, it’ll be removed from its old location first.
clone()  elementCreate clone of element

getAttributes()

Gets the collection of attributes for this stroke.
getFlag(_flag_)  bool

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.
getTransform()

Gets the transform for this shape.
getVisible(_time_)  bool

Get the value of the visible attribute at a particular time.
insert(_index_ , _element_)  None

Insert a new element inside this layer at the given index. The element must be an instance of either the Shape, Stroke or Layer classes. Note that an element cannot be in more than one place in the tree, so if you try to add an element that is already in the tree somewhere else, it’ll be removed from its old location first.
locked

Whether this element is locked.
name

The name for this element.
remove(_index_)  None

Remove the element at the given index from this layer. If the index is out of bounds, an IndexError will be raised.
removeAll()  None

Remove all elements from this layer.
serialise()  string

Returns a string representation of the given element.
setFlag(_flag_ , _value_)  None

Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.
setTransform(_transform_)  None

Replace the existing transform for this shape with a new one. The transform parameter must be an instance of the AnimTransform class.
setVisible(_time_ , _value_)  None

Set the value of the visible attribute at a particular time. value must be a bool.