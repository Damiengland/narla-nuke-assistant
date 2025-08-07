# nuke.animations
nuke.animations()  tuple

Returns a list of animatable things the user wants to work on.
If this is a command being executed from a menu item in a curve editor, a list of the names of all selected curves is returned. If this list is empty a “No curves selected” error is produced.
If this is a command being executed from the pop-up list in a knob then a list of all the fields in the knob is returned.
If this is a command being executed from the right-mouse-button pop-up list in a field of a knob, the name of that field is returned.
Otherwise this produces an error indicating that the command requries a knob context. You can get such a context by doing “in <knob> {command}”
Also see the ‘selected’ argument to the animation command.
See also: animation, animationStart, animationEnd, animationIncrement
Returns

A tuple of animatable things.