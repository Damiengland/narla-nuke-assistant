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
    * nuke.splinewarp.Shape
    * [nuke.splinewarp.ShapeControlPoint](nuke.splinewarp.ShapeControlPoint.html)
    * [nuke.splinewarp.SplineKnob](nuke.splinewarp.SplineKnob.html)
    * [nuke.splinewarp.Stroke](nuke.splinewarp.Stroke.html)
    * [nuke.splinewarp.TransformOrder](nuke.splinewarp.TransformOrder.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.splinewarp](nuke.splinewarp.html) »
  * nuke.splinewarp.Shape
  * 


* * *

# nuke.splinewarp.Shape

_class _nuke.splinewarp.Shape
    

Bases: [`_curveknob.Element`](nuke.splinewarp.Element.html#nuke.splinewarp.Element "_curveknob.Element")

A Roto or SplineWarp shape, which may be animated.

Shapes are represented as a sequence of ShapeControlPoint objects, which group together a ‘center’ control point along with tangent locations and feather offsets. Python’s built-in len() function can be used to get the number of shape control points; and array-style access can be used to get individual shape control points (e.g. shape[0] returns the first shape control point, shape[-1] returns the last shape control point, etc.). You can create a new shape as follows:

>>>import _curveknob >>>rotoNode = nuke.toNode(‘RotoPaint1’) >>>curveKnob = rotoNode[‘curves’] >>>emptyShape = _curveknob.Shape( curveKnob ) >>>twoPointShape = _curveknob.Shape( curveKnob, *((0,0), (10,10)) ) >>> # perform operations on the shape(s).

NOTE: this object was designed to work for Roto shapes, which have feather
    

curves. Please report any problems with this type to [support@thefoundry.co.uk](mailto:support%40thefoundry.co.uk)

Methods

`append` | Add a new control point to the shape.  
---|---  
`clone` |   
`evaluate` | Bake out a curve for the outline of this shape at the specified time.  
`getAttributes` | Gets the collection of attributes for this shape.  
`getFlag` | Check whether a particular flag is set or not.  
`getTransform` | Gets the transform for this shape.  
`getVisible` | Get the value of the visible attribute at a particular time.  
`insert` | Insert a new control point in the shape before the given index.  
`remove` | Remove the control point at the given index.  
`serialise` | Returns a string representation of the given element.  
`setFlag` | Set a particular flag.  
`setVisible` | Set the value of the visible attribute at a particular time.  
  
Attributes

`locked` | Whether this element is locked.  
---|---  
`name` | The name for this element.  
  
append(_shapeControlPoint_) → None
    

Add a new control point to the shape. The shapeControlPoint parameter must be either an instance of the ShapeControlPoint class, or something we can convert to a ShapeControlPoint. This includes a sequence of 2, 3 or 4 floats; a CVec2, CVec3 or CVec4 object; or an AnimControlPoint object.

clone() → elementCreate clone of element
    

evaluate(_curveNum_ , _time_ , _viewName ='default'_) → [CubicCurve](nuke.splinewarp.CubicCurve.html#nuke.splinewarp.CubicCurve "nuke.splinewarp.CubicCurve")
    

Bake out a curve for the outline of this shape at the specified time.

Note that the feather curve is represented as an offset from the main curve. If you want to get the screen position of a point along the feather curve, you’ll need to add it to the corresponding position on the main curve. For example:
    
    
    
    ```python
    >>> frameNum = 10.0
    >>> t = 0.5
    >>> rotoknob = nuke.toNode('RotoPaint1')['curves']
    >>> shape = rotoknob.toElement('Bezier1')
    >>> mainCurve = shape.evaluate(0, frameNum)
    >>> featherCurve = shape.evaluate(1, frameNum)
    >>> pointOnMainCurve = mainCurve.getPoint(t)
    >>> featherOffset = featherCurve.getPoint(t)
    >>> pointOnFeatherCurve = pointOnMainCurve + featherOffset
    ```

Parameters
    

  * **curveNum** – 0 for the main curve, 1 for the feather curve.

  * **time** – The (floating point) frame number to bake the curve from.

  * **viewName** – Optional parameter specifying which view to bake the curve from. If omitted, the default view will be used.




getAttributes() → [AnimAttributes](nuke.splinewarp.AnimAttributes.html#nuke.splinewarp.AnimAttributes "nuke.splinewarp.AnimAttributes")
    

Gets the collection of attributes for this shape.

getFlag(_flag_) → bool
    

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.

getTransform() → [AnimCTransform](nuke.splinewarp.AnimCTransform.html#nuke.splinewarp.AnimCTransform "nuke.splinewarp.AnimCTransform")
    

Gets the transform for this shape.

getVisible(_time_) → bool
    

Get the value of the visible attribute at a particular time.

insert(_index_ , _shapeControlPoint_) → None
    

Insert a new control point in the shape before the given index. The shapeControlPoint parameter must be either an instance of the ShapeControlPoint class, or something we can convert to a ShapeControlPoint. This includes a sequence of 2, 3 or 4 floats; a CVec2, CVec3 or CVec4 object; or an AnimControlPoint object.

locked
    

Whether this element is locked.

name
    

The name for this element.

remove(_index_) → None
    

Remove the control point at the given index. This removes any associated tangent and feather point data as well. If the index is out of bounds, an IndexError will be raised.

serialise() → string
    

Returns a string representation of the given element.

setFlag(_flag_ , _value_) → None
    

Set a particular flag. The flag parameter specifies which flag to set and should be one of the constants from the FlagType class. The value parameter is a boolean value; True will set the flag, False will clear it.

setVisible(_time_ , _value_) → None
    

Set the value of the visible attribute at a particular time. value must be a bool.

[ Previous](nuke.splinewarp.RotationOrder.html "nuke.splinewarp.RotationOrder") [Next ](nuke.splinewarp.ShapeControlPoint.html "nuke.splinewarp.ShapeControlPoint")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
