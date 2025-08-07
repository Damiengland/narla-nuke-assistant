# nukescripts.renderdialog.ExecuteDialog
_class _nukescripts.renderdialog.ExecuteDialog(_dialogState_ , _groupContext_ , _nodeSelection =[]_, _exceptOnError =True_)

Bases:
Methods
`accept` ---
`add`  Add a child widget.
`addCallback`
`addKnob`  Add the knob and make sure it cannot be animated.
`addToPane`
`cancel`
`close`  Called when the widget is asked to be closed.
`create`
`destroy`  Destroy the widget.
`finishModalDialog`
`height`  Get the height.
`hide`  Hide the widget.
`isEnabled`  Return the enabled state.
`isValid`  Returns true if the widget still exists.
`knobChanged`
`knobChangedCallback`
`knobs`
`ok`
`readKnobs`
`reject`
`removeCallback`
`removeKnob`
`run`
`setEnabled`  Enable or disable the widget.
`setMaximumSize`  Set the maximum size.
`setMinimumSize`  Set the minimum size.
`setTooltip`  Set the tooltip.
`setVisible`  Show or hide the widget.
`show`  Show the widget.
`showModal`  Show the dialog as modal, and wait for it to be dismissed.
`showModalDialog`
`tooltip`  Get the tooltip.
`width`  Get the width.
`writeKnobs`

add()

Add a child widget.
addKnob(_knob_)

Add the knob and make sure it cannot be animated.
close()

Called when the widget is asked to be closed.
destroy()

Destroy the widget.
height()

Get the height.
hide()

Hide the widget.
isEnabled()

Return the enabled state.
isValid()

Returns true if the widget still exists. i.e. has not been closed by the user.
setEnabled()

Enable or disable the widget.
setMaximumSize()

Set the maximum size.
setMinimumSize()

Set the minimum size.
setTooltip()

Set the tooltip.
setVisible()

Show or hide the widget.
show()

Show the widget.
showModal(_defaultKnobText =''_)

Show the dialog as modal, and wait for it to be dismissed.
tooltip()

Get the tooltip.
width()

Get the width.