# nuke.createNode
nuke.createNode(_node_ , _knobs_ , _inpanel_)

Creates a node of the specified type and adds it to the DAG.
Parameters

  * **node** (_str_) – Name of node class to create (e.g. ‘Blur’).
  * **knobs** (_str_ _,__optional_) – TCL list of knob name value pairs.
  * **inpanel** (_bool_ _,__optional_) – Open the control bin (only applies when the GUI is running), defaults to True.
Returns

The node created.
Return type