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
    * [nuke.curveknob.CurveKnob](nuke.curveknob.CurveKnob.html)
    * [nuke.curveknob.CurveWidget](nuke.curveknob.CurveWidget.html)
    * [nuke.curveknob.Element](nuke.curveknob.Element.html)
    * [nuke.curveknob.Layer](nuke.curveknob.Layer.html)
    * [nuke.curveknob.Shape](nuke.curveknob.Shape.html)
    * nuke.curveknob.ShapeControlPoint
    * [nuke.curveknob.Stroke](nuke.curveknob.Stroke.html)
  * [nuke.curvelib](nuke.curvelib.html)
  * [nuke.gsv](nuke.gsv.html)
  * [nuke.localization](nuke.localization.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.curveknob](nuke.curveknob.html) »
  * nuke.curveknob.ShapeControlPoint
  * 


* * *

# nuke.curveknob.ShapeControlPoint

_class _nuke.curveknob.ShapeControlPoint
    

Bases: `object`

A control point in a roto shape.

The control point groups together a ‘center’ location, along with tangents and feather offsets.

Methods

Attributes

`center` | The center of the control point  
---|---  
`featherCenter` | The feather point offsets, relative to the center point  
`featherLeftTangent` | The left feather tangent offsets, relative to the feather center point.  
`featherRightTangent` | The right feather tangent offsets, relative to the feather center point.  
`leftTangent` | The left tangent offsets, relative to the center point.  
`rightTangent` | The right tangent offsets, relative to the center point.  
  
center
    

The center of the control point

featherCenter
    

The feather point offsets, relative to the center point

featherLeftTangent
    

The left feather tangent offsets, relative to the feather center point.

featherRightTangent
    

The right feather tangent offsets, relative to the feather center point.

leftTangent
    

The left tangent offsets, relative to the center point.

rightTangent
    

The right tangent offsets, relative to the center point.

[ Previous](nuke.curveknob.Shape.html "nuke.curveknob.Shape") [Next ](nuke.curveknob.Stroke.html "nuke.curveknob.Stroke")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
