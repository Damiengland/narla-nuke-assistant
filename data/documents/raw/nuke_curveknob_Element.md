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
    * nuke.curveknob.Element
    * [nuke.curveknob.Layer](nuke.curveknob.Layer.html)
    * [nuke.curveknob.Shape](nuke.curveknob.Shape.html)
    * [nuke.curveknob.ShapeControlPoint](nuke.curveknob.ShapeControlPoint.html)
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
  * nuke.curveknob.Element
  * 


* * *

# nuke.curveknob.Element

_class _nuke.curveknob.Element
    

Bases: `object`

The base class for the different types of elements you can create in the RotoPaint node.

Methods

`clone` |   
---|---  
`getVisible` | Get the value of the visible attribute at a particular time.  
`serialise` | Returns a string representation of the given element.  
`setVisible` | Set the value of the visible attribute at a particular time.  
  
Attributes

`locked` | Whether this element is locked.  
---|---  
`name` | The name for this element.  
  
clone() → elementCreate clone of element
    

getVisible(_time_) → bool
    

Get the value of the visible attribute at a particular time.

locked
    

Whether this element is locked.

name
    

The name for this element.

serialise() → string
    

Returns a string representation of the given element.

setVisible(_time_ , _value_) → None
    

Set the value of the visible attribute at a particular time. value must be a bool.

[ Previous](nuke.curveknob.CurveWidget.html "nuke.curveknob.CurveWidget") [Next ](nuke.curveknob.Layer.html "nuke.curveknob.Layer")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
