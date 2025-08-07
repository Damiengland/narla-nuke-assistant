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
    * nuke.rotopaint.Stroke
    * [nuke.rotopaint.TransformOrder](nuke.rotopaint.TransformOrder.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.rotopaint](nuke.rotopaint.html) »
  * nuke.rotopaint.Stroke
  * 


* * *

# nuke.rotopaint.Stroke

_class _nuke.rotopaint.Stroke
    

Bases: [`_curveknob.Element`](nuke.splinewarp.Element.html#nuke.splinewarp.Element "_curveknob.Element")

A paint stroke, which may be animated.

A paint stroke is represented as a sequence of AnimControlPoint objects. You can find out how many control points there are in the stroke using python’s built-in len() function; and you can access individual control points using the array-style syntax (e.g. stroke[0] returns the first control point, stroke[-1] returns the last control point, etc.).

Methods

`append` | Add a new control point to the stroke.  
---|---  
`clone` |   
`evaluate` | Bake out a curve for the path of this stroke at the specified time.  
`getAttributes` | Gets the collection of attributes for this stroke.  
`getFlag` | Check whether a particular flag is set or not.  
`getTransform` | Gets the transform for this shape.  
`getVisible` | Get the value of the visible attribute at a particular time.  
`insert` | Insert a new control point in the stroke before the given index.  
`remove` | Remove the control point at the given index.  
`serialise` | Returns a string representation of the given element.  
`setFlag` | Set a particular flag.  
`setVisible` | Set the value of the visible attribute at a particular time.  
  
Attributes

`locked` | Whether this element is locked.  
---|---  
`name` | The name for this element.  
  
append(_controlPoint_) → None
    

Add a new control point to the stroke. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.

clone() → elementCreate clone of element
    

evaluate(_time_ , _viewName ='default'_) → [CubicCurve](nuke.rotopaint.CubicCurve.html#nuke.rotopaint.CubicCurve "nuke.rotopaint.CubicCurve")
    

Bake out a curve for the path of this stroke at the specified time. :param time: The (floating point) frame number to bake the curve from. :param viewName: Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.

getAttributes() → [AnimAttributes](nuke.rotopaint.AnimAttributes.html#nuke.rotopaint.AnimAttributes "nuke.rotopaint.AnimAttributes")
    

Gets the collection of attributes for this stroke.

getFlag(_flag_) → bool
    

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.

getTransform() → [AnimCTransform](nuke.rotopaint.AnimCTransform.html#nuke.rotopaint.AnimCTransform "nuke.rotopaint.AnimCTransform")
    

Gets the transform for this shape.

getVisible(_time_) → bool
    

Get the value of the visible attribute at a particular time.

insert(_index_ , _controlPoint_) → None
    

Insert a new control point in the stroke before the given index. The controlPoint parameter must be either an instance of the AnimControlPoint class, or something we can convert to an AnimControlPoint. This includes a sequence of 2, 3 or 4 floats; or a CVec2, CVec3 or CVec4 object.

locked
    

Whether this element is locked.

name
    

The name for this element.

remove(_index_) → None
    

Remove the control point at the given index. If the index is out of bounds, an IndexError will be raised.

serialise() → string
    

Returns a string representation of the given element.

setFlag(_flag_ , _value_) → None
    

Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.

setVisible(_time_ , _value_) → None
    

Set the value of the visible attribute at a particular time. value must be a bool.

[ Previous](nuke.rotopaint.ShapeControlPoint.html "nuke.rotopaint.ShapeControlPoint") [Next ](nuke.rotopaint.TransformOrder.html "nuke.rotopaint.TransformOrder")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
