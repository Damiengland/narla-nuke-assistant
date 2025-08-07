# nuke.allNodes
nuke.allNodes(_filter_ , _group_ , _recurseGroups_)  list

List of all nodes in a group. If you need to get all the nodes in the script from a context which has no child nodes, for instance a control panel, use nuke.root().nodes().
Parameters

  * **filter** – Optional. Only return nodes of the specified class.
  * **group** – Optional. If the group is omitted the current group (ie the group the user picked a menu item from the toolbar of) is used.
  * **recurseGroups** – Optional. If True, will also return all child nodes within any group nodes. This is done recursively and defaults to False.
Returns

list