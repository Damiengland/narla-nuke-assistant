# nuke.addDefaultColorspaceMapper
nuke.addDefaultColorspaceMapper(_call_ , _args =()_, _kwargs ={}_, _nodeClass ='*'_)

Add a function to modify default colorspaces before Nuke passes them to Readers or Writers.
Functions should have the same positional argument as in the definition of defaultLUTMapper()
All added functions are called in backwards order.