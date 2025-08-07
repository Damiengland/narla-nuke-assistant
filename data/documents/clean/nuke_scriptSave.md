# nuke.scriptSave
nuke.scriptSave(_filename =None_)  bool

Saves the current script to the current file name. If there is no current file name and Nuke is running in GUI mode, the user is asked for a name using the file chooser.
Parameters

**filename** – Save to this file name without changing the script name in the project (use scriptSaveAs() if you want it to change).
Returns

True if the file was saved, otherwise an exception is thrown.)