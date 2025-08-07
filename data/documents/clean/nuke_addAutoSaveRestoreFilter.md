# nuke.addAutoSaveRestoreFilter
nuke.addAutoSaveRestoreFilter(_filter_)  None

Add a function to modify the autosave restore file before Nuke attempts to restores the autosave file.
Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.
Parameters

**filter** – A filter function. The first argument to the filter is the current autosave filename.
This function should return the filename to load autosave from or it should return None if the autosave file should be ignored.