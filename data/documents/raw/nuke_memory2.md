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
  * nuke.memory2
    * [nuke.memory2.allocatorInfo](nuke.memory2.allocatorInfo.html)
    * [nuke.memory2.clearUsage](nuke.memory2.clearUsage.html)
    * [nuke.memory2.info](nuke.memory2.info.html)
    * [nuke.memory2.maxUsage](nuke.memory2.maxUsage.html)
    * [nuke.memory2.setMaxUsage](nuke.memory2.setMaxUsage.html)
    * [nuke.memory2.setUsage](nuke.memory2.setUsage.html)
    * [nuke.memory2.totalRAM](nuke.memory2.totalRAM.html)
    * [nuke.memory2.totalVM](nuke.memory2.totalVM.html)
    * [nuke.memory2.usage](nuke.memory2.usage.html)
  * [nuke.nukemath](nuke.nukemath.html)
  * [nuke.rotopaint](nuke.rotopaint.html)
  * [nuke.splinewarp](nuke.splinewarp.html)
  * [nukescripts](nukescripts.html)



__[Nuke Python API Reference](../index.html)

  * [](../index.html) »
  * nuke.memory2
  * 


* * *

# nuke.memory2

Memory module containing functionality for querying and controlling Nuke’s Memory API, currently the module is named memory2 for backwards compatibility with the old nuke.memory(cmd, value) function which is now deprecated. Once removed this module will be deprecated and it will be renamed to nuke.memory. To avoid future conflicts it is recommended to import like so:

from nuke import memory2 as memory

Functions

[`allocatorInfo`](nuke.memory2.allocatorInfo.html#nuke.memory2.allocatorInfo "nuke.memory2.allocatorInfo") | Creates a dictionary of allocators mapped by their name to another dictionary containing various metadata information about the allocator.  
---|---  
[`clearUsage`](nuke.memory2.clearUsage.html#nuke.memory2.clearUsage "nuke.memory2.clearUsage") | Attempts to clear all memory, setUsage(0) and clearUsage() are effectively the same.  
[`info`](nuke.memory2.info.html#nuke.memory2.info "nuke.memory2.info") | Creates a dictionary of Node names mapped to a list of memory information for that node.  
[`maxUsage`](nuke.memory2.maxUsage.html#nuke.memory2.maxUsage "nuke.memory2.maxUsage") | Reports the maximum memory usage Nuke will aim to use.  
[`setMaxUsage`](nuke.memory2.setMaxUsage.html#nuke.memory2.setMaxUsage "nuke.memory2.setMaxUsage") | Set the maximum memory usage Nuke will aim to use.  
[`setUsage`](nuke.memory2.setUsage.html#nuke.memory2.setUsage "nuke.memory2.setUsage") | If the value given is less than the current usage, free memory to the new usage.  
[`totalRAM`](nuke.memory2.totalRAM.html#nuke.memory2.totalRAM "nuke.memory2.totalRAM") | Reports the total RAM detected by Nuke.  
[`totalVM`](nuke.memory2.totalVM.html#nuke.memory2.totalVM "nuke.memory2.totalVM") | Reports the total virtual memory (VM) detected by Nuke.  
[`usage`](nuke.memory2.usage.html#nuke.memory2.usage "nuke.memory2.usage") | Reports the current memory usage allocated.  
  
[ Previous](nuke.localization.ReadStatus.html "nuke.localization.ReadStatus") [Next ](nuke.memory2.allocatorInfo.html "nuke.memory2.allocatorInfo")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
