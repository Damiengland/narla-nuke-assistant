# nuke.inputs
nuke.inputs(_n_ , _i_)  int

Deprecated. Use Node.inputs.
Get how many inputs the node has. Normally this is a constant but some nodes have a variable number, the user can keep connecting them and the count will increase. Attempting to set the number will just disconnect all inputs greater or equal to number. For a variable input node this may decrease inputs to the new value. For most nodes this will have no effect on the value of inputs.
Parameters

  * **n** – Node.
  * **i** – Optional number of inputs requested.
Returns

Number of inputs.