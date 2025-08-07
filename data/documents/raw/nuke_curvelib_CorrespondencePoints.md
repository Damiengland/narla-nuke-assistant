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
    * [nuke.curvelib.CTransform](nuke.curvelib.CTransform.html)
    * [nuke.curvelib.CVec2](nuke.curvelib.CVec2.html)
    * [nuke.curvelib.CVec3](nuke.curvelib.CVec3.html)
    * [nuke.curvelib.CVec4](nuke.curvelib.CVec4.html)
    * [nuke.curvelib.ControlPoint](nuke.curvelib.ControlPoint.html)
    * nuke.curvelib.CorrespondencePoints
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
  * nuke.curvelib.CorrespondencePoints
  * 


* * *

# nuke.curvelib.CorrespondencePoints

_class _nuke.curvelib.CorrespondencePoints
    

Bases: `object`

Correspondence points add a relation to the interpolation of two curves. These points are made up of two values; a t-value on the source curve and a corresponding t-value on the destination curve T-values should be in the range [0-1], where 0 is the start of the curve, and 1 is the end of the curve

Methods

`addPoint` | Adds a correspondence point :param time: Time at which to t_src and t_dest will be set :param t_src: Position on the source curve (where 0=start and 1=end) :param t_dest: Position on the destination curve Note that the correspondence point is not animated.  
---|---  
`getAnimCurve` | 

param index
    Index to the point to get the associated AnimCurve  
`getNumPoints` | 

return
    Returns the number of correspondence points in the object  
`getPointValues` | 

param time
    Time at which to evaluate point's values  
`modifyPoint` | 

param time
    Time at which to t_in and t_out will be set  
`removePoint` | 

param index
    Index to the point to remove  
`reset` | cps->reset() Resets the correspondence points object to empty  
  
addPoint(_time_ , _t_src_ , _t_dest_)
    

Adds a correspondence point :param time: Time at which to t_src and t_dest will be set :param t_src: Position on the source curve (where 0=start and 1=end) :param t_dest: Position on the destination curve Note that the correspondence point is not animated. Animation must be set manually to avoid conflicting with existing points.

getAnimCurve(_index_ , _which_) → [AnimCurve](nuke.curvelib.AnimCurve.html#nuke.curvelib.AnimCurve "nuke.curvelib.AnimCurve")
    

Parameters
    

**index** – Index to the point to get the associated AnimCurve

object for :param which: Whether the source (0) or destination (1) t-value is being modified :return: An AnimCurve object for the timeline of the specified point and src/dest value

getNumPoints()
    

Returns
    

Returns the number of correspondence points in the object

getPointValues(_time_ , _index_)
    

Parameters
    

  * **time** – Time at which to evaluate point’s values

  * **index** – Index to the point to evaluate



Returns
    

A tuple containing source and destionation t-values

modifyPoint(_time_ , _index_ , _which_ , _t_)
    

Parameters
    

  * **time** – Time at which to t_in and t_out will be set

  * **index** – Index to the point to modify

  * **which** – Whether the source (0) or destination (1) t-value is




being modified :param t: Position on the curve specified in by ‘which’

removePoint(_index_)
    

Parameters
    

**index** – Index to the point to remove

reset()
    

cps->reset() Resets the correspondence points object to empty

[ Previous](nuke.curvelib.ControlPoint.html "nuke.curvelib.ControlPoint") [Next ](nuke.curvelib.CubicCurve.html "nuke.curvelib.CubicCurve")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
