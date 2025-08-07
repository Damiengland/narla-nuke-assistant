# nuke.menu
nuke.menu(_name_)

Find and return the Menu object with the given name.
Parameters

**name** – The name of the menu to get. Must be on the following values: \- ‘Nuke’: The application menu \- ‘Pane’: The UI Panes & Panels menu \- ‘Nodes’: The Nodes toolbar (and Nodegraph right mouse menu) \- ‘Properties’: The Properties panel right mouse menu \- ‘Animation’: The knob Animation menu and Curve Editor right mouse menu \- ‘Viewer’: The Viewer right mouse menu \- ‘Node Graph’: The Node Graph right mouse menu \- ‘Axis’: Functions which appear in menus on all Axis_Knobs.
Returns

The menu.
Raises

RuntimeError: if Nuke isn’t in GUI mode.