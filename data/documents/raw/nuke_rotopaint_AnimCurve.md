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
    * [nuke.rotopaint.convertDirectoryToNuke6](nuke.rotopaint.convertDirectoryToNuke6.html)
    * [nuke.rotopaint.convertDirectoryToNuke7](nuke.rotopaint.convertDirectoryToNuke7.html)
    * [nuke.rotopaint.convertToNuke6](nuke.rotopaint.convertToNuke6.html)
    * [nuke.rotopaint.convertToNuke7](nuke.rotopaint.convertToNuke7.html)
    * [nuke.rotopaint.AnimAttributes](nuke.rotopaint.AnimAttributes.html)
    * [nuke.rotopaint.AnimCTransform](nuke.rotopaint.AnimCTransform.html)
    * [nuke.rotopaint.AnimControlPoint](nuke.rotopaint.AnimControlPoint.html)
    * nuke.rotopaint.AnimCurve
    * [nuke.rotopaint.AnimCurveKey](nuke.rotopaint.AnimCurveKey.html)
    * [nuke.rotopaint.AnimCurveViews](nuke.rotopaint.AnimCurveViews.html)
    * [nuke.rotopaint.BaseCurve](nuke.rotopaint.BaseCurve.html)
    * [nuke.rotopaint.CMatrix4](nuke.rotopaint.CMatrix4.html)
    * [nuke.rotopaint.CTransform](nuke.rotopaint.CTransform.html)
    * [nuke.rotopaint.CVec2](nuke.rotopaint.CVec2.html)
    * [nuke.rotopaint.CVec3](nuke.rotopaint.CVec3.html)
    * [nuke.rotopaint.CVec4](nuke.rotopaint.CVec4.html)
    * [nuke.rotopaint.ControlPoint](nuke.rotopaint.ControlPoint.html)
    * [nuke.rotopaint.CubicCurve](nuke.rotopaint.CubicCurve.html)
    * [nuke.rotopaint.CurveKnob](nuke.rotopaint.CurveKnob.html)
    * [nuke.rotopaint.CurveType](nuke.rotopaint.CurveType.html)
    * [nuke.rotopaint.Element](nuke.rotopaint.Element.html)
    * [nuke.rotopaint.ExtrapolationType](nuke.rotopaint.ExtrapolationType.html)
    * [nuke.rotopaint.Flag](nuke.rotopaint.Flag.html)
    * [nuke.rotopaint.FlagType](nuke.rotopaint.FlagType.html)
    * [nuke.rotopaint.Hash](nuke.rotopaint.Hash.html)
    * [nuke.rotopaint.InterpolationType](nuke.rotopaint.InterpolationType.html)
    * [nuke.rotopaint.Layer](nuke.rotopaint.Layer.html)
    * [nuke.rotopaint.RotationOrder](nuke.rotopaint.RotationOrder.html)
    * [nuke.rotopaint.Shape](nuke.rotopaint.Shape.html)
    * [nuke.rotopaint.ShapeControlPoint](nuke.rotopaint.ShapeControlPoint.html)
    * [nuke.rotopaint.Stroke](nuke.rotopaint.Stroke.html)
    * [nuke.rotopaint.TransformOrder](nuke.rotopaint.TransformOrder.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.rotopaint](nuke.rotopaint.html) »
  * nuke.rotopaint.AnimCurve
  * 


* * *

# nuke.rotopaint.AnimCurve

_class _nuke.rotopaint.AnimCurve
    

Bases: [`_curvelib.BaseCurve`](nuke.splinewarp.BaseCurve.html#nuke.splinewarp.BaseCurve "_curvelib.BaseCurve")

An animated curve. The curve is described as a series of key values (instances of the AnimCurveKey class) which say what value it should have a particular time. For any time in between keys, the neighbouring key values are interpolated based on a curve type and interpolation settings specified at each key.

Each curve can only represent a single floating point value over time.

Methods

`addKey` | Add a new key to this curve.  
---|---  
`evaluate` | Calculate the value of the curve at a specific time, the pass that in to the expression for the curve.  
`evaluateY` | Calculates the value of the curve at a specific time.  
`getFlag` | Gets the specified flag.  
`getKey` | Returns one of the keys on this curve.  
`getNumberOfKeys` | Returns the number of keys along this curve.  
`isDefault` | Check whether this curve has been modified away from its default values.  
`removeAllKeys` | Removes all keys from this curve.  
`removeKey` | Remove an existing key from this curve.  
`reset` | Reset this object to its default values.  
`setFlag` | Set or clear the specified flag.  
  
Attributes

`constantValue` | The constant (not-animated) value for this curve, if any.  
---|---  
`curveTension` | The tension type for this curve.  
`curveType` | The type of curve to treat this as.  
`expressionString` | The expression string for the this curve, if any.  
`kDefaultConstantValue` |   
`kDefaultCurveFlag` |   
`kDefaultCurveTension` |   
`kDefaultCurveType` |   
`name` | The name for this curve.  
`useExpression` | Whether or not to use the expression string to calculate a value for this curve.  
  
addKey(_time_ , _value_) → None
addKey(_keyObj_) → None
    

Add a new key to this curve. You can pass in either a time and value pair (the value parameter is optional), or an AnimCurveKey object you’ve created yourself. In the former case, a new AnimCurveKey object will be created and added to the curve; in the latter case, the key you pass in will be added directly.

constantValue
    

The constant (not-animated) value for this curve, if any.

curveTension
    

The tension type for this curve.

curveType
    

The type of curve to treat this as.

evaluate(_time_) → float
    

Calculate the value of the curve at a specific time, the pass that in to the expression for the curve. The return value is the result of the expression.

evaluateY(_time_) → float
    

Calculates the value of the curve at a specific time.

expressionString
    

The expression string for the this curve, if any.

getFlag(_flag_) → bool
    

Gets the specified flag. The parameter should be one of the FlagType constants.

getKey(_index_) → [AnimCurveKey](nuke.rotopaint.AnimCurveKey.html#nuke.rotopaint.AnimCurveKey "nuke.rotopaint.AnimCurveKey")
    

Returns one of the keys on this curve.

getNumberOfKeys() → int
    

Returns the number of keys along this curve.

isDefault() → bool
    

Check whether this curve has been modified away from its default values.

name
    

The name for this curve.

removeAllKeys() → None
    

Removes all keys from this curve.

removeKey(_timeOrHash_) → None
    

Remove an existing key from this curve. The key is identified by either the time it occurs at, or its hash (as returned by the key’s getHash() method.

reset() → None
    

Reset this object to its default values.

setFlag(_flag_ , _value_) → None
    

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.

useExpression
    

Whether or not to use the expression string to calculate a value for this curve.

[ Previous](nuke.rotopaint.AnimControlPoint.html "nuke.rotopaint.AnimControlPoint") [Next ](nuke.rotopaint.AnimCurveKey.html "nuke.rotopaint.AnimCurveKey")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
