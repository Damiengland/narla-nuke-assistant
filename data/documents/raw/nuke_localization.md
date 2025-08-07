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
  * nuke.localization
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
    * [nuke.localization.FileEvent](nuke.localization.FileEvent.html)
    * [nuke.localization.ReadStatus](nuke.localization.ReadStatus.html)
  * [nuke.memory2](nuke.memory2.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * nuke.localization
  * 


* * *

# nuke.localization

APIs for Nuke’s localization functionality.

Use help(‘_localization’) to get detailed help on the classes exposed here.

This module provides the public interface to the localization module and will remain stable. It uses an underlying native module called _localization to provide this interface. While there is nothing stopping you from using the _localization module directly, it may change in a future release and break backwards compatibility.

Functions

[`addFileCallback`](nuke.localization.addFileCallback.html#nuke.localization.addFileCallback "nuke.localization.addFileCallback") | 

param callback
    is a python callable object with arguments for path and event. See nuke.localization.FileEvent for possible file events.  
---|---  
[`addReadCallback`](nuke.localization.addReadCallback.html#nuke.localization.addReadCallback "nuke.localization.addReadCallback") | Adds a callback for read localization events.  
[`checkForUpdates`](nuke.localization.checkForUpdates.html#nuke.localization.checkForUpdates "nuke.localization.checkForUpdates") | Trigger a manual file check, which checks and updates the states of localised files.  
[`clearUnusedFiles`](nuke.localization.clearUnusedFiles.html#nuke.localization.clearUnusedFiles "nuke.localization.clearUnusedFiles") | Clears unused files in the localization folder.  
[`findNodes`](nuke.localization.findNodes.html#nuke.localization.findNodes "nuke.localization.findNodes") | Returns the list of read nodes that read from the argument paths.  
[`forceUpdateAll`](nuke.localization.forceUpdateAll.html#nuke.localization.forceUpdateAll "nuke.localization.forceUpdateAll") | Update all localized files currently in use in Nuke.  
[`forceUpdateOnDemand`](nuke.localization.forceUpdateOnDemand.html#nuke.localization.forceUpdateOnDemand "nuke.localization.forceUpdateOnDemand") | forceUpdateAll() -> None  
[`forceUpdateSelectedNodes`](nuke.localization.forceUpdateSelectedNodes.html#nuke.localization.forceUpdateSelectedNodes "nuke.localization.forceUpdateSelectedNodes") | Update all localized files used by nodes that are currently selected.  
[`isLocalizationPaused`](nuke.localization.isLocalizationPaused.html#nuke.localization.isLocalizationPaused "nuke.localization.isLocalizationPaused") | 

return
    whether localization was paused  
[`localizationProgress`](nuke.localization.localizationProgress.html#nuke.localization.localizationProgress "nuke.localization.localizationProgress") | gets the percentage of localization completed.  
[`localizedPaths`](nuke.localization.localizedPaths.html#nuke.localization.localizedPaths "nuke.localization.localizedPaths") | gets paths of files which are currently localized.  
[`mode`](nuke.localization.mode.html#nuke.localization.mode "nuke.localization.mode") | :return string 'on', 'off' or 'manual'  
[`pauseLocalization`](nuke.localization.pauseLocalization.html#nuke.localization.pauseLocalization "nuke.localization.pauseLocalization") | Pause the localization background thread if it was running.  
[`removeFileCallback`](nuke.localization.removeFileCallback.html#nuke.localization.removeFileCallback "nuke.localization.removeFileCallback") | Removes a callback for file localization events.  
[`removeReadCallback`](nuke.localization.removeReadCallback.html#nuke.localization.removeReadCallback "nuke.localization.removeReadCallback") | Removes a callback for read localization events  
[`resumeLocalization`](nuke.localization.resumeLocalization.html#nuke.localization.resumeLocalization "nuke.localization.resumeLocalization") | Resume the localization background thread if it was paused  
[`setMode`](nuke.localization.setMode.html#nuke.localization.setMode "nuke.localization.setMode") | sets the localization system mode.  
  
Classes

[`FileEvent`](nuke.localization.FileEvent.html#nuke.localization.FileEvent "nuke.localization.FileEvent") | Events received in file callbacks  
---|---  
[`ReadStatus`](nuke.localization.ReadStatus.html#nuke.localization.ReadStatus "nuke.localization.ReadStatus") | Localization status recieved by Read callbacks  
  
[ Previous](nuke.gsv.DataType.html "nuke.gsv.DataType") [Next ](nuke.localization.addFileCallback.html "nuke.localization.addFileCallback")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
