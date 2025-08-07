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
    * [nuke.localization.addFileCallback](nuke.localization.addFileCallback.html)
    * [nuke.localization.addReadCallback](nuke.localization.addReadCallback.html)
    * [nuke.localization.checkForUpdates](nuke.localization.checkForUpdates.html)
    * [nuke.localization.clearUnusedFiles](nuke.localization.clearUnusedFiles.html)
    * [nuke.localization.findNodes](nuke.localization.findNodes.html)
    * [nuke.localization.forceUpdateAll](nuke.localization.forceUpdateAll.html)
    * [nuke.localization.forceUpdateOnDemand](nuke.localization.forceUpdateOnDemand.html)
    * [nuke.localization.forceUpdateSelectedNodes](nuke.localization.forceUpdateSelectedNodes.html)
    * [nuke.localization.isLocalizationPaused](nuke.localization.isLocalizationPaused.html)
    * [nuke.localization.localizationProgress](nuke.localization.localizationProgress.html)
    * [nuke.localization.localizedPaths](nuke.localization.localizedPaths.html)
    * [nuke.localization.mode](nuke.localization.mode.html)
    * [nuke.localization.pauseLocalization](nuke.localization.pauseLocalization.html)
    * [nuke.localization.removeFileCallback](nuke.localization.removeFileCallback.html)
    * [nuke.localization.removeReadCallback](nuke.localization.removeReadCallback.html)
    * [nuke.localization.resumeLocalization](nuke.localization.resumeLocalization.html)
    * [nuke.localization.setMode](nuke.localization.setMode.html)
    * nuke.localization.FileEvent
    * [nuke.localization.ReadStatus](nuke.localization.ReadStatus.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * [nuke.localization](nuke.localization.html) »
  * nuke.localization.FileEvent
  * 


* * *

# nuke.localization.FileEvent

_class _nuke.localization.FileEvent[[source]](../_modules/nuke_internal/localization.html#FileEvent)
    

Bases: `object`

Events received in file callbacks

Methods

Attributes

`CACHE_FULL` |   
---|---  
`DISK_FULL` |   
`LOCALIZED` |   
`OUT_OF_DATE` |   
`REMOVED` |   
  
[ Previous](nuke.localization.setMode.html "nuke.localization.setMode") [Next ](nuke.localization.ReadStatus.html "nuke.localization.ReadStatus")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
