# nuke.dependencies
nuke.dependencies(_nodes_ , _what =31_)

List all nodes referred to by the nodes argument. ‘what’ is an optional integer (see below).

You can use the following constants or’ed together to select the types of dependencies that are looked for:

nuke.EXPRESSIONS = expressions nuke.LINKINPUTS = link knob inputs nuke.LINKNODE_INPUTS = link nodes nuke.INPUTS = visible input pipes nuke.HIDDEN_INPUTS = hidden input pipes.
The default is to look for all types of connections.
Example:

n1 = nuke.nodes.Blur() n2 = nuke.nodes.Merge() n2.setInput(0, n1) deps = nuke.dependencies([n2], nuke.INPUTS  nuke.HIDDEN_INPUTS  nuke.EXPRESSIONS)