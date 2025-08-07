# nukescripts.flipbook
nukescripts.flipbook(_command_ , _node_ , _framesAndViews =None_)

Runs an arbitrary command on the images output by a node. This checks to see if the node is a Read or Write and calls the function directly otherwise it creates a temporary Write, executes it, and then calls the command on that temporary Write, then deletes it.
By writing your own function you can use this to launch your own flipbook or video-output programs.
Specify framesAndViews as a tuple if desired, like so: (“1,5”, [“main”]) This can be useful when running without a GUI.