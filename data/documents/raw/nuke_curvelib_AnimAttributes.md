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
    * nuke.curvelib.AnimAttributes
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
  * [nuke.curvelib](nuke.curvelib.html) »
  * nuke.curvelib.AnimAttributes
  * 


* * *

# nuke.curvelib.AnimAttributes

_class _nuke.curvelib.AnimAttributes
    

Bases: `object`

A collection of named attributes.

Each attribute is represented as a curve, parameterised over time. Convenience methods for managing the curves (adding and removing keys, etc.) are provided, as well as methods for managing the list of available attributes.

Attributes can be accessed by index or by name. This class defines constants for standard names in use by Nuke.

Methods

`add` | Add a new attribute.  
---|---  
`addKey` | When a name and value is specified, this method adds a new key to an existing attribute at the given time.  
`getCurve` | Gets the AnimCurve object for a particular attribute.  
`getKeyTime` | Gets the time a particular key is set at.  
`getName` | Get the name of an attribute when you know its index.  
`getNumberOfKeys` | Returns the number of keys in the curve for a particular attribute.  
`getValue` | Evaluates the anim curve of an attribute at a particular time and returns the value.  
`remove` | Remove an attribute.  
`removeAll` | Remove all attributes.  
`removeKey` | Remove a particular key from an attribute.  
`removeKeys` | Remove all keys from an attribute.  
`reset` | Reset the object to have no attributes.  
`set` | Set the value of an attribute.  
`setCurve` | Replace the current anim curve for an attribute with a new one.  
`setKey` | Set a key for an attribute.  
`setName` | Change the name of an existing attribute.  
  
Attributes

`kAlphaAttribute` |   
---|---  
`kAlphaOverlayAttribute` |   
`kBlendingModeAttribute` |   
`kBlueAttribute` |   
`kBlueOverlayAttribute` |   
`kBrushSizeAttribute` |   
`kBrushSpacingAttribute` |   
`kBrushTypeAttribute` |   
`kBuildUpAttribute` |   
`kDynamicHardnessAttribute` |   
`kDynamicSizeAttribute` |   
`kDynamicTransparencyAttribute` |   
`kEffectParameter1Attribute` |   
`kEffectParameter2Attribute` |   
`kEffectParameter3Attribute` |   
`kFeatherFallOffAttribute` |   
`kFeatherOnAttribute` |   
`kFeatherTypeAttribute` |   
`kFeatherXAttribute` |   
`kFeatherYAttribute` |   
`kGreenAttribute` |   
`kGreenOverlayAttribute` |   
`kHardnessAttribute` |   
`kInvertedAttribute` |   
`kLifeTimeMAttribute` |   
`kLifeTimeNAttribute` |   
`kLifeTimeTypeAttribute` |   
`kMotionBlurAttribute` |   
`kMotionBlurOnAttribute` |   
`kMotionBlurShutterAttribute` |   
`kMotionBlurShutterOffsetAttribute` |   
`kMotionBlurShutterOffsetTypeAttribute` |   
`kNumberOfViewsAttribute` |   
`kOpacityAttribute` |   
`kPlanarTrackLayerAttribute` |   
`kRedAttribute` |   
`kRedOverlayAttribute` |   
`kSourceAttribute` |   
`kSourcePivotPointXAttribute` |   
`kSourcePivotPointYAttribute` |   
`kSourceRotateAttribute` |   
`kSourceScaleXAttribute` |   
`kSourceScaleYAttribute` |   
`kSourceSkewOrderAttribute` |   
`kSourceSkewXAttribute` |   
`kSourceSkewYAttribute` |   
`kSourceTimeOffsetAttribute` |   
`kSourceTimeOffsetTypeAttribute` |   
`kSourceTranslateRoundAttribute` |   
`kSourceTranslateXAttribute` |   
`kSourceTranslateYAttribute` |   
`kTensionAttribute` |   
`kViewAttribute` |   
`kVisibleAttribute` |   
`kWriteOnEndAttribute` |   
`kWriteOnStartAttribute` |   
  
add(_name_ , _value_) → None
    

Add a new attribute. The name parameter is the name for the attribute and value is the initial int or float value to assign to it.

addKey(_time_ , _name_ , _value_ , _view_) → None
addKey(_time_ , _view_) → None
    

When a name and value is specified, this method adds a new key to an existing attribute at the given time. When the name and value are omitted, a new key is added to all attributes at the specified time. The view parameter is optional in either case.

getCurve(_attr_ , _view_) → [AnimCurve](nuke.curvelib.AnimCurve.html#nuke.curvelib.AnimCurve "nuke.curvelib.AnimCurve")
    

Gets the AnimCurve object for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.

getKeyTime(_index_ , _keyIndexOrHash_ , _view_) → float
    

Gets the time a particular key is set at. The index parameter is the index of the attribute; keyIndexOrHash is either the index of the key in the attributes AnimCurve, or its associated Hash; and view is the optional view name.

getName(_index_) → str
    

Get the name of an attribute when you know its index.

getNumberOfKeys(_attr_ , _view_) → int
    

Returns the number of keys in the curve for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.

getValue(_time_ , _indexOrName_ , _view_) → float
    

Evaluates the anim curve of an attribute at a particular time and returns the value. time is the time for which to evaluate the attribute; indexOrName is either the index of the attribute to evaluate, or its name; and view is the optional view name.

remove(_attributeIndexOrName_) → None
    

Remove an attribute. You can give the name or index of the attribute.

removeAll() → None
    

Remove all attributes.

removeKey(_time_ , _attributeIndex_ , _view_) → None
    

Remove a particular key from an attribute. The view parameter is optional.

removeKeys(_attributeIndex_ , _view_) → None
    

Remove all keys from an attribute. The view parameter is optional.

reset() → None
    

Reset the object to have no attributes.

set(_time_ , _attributeIndexOrName_ , _value_ , _view_) → None
    

Set the value of an attribute. The time parameter is optional: if it’s present, a new key is created at that time with the specified value; if it’s not present, a constant value is set for the attribute. The attribute to set may be identified by its name or index. The view parameter is optional.

setCurve(_index_ , _curve_) → None
    

Replace the current anim curve for an attribute with a new one. The index parameter is the index of the attribute; and curve is an AnimCurve instance.

setKey(_time_ , _attributeIndex_ , _hash_ , _value_ , _view_) → None
    

Set a key for an attribute. The time parameter is when the new key will be created for; the attributeIndex says which attribute to set the key for; the

setName(_attributeIndex_ , _newName_) → None
    

Change the name of an existing attribute.

[ Previous](nuke.curvelib.html "nuke.curvelib") [Next ](nuke.curvelib.AnimCTransform.html "nuke.curvelib.AnimCTransform")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
