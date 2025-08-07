# nuke.frame
nuke.frame(_f_)  Current frame.

Return or set the current frame number. Deprecated. Use Root.frame.
Returns the current frame. Normally this is the frame number set in the root node, typically by the user moving the frame slider in a viewer. If a number is given, it sets the current frame number to that number. If the current context is the root this changes the root frame.
Parameters

**f** – Optional frame number.
Returns

Current frame.