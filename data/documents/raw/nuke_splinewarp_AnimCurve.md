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
    * nuke.splinewarp.AnimCurve
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
    * [nuke.splinewarp.SplineKnob](nuke.splinewarp.SplineKnob.html)
    * [nuke.splinewarp.Stroke](nuke.splinewarp.Stroke.html)
    * [nuke.splinewarp.TransformOrder](nuke.splinewarp.TransformOrder.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.splinewarp](nuke.splinewarp.html) »
  * nuke.splinewarp.AnimCurve
  * 


* * *

# nuke.splinewarp.AnimCurve

_class _nuke.splinewarp.AnimCurve
    

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

getKey(_index_) → [AnimCurveKey](nuke.splinewarp.AnimCurveKey.html#nuke.splinewarp.AnimCurveKey "nuke.splinewarp.AnimCurveKey")
    

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

[ Previous](nuke.splinewarp.AnimControlPoint.html "nuke.splinewarp.AnimControlPoint") [Next ](nuke.splinewarp.AnimCurveKey.html "nuke.splinewarp.AnimCurveKey")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
