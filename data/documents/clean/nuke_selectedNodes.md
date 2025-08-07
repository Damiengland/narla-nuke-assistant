# nuke.selectedNodes
nuke.selectedNodes(_filter_ , _recursive_)  list

Returns a list of all selected nodes in the current group by default.
If recursive=True is specified, the algorithm will search recursively for selected nodes. An attempt is made to return them in ‘useful’ order where inputs are done before the final node, so commands applied to this list go from top-down.
Parameters

  * **filter** (_str_ _,__optional_) – Only return nodes of the specified node class.
  * **recursive** (_bool_ _,__optional_) – If True, the algorithm will search recursively for selected nodes.
Returns

The list of selected nodes.
Return type

list