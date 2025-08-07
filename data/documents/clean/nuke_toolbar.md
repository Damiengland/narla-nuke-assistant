# nuke.toolbar
nuke.toolbar(_name_ , _create =True_)

Find and return the ToolBar object with the given name. The name of the built-in nodes toolbar is ‘Nodes’.
Parameters

  * **name** – The name of the toolbar to find or create.
  * **create** – Optional parameter. True (the default value) will mean that a new toolbar gets created if one with the given name couldn’t be found; False will mean that no new toolbar will be created.
Raises

A RuntimeException is thrown if not in GUI mode.
Returns

The toolbar, or None if no toolbar was found and ‘create’ was False.