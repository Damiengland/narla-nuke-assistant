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
    * [nuke.curvelib.AnimControlPoint](nuke.curvelib.AnimControlPoint.html)
    * nuke.curvelib.AnimCurve
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
  * nuke.curvelib.AnimCurve
  * 


* * *

# nuke.curvelib.AnimCurve

_class _nuke.curvelib.AnimCurve
    

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

getKey(_index_) → [AnimCurveKey](nuke.curvelib.AnimCurveKey.html#nuke.curvelib.AnimCurveKey "nuke.curvelib.AnimCurveKey")
    

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

[ Previous](nuke.curvelib.AnimControlPoint.html "nuke.curvelib.AnimControlPoint") [Next ](nuke.curvelib.AnimCurveKey.html "nuke.curvelib.AnimCurveKey")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
