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
    * nuke.nukemath.Quaternion
    * [nuke.nukemath.Vector2](nuke.nukemath.Vector2.html)
    * [nuke.nukemath.Vector3](nuke.nukemath.Vector3.html)
    * [nuke.nukemath.Vector4](nuke.nukemath.Vector4.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.nukemath](nuke.nukemath.html) »
  * nuke.nukemath.Quaternion
  * 


* * *

# nuke.nukemath.Quaternion

_class _nuke.nukemath.Quaternion(_* args_, _** kwargs_)
    

Bases: `pybind11_builtins.pybind11_object`

Overloaded function.

  1. __init__(self: nukemath.Quaternion, arg0: float, arg1: float, arg2: float, arg3: float) -> None

  2. __init__(self: nukemath.Quaternion, arg0: float, arg1: nukemath.Vector3) -> None

  3. __init__(self: nukemath.Quaternion, arg0: nukemath.Quaternion) -> None

  4. __init__(self: nukemath.Quaternion, arg0: nukemath.Matrix4) -> None

  5. __init__(self: nukemath.Quaternion, arg0: nukemath.Vector3, arg1: nukemath.Vector3) -> None




Methods

`addInverse` |   
---|---  
`conjugate` |   
`length` |   
`lengthSquared` |   
`magnitude` |   
`matrix` |   
`multInverse` |   
`set` |   
`slerp` |   
  
Attributes

`s` |   
---|---  
`vx` |   
`vy` |   
`vz` |   
  
__add__(_self : nukemath.Quaternion_, _arg0 : nukemath.Quaternion_) → nukemath.Quaternion
    

__mul__(_* args_, _** kwargs_)
    

Overloaded function.

  1. __mul__(self: nukemath.Quaternion, arg0: float) -> nukemath.Quaternion

  2. __mul__(self: nukemath.Quaternion, arg0: nukemath.Quaternion) -> nukemath.Quaternion




addInverse(_self : nukemath.Quaternion_) → nukemath.Quaternion
    

conjugate(_self : nukemath.Quaternion_) → nukemath.Quaternion
    

length(_self : nukemath.Quaternion_) → float
    

lengthSquared(_self : nukemath.Quaternion_) → float
    

magnitude(_self : nukemath.Quaternion_) → float
    

matrix(_self : nukemath.Quaternion_) → [nukemath.Matrix4](nuke.nukemath.Matrix4.html#nuke.nukemath.Matrix4 "nukemath.Matrix4")
    

multInverse(_self : nukemath.Quaternion_) → nukemath.Quaternion
    

set(_self : nukemath.Quaternion_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_) → None
    

slerp(_self : nukemath.Quaternion_, _arg0 : nukemath.Quaternion_, _arg1 : float_) → nukemath.Quaternion
    

[ Previous](nuke.nukemath.Matrix4.html "nuke.nukemath.Matrix4") [Next ](nuke.nukemath.Vector2.html "nuke.nukemath.Vector2")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
