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
  * nuke.splinewarp
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
    * [nuke.splinewarp.Stroke](nuke.splinewarp.Stroke.html)
    * [nuke.splinewarp.TransformOrder](nuke.splinewarp.TransformOrder.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * nuke.splinewarp
  * 


* * *

# nuke.splinewarp

The Python interface for used by SplineWarp

Use help(‘_splinewarp’) to get detailed help on the classes exposed here.

Classes

[`AnimAttributes`](nuke.splinewarp.AnimAttributes.html#nuke.splinewarp.AnimAttributes "nuke.splinewarp.AnimAttributes") | A collection of named attributes.  
---|---  
[`AnimCTransform`](nuke.splinewarp.AnimCTransform.html#nuke.splinewarp.AnimCTransform "nuke.splinewarp.AnimCTransform") | An animated transform, where each part of the transform is represented as a curve over time.  
[`AnimControlPoint`](nuke.splinewarp.AnimControlPoint.html#nuke.splinewarp.AnimControlPoint "nuke.splinewarp.AnimControlPoint") | An animated control point.  
[`AnimCurve`](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve") | An animated curve.  
[`AnimCurveKey`](nuke.splinewarp.AnimCurveKey.html#nuke.splinewarp.AnimCurveKey "nuke.splinewarp.AnimCurveKey") | A key value in a parametric curve represented as a value at a particular time.  
[`AnimCurveViews`](nuke.splinewarp.AnimCurveViews.html#nuke.splinewarp.AnimCurveViews "nuke.splinewarp.AnimCurveViews") |   
[`BaseCurve`](nuke.splinewarp.BaseCurve.html#nuke.splinewarp.BaseCurve "nuke.splinewarp.BaseCurve") | A base class for animated curves.  
[`CMatrix4`](nuke.splinewarp.CMatrix4.html#nuke.splinewarp.CMatrix4 "nuke.splinewarp.CMatrix4") | A 4x4 matrix with methods for affine transformations.  
[`CTransform`](nuke.splinewarp.CTransform.html#nuke.splinewarp.CTransform "nuke.splinewarp.CTransform") | A transform at a single point in time.  
[`CVec2`](nuke.splinewarp.CVec2.html#nuke.splinewarp.CVec2 "nuke.splinewarp.CVec2") | A 2-component vector.  
[`CVec3`](nuke.splinewarp.CVec3.html#nuke.splinewarp.CVec3 "nuke.splinewarp.CVec3") | A 3-component vector.  
[`CVec4`](nuke.splinewarp.CVec4.html#nuke.splinewarp.CVec4 "nuke.splinewarp.CVec4") | A 4-component vector.  
[`ControlPoint`](nuke.splinewarp.ControlPoint.html#nuke.splinewarp.ControlPoint "nuke.splinewarp.ControlPoint") | A control point at a particular point in time.  
[`CubicCurve`](nuke.splinewarp.CubicCurve.html#nuke.splinewarp.CubicCurve "nuke.splinewarp.CubicCurve") | A baked out curve for a specific frame and view.  
[`CurveKnob`](nuke.splinewarp.CurveKnob.html#nuke.splinewarp.CurveKnob "nuke.splinewarp.CurveKnob") | The knob which holds the tree of paint elements (Layers, Shapes and Strokes).  
[`CurveType`](nuke.splinewarp.CurveType.html#nuke.splinewarp.CurveType "nuke.splinewarp.CurveType") | Constants for use in parameters which require a curve type.  
[`Element`](nuke.splinewarp.Element.html#nuke.splinewarp.Element "nuke.splinewarp.Element") | The base class for the different types of elements you can create in the RotoPaint node.  
[`ExtrapolationType`](nuke.splinewarp.ExtrapolationType.html#nuke.splinewarp.ExtrapolationType "nuke.splinewarp.ExtrapolationType") | Constants for use in parameters which require an extrapolation type.  
[`Flag`](nuke.splinewarp.Flag.html#nuke.splinewarp.Flag "nuke.splinewarp.Flag") | A base class for objects which have a set of flags that can be set.  
[`FlagType`](nuke.splinewarp.FlagType.html#nuke.splinewarp.FlagType "nuke.splinewarp.FlagType") | Constants for use in parameters which require a flag type.  
[`InterpolationType`](nuke.splinewarp.InterpolationType.html#nuke.splinewarp.InterpolationType "nuke.splinewarp.InterpolationType") | Constants for use in parameters which require an interpolation type.  
[`Layer`](nuke.splinewarp.Layer.html#nuke.splinewarp.Layer "nuke.splinewarp.Layer") | A layer, used to group other elements in the paint tree.  
[`RotationOrder`](nuke.splinewarp.RotationOrder.html#nuke.splinewarp.RotationOrder "nuke.splinewarp.RotationOrder") | Constants for use in parameters which require a rotation order.  
[`Shape`](nuke.splinewarp.Shape.html#nuke.splinewarp.Shape "nuke.splinewarp.Shape") | A Roto or SplineWarp shape, which may be animated.  
[`ShapeControlPoint`](nuke.splinewarp.ShapeControlPoint.html#nuke.splinewarp.ShapeControlPoint "nuke.splinewarp.ShapeControlPoint") | A control point in a roto shape.  
[`SplineKnob`](nuke.splinewarp.SplineKnob.html#nuke.splinewarp.SplineKnob "nuke.splinewarp.SplineKnob") |   
[`Stroke`](nuke.splinewarp.Stroke.html#nuke.splinewarp.Stroke "nuke.splinewarp.Stroke") | A paint stroke, which may be animated.  
[`TransformOrder`](nuke.splinewarp.TransformOrder.html#nuke.splinewarp.TransformOrder "nuke.splinewarp.TransformOrder") | Constants for use in parameters which require a transform order.  
  
[ Previous](nuke.rotopaint.TransformOrder.html "nuke.rotopaint.TransformOrder") [Next ](nuke.splinewarp.AnimAttributes.html "nuke.splinewarp.AnimAttributes")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
