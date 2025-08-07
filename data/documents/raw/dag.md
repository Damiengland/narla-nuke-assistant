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
  * Manipulating the Node Graph
    * Getting and Setting Node Positions
    * Controlling the Node Graph’s Pan and Zoom
    * Examples
      * A Circle Made of Dot Nodes
      * A Spiral
      * Controlling the Distance between Nodes
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
  * Manipulating the Node Graph
  * 


* * *

# Manipulating the Node Graph

You can use Python to:

  * get and set node properties that define the node’s position in the Node Graph (sometimes called the DAG)

  * control the Node Graph’s zoom and pan values.




There is a video tutorial about manipulating the Node Graph on [Nukepedia](http://www.nukepedia.com/video-tutorials/39/video/).

## Getting and Setting Node Positions

You can access a node’s x and y position in the Node Graph via its knobs:
    
    
    ```python
    node = nuke.createNode( 'NoOp' )
    print node['xpos'].value()
    ```

Use the usual knob method to set a new position:
    
    
    ```python
    node['xpos'].setValue( 100 )
    print 'new position is', node['xpos'].value()
    ```

For convenience, there are also methods to set and get node positions:
    
    
    ```python
    node.setXpos( 111 )
    node.setYpos( 222 )
    
    xPos = node.xpos()
    yPos = node.ypos()
    print 'new x position is', xPos
    print 'new y position is', yPos
    ```

To set both x and y value at once:
    
    
    ```python
    node.setXYpos( 123, 234 )
    ```

To get a node’s width and height in pixels at zoom level 1:
    
    
    ```python
    nodeWidth = node.screenWidth()
    nodeHeight = node.screenHeight()
    
    print "Node dimensions are %s x %s" % ( nodeWidth, nodeHeight )
    ```

To arrange nodes in a neat tree formation so they don’t overlap, use **node.autoplace()** :
    
    
    ```python
    for n in nuke.allNodes():
        n.autoplace()
    ```

To snap nodes to the nearest grid position:
    
    
    ```python
    for n in nuke.allNodes():
        nuke.autoplaceSnap( n )
    ```

## Controlling the Node Graph’s Pan and Zoom

To pan and zoom the Node Graph, use **nuke.zoom()**.

When called without any arguments, this simply returns the current zoom level:
    
    
    ```python
    nuke.zoom()
    ```

With an argument larger than 0, the Node Graph zooms to the given level. For example, to reset the view to 1:1, use:
    
    
    ```python
    nuke.zoom(1)
    ```

You can also specify the center of the zoom operation. To zoom into the selected node, use:
    
    
    ```python
    node = nuke.selectedNode()
    nuke.zoom( 3, [ node.xpos(), node.ypos() ])
    ```

The above example actually zooms into the node’s upper left corner. Let’s zoom into the center of the node instead:
    
    
    ```python
    node = nuke.selectedNode()
    xC = node.xpos() + node.screenWidth()/2
    yC = node.ypos() + node.screenHeight()/2
    nuke.zoom( 3, [ xC, yC ])
    ```

## Examples

### A Circle Made of Dot Nodes
    
    
    ```python
    import math
    for x in xrange(1000):
        n = nuke.nodes.Dot( xpos = math.sin(x)*100, ypos = math.cos(x)*100)
        n['hide_input'].setValue(True)
    ```

![_images/dag_01.png](_images/dag_01.png)

### A Spiral
    
    
    ```python
    import math
    for x in xrange(1000):
        n = nuke.nodes.Dot( xpos = math.sin(x)*x/10, ypos = math.cos(x)*x/10)
        n['hide_input'].setValue(True)
    ```

![_images/dag_02.png](_images/dag_02.png)

### Controlling the Distance between Nodes
    
    
    ```python
    import nuke
    def scaleNodes( scale ):
        nodes = nuke.selectedNodes()    # GET SELECTED NODES
        amount = len( nodes )    # GET NUMBER OF SELECTED NODES
        if amount == 0:    return # DO NOTHING IF NO NODES WERE SELECTED
    
        allX = sum( [ n.xpos()+n.screenWidth()/2 for n in nodes ] )  # SUM OF ALL X VALUES
        allY = sum( [ n.ypos()+n.screenHeight()/2 for n in nodes ] ) # SUM OF ALL Y VALUES
    
        # CENTER OF SELECTED NODES
        centreX = allX / amount
        centreY = allY / amount
    
        # REASSIGN NODE POSITIONS AS A FACTOR OF THEIR DISTANCE TO THE SELECTION CENTER
        for n in nodes:
            n.setXpos( centreX + ( n.xpos() - centreX ) * scale )
            n.setYpos( centreY + ( n.ypos() - centreY ) * scale )
    ```

![_images/dag_03.png](_images/dag_03.png)
    
    
    ```python
    scaleNodes( 3 )
    ```

![_images/dag_04.png](_images/dag_04.png)
    
    
    ```python
    scaleNodes( .7 )
    ```

![_images/dag_05.png](_images/dag_05.png)

[ Previous](channels.html "Working with Channels and Layers") [Next ](formats.html "Formats")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
