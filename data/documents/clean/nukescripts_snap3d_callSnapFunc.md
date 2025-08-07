# nukescripts.snap3d.callSnapFunc
nukescripts.snap3d.callSnapFunc(_nodeToSnap_)  None

Call the snapping function on a node.
The nodeToSnap parameter is optional. If it’s not specified, or is None, we use the result of nuke.thisNode() instead.
The node must have an Enumeration_Knob called “snapFunc” which selects the snapping function to call.