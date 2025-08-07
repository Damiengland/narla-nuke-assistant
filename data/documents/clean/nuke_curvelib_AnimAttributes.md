# nuke.curvelib.AnimAttributes
_class _nuke.curvelib.AnimAttributes

Bases: `object`
A collection of named attributes.
Each attribute is represented as a curve, parameterised over time. Convenience methods for managing the curves (adding and removing keys, etc.) are provided, as well as methods for managing the list of available attributes.
Attributes can be accessed by index or by name. This class defines constants for standard names in use by Nuke.
Methods
`add`  Add a new attribute.---
`addKey`  When a name and value is specified, this method adds a new key to an existing attribute at the given time.
`getCurve`  Gets the AnimCurve object for a particular attribute.
`getKeyTime`  Gets the time a particular key is set at.
`getName`  Get the name of an attribute when you know its index.
`getNumberOfKeys`  Returns the number of keys in the curve for a particular attribute.
`getValue`  Evaluates the anim curve of an attribute at a particular time and returns the value.
`remove`  Remove an attribute.
`removeAll`  Remove all attributes.
`removeKey`  Remove a particular key from an attribute.
`removeKeys`  Remove all keys from an attribute.
`reset`  Reset the object to have no attributes.
`set`  Set the value of an attribute.
`setCurve`  Replace the current anim curve for an attribute with a new one.
`setKey`  Set a key for an attribute.
`setName`  Change the name of an existing attribute.

Attributes
`kAlphaAttribute` ---
`kAlphaOverlayAttribute`
`kBlendingModeAttribute`
`kBlueAttribute`
`kBlueOverlayAttribute`
`kBrushSizeAttribute`
`kBrushSpacingAttribute`
`kBrushTypeAttribute`
`kBuildUpAttribute`
`kDynamicHardnessAttribute`
`kDynamicSizeAttribute`
`kDynamicTransparencyAttribute`
`kEffectParameter1Attribute`
`kEffectParameter2Attribute`
`kEffectParameter3Attribute`
`kFeatherFallOffAttribute`
`kFeatherOnAttribute`
`kFeatherTypeAttribute`
`kFeatherXAttribute`
`kFeatherYAttribute`
`kGreenAttribute`
`kGreenOverlayAttribute`
`kHardnessAttribute`
`kInvertedAttribute`
`kLifeTimeMAttribute`
`kLifeTimeNAttribute`
`kLifeTimeTypeAttribute`
`kMotionBlurAttribute`
`kMotionBlurOnAttribute`
`kMotionBlurShutterAttribute`
`kMotionBlurShutterOffsetAttribute`
`kMotionBlurShutterOffsetTypeAttribute`
`kNumberOfViewsAttribute`
`kOpacityAttribute`
`kPlanarTrackLayerAttribute`
`kRedAttribute`
`kRedOverlayAttribute`
`kSourceAttribute`
`kSourcePivotPointXAttribute`
`kSourcePivotPointYAttribute`
`kSourceRotateAttribute`
`kSourceScaleXAttribute`
`kSourceScaleYAttribute`
`kSourceSkewOrderAttribute`
`kSourceSkewXAttribute`
`kSourceSkewYAttribute`
`kSourceTimeOffsetAttribute`
`kSourceTimeOffsetTypeAttribute`
`kSourceTranslateRoundAttribute`
`kSourceTranslateXAttribute`
`kSourceTranslateYAttribute`
`kTensionAttribute`
`kViewAttribute`
`kVisibleAttribute`
`kWriteOnEndAttribute`
`kWriteOnStartAttribute`

add(_name_ , _value_)  None

Add a new attribute. The name parameter is the name for the attribute and value is the initial int or float value to assign to it.
addKey(_time_ , _name_ , _value_ , _view_)  None
addKey(_time_ , _view_)  None

When a name and value is specified, this method adds a new key to an existing attribute at the given time. When the name and value are omitted, a new key is added to all attributes at the specified time. The view parameter is optional in either case.
getCurve(_attr_ , _view_)

Gets the AnimCurve object for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.
getKeyTime(_index_ , _keyIndexOrHash_ , _view_)  float

Gets the time a particular key is set at. The index parameter is the index of the attribute; keyIndexOrHash is either the index of the key in the attributes AnimCurve, or its associated Hash; and view is the optional view name.
getName(_index_)  str

Get the name of an attribute when you know its index.
getNumberOfKeys(_attr_ , _view_)  int

Returns the number of keys in the curve for a particular attribute. The attr parameter can be the index or name of the attribute. The view parameter is optional.
getValue(_time_ , _indexOrName_ , _view_)  float

Evaluates the anim curve of an attribute at a particular time and returns the value. time is the time for which to evaluate the attribute; indexOrName is either the index of the attribute to evaluate, or its name; and view is the optional view name.
remove(_attributeIndexOrName_)  None

Remove an attribute. You can give the name or index of the attribute.
removeAll()  None

Remove all attributes.
removeKey(_time_ , _attributeIndex_ , _view_)  None

Remove a particular key from an attribute. The view parameter is optional.
removeKeys(_attributeIndex_ , _view_)  None

Remove all keys from an attribute. The view parameter is optional.
reset()  None

Reset the object to have no attributes.
set(_time_ , _attributeIndexOrName_ , _value_ , _view_)  None

Set the value of an attribute. The time parameter is optional: if it’s present, a new key is created at that time with the specified value; if it’s not present, a constant value is set for the attribute. The attribute to set may be identified by its name or index. The view parameter is optional.
setCurve(_index_ , _curve_)  None

Replace the current anim curve for an attribute with a new one. The index parameter is the index of the attribute; and curve is an AnimCurve instance.
setKey(_time_ , _attributeIndex_ , _hash_ , _value_ , _view_)  None

Set a key for an attribute. The time parameter is when the new key will be created for; the attributeIndex says which attribute to set the key for; the
setName(_attributeIndex_ , _newName_)  None

Change the name of an existing attribute.