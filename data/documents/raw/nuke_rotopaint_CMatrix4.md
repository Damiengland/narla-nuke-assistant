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
    * [nuke.rotopaint.convertDirectoryToNuke6](nuke.rotopaint.convertDirectoryToNuke6.html)
    * [nuke.rotopaint.convertDirectoryToNuke7](nuke.rotopaint.convertDirectoryToNuke7.html)
    * [nuke.rotopaint.convertToNuke6](nuke.rotopaint.convertToNuke6.html)
    * [nuke.rotopaint.convertToNuke7](nuke.rotopaint.convertToNuke7.html)
    * [nuke.rotopaint.AnimAttributes](nuke.rotopaint.AnimAttributes.html)
    * [nuke.rotopaint.AnimCTransform](nuke.rotopaint.AnimCTransform.html)
    * [nuke.rotopaint.AnimControlPoint](nuke.rotopaint.AnimControlPoint.html)
    * [nuke.rotopaint.AnimCurve](nuke.rotopaint.AnimCurve.html)
    * [nuke.rotopaint.AnimCurveKey](nuke.rotopaint.AnimCurveKey.html)
    * [nuke.rotopaint.AnimCurveViews](nuke.rotopaint.AnimCurveViews.html)
    * [nuke.rotopaint.BaseCurve](nuke.rotopaint.BaseCurve.html)
    * nuke.rotopaint.CMatrix4
    * [nuke.rotopaint.CTransform](nuke.rotopaint.CTransform.html)
    * [nuke.rotopaint.CVec2](nuke.rotopaint.CVec2.html)
    * [nuke.rotopaint.CVec3](nuke.rotopaint.CVec3.html)
    * [nuke.rotopaint.CVec4](nuke.rotopaint.CVec4.html)
    * [nuke.rotopaint.ControlPoint](nuke.rotopaint.ControlPoint.html)
    * [nuke.rotopaint.CubicCurve](nuke.rotopaint.CubicCurve.html)
    * [nuke.rotopaint.CurveKnob](nuke.rotopaint.CurveKnob.html)
    * [nuke.rotopaint.CurveType](nuke.rotopaint.CurveType.html)
    * [nuke.rotopaint.Element](nuke.rotopaint.Element.html)
    * [nuke.rotopaint.ExtrapolationType](nuke.rotopaint.ExtrapolationType.html)
    * [nuke.rotopaint.Flag](nuke.rotopaint.Flag.html)
    * [nuke.rotopaint.FlagType](nuke.rotopaint.FlagType.html)
    * [nuke.rotopaint.Hash](nuke.rotopaint.Hash.html)
    * [nuke.rotopaint.InterpolationType](nuke.rotopaint.InterpolationType.html)
    * [nuke.rotopaint.Layer](nuke.rotopaint.Layer.html)
    * [nuke.rotopaint.RotationOrder](nuke.rotopaint.RotationOrder.html)
    * [nuke.rotopaint.Shape](nuke.rotopaint.Shape.html)
    * [nuke.rotopaint.ShapeControlPoint](nuke.rotopaint.ShapeControlPoint.html)
    * [nuke.rotopaint.Stroke](nuke.rotopaint.Stroke.html)
    * [nuke.rotopaint.TransformOrder](nuke.rotopaint.TransformOrder.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.rotopaint](nuke.rotopaint.html) »
  * nuke.rotopaint.CMatrix4
  * 


* * *

# nuke.rotopaint.CMatrix4

_class _nuke.rotopaint.CMatrix4
    

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

[ Previous](nuke.rotopaint.BaseCurve.html "nuke.rotopaint.BaseCurve") [Next ](nuke.rotopaint.CTransform.html "nuke.rotopaint.CTransform")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
