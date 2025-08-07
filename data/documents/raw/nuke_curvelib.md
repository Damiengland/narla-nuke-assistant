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
  * nuke.curvelib
    * [nuke.curvelib.AnimAttributes](nuke.curvelib.AnimAttributes.html)
    * [nuke.curvelib.AnimCTransform](nuke.curvelib.AnimCTransform.html)
    * [nuke.curvelib.AnimControlPoint](nuke.curvelib.AnimControlPoint.html)
    * [nuke.curvelib.AnimCurve](nuke.curvelib.AnimCurve.html)
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
  * nuke.curvelib
  * 


* * *

# nuke.curvelib

The Python API for the Nuke’s core curve library

Classes

[`AnimAttributes`](nuke.curvelib.AnimAttributes.html#nuke.curvelib.AnimAttributes "nuke.curvelib.AnimAttributes") | A collection of named attributes.  
---|---  
[`AnimCTransform`](nuke.curvelib.AnimCTransform.html#nuke.curvelib.AnimCTransform "nuke.curvelib.AnimCTransform") | An animated transform, where each part of the transform is represented as a curve over time.  
[`AnimControlPoint`](nuke.curvelib.AnimControlPoint.html#nuke.curvelib.AnimControlPoint "nuke.curvelib.AnimControlPoint") | An animated control point.  
[`AnimCurve`](nuke.curvelib.AnimCurve.html#nuke.curvelib.AnimCurve "nuke.curvelib.AnimCurve") | An animated curve.  
[`AnimCurveKey`](nuke.curvelib.AnimCurveKey.html#nuke.curvelib.AnimCurveKey "nuke.curvelib.AnimCurveKey") | A key value in a parametric curve represented as a value at a particular time.  
[`AnimCurveViews`](nuke.curvelib.AnimCurveViews.html#nuke.curvelib.AnimCurveViews "nuke.curvelib.AnimCurveViews") |   
[`BaseCurve`](nuke.curvelib.BaseCurve.html#nuke.curvelib.BaseCurve "nuke.curvelib.BaseCurve") | A base class for animated curves.  
[`CMatrix4`](nuke.curvelib.CMatrix4.html#nuke.curvelib.CMatrix4 "nuke.curvelib.CMatrix4") | A 4x4 matrix with methods for affine transformations.  
[`CTransform`](nuke.curvelib.CTransform.html#nuke.curvelib.CTransform "nuke.curvelib.CTransform") | A transform at a single point in time.  
[`CVec2`](nuke.curvelib.CVec2.html#nuke.curvelib.CVec2 "nuke.curvelib.CVec2") | A 2-component vector.  
[`CVec3`](nuke.curvelib.CVec3.html#nuke.curvelib.CVec3 "nuke.curvelib.CVec3") | A 3-component vector.  
[`CVec4`](nuke.curvelib.CVec4.html#nuke.curvelib.CVec4 "nuke.curvelib.CVec4") | A 4-component vector.  
[`ControlPoint`](nuke.curvelib.ControlPoint.html#nuke.curvelib.ControlPoint "nuke.curvelib.ControlPoint") | A control point at a particular point in time.  
[`CorrespondencePoints`](nuke.curvelib.CorrespondencePoints.html#nuke.curvelib.CorrespondencePoints "nuke.curvelib.CorrespondencePoints") | Correspondence points add a relation to the interpolation of two curves.  
[`CubicCurve`](nuke.curvelib.CubicCurve.html#nuke.curvelib.CubicCurve "nuke.curvelib.CubicCurve") | A baked out curve for a specific frame and view.  
[`CurveType`](nuke.curvelib.CurveType.html#nuke.curvelib.CurveType "nuke.curvelib.CurveType") | Constants for use in parameters which require a curve type.  
[`ExtrapolationType`](nuke.curvelib.ExtrapolationType.html#nuke.curvelib.ExtrapolationType "nuke.curvelib.ExtrapolationType") | Constants for use in parameters which require an extrapolation type.  
[`Flag`](nuke.curvelib.Flag.html#nuke.curvelib.Flag "nuke.curvelib.Flag") | A base class for objects which have a set of flags that can be set.  
[`FlagType`](nuke.curvelib.FlagType.html#nuke.curvelib.FlagType "nuke.curvelib.FlagType") | Constants for use in parameters which require a flag type.  
[`InterpolationType`](nuke.curvelib.InterpolationType.html#nuke.curvelib.InterpolationType "nuke.curvelib.InterpolationType") | Constants for use in parameters which require an interpolation type.  
[`RotationOrder`](nuke.curvelib.RotationOrder.html#nuke.curvelib.RotationOrder "nuke.curvelib.RotationOrder") | Constants for use in parameters which require a rotation order.  
[`TransformOrder`](nuke.curvelib.TransformOrder.html#nuke.curvelib.TransformOrder "nuke.curvelib.TransformOrder") | Constants for use in parameters which require a transform order.  
  
[ Previous](nuke.curveknob.Stroke.html "nuke.curveknob.Stroke") [Next ](nuke.curvelib.AnimAttributes.html "nuke.curvelib.AnimAttributes")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
