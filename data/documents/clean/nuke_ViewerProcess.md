# nuke.ViewerProcess
_class _nuke.ViewerProcess

Bases: `object`
Methods
`node`  Returns a ViewerProcess node.---
`nodeMonitorOut`  Returns a ViewerProcess node for Monitor Out.
`register`  Register a ViewerProcess.
`registeredNames`  Returns a list containing the names of all currently regisered ViewerProcesses.
`restoreSelectionAfterReload`  Restores the viewer process selection after an OCIO or Nuke Config has been reloaded this is normally called after nuke.ViewerProcess.storeSelectionBeforeReload()
`storeSelectionBeforeReload`  When the user reloads an OCIO or Nuke config the viewer process selection is stored in the the viewer process object Following the reload you can call nuke.ViewerProcess.restoreSelectionAfterReload() which will then restore the selection instead of the default.
`unregister`  Unregister a ViewerProcess.

node(_name_ , _viewer_)  Node.

Returns a ViewerProcess node. Default is to return the current selected one. This is a class method.
Parameters

  * **name** – Optional ViewerProcess name.
  * **viewer** – Optional viewer name.
Returns

Node.
nodeMonitorOut(_name_ , _viewer_)  Node.

Returns a ViewerProcess node for Monitor Out. If a viewer has not been specified, returns the current selected one. This is a class method.
Parameters

  * **name** – Optional ViewerProcess name.
  * **viewer** – Optional viewer name.
Returns

Node.
register(_name_ , _call_ , _args_ , _kwargs_)  None.

Register a ViewerProcess. This is a class method.
Parameters

  * **name** – Menu name.
  * **call** – Python callable. Must return a Node.
  * **args** – Arguments to call.
  * **kwargs** – Optional named arguments.
Returns

None.
registeredNames()  List.

Returns a list containing the names of all currently regisered ViewerProcesses.
Returns

List.
restoreSelectionAfterReload()  None.

Restores the viewer process selection after an OCIO or Nuke Config has been reloaded this is normally called after nuke.ViewerProcess.storeSelectionBeforeReload()
Returns

None.
storeSelectionBeforeReload()  None.

When the user reloads an OCIO or Nuke config the viewer process selection is stored in the the viewer process object Following the reload you can call nuke.ViewerProcess.restoreSelectionAfterReload() which will then restore the selection instead of the default.
Returns

None.
unregister(_name_)  None.

Unregister a ViewerProcess. This is a class method.
Parameters

**name** – Menu name.
Returns

None.