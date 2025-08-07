# nuke.addFilenameFilter
nuke.addFilenameFilter(_call_ , _args =()_, _kwargs ={}_, _nodeClass ='*'_)

Add a function to modify filenames before Nuke passes them to the operating system. The first argument to the function is the filename, and it should return the new filename. None is the same as returning the string unchanged. All added functions are called in backwards order.