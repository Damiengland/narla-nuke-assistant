# nuke.showCreateViewsDialog
nuke.showCreateViewsDialog()

pluginPath() -> string list
List all the directories Nuke will search in for plugins.
The built-in default is ~/.nuke and the ‘plugins’ directory from the same location the NUKE executable file is in. Setting the environment variable $NUKE_PATH to a colon-separated list of directories will replace the ~/.nuke with your own set of directories, but the plugins directory is always on the end.
Returns

List of paths.