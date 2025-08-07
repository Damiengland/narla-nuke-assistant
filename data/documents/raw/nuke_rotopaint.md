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
  * nuke.rotopaint
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
    * [nuke.rotopaint.Stroke](nuke.rotopaint.Stroke.html)
    * [nuke.rotopaint.TransformOrder](nuke.rotopaint.TransformOrder.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * nuke.rotopaint
  * 


* * *

# nuke.rotopaint

The Python interface for RotoPaint

Use help(‘_rotopaint’) to get detailed help on the classes exposed here.

Functions

[`convertDirectoryToNuke6`](nuke.rotopaint.convertDirectoryToNuke6.html#nuke.rotopaint.convertDirectoryToNuke6 "nuke.rotopaint.convertDirectoryToNuke6") | Convert a directory containing NUKE 7 roto scripts in one containing the old format.  
---|---  
[`convertDirectoryToNuke7`](nuke.rotopaint.convertDirectoryToNuke7.html#nuke.rotopaint.convertDirectoryToNuke7 "nuke.rotopaint.convertDirectoryToNuke7") | Convert a directory containing NUKE 6 roto scripts in one containing the new format.  
[`convertToNuke6`](nuke.rotopaint.convertToNuke6.html#nuke.rotopaint.convertToNuke6 "nuke.rotopaint.convertToNuke6") | Convert a script containing NUKE 7 roto in one containing the old format.  
[`convertToNuke7`](nuke.rotopaint.convertToNuke7.html#nuke.rotopaint.convertToNuke7 "nuke.rotopaint.convertToNuke7") | Convert a script containing NUKE 6 roto in one containing the new format.  
  
Classes

[`AnimAttributes`](nuke.rotopaint.AnimAttributes.html#nuke.rotopaint.AnimAttributes "nuke.rotopaint.AnimAttributes") | A collection of named attributes.  
---|---  
[`AnimCTransform`](nuke.rotopaint.AnimCTransform.html#nuke.rotopaint.AnimCTransform "nuke.rotopaint.AnimCTransform") | An animated transform, where each part of the transform is represented as a curve over time.  
[`AnimControlPoint`](nuke.rotopaint.AnimControlPoint.html#nuke.rotopaint.AnimControlPoint "nuke.rotopaint.AnimControlPoint") | An animated control point.  
[`AnimCurve`](nuke.rotopaint.AnimCurve.html#nuke.rotopaint.AnimCurve "nuke.rotopaint.AnimCurve") | An animated curve.  
[`AnimCurveKey`](nuke.rotopaint.AnimCurveKey.html#nuke.rotopaint.AnimCurveKey "nuke.rotopaint.AnimCurveKey") | A key value in a parametric curve represented as a value at a particular time.  
[`AnimCurveViews`](nuke.rotopaint.AnimCurveViews.html#nuke.rotopaint.AnimCurveViews "nuke.rotopaint.AnimCurveViews") |   
[`BaseCurve`](nuke.rotopaint.BaseCurve.html#nuke.rotopaint.BaseCurve "nuke.rotopaint.BaseCurve") | A base class for animated curves.  
[`CMatrix4`](nuke.rotopaint.CMatrix4.html#nuke.rotopaint.CMatrix4 "nuke.rotopaint.CMatrix4") | A 4x4 matrix with methods for affine transformations.  
[`CTransform`](nuke.rotopaint.CTransform.html#nuke.rotopaint.CTransform "nuke.rotopaint.CTransform") | A transform at a single point in time.  
[`CVec2`](nuke.rotopaint.CVec2.html#nuke.rotopaint.CVec2 "nuke.rotopaint.CVec2") | A 2-component vector.  
[`CVec3`](nuke.rotopaint.CVec3.html#nuke.rotopaint.CVec3 "nuke.rotopaint.CVec3") | A 3-component vector.  
[`CVec4`](nuke.rotopaint.CVec4.html#nuke.rotopaint.CVec4 "nuke.rotopaint.CVec4") | A 4-component vector.  
[`ControlPoint`](nuke.rotopaint.ControlPoint.html#nuke.rotopaint.ControlPoint "nuke.rotopaint.ControlPoint") | A control point at a particular point in time.  
[`CubicCurve`](nuke.rotopaint.CubicCurve.html#nuke.rotopaint.CubicCurve "nuke.rotopaint.CubicCurve") | A baked out curve for a specific frame and view.  
[`CurveKnob`](nuke.rotopaint.CurveKnob.html#nuke.rotopaint.CurveKnob "nuke.rotopaint.CurveKnob") | The knob which holds the tree of paint elements (Layers, Shapes and Strokes).  
[`CurveType`](nuke.rotopaint.CurveType.html#nuke.rotopaint.CurveType "nuke.rotopaint.CurveType") | Constants for use in parameters which require a curve type.  
[`Element`](nuke.rotopaint.Element.html#nuke.rotopaint.Element "nuke.rotopaint.Element") | The base class for the different types of elements you can create in the RotoPaint node.  
[`ExtrapolationType`](nuke.rotopaint.ExtrapolationType.html#nuke.rotopaint.ExtrapolationType "nuke.rotopaint.ExtrapolationType") | Constants for use in parameters which require an extrapolation type.  
[`Flag`](nuke.rotopaint.Flag.html#nuke.rotopaint.Flag "nuke.rotopaint.Flag") | A base class for objects which have a set of flags that can be set.  
[`FlagType`](nuke.rotopaint.FlagType.html#nuke.rotopaint.FlagType "nuke.rotopaint.FlagType") | Constants for use in parameters which require a flag type.  
[`Hash`](nuke.rotopaint.Hash.html#nuke.rotopaint.Hash "nuke.rotopaint.Hash") | A hash value for any number of objects.  
[`InterpolationType`](nuke.rotopaint.InterpolationType.html#nuke.rotopaint.InterpolationType "nuke.rotopaint.InterpolationType") | Constants for use in parameters which require an interpolation type.  
[`Layer`](nuke.rotopaint.Layer.html#nuke.rotopaint.Layer "nuke.rotopaint.Layer") | A layer, used to group other elements in the paint tree.  
[`RotationOrder`](nuke.rotopaint.RotationOrder.html#nuke.rotopaint.RotationOrder "nuke.rotopaint.RotationOrder") | Constants for use in parameters which require a rotation order.  
[`Shape`](nuke.rotopaint.Shape.html#nuke.rotopaint.Shape "nuke.rotopaint.Shape") | A Roto or SplineWarp shape, which may be animated.  
[`ShapeControlPoint`](nuke.rotopaint.ShapeControlPoint.html#nuke.rotopaint.ShapeControlPoint "nuke.rotopaint.ShapeControlPoint") | A control point in a roto shape.  
[`Stroke`](nuke.rotopaint.Stroke.html#nuke.rotopaint.Stroke "nuke.rotopaint.Stroke") | A paint stroke, which may be animated.  
[`TransformOrder`](nuke.rotopaint.TransformOrder.html#nuke.rotopaint.TransformOrder "nuke.rotopaint.TransformOrder") | Constants for use in parameters which require a transform order.  
  
[ Previous](nuke.nukemath.Vector4.html "nuke.nukemath.Vector4") [Next ](nuke.rotopaint.convertDirectoryToNuke6.html "nuke.rotopaint.convertDirectoryToNuke6")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
