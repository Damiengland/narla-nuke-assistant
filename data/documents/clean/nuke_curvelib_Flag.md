# nuke.curvelib.Flag
_class _nuke.curvelib.Flag

Bases: `object`
A base class for objects which have a set of flags that can be set.
You should never be instantiating this class directly - it only exists for other classes to inherit from.
Methods
`getFlag`  Gets the specified flag.---
`setFlag`  Set or clear the specified flag.

getFlag(_flag_)  bool

Gets the specified flag. The parameter should be one of the FlagType constants.
setFlag(_flag_ , _value_)  None

Set or clear the specified flag. The flag parameter should be one of the FlagType constants and value should be True or False.