# nuke.addValidateFilename
nuke.addValidateFilename(_call_ , _args =()_, _kwargs ={}_, _nodeClass ='Write'_)

Add a function to validate a filename in Write nodes. The first argument is the filename and it should return a Boolean as to whether the filename is valid or not. If a callback is provided, it will control whether the Render button of Write nodes and the Execute button of WriteGeo nodes is enabled or not.