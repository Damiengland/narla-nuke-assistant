# nuke.addAutoSaveFilter
nuke.addAutoSaveFilter(_filter_)  None

Add a function to modify the autosave filename before Nuke saves the current script on an autosave timeout.
Look at rollingAutoSave.py in the nukescripts directory for an example of using the auto save filters.
Parameters

**filter** – A filter function. The first argument to the filter is the current autosave filename.
The filter should return the filename to save the autosave to.