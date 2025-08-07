# nuke.addAutoSaveDeleteFilter
nuke.addAutoSaveDeleteFilter(_filter_)  None

Add a function to modify the autosave filename before Nuke attempts delete the autosave file.
Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.
Parameters

**filter** – A filter function. The first argument to the filter is the current autosave filename.
This function should return the filename to delete or return None if no file should be deleted.