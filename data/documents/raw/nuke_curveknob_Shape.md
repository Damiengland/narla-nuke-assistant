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
    * [nuke.curveknob.CurveKnob](nuke.curveknob.CurveKnob.html)
    * [nuke.curveknob.CurveWidget](nuke.curveknob.CurveWidget.html)
    * [nuke.curveknob.Element](nuke.curveknob.Element.html)
    * [nuke.curveknob.Layer](nuke.curveknob.Layer.html)
    * nuke.curveknob.Shape
    * [nuke.curveknob.ShapeControlPoint](nuke.curveknob.ShapeControlPoint.html)
    * [nuke.curveknob.Stroke](nuke.curveknob.Stroke.html)
  * [nuke.curvelib](nuke.curvelib.html)
  * [nuke.gsv](nuke.gsv.html)
  * [nuke.localization](nuke.localization.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.curveknob](nuke.curveknob.html) »
  * nuke.curveknob.Shape
  * 


* * *

# nuke.curveknob.Shape

_class _nuke.curveknob.Shape
    

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
    

evaluate(_curveNum_ , _time_ , _viewName ='default'_) → [CubicCurve](nuke.curvelib.CubicCurve.html#nuke.curvelib.CubicCurve "nuke.curvelib.CubicCurve")
    

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




getAttributes() → [AnimAttributes](nuke.curvelib.AnimAttributes.html#nuke.curvelib.AnimAttributes "nuke.curvelib.AnimAttributes")
    

Gets the collection of attributes for this shape.

getFlag(_flag_) → bool
    

Check whether a particular flag is set or not. The flag parameter should be one of the constants from the FlagType class. The return value will be True if the flag is set, False if it isn’t.

getTransform() → [AnimCTransform](nuke.curvelib.AnimCTransform.html#nuke.curvelib.AnimCTransform "nuke.curvelib.AnimCTransform")
    

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

[ Previous](nuke.curveknob.Layer.html "nuke.curveknob.Layer") [Next ](nuke.curveknob.ShapeControlPoint.html "nuke.curveknob.ShapeControlPoint")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
