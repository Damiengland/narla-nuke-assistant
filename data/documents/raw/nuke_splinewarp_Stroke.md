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
    * [nuke.splinewarp.SplineKnob](nuke.splinewarp.SplineKnob.html)
    * nuke.splinewarp.Stroke
    * [nuke.splinewarp.TransformOrder](nuke.splinewarp.TransformOrder.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.splinewarp](nuke.splinewarp.html) »
  * nuke.splinewarp.Stroke
  * 


* * *

# nuke.splinewarp.Stroke

_class _nuke.splinewarp.Stroke
    

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
    

evaluate(_time_ , _viewName ='default'_) → [CubicCurve](nuke.splinewarp.CubicCurve.html#nuke.splinewarp.CubicCurve "nuke.splinewarp.CubicCurve")
    

Bake out a curve for the path of this stroke at the specified time. :param time: The (floating point) frame number to bake the curve from. :param viewName: Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.

getAttributes() → [AnimAttributes](nuke.splinewarp.AnimAttributes.html#nuke.splinewarp.AnimAttributes "nuke.splinewarp.AnimAttributes")
    

Gets the collection of attributes for this stroke.

getFlag(_flag_) → bool
    

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.

getTransform() → [AnimCTransform](nuke.splinewarp.AnimCTransform.html#nuke.splinewarp.AnimCTransform "nuke.splinewarp.AnimCTransform")
    

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

[ Previous](nuke.splinewarp.SplineKnob.html "nuke.splinewarp.SplineKnob") [Next ](nuke.splinewarp.TransformOrder.html "nuke.splinewarp.TransformOrder")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
