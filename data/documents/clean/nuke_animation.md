# nuke.animation
nuke.animation(_object_ , _* commands_)  None

Does operations on an animation curve.
The following commands are supported:

  * B{clear} deletes all the keys from the animation.
  * B{erase} `index I{last_index`} removes all keyframes between index and last_index
  * B{expression} `I{newvalue`} returns or sets the expression for the animation. The default is ‘curve’ or ‘y’ which returns the interpolation of the keys.
  * B{generate} `start end increment field expression I{field expression` …} generates an animation with start, end, and increment. Multiple field/expression pairs generate a keyframe. Possible field commands are:
>     * B{x} sets the frame number for the next keyframe
>
>     * B{y} sets the keyframe value
>
>     * B{dy} sets the left slope
>
>     * B{ldy} sets left and right slope to the same value
>
>     * B{la} and B{ra} are the length of the slope handle in x direction. A value of 1 generates a handle that is one third of the distance to the next keyframe.
  * B{index} `x` returns the index of the last key with x <= t, return -1 for none.
  * B{is_key} return non-zero if there is a key with x == t. The actual return value is the index+1.
  * B{move} `field expression I{field expression`} replaces all selected keys in an animation with new ones as explained above in B{generate}
  * B{name} returns a user-friendly name for this animation. This will eliminate any common prefix between this animation and all other selected ones, and also replaces mangled names returned by animations with nice ones.
  * B{size} returns the number of keys in the animation.
  * B{test} errors if no points in the animation are selected
  * B{y} index `I{newvalue`} gets or sets the value of an animation.
  * B{x} index `I{newvalue`} gets or sets the horizontal postion of a key. If the animation contains an expression or keyframes, the new value will be overridden.
See also: animations
Parameters

  * **object** – The animation curve.
  * **commands** – a varargs-style list of commands, where each command is one of those defined above.
Returns

None