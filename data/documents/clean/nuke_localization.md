# nuke.localization
APIs for Nuke’s localization functionality.
Use help(‘_localization’) to get detailed help on the classes exposed here.
This module provides the public interface to the localization module and will remain stable. It uses an underlying native module called _localization to provide this interface. While there is nothing stopping you from using the _localization module directly, it may change in a future release and break backwards compatibility.
Functions
param callback
    is a python callable object with arguments for path and event. See nuke.localization.FileEvent for possible file events.---  Adds a callback for read localization events.  Trigger a manual file check, which checks and updates the states of localised files.  Clears unused files in the localization folder.  Returns the list of read nodes that read from the argument paths.  Update all localized files currently in use in Nuke.  forceUpdateAll() -> None  Update all localized files used by nodes that are currently selected.
return
    whether localization was paused  gets the percentage of localization completed.  gets paths of files which are currently localized.  :return string 'on', 'off' or 'manual'  Pause the localization background thread if it was running.  Removes a callback for file localization events.  Removes a callback for read localization events  Resume the localization background thread if it was paused  sets the localization system mode.

Classes  Events received in file callbacks---  Localization status recieved by Read callbacks