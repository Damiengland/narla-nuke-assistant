# nuke.numvalue
nuke.numvalue(_knob_ , _default =infinity_)  float

The numvalue function returns the current value of a knob.
This is the same as the value() command except it will always return a number. For enumerations this returns the index into the menu, starting at zero. For checkmarks this returns 0 for false and 1 for true.
Parameters

  * **knob** – A knob.
  * **default** – Optional default value to return if the knob’s value cannot be converted to a number.
Returns

A numeric value for the knob, or the default value (if any).