# nuke.runIn
nuke.runIn(_object_ , _cmd_)  bool

Execute commands with a given node/knob/field as the ‘context’. This means that all names are evaluated relative to this object, and commands that modify ‘this’ node will modify the given one.
Parameters

  * **object** – Name of object.
  * **cmd** – Command to run.
Returns

True if succeeded, False otherwise.