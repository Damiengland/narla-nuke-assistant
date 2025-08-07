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
    * [nuke.nukemath.Matrix3](nuke.nukemath.Matrix3.html)
    * [nuke.nukemath.Matrix4](nuke.nukemath.Matrix4.html)
    * [nuke.nukemath.Quaternion](nuke.nukemath.Quaternion.html)
    * [nuke.nukemath.Vector2](nuke.nukemath.Vector2.html)
    * nuke.nukemath.Vector3
    * [nuke.nukemath.Vector4](nuke.nukemath.Vector4.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.nukemath](nuke.nukemath.html) »
  * nuke.nukemath.Vector3
  * 


* * *

# nuke.nukemath.Vector3

_class _nuke.nukemath.Vector3(_* args_, _** kwargs_)
    

Bases: `pybind11_builtins.pybind11_object`

Overloaded function.

  1. __init__(self: nukemath.Vector3) -> None

  2. __init__(self: nukemath.Vector3, arg0: float, arg1: float, arg2: float) -> None

  3. __init__(self: nukemath.Vector3, arg0: nukemath.Vector3) -> None




Methods

`cross` |   
---|---  
`distanceBetween` |   
`distanceFromPlane` |   
`distanceSquared` |   
`dot` |   
`fast_normalize` |   
`length` |   
`lengthSquared` |   
`maximum` |   
`minimum` |   
`negate` |   
`normalize` |   
`reflect` |   
`set` |   
  
Attributes

`x` |   
---|---  
`y` |   
`z` |   
  
__add__(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → nukemath.Vector3
    

__mul__(_* args_, _** kwargs_)
    

Overloaded function.

  1. __mul__(self: nukemath.Vector3, arg0: float) -> nukemath.Vector3

  2. __mul__(self: nukemath.Vector3, arg0: nukemath.Vector3) -> nukemath.Vector3

  3. __mul__(self: nukemath.Vector3, arg0: float) -> nukemath.Vector3




cross(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → nukemath.Vector3
    

distanceBetween(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → float
    

distanceFromPlane(_self : nukemath.Vector3_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_) → float
    

distanceSquared(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → float
    

dot(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → float
    

fast_normalize(_self : nukemath.Vector3_) → float
    

length(_self : nukemath.Vector3_) → float
    

lengthSquared(_self : nukemath.Vector3_) → float
    

maximum(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → nukemath.Vector3
    

minimum(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → nukemath.Vector3
    

negate(_self : nukemath.Vector3_) → None
    

normalize(_self : nukemath.Vector3_) → float
    

reflect(_self : nukemath.Vector3_, _arg0 : nukemath.Vector3_) → nukemath.Vector3
    

set(_self : nukemath.Vector3_, _arg0 : float_, _arg1 : float_, _arg2 : float_) → None
    

[ Previous](nuke.nukemath.Vector2.html "nuke.nukemath.Vector2") [Next ](nuke.nukemath.Vector4.html "nuke.nukemath.Vector4")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
