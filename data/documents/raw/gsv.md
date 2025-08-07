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
  * Graph Scope Variables / Multi-shot Set-up
    * The _Gsv_Knob_
    * The _Gsv_Knob_ Value Format
    * Removing and Editing Variables and Sets
    * Specifying GSV Value Options
    * Adding GSVs to the Variables Panel
    * Variable Scopes and Overrides
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
  * Graph Scope Variables / Multi-shot Set-up
  * 


* * *

# Graph Scope Variables / Multi-shot Set-up

Graph Scope Variables allow you to define, store and access the data required for multiple contexts or scopes in a single Nuke script. You can, optionally, define these scopes as VariableGroup nodes in your Node Graph and switch the scope based on the variables available.

To share a Graph Scope Variable set-up between Nuke scripts, you can add variables to existing scripts using the python API. Here we will run through an example of setting up the GSVs using python within an script.

## The _Gsv_Knob_

The [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") provides the interface to interact with _Graph_ _Scope Variables_. The [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") holds the _Graph Variables_ created within the scope of each group.

We will start by considering the Root [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob").

The Root [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") can be obtained as follows:
    
    
    ```python
    root_node = nuke.root()
    gsv_knob = root_node['gsv']
    ```

The [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") holds _Variable Sets_ which contain the _Variables_. The [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") has a special _Variable Set_ called **__default__**. This set is used for _Variables_ which you would like to display directly inside the group (in this case the Root).

Let’s use **__default__** to add GSVs to the project:
    
    
    ```python
    gsv_knob.setGsvValue("__default__.show_name", "sidi_ali")
    gsv_knob.setGsvValue("__default__.show_root", "/Volumes/Projects/Multishot")
    gsv_knob.setGsvValue("__default__.shot", "shot30")
    ...
    ```

Note

[`setGsvValue()`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob.setGsvValue "nuke.Gsv_Knob.setGsvValue") takes a `path` as the first parameter. This is composed as a dot separated path, i.e. `variable_set.variable_name`.

Here is an example of the Root projects settings after adding variables:

![_images/gsv_variables_01.png](_images/gsv_variables_01.png)

We can also add shot specific variables to a named _Variable Set_ :
    
    
    ```python
    gsv_knob.addGsvSet("shot10_plate")
    gsv_knob.setGsvValue("shot10_plate.name", "s00010")
    ...
    ```

This is how the Root project settings looks after adding _Variables_ under a _Variable Set_ :

![_images/gsv_variables_02.png](_images/gsv_variables_02.png)

## The _Gsv_Knob_ Value Format

The value of the Root [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") can be obtained with [`value()`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob.value "nuke.Gsv_Knob.value"):
    
    
    ```python
    gsv_knob.value()
    # Result: {
      '__default__': {
        'shot': 'shot30',
        'show_name': 'sidi_ali',
        'show_root': '/Volumes/Projects/Multishot'
      },
      'shot10_plate': {
        'name': 's00010'
      }
    }
    ```

The format of the value is a dictionary of sets, each containing a dictionary of `'variable_name': 'value'` pairs.

Note

Remember that every GSV is contained in a set. The GSVs directly under the group are placed in the special set called **__default__**.

Rather than settings GSVs one at a time, they can all be set at once by rebuilding the knob value using [`setValue()`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob.setValue "nuke.Gsv_Knob.setValue"), for example:
    
    
    ```python
    gsv_knob.setValue(
      {
         '__default__': {
           'shot': 'shot30',
           'show_name': 'sidi_ali2',
           'show_root': '/Volumes/Projects/Multishot2'
         },
         'shot10_plate': {
           'name': 's00010'
         }
       }
    )
    ```

## Removing and Editing Variables and Sets

To make edits to existing GSVs you may want to rename variable sets and GSVs:
    
    
    ```python
    gsv_knob.renameGsvSet("shot10_plate", "plates_shot10")
    gsv_knob.renameGsv("plates_shot10.name", "shot_name")
    ```

You can also remove variables and sets:
    
    
    ```python
    gsv_knob.removeGsvSet("plates_shot10")
    gsv_knob.removeGsv("__default__.show_name")
    ```

To change the value of a GSV, simply set the value again:
    
    
    ```python
    gsv_knob.setGsvValue("__default__.shot", "shot20")
    ```

## Specifying GSV Value Options

Often GSVs only have a few options available. To help simplify the process of setting variables, they can be registered as a _List_ data type. This requires a list of options to be specified. This can be done in python as follows:
    
    
    ```python
    gsv_knob.setDataType("__default__.shot", nuke.gsv.DataType.List)
    gsv_knob.setListOptions("__default__.shot", ["shot10", "shot20", "shot30"])
    ```

## Adding GSVs to the Variables Panel

Variables to which you would like quick and easy access can be added to the Variables panel:

![_images/gsv_panel_01.png](_images/gsv_panel_01.png)

Let us add some global settings to our GSVs:
    
    
    ```python
    gsv_knob.addGsvSet("Global_Settings")
    
    gsv_knob.setGsvValue("Global_Settings.FastDefocus", "on")
    gsv_knob.setDataType("Global_Settings.FastDefocus", nuke.gsv.DataType.List)
    gsv_knob.setListOptions("Global_Settings.FastDefocus", ["on", "off"])
    
    gsv_knob.setGsvValue("Global_Settings.MotionBlur", "off")
    gsv_knob.setDataType("Global_Settings.MotionBlur", nuke.gsv.DataType.List)
    gsv_knob.setListOptions("Global_Settings.MotionBlur", ["on", "off"])
    ...
    ```

We can then add accessible variables to the Variables Panel:
    
    
    ```python
    gsv_knob.setFavorite("__default__.shot", True)
    gsv_knob.setFavorite("Global_Settings.FastDefocus", True)
    gsv_knob.setFavorite("Global_Settings.MotionBlur", True)
    ```

To remove the GSVs from the Variables Panel, simple turn off the favorite property:
    
    
    ```python
    gsv_knob.setFavorite("Global_Settings.MotionBlur", False)
    ```

## Variable Scopes and Overrides

To set up variables which are simultaneously available at different values in different parts of the single Nuke script, you need to define _scopes_ for the variables. Scopes are created by _VariableGroups_. Each VariableGroup inherits the GSVs of its parent Group but it may override each GSV by providing its own value for the variable.

Note

VariableGroups pass GSV definitions and overrides up the graph. This causes nodes which provide inputs for multiple VariableGroups to be evaluated with multiple values for the same GSV simultaneously. This acts in a similar way to TimeOffset nodes. Multiple TimeOffset nodes may access input nodes at multiple times/frames simultaneously.

Firstly create VariableGroups to introduce new GSVs:
    
    
    ```python
    # Outer VariableGroup
    sequenceGroup = nuke.nodes.VariableGroup(name="sq_robot_dance")
    with sequenceGroup:
      # Inner VariableGroup
      shotGroup = nuke.nodes.VariableGroup(name="s50_robot")
    ```

Next add the GSVs:
    
    
    ```python
    gsv_knob.setGsvValue("sq_robot_dance.__default__.name", "robot_dance")
    gsv_knob.setGsvValue("sq_robot_dance.__default__.scope", "sequence")
    gsv_knob.setGsvValue("sq_robot_dance.__default__.frame_start", "1001")
    gsv_knob.setGsvValue("sq_robot_dance.__default__.frame_end", "1152")
    
    gsv_knob.setGsvValue("sq_robot_dance.s50_robot.__default__.name", "s00050")
    gsv_knob.setGsvValue("sq_robot_dance.s50_robot.__default__.scope", "shot")
    ```

Note

[`setGsvValue()`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob.setGsvValue "nuke.Gsv_Knob.setGsvValue") `path` parameter is extended for VariableGroups to become `variable_group...variable_set.variable_name`, where the elipsis represents a dot separated hierarchy of groups. Each VariableGroup has a [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") which can be used to access the variable sets defined by the VariableGroup directly. Paths are then relative to the [`Gsv_Knob`](_autosummary/nuke.Gsv_Knob.html#nuke.Gsv_Knob "nuke.Gsv_Knob") owner.

For example:
    
    
    ```python
    sq_gsv_knob = sequenceGroup['gsv']
    sq_gsv_knob.getGsvValue("__default__.scope")
    # Result: 'sequence'
    sq_gsv_knob.getGsvValue("s50_robot.__default__.scope")
    # Result: 'shot'
    ```

Having added these variables to the parent (sequence) and child (shot) groups, **s50_robot** inherits **name** , **scope** , **frame_start** and **frame_end** from **sq_robot_dance**. However, **name** and **scope** have been overridden.

To override **frame_start** and **frame_end** it is only necessary to set the variables in **s50_robot** :
    
    
    ```python
    gsv_knob.setGsvValue("sq_robot_dance.s50_robot.__default__.frame_start", "1011")
    gsv_knob.setGsvValue("sq_robot_dance.s50_robot.__default__.frame_end", "1951")
    ```

[ Previous](openassetio.html "OpenAssetIO Integration") [Next ](threading.html "Threading")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
