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
  * Render Farm Integration (Concept)
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
  * Render Farm Integration (Concept)
  * 


* * *

# Render Farm Integration (Concept)

Every render manager works in a different manner and facilities’ requirements for their pipeline integration vary, so here is a very brief example describing the basic concept of integrating a render manager.

Tip

You can find more information on this on [Nukepedia](http://www.nukepedia.com/written-tutorials/) (look for “Render Manager”).

Here is a simple panel example for collecting information that might be relevant to a render farm submission:
    
    
    ```python
    p = nuke.Panel( 'submit to farm' )
    
    p.addSingleLineInput( 'first', nuke.root().firstFrame() )
    p.addSingleLineInput( 'last', nuke.root().lastFrame() )
    
    p.addEnumerationPulldown( 'threads', '1 2 4 8' )
    p.addSingleLineInput( 'batch size', '10' )
    p.addBooleanCheckBox( 'local render', 0 )
    
    p.show()
    ```

![_images/renderMan_01.png](_images/renderMan_01.png)

You could then collect the user input in variables and build the required command for the submission. This snippet just generates pseudo code, which could be tweaked to create a valid submission command:
    
    
    ```python
    if p.show():
        args = dict( first = p.value('first'),
            last = p.value('last'),
            threads = p.value('threads'),
            batchSize = p.value('batch size'),
            local = p.value('local'))
    
        application = 'echo'
        #args = [ application, first, last, threads, batchSize, local ]
        cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args
    
        subprocess.Popen( cmdString.split() )
    ```

The above could then be wrapped into a function and placed in NUKE’s Render menu:
    
    
    ```python
    def submitToFarm():
        p = nuke.Panel( 'submit to farm' )
    
        p.addSingleLineInput( 'first', nuke.root().firstFrame() )
        p.addSingleLineInput( 'last', nuke.root().lastFrame() )
    
        p.addEnumerationPulldown( 'threads', '1 2 4 8' )
        p.addSingleLineInput( 'batch size', '10' )
        p.addBooleanCheckBox( 'local render', 0 )
    
        if p.show():
            args = dict( first = p.value('first'),
                last = p.value('last'),
                threads = p.value('threads'),
                batchSize = p.value('batch size'),
                local = p.value('local'))
    
            application = 'echo'
            #args = [ application, first, last, threads, batchSize, local ]
            cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args
    
            subprocess.Popen( cmdString.split() )
    
    nuke.menu( 'Nuke' ).addCommand( 'Render/Send to Farm', submitToFarm )
    ```

![_images/renderMan_02.png](_images/renderMan_02.png)

You can use [Python Panels](custom_panels.html#pythonpanel-ref-label) to create more complex panels and non-modal panels that can be docked to the UI and saved with layouts. You could also add custom knobs to the Write nodes to launch a network render. See [Adding Controls to Nodes](basics.html#addingparamstonodes-ref-label) for details on this.

[ Previous](threading.html "Threading") [Next ](performance.html "Performance Profiling")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
