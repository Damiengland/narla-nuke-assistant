# nuke.ViewerWindow
_class _nuke.ViewerWindow

Bases: `object`
Methods
`activateInput`  Set the given viewer input to be active - i.---
`activeInput`  Returns the currently active input of the viewer - i.
`frameControl`  i is an integer indicating viewer frame control 'button' to execute:
`getCurrentErrorMessage`  Returns the error currently displayed in this viewer.
`getGLCameraMatrix`  Return the world transformations of the current GL viewer camera.
`getGeometryNodes`  self.getGeometry() -> None Returns the a list of geometry nodes attached with this viewer :return: Nodes: a list of the geometry nodes.
`nextView`
`node`  Returns the Viewer node currently associated with this window.
`play`  Play forward (1) or reverse (0).
`previousView`
`setView`
`stop`  Stop playing.
`view`

activateInput(_input_ , _secondary =False_)  None

Set the given viewer input to be active - i. e. show its image in the output window. :param input: The viewer input number, starting with 0 for the first. If the input is not connected, a ValueError exception is raised. :param secondary: True if the input should be connected as the secondary (wipe) input, or False to connect it as the primary input (the default). :return: None
activeInput(_secondary =False_)  int

Returns the currently active input of the viewer - i. e. the one with its image in the output window. :param secondary: True to return the index of the active secondary (wipe) input, or False (the default) to return the primary input. :return: int: The currently active input of the viewer, starting with 0 for the first, or None if no input is active.
frameControl(_i_)  True.

i is an integer indicating viewer frame control ‘button’ to execute:
> -6 go to start -5 play reverse -4 go to previous keyframe -3 step back by increment -2 go back previous keyframe or increment, whichever is closer -1 step back one frame
>
>> 0 stop
>
> +1 step forward one frame +2 go to next keyframe or increment, whichever is closer +3 step forward by increment +4 go to next keyframe +5 play forward +6 go to end
getCurrentErrorMessage()  Error.

Returns the error currently displayed in this viewer. :return: Error string if an error is present, otherwise None.
getGLCameraMatrix()

Return the world transformations of the current GL viewer camera. :return: Matrix4: GL camera world transformation.
getGeometryNodes()

self.getGeometry() -> None Returns the a list of geometry nodes attached with this viewer :return: Nodes: a list of the geometry nodes.
nextView()  switch to next view in settings Views list.

node()  Node.

Returns the Viewer node currently associated with this window. :return: Node.
play()

Play forward (1) or reverse (0).
previousView()  switch to previous view in settings Views list.

setView(_s_)  set 'current' multi-view view to 's'.

stop()

Stop playing.
view()  string name of 'current' multi-view view.