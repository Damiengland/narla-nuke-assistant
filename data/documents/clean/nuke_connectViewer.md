# nuke.connectViewer
nuke.connectViewer(_inputNum_ , _node_)  None

Connect a viewer input to a node. The argument i is the input number and n is either a Nuke node or None. Some viewer in the current group is found, if there are no viewers one is created. The viewer is then altered to have at least n+1 inputs and then input n is connected to the given node. This function is used by the numeric shortcuts in the DAG view menu.
Parameters

  * **inputNum** – Input number.
  * **node** – The Node to connect to the input.
Returns

None