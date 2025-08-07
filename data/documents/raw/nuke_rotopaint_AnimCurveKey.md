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
    * [nuke.rotopaint.AnimCurve](nuke.rotopaint.AnimCurve.html)
    * nuke.rotopaint.AnimCurveKey
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
  * nuke.rotopaint.AnimCurveKey
  * 


* * *

# nuke.rotopaint.AnimCurveKey

_class _nuke.rotopaint.AnimCurveKey
    

Bases: [`_curvelib.Flag`](nuke.splinewarp.Flag.html#nuke.splinewarp.Flag "_curvelib.Flag")

A key value in a parametric curve represented as a value at a particular time.

Methods

`getFlag` | Gets the specified flag.  
---|---  
`reset` | Reset this key to its default values.  
`setFlag` | Set or clear the specified flag.  
  
Attributes

`interpolationType` | The interpolation type to use for this key.  
---|---  
`kDefaultAnimCurveKeyInterpolation` |   
`kDefaultAnimCurveKeyTime` |   
`kDefaultAnimCurveKeyValue` |   
`la` | The left bicubic value for this key.  
`lslope` | The left derivative for this key.  
`ra` | The right bicubic value for this key.  
`rslope` | The right derivative for this key.  
`time` | The time this key is set at.  
`value` | The value for this key.  
  
getFlag(_flag_) → bool
    

Gets the specified flag. The parameter should be one of the FlagType constants.

interpolationType
    

The interpolation type to use for this key.

la
    

The left bicubic value for this key.

lslope
    

The left derivative for this key.

ra
    

The right bicubic value for this key.

reset() → None
    

Reset this key to its default values.

rslope
    

The right derivative for this key.

setFlag(_flag_ , _value_) → None
    

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.

time
    

The time this key is set at.

value
    

The value for this key.

[ Previous](nuke.rotopaint.AnimCurve.html "nuke.rotopaint.AnimCurve") [Next ](nuke.rotopaint.AnimCurveViews.html "nuke.rotopaint.AnimCurveViews")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
