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
    * [nuke.curvelib.AnimCurve](nuke.curvelib.AnimCurve.html)
    * [nuke.curvelib.AnimCurveKey](nuke.curvelib.AnimCurveKey.html)
    * [nuke.curvelib.AnimCurveViews](nuke.curvelib.AnimCurveViews.html)
    * [nuke.curvelib.BaseCurve](nuke.curvelib.BaseCurve.html)
    * [nuke.curvelib.CMatrix4](nuke.curvelib.CMatrix4.html)
    * nuke.curvelib.CTransform
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
  * nuke.curvelib.CTransform
  * 


* * *

# nuke.curvelib.CTransform

_class _nuke.curvelib.CTransform
    

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
  
getInverseMatrix() → [CMatrix4](nuke.curvelib.CMatrix4.html#nuke.curvelib.CMatrix4 "nuke.curvelib.CMatrix4")
    

Gets the inverse transform matrix, which can be used for undoing the effects of this transform.

getMatrix() → [CMatrix4](nuke.curvelib.CMatrix4.html#nuke.curvelib.CMatrix4 "nuke.curvelib.CMatrix4")
    

Get the matrix which represents the combination of the translation, scale, rotation, skew and pivotPoint settings for this transform.

getTransposeMatrix() → [CMatrix4](nuke.curvelib.CMatrix4.html#nuke.curvelib.CMatrix4 "nuke.curvelib.CMatrix4")
    

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

[ Previous](nuke.curvelib.CMatrix4.html "nuke.curvelib.CMatrix4") [Next ](nuke.curvelib.CVec2.html "nuke.curvelib.CVec2")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
