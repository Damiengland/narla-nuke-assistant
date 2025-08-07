# nukescripts.addSnapFunc
nukescripts.addSnapFunc(_label_ , _func_)  None

Add a new snapping function to the list.
The label parameter is the text that will appear in (eg.) an Enumeration_Knob for the function. It cannot be the same as any existing snap function label (if it is, the function will abort without changing anything).
The func parameter is the snapping function. It must be a callable object taking a single parameter: the node to perform the snapping on.