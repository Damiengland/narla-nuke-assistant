# nuke.scriptSaveAs
nuke.scriptSaveAs(_filename =None_, _overwrite =- 1_)  None

Saves the current script with the given file name if supplied, or (in GUI mode) asks the user for one using the file chooser. If Nuke is not running in GUI mode, you must supply a filename.
Parameters

  * **filename** – Saves the current script with the given file name if supplied, or (in GUI mode) asks the user for one using the file chooser.
  * **overwrite** – If 1 (true) always overwrite; if 0 (false) never overwrite; otherwise, in GUI mode ask the user, in terminal do same as False. Default is -1, meaning ‘ask the user’.