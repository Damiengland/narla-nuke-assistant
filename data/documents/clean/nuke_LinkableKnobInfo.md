# nuke.LinkableKnobInfo
_class _nuke.LinkableKnobInfo

Bases: `object`
A linkable knob description. Holds a reference to a knob that may be linked to, as well as an indication whether this knob should be used as part of an absolute or relative expression and whether it is enabled.
Methods
`absolute`  Returns whether the values of this knob should be treated as absolute or relative.---
`displayName`  Returns the custom display name that will appear in Link-to menus.
`enabled`  Returns whether the knob is currently enabled or not.
`indices`  Returns a list of the knob channels that should be used with this linkable knob.
`knob`  Returns the knob that may be linked to.

absolute()  Boolean

Returns whether the values of this knob should be treated as absolute or relative. This may be useful for positions.
displayName()  String

Returns the custom display name that will appear in Link-to menus.
enabled()  Boolean

Returns whether the knob is currently enabled or not.
indices()  List

Returns a list of the knob channels that should be used with this linkable knob.
knob()

Returns the knob that may be linked to.