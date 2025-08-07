# nukescripts.renderdialog.DialogState
_class _nukescripts.renderdialog.DialogState

Bases: `object`
Methods
`get`  Return the given knob's stored last state value.---
`getValue`  Recalls the value.
`save`  Store the knob's current value as the 'last state' for the next time the dialog is opened.
`saveValue`  Stores the value with the given id.
`setKnob`  Convenience method for setting a value straight on a knob.

get(_knob_ , _defaultValue =None_)

Return the given knob’s stored last state value. If none exists, defaultValue is returned. Values are stored in a dict referenced by knob name, so names must be unique!
getValue(_id_ , _defaultValue =None_)

Recalls the value. If it was not set before, it will return the defaultValue.
save(_knob_)

Store the knob’s current value as the ‘last state’ for the next time the dialog is opened. Values are stored in a dict referenced by knob name, so names must be unique!
saveValue(_id_ , _value_)

Stores the value with the given id.
setKnob(_knob_ , _defaultValue =None_)

Convenience method for setting a value straight on a knob.