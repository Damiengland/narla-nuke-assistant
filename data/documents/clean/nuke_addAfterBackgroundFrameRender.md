# nuke.addAfterBackgroundFrameRender
nuke.addAfterBackgroundFrameRender(_call_ , _args =()_, _kwargs ={}_)

Add code to execute after each frame of a background render. The call must be in the form of: def foo(context):
> pass
The context object that will be passed in is a dictionary containing the following elements: id => The identifier for the task that’s making progress frame => the current frame number being rendered numFrames => the total number of frames that is being rendered frameProgress => the number of frames rendered so far.
Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).