# nukescripts.readviewscheck.onReadNodeCreated
nukescripts.readviewscheck.onReadNodeCreated()

Callback when a Read node is created. Note that the knob values don’t seem to be set when this callback occurs. Defer the check with a QTimer, which will cause the views check to be done when the Qt event loop next sends events.