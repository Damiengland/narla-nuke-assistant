# nukescripts.createNodeLocal
nukescripts.createNodeLocal(_node_ , _knobs =''_, _inpanel =True_)

Create a node within the context of the last hit group.
Wrapper method that calls nuke.createNode with the context of the last hit group. This allows users to click into an open group view and create nodes. The default last hit group is the DAG window. Shares the same parameters as nuke.createNode:
Parameters

  * **node** (_str_) – Name of node class to create (e.g. ‘Blur’).
  * **knobs** (_str_ _,__optional_) – TCL list of knob name value pairs.
  * **inpanel** (_bool_ _,__optional_) – Open the control bin (only applies when the GUI is running), defaults to True.
Returns

The node created.
Return type