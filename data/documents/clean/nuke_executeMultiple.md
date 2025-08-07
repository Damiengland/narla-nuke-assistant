# nuke.executeMultiple
nuke.executeMultiple(_nodes_ , _ranges_ , _views_ , _continueOnError =False_)  None

Execute the current script for a specified frame range. The argument nodes is a sequence of Nuke nodes and ranges is a sequence of range lists. A Nuke range list is a sequence of 3 integers - first, last and incr ( e.g. nuke.execute((w,), ((1,100,1),)) ). The named nodes must all be Write or other executable operators. If no nodes are given then all executable nodes in the current group are executed. Note that DiskCache and Precomp nodes do not get executed with this call, unless explicitly specified.
If Nuke is run with the GUI up, this will pop up a progress meter. If the user hits the cancel button this command will raise a ‘cancelled’ error. If Nuke is run in terminal mode (with the -t switch) this prints a text percentage as it progresses.
If the user types ^C it will abort the execute() and raise a ‘cancelled’ error.
Parameters

  * **nodes** – Node list.
  * **ranges** – Optional start frame. Default is root.first_frame.
  * **views** – Optional list of views. Default is None. Execute for all.
Returns

None