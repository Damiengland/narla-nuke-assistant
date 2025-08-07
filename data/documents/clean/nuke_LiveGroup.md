# nuke.LiveGroup
_class _nuke.LiveGroup

Bases:
Methods
`Class`
return
    Class of node.---
`addCallback`  Add a callback to a specific event id.
`addKnob`  Add knob k to this node or panel.
`allKnobs`  Get a list of all knobs in this node, including nameless knobs.
`anyOverrides`  If any of the exposed link knobs are overridden it returns with True.
`applyOverrides`  applyOverride() -> bool This function only affects link knobs that are placed on a LiveGroup type node.
`autoplace`  Automatically place nodes, so they do not overlap.
`baseNode`
return
    A node.
`bbox`  Bounding box of the node.
`begin`  All python code that follows will be executed in the context of node.
`canSetInput`  Check whether the output of 'node' can be connected to input i.
`channels`  List channels output by this node.
`clearCallbacks`  Remove all callbacks on the node that were previously added using self.addCallback(string, Callable).
`clearCustomIcon`  Clear the custom icon set for the node.
`cloneInstanceIndex`  The instance index is not guaranteed to be the same between Nuke sessions.
`cloneInstanceNode`
param i
    Instance index.
`cloneInstances`
return
    List of nodes.
`clones`
return
    Number of clones.
`connectInput`  Connect the output of 'node' to the i'th input or the next available unconnected input.
`connectSelectedNodes`  Connect the selected nodes.
`deepSample`  Return pixel values from a deep image.
`deepSampleCount`  Return number of samples for a pixel on a deep image.
`dependencies`  List all nodes referred to by this node. 'what' is an optional integer (see below). You can use the following constants or'ed together to select what types of dependencies are looked for: nuke.EXPRESSIONS = expressions nuke.LINKINPUTS = link knobs nuke.LINKNODE_INPUTS = link nodes nuke.INPUTS = visible input pipes nuke.HIDDEN_INPUTS = hidden input pipes. The default is to look for all types of connections.
`dependent`  List all nodes that read information from this node. 'what' is an optional integer:
`end`  All python code that follows will no longer be executed in the context of node.
`error`  True if the node or any in its input tree have an error, or False otherwise.
`executePythonCallback`  Executes the callback if one was added for the given event id string using self.addCallback(string, Callable).
`expand`  Moves all nodes from the group node into its parent group, maintaining node input and output connections, and deletes the group.
`fileDependencies`
param start
    first frame
`findNode`  Find the first node who's local name matches string 'name', including any clones.
`firstFrame`  First frame in frame range for this node.
`forceUpdateLocalization`
return
    None
`forceValidate`  Force the node to validate itself, updating its hash.
`format`  Format of the node.
`frameRange`  Frame range for this node.
`fullName`  Get the name of this node and any groups enclosing it in 'group.group.name' form.
`getLink`  Returns the node that this node is linked against.
`getNumKnobs`  self.numKnobs() -> The number of knobs.
`getStage`
`hasError`  True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.
`height`  Height of the node.
`help`
return
    Help for the node.
`helpUrl`  :return The current documentation help URL for the node
`hideControlPanel`
return
    None
`input`
param i
    Input number.
`inputs`
return
    Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.
`isClone`
return
    True if the node is a clone, False otherwise.
`isCloneable`
return
    True if the node allows cloning, False otherwise.
`isLinked`  Return True if the node is currently linked to a node.
`isLocal`  Checks if the LiveGroup is local.WARNING: This function is deprecated.
`isLocalizationOutdated`
return
    true if the Localization source file has changed
`isLocalized`
return
    bool
`isSelected`  Returns the current selection state of the node.
`knob`
param p
    A string or an integer.
`knobs`  Get a dictionary of (name, knob) pairs for all knobs in this node.
`lastFrame`  Last frame in frame range for this node.
`linkableKnobs`  Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob.
`localizationProgress`
return
    float, between 0.0 (not localized) and 1.0 (localized)
`lock`
`locked`
`makeEditable`  Puts the LiveGroup into "editable" state.
`makeLocal`  Puts the LiveGroup into "local" state.
`maxInputs`  self.maximumInputs() -> Maximum number of inputs this node can have.
`maxOutputs`  self.maximumOutputs() -> Maximum number of outputs this node can have.
`maximumInputs`
return
    Maximum number of inputs this node can have.
`maximumOutputs`
return
    Maximum number of outputs this node can have.
`metadata`  Return the metadata item for key on this node at current output context, or at optional time and view.
`minInputs`  self.minimumInputs() -> Minimum number of inputs this node can have.
`minimumInputs`
return
    Minimum number of inputs this node can have.
`modified`  Returns True if the anything within the livegroup has changed.
`name`
return
    Name of node.
`node`  Locate a node by name.
`nodes`  List of nodes in group.
`numKnobs`
return
    The number of knobs.
`numNodes`  Number of nodes in group.
`opHashes`  Returns a list of hash values, one for each op in this node.
`optionalInput`
return
    Number of first optional input.
`output`  Return output node of group.
`overrideKnob`  Override knob k on this link node.
`parent`
`performanceInfo`  @category: performance category ( optional ).A performance category, must be either nuke.PROFILE_STORE, nuke.PROFILE_VALIDATE, nuke.PROFILE_REQUEST or nuke.PROFILE_ENGINE The default is nuke.PROFILE_ENGINE which gives the performance info of the render engine.
`pixelAspect`  Pixel Aspect ratio of the node.
`proxy`
return
    True if proxy is enabled, False otherwise.
`publish`  publishLiveGroup(file) -> bool
`published`  Returns True if the LiveGroup is published.
`readKnobs`  Read the knobs from a string (TCL syntax).
`redraw`  Force a redraw of the node.
`reload`  Reloads the livegroup from the livegroups source file.
`removeCallback`  Remove a callback for a specific event id string that was previously added using self.addCallback(string, Callable).
`removeKnob`  Remove knob k from this node or panel.
`removeOverrideKnob`  Remove override from knob k on this link node.
`resetKnobsToDefault`  Reset all the knobs to their default values.
`revertOverrides`  revertOverride() -> bool This function only affects link knobs that are placed on a LiveGroup type node.
`rootNode`
`run`  Execute in the context of node.
`running`  Class method.
`sample`  Return pixel values from an image.
`screenHeight`  Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
`screenWidth`  Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels.
`selectOnly`  Set this node to be the only selection, as if it had been clicked in the DAG.
`selectedNode`  Returns the node the user is most likely thinking about.
`selectedNodes`  Selected nodes.
`setCustomIcon`  Set a custom icon for the node.
`setInput`  Connect input i to node if canSetInput() returns true.
`setName`  Set name of the node and resolve name collisions if optional named argument 'uncollide' is True.
`setSelected`  Set the selection state of the node.
`setTab`
param tabIndex
    The tab to show (first is 0).
`setXYpos`  Set the (x, y) position of node in node graph.
`setXpos`  Set the x position of node in node graph.
`setYpos`  Set the y position of node in node graph.
`showControlPanel`
param forceFloat
    Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.
`showInfo`  Creates a dialog box showing the result of script s.
`shown`
return
    true if the properties panel is open. This can be used to skip updates that are not visible to the user.
`splaySelectedNodes`  Splay the selected nodes.
`subgraphLocked`
`treeHasError`  True if the node or any in its input tree have an error, or False otherwise.
`unlink`  Unlink the node without possibility to resolve.
`unlock`
`upstreamFrameRange`  Frame range for the i'th input of this node.
`width`  Width of the node.
`writeKnobs`  Return a tcl list.
`xpos`
return
    X position of node in node graph.
`ypos`
return
    Y position of node in node graph.

Class()  Class of node.

Returns

Class of node.
addCallback(_string_ , _Callable_)  None

Add a callback to a specific event id. Specific event ids can be found in the documentation of the related type or function. The LiveGroupNode has some examples of these event ids such as nuke.LIVEGROUP_CALLBACK_PUBLISHED. It is possible to use your own event id string and then execute the callback using self.executeCallback(string). Note that this is not related to the standard Nuke callback mechanism. :param string: the string event id to add the callback on. :param callable: callable to execute when the event is triggered. The callable should take the node as a parameter e.g. def callback(node): :return: None
addKnob(_k_)  None.

Add knob k to this node or panel. :param k: Knob. :return: None.
allKnobs()  list

Get a list of all knobs in this node, including nameless knobs.
For example:


    ```python
    >>> b = nuke.nodes.Blur()
    >>> b.allKnobs()
    ```
Returns

List of all knobs.
Note that this doesn’t follow the links for Link_Knobs/Obsolete_Knobs
anyOverrides()  bool

If any of the exposed link knobs are overridden it returns with True.
applyOverrides()

applyOverride() -> bool This function only affects link knobs that are placed on a LiveGroup type node. It replaces the value of the linked knob in the live group with the value set in the LiveGroup node.
autoplace()  None.

Automatically place nodes, so they do not overlap. :return: None.
baseNode()  Return the 'original'(base) node if this is a clone, or this node if not cloned.

Returns

A node.
bbox()  List of x, y, w, h.

Bounding box of the node. :return: List of x, y, w, h.
begin()  Group.

All python code that follows will be executed in the context of node. All names are evaluated relative to this object. Must be paired with end. :return: Group.
canSetInput(_i_ , _node_)  bool

Check whether the output of ‘node’ can be connected to input i. :param i: Input number. :param node: The node to be connected to input i. :return: True if node can be connected, False otherwise.
channels()  String list.

List channels output by this node. :return: String list.
clearCallbacks()  None

Remove all callbacks on the node that were previously added using self.addCallback(string, Callable). Note that this is not related to the standard Nuke callback mechanism. :return: None
clearCustomIcon()  None.

Clear the custom icon set for the node. :return: None.
cloneInstanceIndex()  The instance index of this node where 0 is the base node, and clones begin at index 1.

The instance index is not guaranteed to be the same between Nuke sessions. :return: Index of clone instance, or -1 if node is not cloned.
cloneInstanceNode()  The node for a valid clone instance index. If index is 0 this node(the base) is returned.

Parameters

**i** – Instance index.
Returns

An instance node, or None if index is invalid for this node.
cloneInstances()  Return a list of all instances for this node.

Returns

List of nodes.
clones()  Number of clones.

Returns

Number of clones.
connectInput(_i_ , _node_)  bool

Connect the output of ‘node’ to the i’th input or the next available unconnected input. The requested input is tried first, but if it is already set then subsequent inputs are tried until an unconnected one is found, as when you drop a connection arrow onto a node in the GUI. :param i: Input number to try first. :param node: The node to connect to input i. :return: True if a connection is made, False otherwise.
connectSelectedNodes(_backward_ , _inputA_)  None.

Connect the selected nodes. :param backward. :param inputA. :return: None.
deepSample(_c_ , _x_ , _y_ , _n_)  Floating point value.

Return pixel values from a deep image. This requires the image to be calculated, so performance may be very bad if this is placed into an expression in a control panel. :param c: Channel name. :param x: Position to sample (X coordinate). :param y: Position to sample (Y coordinate). :param n: Sample index (between 0 and the number returned by deepSampleCount() for this pixel, or -1 for the frontmost). :return: Floating point value.
deepSampleCount(_x_ , _y_)  Integer value.

Return number of samples for a pixel on a deep image. This requires the image to be calculated, so performance may be very bad if this is placed into an expression in a control panel. :param x: Position to sample (X coordinate). :param y: Position to sample (Y coordinate). :return: Integer value.
dependencies(_what_)  List of nodes.

List all nodes referred to by this node. ‘what’ is an optional integer (see below). You can use the following constants or’ed together to select what types of dependencies are looked for:
> nuke.EXPRESSIONS = expressions nuke.LINKINPUTS = link knobs nuke.LINKNODE_INPUTS = link nodes nuke.INPUTS = visible input pipes nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.
Example: nuke.toNode(‘Blur1’).dependencies( nuke.INPUTS  nuke.EXPRESSIONS ) :param what: Or’ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependencies. The default is to look for all types of connections. :return: List of nodes.
dependent(_what_ , _forceEvaluate_)  List of nodes.

List all nodes that read information from this node. ‘what’ is an optional integer:

You can use any combination of the following constants or’ed together to select what types of dependent nodes to look for:

nuke.EXPRESSIONS = expressions nuke.LINKINPUTS = link knobs nuke.LINKNODE_INPUTS = link nodes nuke.INPUTS = visible input pipes nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.
forceEvaluate is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree. This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.
Example: nuke.toNode(‘Blur1’).dependent( nuke.INPUTS  nuke.EXPRESSIONS ) :param what: Or’ed constant of nuke.EXPRESSIONS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections. :param forceEvaluate: Specifies whether a full tree evaluation will take place. Defaults to True. :return: List of nodes.
end()  None.

All python code that follows will no longer be executed in the context of node. Must be paired with begin. :return: None.
error()  bool

True if the node or any in its input tree have an error, or False otherwise.
Error state of the node and its input tree. Deprecated; use hasError or treeHasError instead. Note that this will always return false for viewers, which cannot generate their input trees. Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
executePythonCallback(_string_)  None

Executes the callback if one was added for the given event id string using self.addCallback(string, Callable). Specific event ids can be found in the documentation of the related type or function. The LiveGroupNode has some examples of these event ids such as nuke.LIVEGROUP_CALLBACK_PUBLISHED. It is possible to use your own event id string by adding a callback for it using self.addCallback(string, Callable). Note that this is not related to the standard Nuke callback mechanism. :param string: the string event id with the callback to execute. :return: None
expand()  None.

Moves all nodes from the group node into its parent group, maintaining node input and output connections, and deletes the group. Returns the nodes that were moved, which will also be selected. :return: None.
fileDependencies(_start_ , _end_)  List of nodes and filenames.

Parameters

  * **start** – first frame
  * **end** – last frame
Returns the list of input file dependencies for this node and all nodes upstream from this node for the given frame range. The file dependencies are calcuated by searching for Read ops or ops with a File knob. All views are considered and current proxy mode is used to decide on whether full format or proxy files are returned. Note that Write nodes files are also included but precomps, gizmos and external plugins are not. Any time shifting operation such as frameholds, timeblurs, motionblur etc are taken into consideration. :return The return list is a list of nodes and files they require. Eg. [Read1, [‘file1.dpx, file2.dpx’] ], [Read2, [‘file3.dpx’, ‘file4.dpx’] ] ]
findNode(_name_)

Find the first node who’s local name matches string ‘name’, including any clones. Assumes the string contains only the node’s local name, not the full path of the node which may contain parents or expressions.:param s: A string. :return: Node with local name matching string ‘name’, or None if not found.
firstFrame()  int.

First frame in frame range for this node. :return: int.
forceUpdateLocalization()  Force Updates the localized files for this node.

Returns

None
forceValidate()  None

Force the node to validate itself, updating its hash.
format()  Format.

Format of the node. :return: Format.
frameRange()  FrameRange.

Frame range for this node. :return: FrameRange.
fullName()  str

Get the name of this node and any groups enclosing it in ‘group.group.name’ form. :return: The fully-qualified name of this node, as a string.
getLink()

Returns the node that this node is linked against.
Raises

**TypeError** – If the node is not a linkable node.
Returns

Node this node is linked against, returns None if not linked.
getNumKnobs()

self.numKnobs() -> The number of knobs. :return: The number of knobs.
getStage([_OutputContext_][, _list of additional times_])  Runs the graph and returns the composed stage for geometry, Viewer or ScanlineRender nodes (if the latter two have geometry nodes connected, else None). Returns None for other node types.

hasError()  bool

True if the node itself has an error, regardless of the state of the ops in its input tree, or False otherwise.
Error state of the node itself, regardless of the state of the ops in its input tree. Note that an error on a node may not appear if there is an error somewhere in its input tree, because it may not be possible to validate the node itself correctly in that case.
height()  int.

Height of the node. :return: int.
help()  str

Returns

Help for the node.
helpUrl()

:return The current documentation help URL for the node
hideControlPanel()  None

Returns

None
input(_i_)  The i'th input.

Parameters

**i** – Input number.
Returns

The i’th input.
inputs()  Gets the maximum number of connected inputs.

Returns

Number of the highest connected input + 1. If inputs 0, 1, and 3 are connected, this will return 4.
isClone()  Is this node a clone? If so use baseNode() to retrieve the 'original' node.

Returns

True if the node is a clone, False otherwise.
isCloneable()  If the node permits cloning.

Returns

True if the node allows cloning, False otherwise.
isLinked()  bool

Return True if the node is currently linked to a node.
Raises

**TypeError** – If the node is not a linkable node.
Returns

True if linked.
isLocal()  bool

Checks if the LiveGroup is local.WARNING: This function is deprecated. Use published() instead.
isLocalizationOutdated()  Returns if there are changes detected in the source file.

Returns

true if the Localization source file has changed
isLocalized()  returns True/False whether the node is completely localized.

Returns

bool
isSelected()  bool

Returns the current selection state of the node. This is the same as checking the ‘selected’ knob. :return: True if selected, or False if not.
knob(_p_[, _follow_link_])  The knob named p or the pth knob.

Parameters

  * **p** – A string or an integer.
  * **follow_link** – Should it follow links to Link_Knob until resolution. Default is True.
Returns

The knob named p or the pth knob.
knobs()  dict

Get a dictionary of (name, knob) pairs for all knobs in this node.
For example:


    ```python
    >>> b = nuke.nodes.Blur()
    >>> b.knobs()
    ```
Returns

Dictionary of all knobs.
Note that this doesn’t follow the links for Link_Knobs/Obsolete_Knobs
lastFrame()  int.

Last frame in frame range for this node. :return: int.
linkableKnobs(_knobType_)  List

Returns a list of any knobs that may be linked to from the node as well as some meta information about the knob. This may include whether the knob is enabled and whether it should be used for absolute or relative values. Not all of these variables may make sense for all knobs.. :param knobType A KnobType describing the type of knobs you want.:return: A list of LinkableKnobInfo that may be empty .
localizationProgress()  Checks and reports on progress of localization of the current node.

Returns

float, between 0.0 (not localized) and 1.0 (localized)
lock()  Sets the node to a locked state where knobs cannot be edited.

locked()  Returns True if the node is locked, False otherwise.

makeEditable()  None

Puts the LiveGroup into “editable” state.
makeLocal()  None

Puts the LiveGroup into “local” state. WARNING: This function is deprecated. Use makeEditable() instead.
maxInputs()

self.maximumInputs() -> Maximum number of inputs this node can have. :return: Maximum number of inputs this node can have.
maxOutputs()

self.maximumOutputs() -> Maximum number of outputs this node can have. :return: Maximum number of outputs this node can have.
maximumInputs()  Maximum number of inputs this node can have.

Returns

Maximum number of inputs this node can have.
maximumOutputs()  Maximum number of outputs this node can have.

Returns

Maximum number of outputs this node can have.
metadata(_key_ , _time_ , _view_)  value or dict

Return the metadata item for key on this node at current output context, or at optional time and view. If key is not specified a dictionary containing all key/value pairs is returned. None is returned if key does not exist on this node. :param key: Optional name of the metadata key to retrieve. :param time: Optional time to evaluate at (default is taken from node’s current output context). :param view: Optional view to evaluate at (default is taken from node’s current output context). :return: The requested metadata value, a dictionary containing all keys if a key name is not provided, or None if the specified key is not matched.
minInputs()

self.minimumInputs() -> Minimum number of inputs this node can have. :return: Minimum number of inputs this node can have.
minimumInputs()  Minimum number of inputs this node can have.

Returns

Minimum number of inputs this node can have.
modified()  bool

Returns True if the anything within the livegroup has changed.
name()  str

Returns

Name of node.
node(_s_)  Node with name s or None.

Locate a node by name. :param s: A string. :return: Node with name s or None.
nodes()  List of nodes

List of nodes in group. :return: List of nodes
numKnobs()  The number of knobs.

Returns

The number of knobs.
numNodes()  Number of nodes

Number of nodes in group. :return: Number of nodes
opHashes()  list of int

Returns a list of hash values, one for each op in this node.
optionalInput()  Number of first optional input.

Returns

Number of first optional input.
output()  Node or None.

Return output node of group. :return: Node or None.
overrideKnob(_k_)  bool

Override knob k on this link node.
Parameters

**k** – Knob to override.
Raises

  * **TypeError** – If the node is not a linkable node.
  * **RuntimeError** – If not linked.
Returns

True if knob successfully overridden.
parent()  Return the parent group node for this node.

performanceInfo(_category_)  Returns performance information for this node. Performance timing must be enabled.

@category: performance category ( optional ).A performance category, must be either nuke.PROFILE_STORE, nuke.PROFILE_VALIDATE, nuke.PROFILE_REQUEST or nuke.PROFILE_ENGINE The default is nuke.PROFILE_ENGINE which gives the performance info of the render engine. :return: A dictionary containing the cumulative performance info for this category, where: callCount = the number of calls made timeTakenCPU = the CPU time spent in microseconds timeTakenWall = the actual time ( wall time ) spent in microseconds
pixelAspect()  int.

Pixel Aspect ratio of the node. :return: float.
proxy()  bool

Returns

True if proxy is enabled, False otherwise.
publish()

publishLiveGroup(file) -> bool
Writes a LiveGroup to a file.
Parameters

**file** – (optional) The path to which we want to publish this LiveGroup. If None then write to the path currently defined by the file knob. If the file specified by this param already exists, Nuke will attempt to over write it without a warning. Otherwise a new file will be created.
Returns

bool. True if successful, else, False.
published()  bool

Returns True if the LiveGroup is published.
readKnobs(_s_)  None.

Read the knobs from a string (TCL syntax). :param s: A string. :return: None.
redraw()  None.

Force a redraw of the node. :return: None.
reload()  None

Reloads the livegroup from the livegroups source file.
removeCallback(_string_)  None

Remove a callback for a specific event id string that was previously added using self.addCallback(string, Callable). Note that this is not related to the standard Nuke callback mechanism. :param string: the string event id with the callback to remove. :return: None
removeKnob(_k_)  None.

Remove knob k from this node or panel. Throws a ValueError exception if k is not found on the node. :param k: Knob. :return: None.
removeOverrideKnob(_k_)  bool

Remove override from knob k on this link node.
Parameters

**k** – Knob to remove override from.
Raises

  * **TypeError** – If the node is not a linkable node.
  * **RuntimeError** – If not linked.
Returns

True if override removed successfully.
resetKnobsToDefault()  None

Reset all the knobs to their default values.
revertOverrides()

revertOverride() -> bool This function only affects link knobs that are placed on a LiveGroup type node. When called the LinkKnob will revert to the linked knob value and will follow it after reloads.
rootNode()  Returns this node's root node. This may differ from nuke.root() for example if the read node was created importing footage to the timeline.

run(_callable_)  Result of callable.

Execute in the context of node. All names are evaluated relative to this object. :param callable: callable to execute. :return: Result of callable.
running()  Node rendering when paralled threads are running or None.

Class method. :return: Node rendering when paralled threads are running or None.
sample(_c_ , _x_ , _y_ , _dx_ , _dy_)  Floating point value.

Return pixel values from an image. This requires the image to be calculated, so performance may be very bad if this is placed into an expression in a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result, this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates. If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called ‘impulse filtering’. :param c: Channel name. :param x: Centre of the area to sample (X coordinate). :param y: Centre of the area to sample (Y coordinate). :param dx: Optional size of the area to sample (X coordinate). :param dy: Optional size of the area to sample (Y coordinate). :param frame: Optional frame to sample the node at. :return: Floating point value.
screenHeight()  int.

Height of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels. :return: int.
screenWidth()  int.

Width of the node when displayed on screen in the DAG, at 1:1 zoom, in pixels. :return: int.
selectOnly()  None.

Set this node to be the only selection, as if it had been clicked in the DAG. :return: None.
selectedNode()  Node or None.

Returns the node the user is most likely thinking about. This is the last node the user clicked on, if it is selected. Otherwise it is an ‘output’ (one with no selected outputs) of the set of selected nodes. If no nodes are selected then None is returned. :return: Node or None.
selectedNodes()  Node or None.

Selected nodes. :return: Node or None.
setCustomIcon(_image_ , _scale_ , _offsetX_ , _offsetY_)  bool.

Set a custom icon for the node. :param image: filepath to image to be used as an icon. :param scale: Optional. scale factor for the icon. :param offsetX: Optional. offset the icon in the x axis from the top left corner of the node. :param offsetY: Optional. offset the icon in the y axis from the top left corner of the node. :return: True if icon has been set, else false.
setInput(_i_ , _node_)  bool

Connect input i to node if canSetInput() returns true. :param i: Input number. :param node: The node to connect to input i. :return: True if canSetInput() returns true, or if the input is already correct.
setName(_name_ , _uncollide =True_, _updateExpressions =False_)  None

Set name of the node and resolve name collisions if optional named argument ‘uncollide’ is True. :param name: A string. :param uncollide: Optional boolean to resolve name collisions. Defaults to True. :param updateExpressions: Optional boolean to update expressions in other nodes to point at the new name. Defaults to False. :return: None
setSelected(_selected_)  None.

Set the selection state of the node. This is the same as changing the ‘selected’ knob. :param selected: New selection state - True or False. :return: None.
setTab(_tabIndex_)  None

Parameters

**tabIndex** – The tab to show (first is 0).
Returns

None
setXYpos(_x_ , _y_)  None.

Set the (x, y) position of node in node graph. :param x: The x position of node in node graph. :param y: The y position of node in node graph. :return: None.
setXpos(_x_)  None.

Set the x position of node in node graph. :param x: The x position of node in node graph. :return: None.
setYpos(_y_)  None.

Set the y position of node in node graph. :param y: The y position of node in node graph. :return: None.
showControlPanel(_forceFloat =false_)  None

Parameters

**forceFloat** – Optional python object. If it evaluates to True the control panel will always open as a floating panel. Default is False.
Returns

None
showInfo(_s_)  None.

Creates a dialog box showing the result of script s. :param s: A string. :return: None.
shown()  true if the properties panel is open. This can be used to skip updates that are not visible to the user.

Returns

true if the properties panel is open. This can be used to skip updates that are not visible to the user.
splaySelectedNodes(_backward_ , _inputA_)  None.

Splay the selected nodes. :param backward. :param inputA. :return: None.
treeHasError()  bool

True if the node or any in its input tree have an error, or False otherwise.
Error state of the node and its input tree. Note that this will always return false for viewers, which cannot generate their input trees. Instead, choose an input of the viewer (e.g. the active one), and call treeHasError() on that.
unlink()  None

Unlink the node without possibility to resolve.
Raises

**TypeError** – If the node is not a linkable node.
unlock()  Unlocks the node and makes knobs editable.

upstreamFrameRange(_i_)

Frame range for the i’th input of this node. :param i: Input number. :return: FrameRange. Returns None when querying an invalid input.
width()  int.

Width of the node. :return: int.
writeKnobs(_i_)  String in .nk form.

Return a tcl list. If TO_SCRIPT  TO_VALUE is not on, this is a simple list of knob names. If it is on, it is an alternating list of knob names and the output of to_script().
Flags can be any of these or’d together: \- nuke.TO_SCRIPT produces to_script(0) values \- nuke.TO_VALUE produces to_script(context) values \- nuke.WRITE_NON_DEFAULT_ONLY skips knobs with not_default() false \- nuke.WRITE_USER_KNOB_DEFS writes addUserKnob commands for user knobs \- nuke.WRITE_ALL writes normally invisible knobs like name, xpos, ypos
Parameters

**i** – The set of flags or’d together. Default is TO_SCRIPT  TO_VALUE.
Returns

String in .nk form.
xpos()  X position of node in node graph.

Returns

X position of node in node graph.
ypos()  Y position of node in node graph.

Returns

Y position of node in node graph.