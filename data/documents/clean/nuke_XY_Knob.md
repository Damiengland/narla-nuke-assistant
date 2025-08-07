# nuke.XY_Knob
_class _nuke.XY_Knob

Bases:
A knob which describes a 2D position.
Methods
`Class`
return
    Class name.---
`ClassID`
return
    Class ID.
`animation`  Return the AnimationCurve for the channel 'chan' and view 'view'.
`animations`
param view
    Optional view.
`array`
return
    List of knob values.
`arraySize`
return
    Number of elements in array.
`clearAnimated`  Delete animation.
`clearFlag`  Clear flag.
`copyAnimation`  Copies the i'th channel of the AnimationCurve curve to this object.
`copyAnimations`  Copies the AnimationCurves from curves to this object.
`critical`
param message
    message to put the knob in error, and do a popup.
`debug`
param message
    message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
`defaultValue`
return
    Default value.
`deleteAnimation`  Deletes the AnimationCurve.
`dimensions`
return
    Dimensions in array.
`enabled`
return
    True if the knob is enabled, False if it's disabled.
`error`
param message
    message to put the knob in error.
`frame`
return
    Frame number.
`fromScript`  Set value of the knob to a user defined script (TCL syntax, as in .nk file).
`fullyQualifiedName`  Returns the fully-qualified name of the knob within the node.
`getAuthorMode`  Returns the authoring mode currently set on the knob.
`getAuthorModes`  Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list.
`getDerivative`  Return derivative at time 't' and index 'i'.
`getFlag`  Returns whether the input flag is set.
`getIntegral`  Return integral at time interval [t1, t2] and index 'i'.
`getKeyIndex`  Return index of the keyframe at time 't' and channel 'c'.
`getKeyList`  Get all unique keys on the knob.
`getKeyTime`  Return time of the keyframe at time 't' and channel 'c'.
`getNthDerivative`  Return n'th derivative at time 't' and index 'i'.
`getNumKeys`  Return number of keys at channel 'c'.
`getValue`  self.value(index, view, time) -> Floating point or List of floating point values (in case some are different).
`getValueAt`  self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different).
`hasExpression`
param index
    Optional index.
`height`
return
    Height of array of values.
`isAnimated`
param index
    Optional index.
`isKey`
param index
    Optional index.
`isKeyAt`  Returns True if there is a keyframe at specified time, optional index and view, otherwise returns False.
`label`
return
    label.
`makeWidget`  Returns an instance of the QWidget subclass used to edit the knob's value.
`max`
return
    Maximum value.
`maximum`  self.max() -> Maximum value.
`min`
return
    Minimum value.
`minimum`  self.min() -> Minimum value.
`name`
return
    name.
`names`  Return name for dimension n.
`node`  Return the node that this knob belongs to.
`notDefault`
return
    True if any of the values is not set to the default, False otherwise.
`removeKey`  Remove key.
`removeKeyAt`  Remove keyframe at specified time, optional index and view.
`resize`  Resize the array.
`setAnimated`  Create an Animation object.
`setAuthorMode`  Sets the authoring mode on the knob.
`setDefaultValue`
param s
    Sequence of floating-point values.
`setEnabled`  Enable or disable the knob.
`setExpression`  Set the expression for a knob.
`setFlag`  Logical OR of the argument and existing knob flags.
`setKeyAt`  Set a key on element 'index', at time and view.
`setLabel`
param s
    New label.
`setName`
param s
    New name.
`setRange`  Set range of values.
`setSingleValue`  Set to just hold a single value or not.
`setTooltip`
param s
    New tooltip.
`setValue`  Set index to value at time and view.
`setValueAt`  Set value of element 'index' at time for view.
`setVisible`  Show or hide the knob.
`singleValue`
param view
    Optional view. Default is current view.
`splitView`  Split the view away from the current knob value.
`toScript`  Return the value of the knob in script syntax.
`toScriptPrefix`  Write commands that must be executed before the to_script() value can be parsed.
`tooltip`
return
    tooltip.
`unsplitView`  Unsplit the view so that it shares a value with other views.
`value`  Return value for dimension n.
`valueAt`  Return value for this knob at specified time, optional index and view.
`vect`
return
    List of knob values.
`visible`
return
    True if the knob is visible, False if it's hidden.
`warning`
param message
    message to put a warning on the knob.
`width`
return
    Width of array of values.
`x`  Return value for x.
`y`  Return value for y.

Class()  Class name.

Returns

Class name.
ClassID()  Class ID.

Returns

Class ID.
animation(_chan_ , _view_)  AnimationCurve or None.

Return the AnimationCurve for the channel ‘chan’ and view ‘view’. The view argument is optional. :param channel: The channel index. :param view: Optional view. :return: AnimationCurve or None.
animations(_view_)  AnimationCurve list.

Parameters

**view** – Optional view.
Returns

AnimationCurve list.
Example: b = nuke.nodes.Blur() k = b[‘size’] k.setAnimated(0) a = k.animations() a[0].setKey(0, 11) a[0].setKey(10, 20)
array()  List of knob values.

Returns

List of knob values.
Should only be used for knobs that are neither animated nor get their values from a ValueProvider. For knobs like that, use Array_Knob.getValue, instead
arraySize()  Number of elements in array.

Returns

Number of elements in array.
clearAnimated(_index_ , _view_)  True if succeeded, False otherwise.

Delete animation. :param index: Optional index. :param view: Optional view. :return: True if succeeded, False otherwise.
clearFlag(_f_)  None.

Clear flag. :param f: Flag. :return: None.
copyAnimation(_channel_ , _curve_ , _view_)  None.

Copies the i’th channel of the AnimationCurve curve to this object. The view is optional and defaults to the current view. :param channel: The channel index. :param curve: AnimationCurve. :param view: Optional view. Defaults to current. :return: None.
copyAnimations(_curves_ , _view_)  None.

Copies the AnimationCurves from curves to this object. The view is optional and defaults to the current view. :param curves: AnimationCurve list. :param view: Optional view. Defaults to current. :return: None.
critical(_message_)  None.

Parameters

**message** – message to put the knob in error, and do a popup.
Returns

None.
debug(_message_)  None.

Parameters

**message** – message to put out to the error console, attached to the knob, if the verbosity level is set high enough.
Returns

None.
defaultValue()  Default value.

Returns

Default value.
deleteAnimation(_curve_)  None. Raises ValueError if not found.

Deletes the AnimationCurve. :param curve: An AnimationCurve instance which belongs to this Knob. :return: None. Raises ValueError if not found.
dimensions()  Dimensions in array.

Returns

Dimensions in array.
enabled()  Boolean.

Returns

True if the knob is enabled, False if it’s disabled.
error(_message_)  None.

Parameters

**message** – message to put the knob in error.
Returns

None.
frame()  Frame number.

Returns

Frame number.
fromScript(_s_)  True if successful, False otherwise.

Set value of the knob to a user defined script (TCL syntax, as in .nk file). Return True if successful. :param s: Nuke script to be set on knob. :return: True if successful, False otherwise.
fullyQualifiedName(_channel =- 1_)  string

Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.
Parameters

**channel** – Optional parameter, specifies the channel number of the sub-knob (for example, channels of 0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the qualified name of the knob only.
Returns

The string of the qualified knob or sub-knob, which can be used directly in expression links.
getAuthorMode()  Integer.

Returns the authoring mode currently set on the knob. This is a unique string identifier of the option, which is also used for serialisation and deserialisation. It is not meant to change,thus one can rely on it. :return: The string identifier of the current authoring mode set.
getAuthorModes()  List.

Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. :return: The names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. This is a list of strings.
getDerivative()

Return derivative at time ‘t’ and index ‘i’.
getFlag(_f_)  Bool.

Returns whether the input flag is set. :param f: Flag. :return: True if set, False otherwise.
getIntegral()

Return integral at time interval [t1, t2] and index ‘i’.
getKeyIndex()

Return index of the keyframe at time ‘t’ and channel ‘c’.
getKeyList()

Get all unique keys on the knob. Returns list.
getKeyTime()

Return time of the keyframe at time ‘t’ and channel ‘c’.
getNthDerivative()

Return n’th derivative at time ‘t’ and index ‘i’.
getNumKeys()

Return number of keys at channel ‘c’.
getValue()

self.value(index, view, time) -> Floating point or List of floating point values (in case some are different). :param index: Optional index. Default is 0. :param view: Optional view. :param time: Optional time. :return: Floating point or List of floating point values (in case some are different).
getValueAt()

self.valueAt(time, index, view) -> Floating point or List of floating point values (in case some are different). Return value for this knob at specified time, optional index and view. :param time: Time. :param index: Optional index. Default is 0. :param view: Optional view. :return: Floating point or List of floating point values (in case some are different).
hasExpression(_index_)  True if has expression, False otherwise.

Parameters

**index** – Optional index.
Returns

True if has expression, False otherwise.
height()  Height of array of values.

Returns

Height of array of values.
isAnimated(_index_ , _view_)  True if animated, False otherwise.

Parameters

  * **index** – Optional index.
  * **view** – Optional view.
Returns

True if animated, False otherwise.
isKey(_index_ , _view_)  True if succeeded, False otherwise.

Parameters

  * **index** – Optional index.
  * **view** – Optional view.
Returns

True if succeeded, False otherwise.
isKeyAt(_time_ , _index_ , _view_)  True if succeeded, False otherwise.

Returns True if there is a keyframe at specified time, optional index and view, otherwise returns False. :param time: Time. :param index: Optional index. :param view: Optional view. :return: True if succeeded, False otherwise.
label()  label.

Returns

label.
makeWidget()  PySide6.QtWidgets.QWidget.

Returns an instance of the QWidget subclass used to edit the knob’s value. The widget will update the knob’s value when its value changes and should update its displayed value(s) when they change on the knob. Can return null if no widget should be created for the knob. :return: PySide6.QtWidgets.QWidget.
max()  Maximum value.

Returns

Maximum value.
maximum()

self.max() -> Maximum value. :return: Maximum value.
min()  Minimum value.

Returns

Minimum value.
minimum()

self.min() -> Minimum value. :return: Minimum value.
name()  name.

Returns

name.
names(_n_)  string

Return name for dimension n. The argument n is an integer.
node()

Return the node that this knob belongs to. If the node has been cloned, we’ll always return a reference to the original. :return: The node which owns this knob, or None if the knob has no owner yet.
notDefault()  True if any of the values is not set to the default, False otherwise.

Returns

True if any of the values is not set to the default, False otherwise.
removeKey(_index_ , _view_)  True if succeeded, False otherwise.

Remove key. :param index: Optional index. :param view: Optional view. :return: True if succeeded, False otherwise.
removeKeyAt(_time_ , _index_ , _view_)  True if succeeded, False otherwise.

Remove keyframe at specified time, optional index and view. Return True if successful. :param time: Time. :param index: Optional index. :param view: Optional view. :return: True if succeeded, False otherwise.
resize(_w_ , _h_)  True if successful, False otherwise.

Resize the array. :param w: New width :param h: Optional new height :return: True if successful, False otherwise.
setAnimated(_index_ , _view_)  True if succeeded, False otherwise.

Create an Animation object. Return True if successful, in which case caller must initialise it by calling setValue() or setValueAt(). :param index: Optional index. :param view: Optional view. :return: True if succeeded, False otherwise.
setAuthorMode(_authorMode_)  None.

Sets the authoring mode on the knob. This accepts both the unique string identifier, which is also used for serialisation and deserialisation, or index of the option for convenience. These values are not meant to change, thus one can rely on them. :param authorMode: The string identifier or index of the authoring mode. :return: None.
setDefaultValue(_s_)  None.

Parameters

**s** – Sequence of floating-point values.
Returns

None.
setEnabled(_enabled_)  None.

Enable or disable the knob. :param enabled: True to enable the knob, False to disable it.
setExpression(_expression_ , _channel =- 1_, _view =None_)  bool

Set the expression for a knob. You can optionally specify a channel to set the expression for.
Parameters

  * **expression** – The new expression for the knob. This should be a string.
  * **channel** – Optional parameter, specifying the channel to set the expression for. This should be an integer.
  * **view** – Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.
Returns

True if successful, False if not.
setFlag(_f_)  None.

Logical OR of the argument and existing knob flags. :param f: Flag. :return: None.
setKeyAt(_time_ , _index_ , _view_)  None.

Set a key on element ‘index’, at time and view. :param time: Time. :param index: Optional index. :param view: Optional view. :return: None.
setLabel(_s_)  None.

Parameters

**s** – New label.
Returns

None.
setName(_s_)  None.

Parameters

**s** – New name.
Returns

None.
setRange(_f1_ , _f2_)  None.

Set range of values. :param f1 Min value. :param f2 Max value. :return: None.
setSingleValue(_b_ , _view_)  None.

Set to just hold a single value or not. :param b: Boolean object. :param view: Optional view. Default is current view. :return: None.
setTooltip(_s_)  None.

Parameters

**s** – New tooltip.
Returns

None.
setValue(_value_ , _index_ , _time_ , _view_)  True if value changed, False otherwise. Safe to ignore.

Set index to value at time and view. :param value: Floating point value. :param index: Optional index. :param time: Optional time. :param view: Optional view. :return: True if value changed, False otherwise. Safe to ignore.
setValueAt(_value_ , _time_ , _index_ , _view_)  bool.

Set value of element ‘index’ at time for view. If the knob is animated, it will set a new keyframe or change an existing one. Index and view are optional. Return True if successful. :param value: Floating point value. :param time: Time. :param index: Optional index. :param view: Optional view. :return: True if value changed, False otherwise. Safe to ignore.
setVisible(_visible_)  None.

Show or hide the knob. :param visible: True to show the knob, False to hide it.
singleValue(_view_)  True if holds a single value.

Parameters

**view** – Optional view. Default is current view.
Returns

True if holds a single value.
splitView(_view_)  None.

Split the view away from the current knob value. :param view: Optional view. Default is current view. :return: None.
toScript(_quote_ , _context_)  String.

Return the value of the knob in script syntax. :param quote: Optional, default is False. Specify True to return the knob value quoted in {}. :param context: Optional context, default is current, None will be “contextless” (all views, all keys) as in a .nk file. :return: String.
toScriptPrefix()  string

Write commands that must be executed before the to_script() value can be parsed. This is used to write commands to declare Layers and Formats and other objects that are shared by knobs.
tooltip()  tooltip.

Returns

tooltip.
unsplitView(_view_)  None.

Unsplit the view so that it shares a value with other views. :param view: Optional view. Default is current view. :return: None.
value(_n_ , _oc_)  float

Return value for dimension n. The optional argument oc is an OutputContext.
valueAt(_time_ , _index_ , _view_)  Floating point or List of floating point values (in case some are different).

Return value for this knob at specified time, optional index and view. :param time: Time. :param index: Optional index. Default is 0. :param view: Optional view. :return: Floating point or List of floating point values (in case some are different).
vect()  List of knob values.

Returns

List of knob values.
Should only be used for knobs that are neither animated nor get their values from a ValueProvider. For knobs like that, use Array_Knob.getValue, instead
visible()  Boolean.

Returns

True if the knob is visible, False if it’s hidden.
warning(_message_)  None.

Parameters

**message** – message to put a warning on the knob.
Returns

None.
width()  Width of array of values.

Returns

Width of array of values.
x(_oc_)  float

Return value for x. The optional oc argument is an OutputContext
y(_oc_)  float

Return value for y. The optional oc argument is an OutputContext