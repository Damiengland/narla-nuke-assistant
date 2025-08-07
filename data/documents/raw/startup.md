[ Nuke Python API Reference ![Logo](_static/NukeApp128.png) ](index.html)

16.0 

  * [Introduction](intro.html)
  * Start-up Scripts
    * Evaluation Order
    * menu.py
    * init.py
  * [Getting Started](basics.html)
  * [Nuke as a Python Module](nuke_as_python_module.html)
  * [Animation](animation.html)
  * [Using the Command-line](command_line.html)
  * [Callbacks](callbacks.html)
  * [Stereo](stereo.html)
  * [3D](3D.html)
  * [Roto and RotoPaint](rotopaint.html)
  * [Accessing Image Data](image_data.html)
  * [Custom Panels](custom_panels.html)
  * [Extending NUKE with PySide](custom_panels.html#extending-nuke-with-pyside)
  * [Customizing the UI](custom_ui.html)
  * [Custom Flipbooks](flipbook.html)
  * [Metadata](metadata.html)
  * [Working with Channels and Layers](channels.html)
  * [Manipulating the Node Graph](dag.html)
  * [Formats](formats.html)
  * [Math](math.html)
  * [Asset Management Systems / Pipeline Integration](asset.html)
  * [OpenAssetIO Integration](openassetio.html)
  * [Graph Scope Variables / Multi-shot Set-up](gsv.html)
  * [Threading](threading.html)
  * [Render Farm Integration (Concept)](render_farm.html)
  * [Performance Profiling](performance.html)
  * [Installing Plug-ins](installing_plugins.html)
  * [Sample Scripts](samples.html)



API Reference

  * [nuke](_autosummary/nuke.html)
  * [nuke.curveknob](_autosummary/nuke.curveknob.html)
  * [nuke.curvelib](_autosummary/nuke.curvelib.html)
  * [nuke.gsv](_autosummary/nuke.gsv.html)
  * [nuke.localization](_autosummary/nuke.localization.html)
  * [nuke.memory2](_autosummary/nuke.memory2.html)
  * [nuke.nukemath](_autosummary/nuke.nukemath.html)
  * [nuke.rotopaint](_autosummary/nuke.rotopaint.html)
  * [nuke.splinewarp](_autosummary/nuke.splinewarp.html)
  * [nukescripts](_autosummary/nukescripts.html)



__[Nuke Python API Reference](index.html)

  * [](index.html) »
  * Start-up Scripts
  * 


* * *

# Start-up Scripts

This section describes the scripts that NUKE runs on start-up.

## Evaluation Order

NUKE initialization scripts are run in reverse order of the NUKE plug-in path. At start-up, the default NUKE plug-in path is as follows:

[‘/home/nukeuser/.nuke’, ‘/usr/local/NUKE/6.2/plugins’, ‘/usr/local/Nuke6.2v4/plugins/user’, ‘/usr/local/Nuke6.2v4/plugins/icons’, ‘/usr/local/Nuke6.2v4/plugins’]

This example shows the NUKE plug-in path for NUKE 6.2v4 and a user called ‘nukeuser’. In this case, scripts in ‘/usr/local/Nuke6.2v4/plugins’ are run first, with scripts in ‘/home/nukeuser/.nuke’ run last.

You can query the plug-in directory using nuke.pluginPath(). If necessary, you can prefix additional directories to the path by calling nuke.pluginAddPath(), or append them using nuke.pluginAppendPath(). You can also edit the path by modifying the NUKE_PATH environment variable.

In each plug-in directory, NUKE first executes the init.py file (if one exists), followed by the menu.py file (again, if one exists).

## menu.py

Any file called **menu.py** that is placed in one of NUKE’s plug-in path directories is automatically read when NUKE starts in an interactive session. It is **not** read, however, when NUKE is launched for a command-line session or render. Because of this, you should use menu.py exclusively for commands that are only relevant to interactive sessions. A typical example would be adding favorites to the File Browser or creating custom menus and hotkeys. For more details, see [Customizing the UI](custom_ui.html#customisingui-ref-label).

## init.py

Any file called **init.py** that is placed in one of NUKE’s plug-in path directories is automatically read whenever NUKE is launched. In other words, this file is read for both command-line and interactive sessions. Note that you should **not** use init.py for any commands that create UI elements, as this may lead to errors or prevent NUKE from launching.

Here are some examples of what the init.py file is typically used for (though depending on your workflow, most of these can live in the menu.py file instead if they’re not needed in command-line sessions):

  * adding custom plug-in paths - see [Installing Plug-ins](installing_plugins.html#installingplugins-ref-label)

  * setting knob defaults - see [Defining Knob Defaults](custom_ui.html#knobdefaults-ref-label)

  * setting custom formats - see [Formats](formats.html#formats-ref-label).




[ Previous](intro.html "Introduction") [Next ](basics.html "Getting Started")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
