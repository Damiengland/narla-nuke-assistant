# nuke.execute
nuke.execute(_nameOrNode_ , _start_ , _end_ , _incr_ , _views_ , _continueOnError =False_)  None.
nuke.execute(_nameOrNode_ , _frameRangeSet_ , _views_ , _continueOnError =False_)  None.

Execute the named Write node over the specified frames.
There are two variants of this function. The first allows you to specify the frames to write range by giving the start frame number, the end frame number and the frame increment. The second allows you to specify more complicated sets of frames by providing a sequence of FrameRange objects.
If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits the cancel button this command will return ‘cancelled’ error. If Nuke is run from the nuke command line (ie nuke was started with the -t switch) execute() prints a text percentage as it progresses. If the user types ^C it will aborting the execute() and return a ‘cancelled’ error.
Parameters

  * **nameOrNode** – A node name or a node object.
  * **start** – Optional start frame. Default is root.first_frame.
  * **end** – Optional end frame. Default is root.last_frame.
  * **incr** – Optional increment. Default is 1.
  * **views** – Optional list of views. Default is None, meaning all views.
Returns

None