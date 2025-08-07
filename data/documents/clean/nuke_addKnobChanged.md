# nuke.addKnobChanged
nuke.addKnobChanged(_call_ , _args =()_, _kwargs ={}_, _nodeClass ='*'_, _node =None_)

Add code to execute when the user changes a knob The knob is availble in nuke.thisKnob() and the node in nuke.thisNode(). This is also called with dummy knobs when the control panel is opened or when the inputs to the node changes. The purpose is to update other knobs in the control panel. Use addUpdateUI() for changes that should happen even when the panel is closed.