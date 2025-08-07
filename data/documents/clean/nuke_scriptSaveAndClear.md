# nuke.scriptSaveAndClear
nuke.scriptSaveAndClear(_filename =None_, _ignoreUnsavedChanges =False_)  None

Calls nuke.scriptSave and nuke.scriptClear :param filename: Save to this file name without changing the script name in the
> project.
Parameters

**ignoreUnsavedChanges** – Optional. If set to True scripSave will be called, ignoring any unsaved changes
Returns

True when sucessful. False if the user cancels the operation. In this case nuke.scripClear will not be called