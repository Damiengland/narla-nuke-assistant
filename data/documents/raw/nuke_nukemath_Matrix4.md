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
    * nuke.nukemath.Matrix4
    * [nuke.nukemath.Quaternion](nuke.nukemath.Quaternion.html)
    * [nuke.nukemath.Vector2](nuke.nukemath.Vector2.html)
    * [nuke.nukemath.Vector3](nuke.nukemath.Vector3.html)
    * [nuke.nukemath.Vector4](nuke.nukemath.Vector4.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.nukemath](nuke.nukemath.html) »
  * nuke.nukemath.Matrix4
  * 


* * *

# nuke.nukemath.Matrix4

_class _nuke.nukemath.Matrix4(_* args_, _** kwargs_)
    

Bases: `pybind11_builtins.pybind11_object`

Overloaded function.

  1. __init__(self: nukemath.Matrix4) -> None

  2. __init__(self: nukemath.Matrix4, arg0: nukemath.Matrix4) -> None




Methods

`determinant` |   
---|---  
`identity` |   
`inverse` |   
`makeIdentity` |   
`mapQuadToUnitSquare` |   
`mapUnitSquareToQuad` |   
`ntransform` |   
`projection` |   
`rotate` | Overloaded function.  
`rotateX` |   
`rotateY` |   
`rotateZ` |   
`rotation` | Overloaded function.  
`rotationOnly` |   
`rotationX` |   
`rotationY` |   
`rotationZ` |   
`rotationsXYZ` |   
`rotationsXZY` |   
`rotationsYXZ` |   
`rotationsYZX` |   
`rotationsZXY` |   
`rotationsZYX` |   
`scale` | Overloaded function.  
`scaleAndRotationOnly` |   
`scaleOnly` |   
`scaling` | Overloaded function.  
`skew` |   
`skewXY` |   
`transform` | Overloaded function.  
`translate` | Overloaded function.  
`translation` | Overloaded function.  
`translationOnly` |   
`transpose` |   
`vtransform` |   
`xAxis` |   
`yAxis` |   
`zAxis` |   
  
__add__(_self : nukemath.Matrix4_, _arg0 : nukemath.Matrix4_) → nukemath.Matrix4
    

__mul__(_* args_, _** kwargs_)
    

Overloaded function.

  1. __mul__(self: nukemath.Matrix4, arg0: float) -> nukemath.Matrix4

  2. __mul__(self: nukemath.Matrix4, arg0: nukemath.Vector4) -> nukemath.Vector4

  3. __mul__(self: nukemath.Matrix4, arg0: nukemath.Matrix4) -> nukemath.Matrix4




determinant(_self : nukemath.Matrix4_) → float
    

identity() → nukemath.Matrix4
    

inverse(_self : nukemath.Matrix4_) → nukemath.Matrix4
    

makeIdentity(_self : nukemath.Matrix4_) → None
    

mapQuadToUnitSquare(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_, _arg4 : float_, _arg5 : float_, _arg6 : float_, _arg7 : float_) → None
    

mapUnitSquareToQuad(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : float_, _arg4 : float_, _arg5 : float_, _arg6 : float_, _arg7 : float_) → None
    

ntransform(_self : nukemath.Matrix4_, _arg0 : [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")_) → [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")
    

projection(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_, _arg2 : float_, _arg3 : bool_) → None
    

rotate(_* args_, _** kwargs_)
    

Overloaded function.

  1. rotate(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float, arg3: float) -> None

  2. rotate(self: nukemath.Matrix4, arg0: float, arg1: nukemath.Vector3) -> None




rotateX(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotateY(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotateZ(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotation(_* args_, _** kwargs_)
    

Overloaded function.

  1. rotation(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float, arg3: float) -> None

  2. rotation(self: nukemath.Matrix4, arg0: float, arg1: nukemath.Vector3) -> None




rotationOnly(_self : nukemath.Matrix4_) → None
    

rotationX(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotationY(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotationZ(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

rotationsXYZ(_self : nukemath.Matrix4_) → tuple
    

rotationsXZY(_self : nukemath.Matrix4_) → tuple
    

rotationsYXZ(_self : nukemath.Matrix4_) → tuple
    

rotationsYZX(_self : nukemath.Matrix4_) → tuple
    

rotationsZXY(_self : nukemath.Matrix4_) → tuple
    

rotationsZYX(_self : nukemath.Matrix4_) → tuple
    

scale(_* args_, _** kwargs_)
    

Overloaded function.

  1. scale(self: nukemath.Matrix4, arg0: float) -> None

  2. scale(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None




scaleAndRotationOnly(_self : nukemath.Matrix4_) → None
    

scaleOnly(_self : nukemath.Matrix4_) → None
    

scaling(_* args_, _** kwargs_)
    

Overloaded function.

  1. scaling(self: nukemath.Matrix4, arg0: float) -> None

  2. scaling(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None

  3. scaling(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None




skew(_self : nukemath.Matrix4_, _arg0 : float_) → None
    

skewXY(_self : nukemath.Matrix4_, _arg0 : float_, _arg1 : float_) → None
    

transform(_* args_, _** kwargs_)
    

Overloaded function.

  1. transform(self: nukemath.Matrix4, arg0: nukemath.Vector4) -> nukemath.Vector4

  2. transform(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> nukemath.Vector3




translate(_* args_, _** kwargs_)
    

Overloaded function.

  1. translate(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None

  2. translate(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None




translation(_* args_, _** kwargs_)
    

Overloaded function.

  1. translation(self: nukemath.Matrix4) -> tuple

  2. translation(self: nukemath.Matrix4, arg0: float, arg1: float, arg2: float) -> None

  3. translation(self: nukemath.Matrix4, arg0: nukemath.Vector3) -> None




translationOnly(_self : nukemath.Matrix4_) → None
    

transpose(_self : nukemath.Matrix4_) → None
    

vtransform(_self : nukemath.Matrix4_, _arg0 : [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")_) → [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")
    

xAxis(_self : nukemath.Matrix4_) → [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")
    

yAxis(_self : nukemath.Matrix4_) → [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")
    

zAxis(_self : nukemath.Matrix4_) → [nukemath.Vector3](nuke.nukemath.Vector3.html#nuke.nukemath.Vector3 "nukemath.Vector3")
    

[ Previous](nuke.nukemath.Matrix3.html "nuke.nukemath.Matrix3") [Next ](nuke.nukemath.Quaternion.html "nuke.nukemath.Quaternion")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
