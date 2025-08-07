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
    * nuke.splinewarp.CTransform
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
  * nuke.splinewarp.CTransform
  * 


* * *

# nuke.splinewarp.CTransform

_class _nuke.splinewarp.CTransform
    

Bases: `object`

A transform at a single point in time.

This is the result of evaluating an AnimTransform for a particular time.

Methods

`getInverseMatrix` | Gets the inverse transform matrix, which can be used for undoing the effects of this transform.  
---|---  
`getMatrix` | Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.  
`getTransposeMatrix` | Returns a transposed copy of the matrix representing this transform.  
`isDefault` | Returns True if this transform matches the default settings, False if not.  
`reset` | Return this transform to its default settings.  
`setIdentity` | Set this transform to the identity transform (the transform which doesn't change the object at all).  
  
Attributes

`name` | The name for this transform.  
---|---  
`pivotPoint` | The location of the pivot point, represented as a CVec3 object.  
`rotation` | The rotation amounts, represented as a CVec3 object.  
`rotationOrder` | Indicates which order to apply the rotations in.  
`scale` | The scale factors, represented as a CVec3 object.  
`skew` | The skew amounts, represented as a CVec3 object.  
`transformOrder` | Indicates which order to apply the transformations in.  
`translation` | The translation amounts, represented as a CVec3 object.  
  
getInverseMatrix() → [CMatrix4](nuke.splinewarp.CMatrix4.html#nuke.splinewarp.CMatrix4 "nuke.splinewarp.CMatrix4")
    

Gets the inverse transform matrix, which can be used for undoing the effects of this transform.

getMatrix() → [CMatrix4](nuke.splinewarp.CMatrix4.html#nuke.splinewarp.CMatrix4 "nuke.splinewarp.CMatrix4")
    

Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.

getTransposeMatrix() → [CMatrix4](nuke.splinewarp.CMatrix4.html#nuke.splinewarp.CMatrix4 "nuke.splinewarp.CMatrix4")
    

Returns a transposed copy of the matrix representing this transform.

isDefault() → bool
    

Returns True if this transform matches the default settings, False if not.

name
    

The name for this transform.

pivotPoint
    

The location of the pivot point, represented as a CVec3 object.

reset() → None
    

Return this transform to its default settings.

rotation
    

The rotation amounts, represented as a CVec3 object.

rotationOrder
    

Indicates which order to apply the rotations in. The value will be one of the constants from the RotationOrder class.

scale
    

The scale factors, represented as a CVec3 object.

setIdentity() → None
    

Set this transform to the identity transform (the transform which doesn’t change the object at all).

skew
    

The skew amounts, represented as a CVec3 object.

transformOrder
    

Indicates which order to apply the transformations in. The value will be one of the constants from the TransformOrder class.

translation
    

The translation amounts, represented as a CVec3 object.

[ Previous](nuke.splinewarp.CMatrix4.html "nuke.splinewarp.CMatrix4") [Next ](nuke.splinewarp.CVec2.html "nuke.splinewarp.CVec2")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
