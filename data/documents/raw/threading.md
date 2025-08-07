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
  * Threading
    * Examples
      * MirrorNodes
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
  * Threading
  * 


* * *

# Threading

Threading is important, as it allows you to run background processes without making the main thread (your NUKE session) hang and wait for completion of the code. It’s handy for running background conversions, launching external commands or applications, and so on.

Depending on what your code is designed to do, you can simply run an existing function as a thread using Python’s threading interface, like this:
    
    
    ```python
    threading.Thread( target=<function_name>, args=<tuple_of_arguments> ).start()
    ```

Alternatively, you can create your own class inheriting [`threading.Thread`](_autosummary/nukescripts.renderdialog.Thread.html#nukescripts.renderdialog.Thread "threading.Thread"):
    
    
    ```python
    class MyClass( threading.Thread ):
            def __init__( self ):
                    threading.Thread.__init__( self )
    ```

When you want to communicate from a child thread back to the main thread (the NUKE session), you need to use one of the following methods:

  * `executeInMainThread(call, args=(), kwargs={})`
    

Execute the callable ‘call’ with optional arguments ‘args’ and named arguments ‘kwargs’ in NUKE’s main thread and return immediately.

  * `executeInMainThreadWithResult(call, args=(), kwargs={})`
    

Execute the callable ‘call’ with optional arguments ‘args’ and named arguments ‘kwargs’ in NUKE’s main thread and wait for the result to become available.




Warning

Do not run the above functions from within the main thread or NUKE will hang.

The MirrorNodes example below shows how you can animate nodes in the Node Graph (DAG) by using the above methods.

## Examples

### MirrorNodes

This little tool mirrors node position in the Node Graph, which may be helpful when re-organizing large portions of a complex node tree. The script uses threading to animate the nodes to their new position (rather than snap them to it), which makes it visually less confusing – and more fun. So let’s look at the basics first. Here is a code snippet that mirrors the selected nodes horizontally:
    
    
    ```python
    nodes = nuke.selectedNodes()
    positions = [ n.xpos()+n.screenWidth()/2 for n in nodes]
    axis = float( sum( positions ) ) / len( positions )
    ```

In line 2, we collect all node positions to calculate the average number that represents the center line across which we move the nodes to mirror their positions. Note that we need to add half of the nodes’ screen width to get the actual center. This is because a node’s position is measured from its upper left corner, not from its center.

Once we’ve got the center line (stored in **axis**), we can loop through the nodes and move them across that line:
    
    
    ```python
    for n in nodes:
            centrePos = n.xpos() + n.screenWidth()/2
            nodePos = centrePos - 2*( centrePos - axis ) - n.screenWidth()/2.0
            n.setXpos( round( nodePos ) )
    ```

Once again, we need to calculate the nodes’ actual center position (**centrePos**) and use that to get the expected result. In line 3, the mirrored node position is calculated by subtracting twice the node’s distance to the axis. Once again we have to take into account that NUKE moves the node’s upper left corner (rather than its center) to a new position, so we apply an offset of half the node’s screen width to accommodate for that. Lastly, we apply the new position to the node and since the **setXpos()** prefers integers, we round the result first (the method works with floating point numbers as well but may spit out a DepreciationWarning).

When running this script on a selection of nodes, the script snaps them into their new positions, but it’s much cooler to see the nodes move across the Node Graph, so let’s turn the above into a threaded process to animate the nodes:

First, we create a threaded class by inheriting **threading.Thread** and calling its constructor:
    
    
    ```python
    class MirrorNodes( threading.Thread ):
            def __init__( self ):
                    threading.Thread.__init__( self )
    ```

This is not necessarily required to run a function as a separate thread but it’s a little safer than alternative approaches, as some of the commands we will have to use will freeze NUKE if run from the main thread. We will get to that a little later though.

To make this script more flexible, let’s assign arguments to define the nodes to operate on as well as a “direction” argument, so we can mirror nodes both horizontally and vertically:
    
    
    ```python
    class MirrorNodes( threading.Thread ):
            def __init__( self, nodes, direction='x' ):
                    threading.Thread.__init__( self )
    ```

While we are writing the constructor, we go ahead and add a few variables that we are going to need:
    
    
    ```python
    class MirrorNodes( threading.Thread ):
            def __init__( self, nodes, direction='x' ):
                    threading.Thread.__init__( self )
    
                    self.posDict = {}
                    self.nodes= nodes
                    self.direction = direction
    ```

**self.posDict** will hold a dictionary of nodes and their respective new Node Graph positions.

**self.nodes** will hold the nodes that we want to move.

**self.direction** just tells us what direction the user wants to mirror the nodes.

We only allow ‘x’ and ‘y’ (lower or upper case) as valid values for the direction argument, and we need at least two nodes to make this whole thing worth while, so let’s put some error handling in there as well:
    
    
    ```python
    class MirrorNodes( threading.Thread ):
            def __init__( self, nodes, direction='x' ):
                    threading.Thread.__init__( self )
    
                    self.direction = direction.lower()
                    if len( nodes ) < 2:
                            raise ValueError, 'At least two nodes have to be selected'
                    if self.direction not in ('x', 'y'):
                            raise ValueError, 'direction argument must be x or y'
    
                    self.posDict = {}
                    self.nodes= nodes
    ```

In the beginning, we looped through the nodes and assigned a new value to each node as we went. This time, we use the same code to just find the new position for each node and store it in self.posDict instead of actually moving the node. This enables us to move the nodes bit by bit later on and control the speed and smoothness with which they move. So using the code snippet from the beginning, let’s create a method called **__mirrorPos** for our new class. This does most of the work:
    
    
    ```python
    def __mirrorPos( self ):
            positions = [ n.xpos()+n.screenWidth()/2 for n in self.nodes]
            axis = float( sum( positions ) ) / len( positions )
    
            for n in self.nodes:
                    centrePos = n.xpos() + n.screenWidth()/2
                    oldPos = n.xpos()
                    newPos = centrePos - 2*( centrePos - axis ) - n.screenWidth()/2.0
                    self.posDict[ n ] = ( oldPos, round( newPos ) )
    ```

The main differences here compared to our initial snippet are:

  * We use **self.nodes** instead of **nodes** because we define the node selection in the class’ constructor.

  * Instead of directly applying the new position to the nodes in the last line, we just store the old and new positions as a tuple in the dictionary **self.posDict** using the nodes themselves as the keys.




The nodes’ old position is the first item in the assigned tuple and their new position the second. We need to keep track of the original position, as we want to change it bit by bit as we go.

But since we want to make this more flexible, we need to add the case when vertical mirroring is requested:
    
    
    ```python
    def __mirrorPos( self ):
            if self.direction == 'x':
                    positions = [ n.xpos()+n.screenWidth()/2 for n in self.nodes]
            else:
                    positions = [ n.ypos()+n.screenHeight()/2 for n in self.nodes]
    
            axis = float( sum( positions ) ) / len( positions )
            for n in self.nodes:
                    if self.direction == 'x':
                            centrePos = n.xpos() + n.screenWidth()/2
                            oldPos = n.xpos()
                            newPos = centrePos - 2*( centrePos - axis ) - n.screenWidth()/2.0
                    else:
                            centrePos = n.ypos() + n.screenHeight()/2
                            oldPos = n.ypos()
                            newPos = centrePos - 2*( centrePos - axis ) - n.screenHeight()/2.0
                    self.posDict[ n ] = ( oldPos, round( newPos ) )
    ```

Here, we first check **self.direction**. If its value is ‘x’, we use the node methods **xpos()** and **screenWidth()** to figure out the center and respective new positions. Otherwise, we use **ypos()** and **screenHeight()**.

Now for the fun bit:

We override the **run()** method we inherited with the **threading.Thread** class to trigger the actual changes to the nodes in NUKE’s main thread. A Thread object’s **run()** method represents the object’s activity and is run on a separate thread in the background, which means NUKE does not freeze up while the code is being executed (like it would if we weren’t using a threaded approach). The idea is to create a loop through which we move every node by a percentage of the distance between its old and new position (the one stored in **self.posDict**). We do the calculation for each iteration in the background thread, then use the results to move the nodes in the main thread, which means we can actually see what is happening as the code is progressing.

Let’s say we move each node 10 percent towards its new position at a time:
    
    
    ```python
    def run( self ):
            incs = 10
            for i in xrange( incs ):
                    ...
    ```

In each iteration, we loop through the nodes, calculate the current position (that is, a percentage of the distance between the old and new position):
    
    
    ```python
    def run( self ):
            incs = 10
            for i in xrange( incs ):
                    for n in self.nodes:
                            oldPos = self.posDict[ n ][ 0 ]
                            newPos = self.posDict[ n ][ 1 ]
                            curPos = oldPos + ( newPos - oldPos ) / incs * (i+1)
    ```

and apply it to the nodes in NUKE’s main thread:
    
    
    ```python
    def run( self ):
            incs = 10
            for i in xrange( incs ):
                    for n in self.nodes:
                            oldPos = self.posDict[ n ][ 0 ]
                            newPos = self.posDict[ n ][ 1 ]
                            curPos = oldPos + ( newPos - oldPos ) / incs * (i+1)
                            if self.direction == 'x':
                                    nuke.executeInMainThreadWithResult( n.setXpos, int(curPos) )
                            else:
                                    nuke.executeInMainThreadWithResult( n.setYpos, int(curPos) )
    ```

Warning

**nuke.executeInMainThread** and **nuke.executeInMainThreadWithResult** should always be run from a child thread. If run from within the main thread, they freeze NUKE.

To make sure we can actually see what’s happening, we make each iteration wait for a split second before moving the node again by adding a sleep command at the end:
    
    
    ```python
    def run( self ):
            incs = 10
            for i in xrange( incs ):
                    for n in self.nodes:
                            oldPos = self.posDict[ n ][ 0 ]
                            newPos = self.posDict[ n ][ 1 ]
                            curPos = oldPos + ( newPos - oldPos ) / incs * (i+1)
                            if self.direction == 'x':
                                    nuke.executeInMainThreadWithResult( n.setXpos, int(curPos) )
                            else:
                                    nuke.executeInMainThreadWithResult( n.setYpos, int(curPos) )
                    time.sleep(.02)
    ```

One last thing we need to do is to actually run the **self.__mirrorPos()** method in **__init()__** , so the node positions are calculated when the class is first created.

Here is the complete code with the required import statements:
    
    
    ```python
    import nuke
    import time
    import threading
    
    class MirrorNodes( threading.Thread ):
            def __init__( self, nodes, direction='x' ):
                    threading.Thread.__init__( self )
    
                    self.direction = direction.lower()
                    if len( nodes ) < 2:
                            raise ValueError, 'At least two nodes have to be selected'
                    if direction.lower() not in ('x', 'y'):
                            raise ValueError, 'direction argument must be x or y'
    
                    self.posDict = {}
                    self.nodes= nodes
                    self.__mirrorPos()
    
            #----------------------------------
            def __mirrorPos( self ):
                    '''Get the mirrored position for each node'''
                    if self.direction == 'x':
                            positions = [ n.xpos()+n.screenWidth()/2 for n in self.nodes]
                    else:
                            positions = [ n.ypos()+n.screenHeight()/2 for n in self.nodes]
    
                    axis = float( sum( positions ) ) / len( positions )
    
                    for n in self.nodes:
                            if self.direction == 'x':
                                    centrePos = n.xpos() + n.screenWidth()/2
                                    oldPos = n.xpos()
                                    newPos = centrePos - 2*( centrePos - axis ) - n.screenWidth()/2.0
                            else:
                                    centrePos = n.ypos() + n.screenHeight()/2
                                    oldPos = n.ypos()
                                    newPos = centrePos - 2*( centrePos - axis ) - n.screenHeight()/2.0
                            self.posDict[ n ] = ( oldPos, round( newPos ) )
    
            #----------------------------------
            def run( self ):
                    incs = 10
                    for i in xrange( incs ):
                            for n in self.nodes:
                                    oldPos = self.posDict[ n ][ 0 ]
                                    newPos = self.posDict[ n ][ 1 ]
                                    curPos = oldPos + ( newPos - oldPos ) / incs * (i+1)
                                    if self.direction == 'x':
                                            nuke.executeInMainThreadWithResult( n.setXpos, int(curPos) )
                                    else:
                                            nuke.executeInMainThreadWithResult( n.setYpos, int(curPos) )
                            time.sleep(.02)
    ```

After evaluating this, you can now mirror nodes by selecting some nodes in the Node Graph and executing:
    
    
    ```python
    MirrorNodes( nuke.selectedNodes() ).start()
    ```

The **start()** method came with the inherited **Thread** object and takes care that the **run()** method is invoked in a separate thread.

To mirror selected nodes vertically, run this:
    
    
    ```python
    MirrorNodes( nuke.selectedNodes(), 'y' ).start()
    ```

or more explicitly:
    
    
    ```python
    MirrorNodes( nuke.selectedNodes(), direction='y' ).start()
    ```

Finally, here are example entries for the menu.py file. This will have to be modified depending on how the **MirrorNodes** class is saved and imported:
    
    
    ```python
    import examples
    m = nuke.menu( 'Nuke' )
    m.addCommand( 'Mirror Nodes/x', lambda: examples.MirrorNodes( nuke.selectedNodes() ).start() )
    m.addCommand( 'Mirror Nodes/y', lambda: examples.MirrorNodes( nuke.selectedNodes(), direction='y').start() )
    ```

[ Previous](gsv.html "Graph Scope Variables / Multi-shot Set-up") [Next ](render_farm.html "Render Farm Integration \(Concept\)")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
