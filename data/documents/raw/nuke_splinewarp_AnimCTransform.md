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
    * nuke.splinewarp.AnimCTransform
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
  * [nuke.splinewarp](nuke.splinewarp.html) »
  * nuke.splinewarp.AnimCTransform
  * 


* * *

# nuke.splinewarp.AnimCTransform

_class _nuke.splinewarp.AnimCTransform
    

Bases: `object`

An animated transform, where each part of the transform is represented as a curve over time.

Methods

`addPivotPointKey` |   
---|---  
`addRotationKey` |   
`addScaleKey` |   
`addSkewXKey` |   
`addTransformKey` |   
`addTranslationKey` |   
`evaluate` |   
`getExtraMatrixAnimCurve` | Returns the AnimCurve object for the 4i+j element in the transform's extra matrix.The view parameter is optional.  
`getNumberOfPivotPointKeys` | Get the number of keys for the pivotPoint attribute.  
`getNumberOfRotationKeys` | Get the number of keys for the rotation attribute.  
`getNumberOfScaleKeys` | Get the number of keys for the scale attribute.  
`getNumberOfSkewXKeys` | Get the number of keys for the skewX attribute.  
`getNumberOfTransformKeys` | Get the number of keys for all attributes of this transform.  
`getNumberOfTranslationKeys` | Get the number of keys for the translation attribute.  
`getPivotPointAnimCurve` |   
`getPivotPointKeyTime` | Get the time for a specific key on the pivotPoint attribute.  
`getPivotPointKeyTimes` | Get the times for all keys on the pivotPoint attribute.  
`getRotationAnimCurve` |   
`getRotationKeyTime` | Get the time for a specific key on the rotation attribute.  
`getRotationKeyTimes` | Get the times for all keys on the rotation attribute.The view parameter is optional.  
`getScaleAnimCurve` |   
`getScaleKeyTime` | Get the time for a specific key on the scale attribute.  
`getScaleKeyTimes` | Get the times for all keys on the scale attribute.  
`getSkewXAnimCurve` |   
`getSkewXKeyTime` | Get the time for a specific key on the skewX attribute.  
`getSkewXKeyTimes` | Get the times for all keys on the skewX attribute.  
`getTransformKeyTime` | Get the time for a specific key.  
`getTransformKeyTimes` | Get the times for all keys, across all attributes of this transform.  
`getTranslationAnimCurve` |   
`getTranslationKeyTime` | Get the time for a specific key on the translation attribute.  
`getTranslationKeyTimes` | Get the times for all keys on the translation attribute.  
`isDefault` | Check whether this transform has been modified away from the default values.  
`removePivotPointKey` |   
`removeRotationKey` |   
`removeScaleKey` |   
`removeSkewXKey` |   
`removeTransformKey` |   
`removeTranslationKey` |   
`reset` |   
`setExtraMatrixAnimCurve` | Sets the AnimCurve object for the '4i+j'-th element of the extra matrix.The view parameter is optional  
`setIdentity` |   
`setPivotPointAnimCurve` | Set the anim curve for the pivot point attribute of this transform.  
`setRotationAnimCurve` | Set the anim curve for the rotation attribute of this transform.  
`setScaleAnimCurve` | Set the anim curve for the scale attribute of this transform.  
`setSkewXAnimCurve` | Set the anim curve for the skewX attribute of this transform.  
`setTranslationAnimCurve` | Set the anim curve for the translation attribute of this transform.  
  
Attributes

`name` | The name for this transform.  
---|---  
`rotationOrder` | The order in which to perform rotations around the axes.  
`transformOrder` | The order in which to perform the transformations.  
  
addPivotPointKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_) → None
    

addRotationKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_) → None
    

addScaleKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_) → None
    

addSkewXKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_) → None
    

addTransformKey(_time_ , _view_) → None
    

addTranslationKey(_time_ , _x_ , _y_ , _pressure_ , _view ='default'_) → None
    

evaluate(_time_ , _view_) → None
    

getExtraMatrixAnimCurve(_i_ , _j_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

Returns the AnimCurve object for the 4i+j element in the transform’s extra matrix.The view parameter is optional.

getNumberOfPivotPointKeys(_view_) → int
    

Get the number of keys for the pivotPoint attribute. The view parameter is optional.

getNumberOfRotationKeys(_view_) → int
    

Get the number of keys for the rotation attribute. The view parameter is optional.

getNumberOfScaleKeys(_view_) → int
    

Get the number of keys for the scale attribute. The view parameter is optional.

getNumberOfSkewXKeys(_view_) → int
    

Get the number of keys for the skewX attribute. The view parameter is optional.

getNumberOfTransformKeys(_view_) → int
    

Get the number of keys for all attributes of this transform. The view parameter is optional.

getNumberOfTranslationKeys(_view_) → int
    

Get the number of keys for the translation attribute. The view parameter is optional.

getPivotPointAnimCurve(_index_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

getPivotPointKeyTime(_index_ , _view_) → float
    

Get the time for a specific key on the pivotPoint attribute. index is the index of the key. The view parameter is optional.

getPivotPointKeyTimes(_view_) → list of floats
    

Get the times for all keys on the pivotPoint attribute. The view parameter is optional.

getRotationAnimCurve(_index_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

getRotationKeyTime(_index_ , _view_) → float
    

Get the time for a specific key on the rotation attribute. index is the index of the key. The view parameter is optional.

getRotationKeyTimes(_view_) → list of floats
    

Get the times for all keys on the rotation attribute.The view parameter is optional.

getScaleAnimCurve(_index_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

getScaleKeyTime(_index_ , _view_) → float
    

Get the time for a specific key on the scale attribute. index is the index of the key. The view parameter is optional.

getScaleKeyTimes(_view_) → list of floats
    

Get the times for all keys on the scale attribute. The view parameter is optional.

getSkewXAnimCurve(_index_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

getSkewXKeyTime(_index_ , _view_) → float
    

Get the time for a specific key on the skewX attribute. index is the index of the key. The view parameter is optional.

getSkewXKeyTimes(_view_) → list of floats
    

Get the times for all keys on the skewX attribute. The view parameter is optional.

getTransformKeyTime(_index_ , _view_) → float
    

Get the time for a specific key. The view parameter is optional.

getTransformKeyTimes(_view_) → list of floats
    

Get the times for all keys, across all attributes of this transform. The view parameter is optional.

getTranslationAnimCurve(_index_ , _view_) → [AnimCurve](nuke.splinewarp.AnimCurve.html#nuke.splinewarp.AnimCurve "nuke.splinewarp.AnimCurve")
    

getTranslationKeyTime(_index_ , _view_) → float
    

Get the time for a specific key on the translation attribute. index is the index of the key. The view parameter is optional.

getTranslationKeyTimes(_view_) → list of floats
    

Get the times for all keys on the translation attribute. The view parameter is optional.

isDefault() → bool
    

Check whether this transform has been modified away from the default values.

name
    

The name for this transform.

removePivotPointKey(_time_ , _view_) → None
    

removeRotationKey(_time_ , _view_) → None
    

removeScaleKey(_time_ , _view_) → None
    

removeSkewXKey(_time_ , _view_) → None
    

removeTransformKey(_time_ , _view_) → None
    

removeTranslationKey(_time_ , _view_) → None
    

reset() → None
    

rotationOrder
    

The order in which to perform rotations around the axes.

setExtraMatrixAnimCurve(_i_ , _j_ , _animcurve_ , _view_) → None
    

Sets the AnimCurve object for the ‘4i+j’-th element of the extra matrix.The view parameter is optional

setIdentity(_view ='default'_) → None
    

setPivotPointAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the anim curve for the pivot point attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.

setRotationAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the anim curve for the rotation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.

setScaleAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the anim curve for the scale attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.

setSkewXAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the anim curve for the skewX attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.

setTranslationAnimCurve(_index_ , _animCurve_ , _view_) → None
    

Set the anim curve for the translation attribute of this transform. The index parameter should be 0 for the x values, 1 for the y values. The view parameter is optional.

transformOrder
    

The order in which to perform the transformations.

[ Previous](nuke.splinewarp.AnimAttributes.html "nuke.splinewarp.AnimAttributes") [Next ](nuke.splinewarp.AnimControlPoint.html "nuke.splinewarp.AnimControlPoint")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
