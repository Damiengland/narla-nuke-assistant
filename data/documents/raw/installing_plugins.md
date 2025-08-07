[ Nuke Python API Reference ![Logo](_static/NukeApp128.png) ](index.html)

16.0 

  * [Introduction](intro.html)
  * [Start-up Scripts](startup.html)
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
  * Installing Plug-ins
    * Home Directory
    * Custom Plug-in Repository
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
  * Installing Plug-ins
  * 


* * *

# Installing Plug-ins

There are a few different ways to install plug-ins, gizmos, and Python scripts so NUKE can see them. The easiest way is to use your home directory’s ~/.nuke folder, which is created the first time NUKE launches. However, this is not feasible in a multi-user environment. In this case, a custom plug-in directory is preferable. You can set one up using the NUKE_PATH environment variable.

Note

It is not a good idea to place custom plug-ins in NUKE’s install directory, as there may be permission and security issues and the plug-ins will not be available across different versions of NUKE.

Here are the details:

## Home Directory

On [Nukepedia](http://www.nukepedia.com/video-tutorials/22/video/), you can watch a video tutorial about installing plug-ins in the home directory.

As mentioned above, the ~/.nuke directory is created when NUKE launches (if it doesn’t already exist). The path to this directory is added to NUKE’s plug-in path. You can view the plug-in path as follows:
    
    
    ```python
    nuke.pluginPath()
    # Result:
    ['/Users/frank/.nuke', '/Library/Application Support/NUKE/6.2/plugins', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins']
    ```

Everything in the listed directories can be accessed from within NUKE. Without custom UI code in place, you can use the **Other > All Plugins > Update** option to force load everything in those directories into the **Other > All Plugins** menu.

![_images/plugins_01.png](_images/plugins_01.png) ![_images/plugins_02.png](_images/plugins_02.png)

This approach is fine for quick debugging or testing, but is not an acceptable workflow solution. What you want to do once you have your custom gizmo or plug-in in the ~/.nuke directory, is to create a [menu.py](startup.html#menupy-ref-label) file, which is automatically run when NUKE launches in interactive mode. Then, create a custom menu item in that file for the new gizmo or plug-in:
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( 'Other/MyGizmo', lambda: nuke.createNode( 'MyGizmo' ) )
    ```

Here, the second _MyGizmo_ is the file name of the custom plug-in or gizmo (for example, _~/.nuke/MyGizmo.gizmo_).

A similar approach can be taken with Python scripts. Let’s say you have a file called ~/.nuke/myFunctions.py, which contains a function called _doCoolStuff()_. You can import the module in your [menu.py](startup.html#menupy-ref-label), then assign the callable to a custom menu item:
    
    
    ```python
    import myFunctions
    nuke.menu( 'Nuke' ).addCommand( 'My Cool Functions/do cool stuff', myFunctions.doCoolStuff )
    ```

To organize custom files better, you can create sub-directories for each type (for example, “gizmos”, “plugins”, “python”, and so on) and add them to NUKE’s plug-in path at start-up:
    
    
    ```python
    nuke.pluginAddPath( '.gizmos' )
    nuke.pluginAddPath( '.python' )
    nuke.pluginAddPath( '.plugins' )
    ```

The above code is best placed in a file called [init.py](startup.html#initpy-ref-label), which is automatically read every time NUKE launches (both in interactive and command-line mode). You can use both absolute and relative paths. With the above relative paths saved into a file called _~/.nuke/init.py_ , after relaunching NUKE, you can run `nuke.pluginPath()` again to make sure the new directories are now read:
    
    
    ```python
    nuke.pluginPath()
    # Result:
    ['/Users/frank/.nuke/.gizmos', '/Users/frank/.nuke/.python', '/Users/frank/.nuke/.plugins', '/Users/frank/.nuke', '/Library/Application Support/NUKE/6.2/plugins', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins']
    ```

Note that `nuke.pluginAddPath` prefixes paths to the start of the plug-in path. If you want to append them to the end of the path instead, use `nuke.pluginAppendPath`. For details, see [Evaluation Order](startup.html#evaluationorder-ref-label).

## Custom Plug-in Repository

To use a custom plug-in directory that is shared across a network, you can either use the `nuke.pluginAddPath` function in each user’s ~/.nuke/init.py file or use the environment variable NUKE_PATH.

Here is how to do that in a bash shell under Linux or Mac OS X:

![_images/plugins_03.png](_images/plugins_03.png)

Then, in NUKE:
    
    
    ```python
    nuke.pluginPath()
    # Result:
    ['/Users/frank/.nuke', '/Volumes/Library/NukePlugins', '/Library/Application Support/NUKE/6.2/plugins', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins']
    ```

Note

The ~/.nuke directory is always at the start of the plug-in path. This way, any default and facility settings can always be overwritten on a per-user basis.

You can now create any sub-directories you may need for organizing your custom tools and use an [init.py](startup.html#initpy-ref-label) file to include them in the plug-in path:

![_images/plugins_04.png](_images/plugins_04.png)

From the init.py file:
    
    
    ```python
    nuke.pluginAddPath( './gizmos' )
    nuke.pluginAddPath( './python' )
    nuke.pluginAddPath( './plugins' )
    ```

In NUKE:
    
    
    ```python
    nuke.pluginPath()
    # Result:
    ['/Users/frank/.nuke', '/Volumes/Library/NukePlugins/gizmos', '/Volumes/Library/NukePlugins/python', '/Volumes/Library/NukePlugins/plugins', '/Volumes/Library/NukePlugins', '/Library/Application Support/NUKE/6.2/plugins', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/user', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins/icons', '/Applications/Nuke6.2v3/NukeX6.2v3.app/../Nuke6.2v3.app/Contents/MacOS/plugins']
    ```

On that level, you can also create user directories where everyone can park their custom code that is only accessible to the author. Let’s say you add a sub-directory called _Users_ for this purpose, which contains sub-directories for each user’s login name:

![_images/plugins_05.png](_images/plugins_05.png)

You can now place the following code in your top level init.py file to check for the current user when NUKE starts up and only include the respective user directory if it exists:
    
    
    ```python
    import os
    
    user = os.getenv('USER')
    userPath = os.path.join( '/Library/NukePlugins/Users', user )
    if os.path.isdir( userPath ):
        nuke.pluginAddPath( userPath )
    ```

You can also source project-specific tools in the same way. In this example, we assume all show directories live in /projects and we have set an environment variable called SHOW, which tells us the current show’s name. We then look for the /nuke directory inside the current show directory and add that to the plug-in path:

![_images/plugins_06.png](_images/plugins_06.png)
    
    
    ```python
    curShow = os.getenv('SHOW')
    showPath = os.path.join( '/projects', curShow, 'nuke' )
    if os.path.isdir( showPath ):
        nuke.pluginAddPath( showPath )
    ```

You can now place all the show-specific code in each show’s /nuke directory, and use [menu.py](startup.html#menupy-ref-label) and [init.py](startup.html#initpy-ref-label) to further define the structure.

If you want to load all the tools for all the shows (it can be quite handy to quickly grab custom tools from another show when you’re in a pinch), you can use code like this:
    
    
    ```python
    baseDir = '/projects'
    shows = os.listdir( baseDir )
    for s in shows:
        showPath = os.path.join( baseDir, s, 'nuke' )
        if os.path.isdir( showPath ):
            nuke.pluginAddPath( showPath )
    ```

[ Previous](performance.html "Performance Profiling") [Next ](samples.html "Sample Scripts")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
