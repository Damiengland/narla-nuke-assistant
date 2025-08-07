[ Nuke Python API Reference ![Logo](_static/NukeApp128.png) ](index.html)

16.0 

  * [Introduction](intro.html)
  * [Start-up Scripts](startup.html)
  * [Getting Started](basics.html)
  * [Nuke as a Python Module](nuke_as_python_module.html)
  * [Animation](animation.html)
  * Using the Command-line
    * Running NUKE in Python Mode
    * Using Command-line Arguments
    * Modifying Existing NUKE Scripts
    * Executing Frame Ranges
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
  * Using the Command-line
  * 


* * *

# Using the Command-line

This topic covers how to use the NUKE command line to execute Python scripts.

## Running NUKE in Python Mode

NUKE can be executed in Python interpreter mode by using the **-t** argument. For example:
    
    
    ```python
    <Nuke-install-path>/Nuke13.0 -t
    Nuke 13.0v1, 64 bit, built Mar  5 2021.
    Copyright (c) 2021 The Foundry Visionmongers Ltd.  All Rights Reserved.
    >>>
    ```

To execute a Python script at startup, use the script file name after the **-t** switch:
    
    
    ```python
    <Nuke-install-path>/Nuke13.0 -t <mypythonscript.py>
    ```

## Using Command-line Arguments

When NUKE runs a Python script, it passes the script arguments to the script in **sys.argv**.

For example, first make a file called **test.py** containing the following:
    
    
    ```python
    import sys, nuke
    print('sys.argv: {}'.format(sys.argv))
    ```

Now run this from the command line to see what **sys.argv** contains:
    
    
    ```python
    <Nuke-install-path>/Nuke13.0 -t test.py Hello World!
    Nuke 13.0v1, 64 bit, built Mar  5 2021.
    Copyright (c) 2021 The Foundry Visionmongers Ltd.  All Rights Reserved.
    sys.argv: ['test.py', 'Hello', 'World!']
    ```

As you can see, NUKE passes the arguments after **-t** to the Python interpreter.

The only exception to this is if the last argument is a number or frame range. For example:
    
    
    ```python
    <Nuke-install-path>/Nuke13.0 -t test.py Hello World 1,2
    WARNING: The command line argument ' 1,23' will be used as a Frame Range argument and will not be forward to the python sys.argv.
    To define a frame range argument use the -F option.
    Nuke 13.0v1, 64 bit, built Mar  5 2021.
    Copyright (c) 2021 The Foundry Visionmongers Ltd.  All Rights Reserved.
    sys.argv: ['test.py', 'Hello', 'World!']
    ```

In this case, the 1,20 is stripped from **sys.args** and the frame range is available in nuke.tcl(‘frames all’).

To access all the command-line arguments passed to nuke you can use:
    
    
    ```python
    nuke.rawArgs
    ```

For example, edit the **test.py** to contain the following:
    
    
    ```python
    import sys, nuke
    print('sys.argv: {}'.format(sys.argv))
    print('nuke.rawArgs: {}'.format(nuke.rawArgs))
    ```

Now execute this:
    
    
    ```python
    <Nuke-install-path>/Nuke13.0 -t test.py Hello World 1,2
    WARNING: The command line argument ' 1,2' will be used as a Frame Range argument and will not be forward to the python sys.argv.
    To define a frame range argument use the -F option.
    Nuke 13.0v1, 64 bit, built Mar  5 2021.
    Copyright (c) 2021 The Foundry Visionmongers Ltd.  All Rights Reserved.
    sys.argv: ['test.py', 'Hello', 'World!']
    nuke.rawArgs: ['./Nuke13.0', '-t', 'test.py', 'Hello', 'World!', '1,2']
    ```

## Modifying Existing NUKE Scripts

It is sometimes useful to modify existing NUKE scripts using Python, for instance, when rewriting file paths.

The following script opens up a NUKE script on the command-line, rewrites all the write file paths, and finally saves the script:
    
    
    ```python
    ### save this file as replaceWritePaths.py
    
    import nuke
    import os
    import sys
    
    def RecursiveFindNodes(nodeClass, startNode):
            if startNode.Class() == nodeClass:
                    yield startNode
            elif isinstance(startNode, nuke.Group):
                    for child in startNode.nodes():
                            for foundNode in RecursiveFindNodes(nodeClass, child):
                                    yield foundNode
    
    
    
    if len (sys.argv) != 5:
            print('Usage: NUKE replaceWritePaths.py <nuke_script> <new_nuke_script> <in_file_pattern> <new_file_pattern>')
            sys.exit(-1)
    
    inScript = sys.argv[1]
    outScript = sys.argv[2]
    inPattern = sys.argv[3]
    outPattern = sys.argv[4]
    
    nuke.scriptOpen(inScript)
    
    allWriteNodes = [w for w in RecursiveFindNodes('Write', nuke.root())]
    
    for write in allWriteNodes:
            path = write['file'].value()
            path = path.replace(inPattern, outPattern)
            write['file'].setValue(path)
    
    nuke.scriptSave(outScript)
    ```

This example has the following syntax when run:
    
    
    ```python
    ./Nuke13.0 replaceWritePaths.py <nuke_script> <new_nuke_script> <in_file_pattern> <new_file_pattern>
    ```

Where:
    

  * **< nuke_script>** is the script to read in.

  * **< new_nuke_script>** is the name to save the modified script to.

  * **< in_file_pattern>** is string to search for in all the write file paths.

  * **< new_file_pattern>** is the string to replace <in_file_pattern> in all the write file paths.




## Executing Frame Ranges

When running Python with the **-t** switch, NUKE does not render or execute any nodes by default.

To render a node you need to call:
    
    
    ```python
    nuke.execute(nodeName, firstFrame, lastFrame)
    ```

However, when you use the **-x** switch to render a frame range and you supply a Python file (.py) instead of a NUKE (.nk) script, NUKE executes the Python first and then renders all the writes in the script with the given frame range.

For example, save this script as **convert.py** :
    
    
    ```python
    import sys
    import nuke
    r = nuke.nodes.Read(file = sys.argv[1])
    w = nuke.nodes.Write(file = sys.argv[2])
    w.setInput(0, r)
    ```

Now, as an example, run the script from the command line as shown to convert some jpegs to tifs for 5 frames:
    
    
    ```python
    ./Nuke13.0 -x convert.py myfiles.###.jpg myfiles.###.tif 1,5
    ```

[ Previous](animation.html "Animation") [Next ](callbacks.html "Callbacks")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
