# nuke.expr
nuke.expr()

expression(s) -> float
Parse a Nuke expression. Runs the same expression parser as is used by animations. This is not the same as the tcl expr parser. The main differences are:
  * Only floating point numbers are calculated. There are no strings, boolean, or integer values.
  * You can name any knob that returns a floating point value, with a dot-separated name, see knob for details on these names. You may follow the knob name with a time in parenthesis (like a function call) and if it is animated it will be evaluated at that time. If it is animated and no time is given, ‘frame’ is used.
  * The words ‘frame’, ‘t’, and ‘x’ evaluate to the frame number of the context node, or the frame number this animation is being evaluated at.
  * The word ‘y’ in an animation expression evaluates to the value the animation would have if the control points were used and there was no expression. Outside an animation expression y returns zero.
Parameters

**s** – The expression, as a string.
Returns

The result.