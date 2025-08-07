# nuke.dependentNodes
nuke.dependentNodes(_what =31_, _nodes =[]_, _evaluateAll =True_)

List all nodes referred to by the nodes argument. ‘what’ is an optional integer (see below).

You can use the following constants or’ed together to select what types of dependent nodes are looked for:

nuke.EXPRESSIONS = expressions nuke.LINKINPUTS = link knob inputs nuke.LINKNODE_INPUTS = link nodes nuke.INPUTS = visible input pipes nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.
evaluateAll is an optional boolean defaulting to True. When this parameter is true, it forces a re-evaluation of the entire tree. This can be expensive, but otherwise could give incorrect results if nodes are expression-linked.
Example:

n1 = nuke.nodes.Blur() n2 = nuke.nodes.Merge() n2.setInput(0, n1) ndeps = nuke.dependentNodes(nuke.INPUTS  nuke.HIDDEN_INPUTS  nuke.EXPRESSIONS, [n1])
param what

Or’ed constant of nuke.EXPRESSIONS, nuke.LINKINPUTS, nuke.LINKNODE_INPUTS, nuke.INPUTS and nuke.HIDDEN_INPUTS to select the types of dependent nodes. The default is to look for all types of connections.
param evaluateAll

Specifies whether a full tree evaluation will take place. Defaults to True.
return

List of nodes.