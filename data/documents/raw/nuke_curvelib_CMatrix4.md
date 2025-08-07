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
    * nuke.curvelib.CMatrix4
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
  * nuke.curvelib.CMatrix4
  * 


* * *

# nuke.curvelib.CMatrix4

_class _nuke.curvelib.CMatrix4
    

Bases: `object`

A 4x4 matrix with methods for affine transformations.

Methods

`makeIdentity` | Set this matrix to be the identity matrix.  
---|---  
`rotateX` | Post-multiply this matrix by a rotation around the X axis.  
`rotateY` | Post-multiply this matrix by a rotation around the Y axis.  
`rotateZ` | self.rotateY(angleInRadians) -> None Post-multiply this matrix by a rotation around the Z axis.  
`scale` | Post-multiply this matrix by a scale transformation.  
`skew` | Post-multiply this matrix with a skew transformation.  
`translate` | Post-multiply this matrix by a translation matrix.  
`translation` | Set this matrix to be a translation matrix, replacing any existing values.  
`transpose` | Transpose the matrix in-place.  
  
__add__(_value_ , _/_)
    

Return self+value.

__mul__(_value_ , _/_)
    

Return self*value.

makeIdentity() → None
    

Set this matrix to be the identity matrix.

rotateX(_angleInRadians_) → None
    

Post-multiply this matrix by a rotation around the X axis.

rotateY(_angleInRadians_) → None
    

Post-multiply this matrix by a rotation around the Y axis.

rotateZ()
    

self.rotateY(angleInRadians) -> None Post-multiply this matrix by a rotation around the Z axis.

scale(_x_ , _y_ , _z_) → None
    

Post-multiply this matrix by a scale transformation. The y and z parameters may be left out; if so the scale is uniform along all three axes.

skew(_x_ , _y_ , _z_) → None
    

Post-multiply this matrix with a skew transformation. The y and z parameters may be left out; if so, the skew is in the X direction only.

translate(_x_ , _y_ , _z_) → None
    

Post-multiply this matrix by a translation matrix.

translation(_x_ , _y_ , _z_) → None
    

Set this matrix to be a translation matrix, replacing any existing values.

This is different from other methods in this class as it replaces, rather than multiplying by, the existing values in the matrix.

transpose() → None
    

Transpose the matrix in-place.

[ Previous](nuke.curvelib.BaseCurve.html "nuke.curvelib.BaseCurve") [Next ](nuke.curvelib.CTransform.html "nuke.curvelib.CTransform")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
