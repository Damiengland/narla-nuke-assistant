# nuke.localization.addFileCallback
nuke.localization.addFileCallback(_callback_)  Adds a callback for file localization events.

Parameters

**callback** – is a python callable object with arguments for path and event. See nuke.localization.FileEvent for possible file events.
Usage Example:
Usage Example def myCallback( path, event ): if event == nuke.localization.FileEvent.LOCALIZED: print(“file : ” + path + ” is localized”) if event == nuke.localization.FileEvent.OUT_OF_DATE: print(“file : ” + path + ” is out of date”)


    ```python
    nuke.localization.addFileCallback( myCallback )
        # Do some localization and process callbacks, when finished call:
        nuke.localization.removeFileCallback( myCallback )
    ```