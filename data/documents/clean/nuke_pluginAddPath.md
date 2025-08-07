# nuke.pluginAddPath
nuke.pluginAddPath(_args_ , _addToSysPath =True_)

Adds all the paths to the beginning of the Nuke plugin path. If the path already exists in the list of plugin paths, it is moved to the start. If this command is executed inside an init.py then the init.py in the path will be executed. It also adds the paths to the sys.path, if addToSysPath is True.