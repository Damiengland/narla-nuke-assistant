# nuke.addAutolabel
nuke.addAutolabel(_call_ , _args =()_, _kwargs ={}_, _nodeClass ='*'_)

Add code to execute on every node to produce the text to draw on it in the DAG. Any value other than None is converted to a string and used as the text. None indicates that previously-added functions should be tried