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
    * [nuke.curvelib.AnimAttributes](nuke.curvelib.AnimAttributes.html)
    * [nuke.curvelib.AnimCTransform](nuke.curvelib.AnimCTransform.html)
    * nuke.curvelib.AnimControlPoint
    * [nuke.curvelib.AnimCurve](nuke.curvelib.AnimCurve.html)
    * [nuke.curvelib.AnimCurveKey](nuke.curvelib.AnimCurveKey.html)
    * [nuke.curvelib.AnimCurveViews](nuke.curvelib.AnimCurveViews.html)
    * [nuke.curvelib.BaseCurve](nuke.curvelib.BaseCurve.html)
    * [nuke.curvelib.CMatrix4](nuke.curvelib.CMatrix4.html)
    * [nuke.curvelib.CTransform](nuke.curvelib.CTransform.html)
    * [nuke.curvelib.CVec2](nuke.curvelib.CVec2.html)
    * [nuke.curvelib.CVec3](nuke.curvelib.CVec3.html)
    * [nuke.curvelib.CVec4](nuke.curvelib.CVec4.html)
    * [nuke.curvelib.ControlPoint](nuke.curvelib.ControlPoint.html)
    * [nuke.curvelib.CorrespondencePoints](nuke.curvelib.CorrespondencePoints.html)
    * [nuke.curvelib.CubicCurve](nuke.curvelib.CubicCurve.html)
    * [nuke.curvelib.CurveType](nuke.curvelib.CurveType.html)
    * [nuke.curvelib.ExtrapolationType](nuke.curvelib.ExtrapolationType.html)
    * [nuke.curvelib.Flag](nuke.curvelib.Flag.html)
    * [nuke.curvelib.FlagType](nuke.curvelib.FlagType.html)
    * [nuke.curvelib.InterpolationType](nuke.curvelib.InterpolationType.html)
    * [nuke.curvelib.RotationOrder](nuke.curvelib.RotationOrder.html)
    * [nuke.curvelib.TransformOrder](nuke.curvelib.TransformOrder.html)
  * [nuke.gsv](nuke.gsv.html)
  * [nuke.localization](nuke.localization.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.curvelib](nuke.curvelib.html) »
  * nuke.curvelib.AnimControlPoint
  * 


* * *

# nuke.curvelib.AnimControlPoint

_class _nuke.curvelib.AnimControlPoint
    

Bases: [`_curvelib.Flag`](nuke.splinewarp.Flag.html#nuke.splinewarp.Flag "_curvelib.Flag")

An animated control point.

These are used directly by Stroke objects to store the control point locations. Shape objects use a collection of up to 6 of them to represent each control point (see the ShapeControlPoint class for details).

It is advisable to call changed() on the ‘curves’ knob after making modifications to curves. This forces the knob to re-cache the state of its curves.

The ‘view’ argument to the object’s methods can be omitted and the default view ‘main’ will be used.

Methods

`addControlPoint` |   
---|---  
`addKey` |   
`addPositionKey` | Adds a new key to the control point's timeline.  
`evaluate` | Evaluates the animated control point's position at the specific time.  
`getControlPointKeyTimes` | Get the list of times at which this control point has a key.  
`getFlag` | Gets the specified flag.  
`getPosition` | Get the position of this control point at a particular time.  
`getPositionAnimCurve` | Returns the AnimCurve object containing the time line for the control point.  
`getPositionKeyTime` | Get the time of a particular key for this control point.  
`removeAllKeys` |   
`removeKey` |   
`removePositionKey` |   
`reset` | Resets the control point back to an initial empty state.  
`setFlag` | Set or clear the specified flag.  
`setPosition` | Sets the control point's 'constant' position (the position used when there are no keys - see AnimCurve for further info).  
`setPositionAnimCurve` | Set the point's AnimCurve object (its time line).  
`setPositionKey` | Sets an individual dimension (index) of a key to a specific value.  
  
Attributes

`dim` | The dimensionality, or number of components, for this control point (usually 3 - x, y and pressure).  
---|---  
`hash` | The hash value for this control point.  
`name` | The name of the control point (if any).  
  
addControlPoint(_controlPoint_) → None
    

addKey(_time_ , _controlPointOrDim_ , _view_) → None
    

addPositionKey(_time_ , _positionOrDim_ , _view_) → None
    

Adds a new key to the control point’s timeline. positionOrDim can either be a vector or a single scalar that specifies which component (xyzw) to add a key for.

dim
    

The dimensionality, or number of components, for this control point (usually 3 - x, y and pressure).

evaluate(_time_ , _view_) → [ControlPoint](nuke.curvelib.ControlPoint.html#nuke.curvelib.ControlPoint "nuke.curvelib.ControlPoint")
    

Evaluates the animated control point’s position at the specific time.

getControlPointKeyTimes(_view_) → list of floats
    

Get the list of times at which this control point has a key. The view parameter is optional.

getFlag(_flag_) → bool
    

Gets the specified flag. The parameter should be one of the FlagType constants.

getPosition(_time_ , _view_) → [CVec3](nuke.curvelib.CVec3.html#nuke.curvelib.CVec3 "nuke.curvelib.CVec3")
    

Get the position of this control point at a particular time. The time parameter is a float specifying which time to calculate the position for; the view parameter is the optional view name.

getPositionAnimCurve(_index_ , _view_) → [AnimCurve](nuke.curvelib.AnimCurve.html#nuke.curvelib.AnimCurve "nuke.curvelib.AnimCurve")
    

Returns the AnimCurve object containing the time line for the control point.

getPositionKeyTime(_index_ , _keyIndex_ , _view_) → float
    

Get the time of a particular key for this control point. index is 0 for the X coordinate, 1 for Y or 2 for Z. keyIndex is the index of the relevant key. The view parameter is optional.

hash
    

The hash value for this control point.

name
    

The name of the control point (if any).

removeAllKeys(_view_) → None
    

removeKey(_time_ , _view_) → None
    

removePositionKey(_time_ , _view_) → None
    

reset() → None
    

Resets the control point back to an initial empty state.

setFlag(_flag_ , _value_) → None
    

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.

setPosition(_position_ , _view_) → None
    

Sets the control point’s ‘constant’ position (the position used when there are no keys - see AnimCurve for further info). Calling this method when the control point has keys will have no effect.

setPositionAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the point’s AnimCurve object (its time line).

setPositionKey(_time_ , _index_ , _value_ , _id_ , _view_) → None
    

Sets an individual dimension (index) of a key to a specific value. The key to modify is identified by hash (id). The method fails if there is no key at the specified time.

[ Previous](nuke.curvelib.AnimCTransform.html "nuke.curvelib.AnimCTransform") [Next ](nuke.curvelib.AnimCurve.html "nuke.curvelib.AnimCurve")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
