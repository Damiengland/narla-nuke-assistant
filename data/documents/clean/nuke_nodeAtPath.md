# nuke.nodeAtPath
nuke.nodeAtPath(_path_ , _instanceIndex_)

Find the node at the given full path, if it exists, and return it as a Python object. If the ‘instanceIndex’ provided is >= 0 then a specific clone instance (index 1+), or the ‘original’(base) instance (index 0) is returned. If ‘instanceIndex’ value is not valid for the retrieved Node’s context then null is returned.
‘path’ is -always- an absolute path and periods ‘.’ are assumed as the node hierarchy separator, conforming to the standard Nuke node path convention. However unlike ‘toNode()’ embedded expressions are -NOT- supported in the path string. For example you cannot retrieve a node using the path string ‘Group1.FooNode.parent’ as the trailing ‘.parent’ is an expression, while ‘Group1.FooNode’ will work since it ends in an explicit node name.
Parameters

  * **path** – Absolute node path ending in a node name. No expression support provided.
  * **instanceIndex** – Optional. If >= 0 return a specific clone instance where index 0 is the
base node and index 1+ are clones. If instanceIndex is specified but the node is not cloned or the value is out of range then None is returned. :return: Node or None if it does not exist.