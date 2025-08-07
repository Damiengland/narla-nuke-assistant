# nuke.modified
nuke.modified(_status_)  True if modified, False otherwise.

Deprecated. Use Root.modified and Root.setModified.
Get or set the ‘modified’ flag in a script. Setting the value will turn the indicator in the title bar on/off and will start or stop the autosave timeout.
Parameters

**status** – Optional boolean value. If this is present the status will be set to this value; otherwise it will be retrieved instead.
Returns

True if modified, False otherwise.