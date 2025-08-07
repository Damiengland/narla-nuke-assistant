# nuke.pluginAppendPath
nuke.pluginAppendPath(_args_ , _addToSysPath =True_)

Add a filepath to the end of the Nuke plugin path. If the path already exists in the list of plugin paths, it will remain at its current position. It also appends the paths to the sys.path, if addToSysPath is True.