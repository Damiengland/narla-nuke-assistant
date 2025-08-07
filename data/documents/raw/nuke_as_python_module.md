[ Nuke Python API Reference ![Logo](_static/NukeApp128.png) ](index.html)

16.0 

  * [Introduction](intro.html)
  * [Start-up Scripts](startup.html)
  * [Getting Started](basics.html)
  * Nuke as a Python Module
    * Licensing
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
  * Nuke as a Python Module
  * 


* * *

# Nuke as a Python Module

Nuke can be used as a Python module. This means you can use Python to do many of the complex things in your VFX pipeline that you couldn’t otherwise do, easily, and is essentially a production level, incredibly powerful replacement for most 2D, 3D and video-editing Python modules.

Built against the version of Python Nuke ships with you can now comp programmatically having full access to the Nuke Python-API but from within a native Python interpreter instead of Nuke. This means you can do things like quickly re-grade 2000 shots, or change the timings of a set of fades based on a selection sheet all in a simple 5 or 6 line script, the Pythonic way. You can connect Nuke more easily to your infrastructure back-ends, integrate it into your pipelines and even put Nuke into other applications.

To use Nuke as Python module you should use the interpreter shipped with Nuke (the module should work with other interpreters but the one Nuke ships with is the only one we officially support).

As with standard Python, you can either use the interpreter interactively or via a script.

So, for example a basic interactive example would be:
    
    
    ```python
    <Nuke-install-path>$ python
    >>> import nuke
    >>> r = nuke.nodes.Read(file='shot-90123-a.exr')
    >>> g = nuke.nodes.Grade( inputs=[r] )
    >>> g['black'].setValue( 0.05 )
    >>> w = nuke.nodes.Write(file='shot-90123-a-graded-up.exr', inputs=[g])
    >>> nuke.execute( w, 1, 1 )
    ```

Or you could put the code into a script like this:
    
    
    ```python
    # gradeShots.py
    import nuke
    import os
    import sys
    
    shot = sys.argv[0]
    r = nuke.nodes.Read(file=sys.argv[0])
    g = nuke.nodes.Grade( inputs=[r] )
    g['black'].setValue( 0.05 )
    outName = '{}-a-grade-up.mov'.format(os.path.split(shot)[0])
    w = nuke.nodes.Write(file=outName, inputs=[g])
    nuke.execute( w, 1, 1 )
    ```

Which you would then run like:
    
    
    ```python
    <Nuke-install-path>/python gradeShots.py shot-90123-a.exr
    ```

## Licensing

If you wish to import Nuke using an interactive license you will need to set the environment variable NUKE_INTERACTIVE to any non-zero integer.

e.g.

> <Nuke-install-path>$ python >>> import os >>> os.environ[ “NUKE_INTERACTIVE” ] = “1” >>> import nuke >>> … >>> …

There are a million and one things you could do with Nuke’s Python module and we would love to hear what you have done with it.

Written by: Frank Harrison.

[ Previous](basics.html "Getting Started") [Next ](animation.html "Animation")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
