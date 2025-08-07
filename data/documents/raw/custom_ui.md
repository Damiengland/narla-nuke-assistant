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
  * Customizing the UI
    * Creating a Custom Menu
    * Creating a Custom Toolbar
    * Creating a Custom Menu Item
    * Assigning a Hotkey
    * Defining Knob Defaults
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
  * Customizing the UI
  * 


* * *

# Customizing the UI

This chapter explains how to create your own hotkeys, menus, and menu items. This kind of code is typically placed in the [menu.py](startup.html#menupy-ref-label) file. Please refer to [Installing Plug-ins](installing_plugins.html#installingplugins-ref-label) for information on how to install custom files.

The menus currently available in NUKE are:

  * **Nuke** \- the application menu on top of the interface.


![_images/ui_01.png](_images/ui_01.png)

  * **Windows** \- the **Windows** menu found in all content menus.


![_images/ui_02.png](_images/ui_02.png)

  * **Nodes** \- the toolbar (and the right-click menu in the Node Graph).


![_images/ui_03.png](_images/ui_03.png)

  * **Properties** \- right-click menus of properties panels.


![_images/ui_04.png](_images/ui_04.png)

  * **Animation** \- the pop-up menu on the Animation button of all properties panels, and the right-click menu of the Curve Editor.


![_images/ui_05.png](_images/ui_05.png)

  * **Viewer** \- the right-click menu of the Viewer.


![_images/ui_06.png](_images/ui_06.png)

  * **Node Graph** \- the right-click menu of the Node Graph.


![_images/ui_07.png](_images/ui_07.png)

  * **Axis** \- the menus on all Axis_Knobs.


![_images/ui_08.png](_images/ui_08.png)

## Creating a Custom Menu

To create a custom menu, use:
    
    
    ```python
    m = nuke.menu( 'Viewer' )
    myMenu = m.addMenu( 'MyStuff' )
    ```

You can assign an icon to the menu as well:
    
    
    ```python
    m = nuke.menu( 'Viewer' )
    myMenu = m.addMenu( 'MyStuff', icon='ohu_icon.png' )
    ```

![_images/ui_15.png](_images/ui_15.png)

## Creating a Custom Toolbar

To create a custom toolbar, use:
    
    
    ```python
    myToolbar = nuke.toolbar( 'My nodes' )
    ```

![_images/ui_16.png](_images/ui_16.png)

You can add custom items to the toolbar in the same way as to a menu (see below for details):
    
    
    ```python
    myToolbar.addCommand( 'My Gizmo', lambda: nuke.createNode('NoOp') )
    ```

If you don’t specify a toolbar menu for the item, the item is added as a button on the toolbar:

![_images/ui_17.png](_images/ui_17.png)

Otherwise, the item is added as a menu (like in the default toolbar):
    
    
    ```python
    myToolbar.addCommand( 'My Other Tools/tool A', lambda: nuke.createNode('NoOp') )
    myToolbar.addCommand( 'My Other Tools/tool B', lambda: nuke.createNode('NoOp') )
    ```

![_images/ui_18.png](_images/ui_18.png)

To add an icon for the menu, create it explicitly before assigning menu items to it:
    
    
    ```python
    myMenu = myToolbar.addMenu( 'My Other Tools', icon='ohu_icon.png' )
    myMenu.addCommand( 'tool A', lambda: nuke.createNode('NoOp') )
    myMenu.addCommand( 'tool B', lambda: nuke.createNode('NoOp') )
    ```

![_images/ui_19.png](_images/ui_19.png)

## Creating a Custom Menu Item

To add a custom entry to any of the above menus, use `menu.addCommand()`:
    
    
    ```python
    nuke.menu( 'Nuke' ).addCommand( 'MyMenu/my tool 1', lambda: nuke.message('yay, it works') )
    ```

Note

In the above example, we create a menu called _MyMenu_ menu on the fly.

![_images/ui_10.png](_images/ui_10.png)

Instead of using **lambda** to create an anonymous function that isn’t executed until the menu item is evoked, you could also wrap the desired command into a string:
    
    
    ```python
    nuke.menu( 'Nuke' ).addCommand( 'MyMenu/my tool 2', "nuke.message('yay, it works too')" )
    ```

![_images/ui_11.png](_images/ui_11.png)

You can also assign an icon to the menu item from NUKE’s plug-in path:
    
    
    ```python
    nuke.menu( 'Nuke' ).addCommand( 'MyMenu/my tool 2', "nuke.message('yay, it works too')", icon='ohu_icon.png' )
    ```

![_images/ui_12.png](_images/ui_12.png)

To set the position of the item in the menu, use the **index** argument:
    
    
    ```python
    nuke.menu( 'Nuke' ).addCommand( 'MyMenu/my tool 1.5', "nuke.message('yay, it works too')", index=1 )
    ```

![_images/ui_13.png](_images/ui_13.png)

Find the menu by name (we didn’t assign it to a variable at creation time), and add a separator before adding another menu item:
    
    
    ```python
    m = nuke.menu( 'Nuke' ).findItem( 'MyMenu' )
    m.addSeparator()
    nuke.menu( 'Nuke' ).addCommand( 'MyMenu/my tool 3', "nuke.message('yay, it works too')")
    ```

![_images/ui_20.png](_images/ui_20.png)

To find an existing menu item and run its function call, use:
    
    
    ```python
    m = nuke.menu( 'Nuke' ).findItem( 'Edit/Node/Filename/Show' )
    m.invoke()
    ```

To deactivate a menu item, use:
    
    
    ```python
    m = nuke.menu( 'Nuke' ).findItem( 'Render/Proxy Mode' )
    m.setEnabled( False )
    ```

![_images/ui_14.png](_images/ui_14.png)

Note

If you deactivate a menu item, the hotkey assigned to it still continues to work.

## Assigning a Hotkey

To assign a hotkey to an existing menu item, you effectively replace the whole menu item.

Let’s assign a hotkey to the Axis2 node. This node lives in the **Nodes** menu (that is, the toolbar), inside the **3D** sub-menu. Its menu item is called _Axis_.
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', lambda: nuke.createNode( 'Axis2' ), 'a')
    ```

Pressing **a** on the keyboard now creates an Axis node.

![_images/ui_09.png](_images/ui_09.png)

You can also use modifier keys when assigning a hotkey.

To use **Ctrl** (or **cmd** on Mac OS X) as the modifier, use:

  * **ctrl+** followed by the key, or

  * **^** followed by the key.




For example:
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", 'ctrl+a')
    ```
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", '^a')
    ```

To use **alt** as the modifier, use:

  * **alt+** followed by the key, or

  * **#** followed by the key.




For example:
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", 'alt+a')
    ```
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", '#a')
    ```

To use **shift** as the modifier, use:

  * **shift+** followed by the key, or

  * **+** followed by the key.




For example:
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", 'shift+a')
    ```
    
    
    ```python
    nuke.menu( 'Nodes' ).addCommand( '3D/Axis', "nuke.createNode( 'Axis2' )", '+a')
    ```

## Defining Knob Defaults

To change the default values for knobs, use `nuke.knobDefault()`:
    
    
    ```python
    nuke.knobDefault( 'Blur.size', '77' )
    ```

The above line sets the **size** control of any subsequently created Blur nodes to **77** by default.

When skipping the node class, the new default value is applied to all controls of the given name:
    
    
    ```python
    nuke.knobDefault( 'channels', 'rgba' )
    ```

The above sets all **channels** controls to **rgba** on node creation.

[ Previous](custom_panels.html "Custom Panels") [Next ](flipbook.html "Custom Flipbooks")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
