[ Nuke Python API Reference ![Logo](../_static/NukeApp128.png) ](../index.html)

16.0 

  * [Introduction](../intro.html)
  * [Start-up Scripts](../startup.html)
  * [Getting Started](../basics.html)
  * [Nuke as a Python Module](../nuke_as_python_module.html)
  * [Animation](../animation.html)
  * [Using the Command-line](../command_line.html)
  * [Callbacks](../callbacks.html)
  * [Stereo](../stereo.html)
  * [3D](../3D.html)
  * [Roto and RotoPaint](../rotopaint.html)
  * [Accessing Image Data](../image_data.html)
  * [Custom Panels](../custom_panels.html)
  * [Extending NUKE with PySide](../custom_panels.html#extending-nuke-with-pyside)
  * [Customizing the UI](../custom_ui.html)
  * [Custom Flipbooks](../flipbook.html)
  * [Metadata](../metadata.html)
  * [Working with Channels and Layers](../channels.html)
  * [Manipulating the Node Graph](../dag.html)
  * [Formats](../formats.html)
  * [Math](../math.html)
  * [Asset Management Systems / Pipeline Integration](../asset.html)
  * [OpenAssetIO Integration](../openassetio.html)
  * [Graph Scope Variables / Multi-shot Set-up](../gsv.html)
  * [Threading](../threading.html)
  * [Render Farm Integration (Concept)](../render_farm.html)
  * [Performance Profiling](../performance.html)
  * [Installing Plug-ins](../installing_plugins.html)
  * [Sample Scripts](../samples.html)



API Reference

  * [nuke](nuke.html)
  * [nuke.curveknob](nuke.curveknob.html)
  * [nuke.curvelib](nuke.curvelib.html)
  * [nuke.gsv](nuke.gsv.html)
  * [nuke.localization](nuke.localization.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
    * [nuke.splinewarp.AnimAttributes](nuke.splinewarp.AnimAttributes.html)
    * [nuke.splinewarp.AnimCTransform](nuke.splinewarp.AnimCTransform.html)
    * [nuke.splinewarp.AnimControlPoint](nuke.splinewarp.AnimControlPoint.html)
    * [nuke.splinewarp.AnimCurve](nuke.splinewarp.AnimCurve.html)
    * [nuke.splinewarp.AnimCurveKey](nuke.splinewarp.AnimCurveKey.html)
    * [nuke.splinewarp.AnimCurveViews](nuke.splinewarp.AnimCurveViews.html)
    * [nuke.splinewarp.BaseCurve](nuke.splinewarp.BaseCurve.html)
    * [nuke.splinewarp.CMatrix4](nuke.splinewarp.CMatrix4.html)
    * [nuke.splinewarp.CTransform](nuke.splinewarp.CTransform.html)
    * [nuke.splinewarp.CVec2](nuke.splinewarp.CVec2.html)
    * [nuke.splinewarp.CVec3](nuke.splinewarp.CVec3.html)
    * [nuke.splinewarp.CVec4](nuke.splinewarp.CVec4.html)
    * [nuke.splinewarp.ControlPoint](nuke.splinewarp.ControlPoint.html)
    * [nuke.splinewarp.CubicCurve](nuke.splinewarp.CubicCurve.html)
    * [nuke.splinewarp.CurveKnob](nuke.splinewarp.CurveKnob.html)
    * [nuke.splinewarp.CurveType](nuke.splinewarp.CurveType.html)
    * [nuke.splinewarp.Element](nuke.splinewarp.Element.html)
    * [nuke.splinewarp.ExtrapolationType](nuke.splinewarp.ExtrapolationType.html)
    * [nuke.splinewarp.Flag](nuke.splinewarp.Flag.html)
    * [nuke.splinewarp.FlagType](nuke.splinewarp.FlagType.html)
    * [nuke.splinewarp.InterpolationType](nuke.splinewarp.InterpolationType.html)
    * [nuke.splinewarp.Layer](nuke.splinewarp.Layer.html)
    * [nuke.splinewarp.RotationOrder](nuke.splinewarp.RotationOrder.html)
    * [nuke.splinewarp.Shape](nuke.splinewarp.Shape.html)
    * [nuke.splinewarp.ShapeControlPoint](nuke.splinewarp.ShapeControlPoint.html)
    * nuke.splinewarp.SplineKnob
    * [nuke.splinewarp.Stroke](nuke.splinewarp.Stroke.html)
    * [nuke.splinewarp.TransformOrder](nuke.splinewarp.TransformOrder.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.splinewarp](nuke.splinewarp.html) »
  * nuke.splinewarp.SplineKnob
  * 


* * *

# nuke.splinewarp.SplineKnob

_class _nuke.splinewarp.SplineKnob
    

Bases: [`_curveknob.CurveKnob`](nuke.splinewarp.CurveKnob.html#nuke.splinewarp.CurveKnob "_curveknob.CurveKnob")

Methods

`Class` | 

return
    Class name.  
---|---  
`ClassID` | 

return
    Class ID.  
`changed` | Call this after performing updates on the tree, to tell it that it's been updated.  
`clearAnimated` | Clear animation for channel 'c'.  
`clearFlag` | Clear flag.  
`critical` | 

param message
    message to put the knob in error, and do a popup.  
`debug` | 

param message
    message to put out to the error console, attached to the knob, if the verbosity level is set high enough.  
`defaultJoin` | Joins the two given SplineWarp elements.  
`enabled` | 

return
    True if the knob is enabled, False if it's disabled.  
`error` | 

param message
    message to put the knob in error.  
`fromScript` | Initialise from script.  
`fullyQualifiedName` | Returns the fully-qualified name of the knob within the node.  
`getAB` | Returns a string denoting the channel the given shape is in.  
`getAuthorMode` | Returns the authoring mode currently set on the knob.  
`getAuthorModes` | Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list.  
`getCorrespondencePoints` | Gets the collection of correspondence point collection for the element specified by the path.  
`getDerivative` | Return derivative at time 't' for channel 'c'.  
`getFlag` | Returns whether the input flag is set.  
`getIntegral` | Return integral at the interval [t1, t2] for channel 'c'.  
`getKeyIndex` | Return keyframe index at time 't' for channel 'c'.  
`getKeyList` | Get all unique keys on the knob.  
`getKeyTime` | Return index of the keyframe at time 't' for channel 'c'.  
`getNthDerivative` | Return nth derivative at time 't' for channel 'c'.  
`getNumKeys` | Return number of keyframes for channel 'c'.  
`getSelected` | Returns list of all selected items in a curve knob As an example, say you have a Bezier curve selected,the following will return 'Bezier1' >>> curveKnob = nuke.toNode('RotoPaint1)['curves'] >>> selected = curveKnob.getSelected() >>> selected[0].name  
`getValue` | Return value at the current frame for channel 'c'.  
`getValueAt` | Return value at time 't' for channel 'c'.  
`hasExpression` | Return True if animation at index 'index' has an expression.  
`isAnimated` | Return True if channel 'c' is animated.  
`isKey` | Return True if there is a keyframe at the current frame for channel 'c'.  
`isKeyAt` | Return True if there is a keyframe at time 't' for channel 'c'.  
`label` | 

return
    label.  
`makeWidget` | Returns an instance of the QWidget subclass used to edit the knob's value.  
`name` | 

return
    name.  
`node` | Return the node that this knob belongs to.  
`notDefault` | 

return
    True if any of the values is not set to the default, False otherwise.  
`removeKey` | Remove key for channel 'c'.  
`removeKeyAt` | Remove key at time 't' for channel 'c'.  
`setAB` | Puts the given shape into the 'A' or the 'B' channel.  
`setAnimated` | Set channel 'c' to be animated.  
`setAuthorMode` | Sets the authoring mode on the knob.  
`setEnabled` | Enable or disable the knob.  
`setExpression` | Set the expression for a knob.  
`setFlag` | Logical OR of the argument and existing knob flags.  
`setLabel` | 

param s
    New label.  
`setName` | 

param s
    New name.  
`setTooltip` | 

param s
    New tooltip.  
`setValue` | Sets the value 'val' at channel 'chan'.  
`setValueAt` | Sets the value 'val' at channel 'chan' for time 'time'.  
`setVisible` | Show or hide the knob.  
`toElement` | Takes a path which identifies a particular element in the curve tree and returns the corresponding Layer, Stroke or Shape object.  
`toScript` | Return the value of the knob in script syntax.  
`toScriptPrefix` | Write commands that must be executed before the to_script() value can be parsed.  
`tooltip` | 

return
    tooltip.  
`value` | Return value at the current frame for channel 'c'.  
`visible` | 

return
    True if the knob is visible, False if it's hidden.  
`warning` | 

param message
    message to put a warning on the knob.  
  
Attributes

`curveWidget` | Curve Widget  
---|---  
`rootLayer` | The root layer.  
  
Class() → Class name.
    

Returns
    

Class name.

ClassID() → Class ID.
    

Returns
    

Class ID.

changed() → None
    

Call this after performing updates on the tree, to tell it that it’s been updated. For many operations this is called automatically, but you can call it manually for those cases where it isn’t.

clearAnimated()
    

Clear animation for channel ‘c’. Return True if successful.

clearFlag(_f_) → None.
    

Clear flag. :param f: Flag. :return: None.

critical(_message_) → None.
    

Parameters
    

**message** – message to put the knob in error, and do a popup.

Returns
    

None.

curveWidget
    

Curve Widget

debug(_message_) → None.
    

Parameters
    

**message** – message to put out to the error console, attached to the knob, if the verbosity level is set high enough.

Returns
    

None.

defaultJoin(_AShape_ , _BShape_) → [CorrespondencePoints](nuke.curvelib.CorrespondencePoints.html#nuke.curvelib.CorrespondencePoints "nuke.curvelib.CorrespondencePoints")
    

Joins the two given SplineWarp elements. Does not create an undo nor call knob.changed on the spline knob

enabled() → Boolean.
    

Returns
    

True if the knob is enabled, False if it’s disabled.

error(_message_) → None.
    

Parameters
    

**message** – message to put the knob in error.

Returns
    

None.

fromScript()
    

Initialise from script.

fullyQualifiedName(_channel =- 1_) → string
    

Returns the fully-qualified name of the knob within the node. This can be useful for expression linking.

Parameters
    

**channel** – Optional parameter, specifies the channel number of the sub-knob (for example, channels of 0 and 1 would refer to the x and y of a XY_Knob respectively), leave blank or set to -1 to get the qualified name of the knob only.

Returns
    

The string of the qualified knob or sub-knob, which can be used directly in expression links.

getAB(_shapeObj_) → ['A' | 'B' | 'UNDEFINED']
    

Returns a string denoting the channel the given shape is in. A utility function wrapping the attribute getter for the ABAttribute

getAuthorMode() → Integer.
    

Returns the authoring mode currently set on the knob. This is a unique string identifier of the option, which is also used for serialisation and deserialisation. It is not meant to change,thus one can rely on it. :return: The string identifier of the current authoring mode set.

getAuthorModes() → List.
    

Returns the names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. :return: The names of the authoring modes of the knob if the knob is an authoring knob, otherwise an empty list. This is a list of strings.

getCorrespondencePoints(_'path/to/element'_) → [CorrespondencePoints](nuke.curvelib.CorrespondencePoints.html#nuke.curvelib.CorrespondencePoints "nuke.curvelib.CorrespondencePoints")
    

Gets the collection of correspondence point collection for the element specified by the path.

getDerivative()
    

Return derivative at time ‘t’ for channel ‘c’.

getFlag(_f_) → Bool.
    

Returns whether the input flag is set. :param f: Flag. :return: True if set, False otherwise.

getIntegral()
    

Return integral at the interval [t1, t2] for channel ‘c’.

getKeyIndex()
    

Return keyframe index at time ‘t’ for channel ‘c’.

getKeyList()
    

Get all unique keys on the knob. Returns list.

getKeyTime()
    

Return index of the keyframe at time ‘t’ for channel ‘c’.

getNthDerivative()
    

Return nth derivative at time ‘t’ for channel ‘c’.

getNumKeys()
    

Return number of keyframes for channel ‘c’.

getSelected() → [selectedObjects]
    

Returns list of all selected items in a curve knob As an example, say you have a Bezier curve selected,the following will return ‘Bezier1’ >>> curveKnob = nuke.toNode(‘RotoPaint1)[‘curves’] >>> selected = curveKnob.getSelected() >>> selected[0].name

getValue()
    

Return value at the current frame for channel ‘c’.

getValueAt()
    

Return value at time ‘t’ for channel ‘c’.

hasExpression(_index =- 1_) → bool
    

Return True if animation at index ‘index’ has an expression. :param index: Optional index parameter. Defaults to -1 if not specified. This can be specified as a keyword parameter if desired. :return: True if has expression, False otherwise.

isAnimated()
    

Return True if channel ‘c’ is animated.

isKey()
    

Return True if there is a keyframe at the current frame for channel ‘c’.

isKeyAt()
    

Return True if there is a keyframe at time ‘t’ for channel ‘c’.

label() → label.
    

Returns
    

label.

makeWidget() → PySide6.QtWidgets.QWidget.
    

Returns an instance of the QWidget subclass used to edit the knob’s value. The widget will update the knob’s value when its value changes and should update its displayed value(s) when they change on the knob. Can return null if no widget should be created for the knob. :return: PySide6.QtWidgets.QWidget.

name() → name.
    

Returns
    

name.

node() → [nuke.Node](nuke.Node.html#nuke.Node "nuke.Node")
    

Return the node that this knob belongs to. If the node has been cloned, we’ll always return a reference to the original. :return: The node which owns this knob, or None if the knob has no owner yet.

notDefault() → True if any of the values is not set to the default, False otherwise.
    

Returns
    

True if any of the values is not set to the default, False otherwise.

removeKey()
    

Remove key for channel ‘c’. Return True if successful.

removeKeyAt()
    

Remove key at time ‘t’ for channel ‘c’. Return True if successful.

rootLayer
    

The root layer.

setAB(_shapeObj_[, _"A"|"B"_]) → None
    

Puts the given shape into the ‘A’ or the ‘B’ channel. A utility function wrapping the attribute setter for the ABAttribute Does not create an undo nor call knob.changed on the spline knob

setAnimated()
    

Set channel ‘c’ to be animated.

setAuthorMode(_authorMode_) → None.
    

Sets the authoring mode on the knob. This accepts both the unique string identifier, which is also used for serialisation and deserialisation, or index of the option for convenience. These values are not meant to change, thus one can rely on them. :param authorMode: The string identifier or index of the authoring mode. :return: None.

setEnabled(_enabled_) → None.
    

Enable or disable the knob. :param enabled: True to enable the knob, False to disable it.

setExpression(_expression_ , _channel =- 1_, _view =None_) → bool
    

Set the expression for a knob. You can optionally specify a channel to set the expression for.

Parameters
    

  * **expression** – The new expression for the knob. This should be a string.

  * **channel** – Optional parameter, specifying the channel to set the expression for. This should be an integer.

  * **view** – Optional view parameter. Without, this command will set the expression for the current view theinterface is displaying. Can be the name of the view or the index.



Returns
    

True if successful, False if not.

setFlag(_f_) → None.
    

Logical OR of the argument and existing knob flags. :param f: Flag. :return: None.

setLabel(_s_) → None.
    

Parameters
    

**s** – New label.

Returns
    

None.

setName(_s_) → None.
    

Parameters
    

**s** – New name.

Returns
    

None.

setTooltip(_s_) → None.
    

Parameters
    

**s** – New tooltip.

Returns
    

None.

setValue(_val_ , _chan_) → bool
    

Sets the value ‘val’ at channel ‘chan’. :return: True if successful, False if not.

setValueAt(_val_ , _time_ , _chan_) → bool
    

Sets the value ‘val’ at channel ‘chan’ for time ‘time’. :return: True if successful, False if not.

setVisible(_visible_) → None.
    

Show or hide the knob. :param visible: True to show the knob, False to hide it.

toElement(_path_) → [Element](nuke.splinewarp.Element.html#nuke.splinewarp.Element "nuke.splinewarp.Element")
    

Takes a path which identifies a particular element in the curve tree and returns the corresponding Layer, Stroke or Shape object. The path is a slash separated string and is always resolved relative to the root layer. So if, for example, you have a RotoPaint node with a layer called ‘Layer1’ which contains a shape called ‘Shape1’, the path to the shape would be ‘Layer1/Shape1’. >>> knob = nuke.toNode(‘RotoPaint1)[‘curves’] >>> shape = knob.toElement(‘Layer1/Shape1’) >>> shape.name ‘Shape1’

toScript(_quote_ , _context =current_) → string.
    

Return the value of the knob in script syntax. Pass True for quote to return results quoted in {}. Pass None for context to get results for all views and key times (as stored in a .nk file).

toScriptPrefix() → string
    

Write commands that must be executed before the to_script() value can be parsed. This is used to write commands to declare Layers and Formats and other objects that are shared by knobs.

tooltip() → tooltip.
    

Returns
    

tooltip.

value()
    

Return value at the current frame for channel ‘c’.

visible() → Boolean.
    

Returns
    

True if the knob is visible, False if it’s hidden.

warning(_message_) → None.
    

Parameters
    

**message** – message to put a warning on the knob.

Returns
    

None.

[ Previous](nuke.splinewarp.ShapeControlPoint.html "nuke.splinewarp.ShapeControlPoint") [Next ](nuke.splinewarp.Stroke.html "nuke.splinewarp.Stroke")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
