# nuke.createToolset
nuke.createToolset(_filename =None_, _overwrite =- 1_, _rootPath =None_)  None

Creates a tool preset based on the currently selected nodes.
Parameters

  * **filename** – Saves the preset as a script with the given file name.
  * **overwrite** – If 1 (true) always overwrite; if 0 (false) never overwrite;
  * **rootPath** – If specified, use this as the root path to save the Toolset to. If not specified, save to the user’s .nuke/Toolsets folder. otherwise, in GUI mode ask the user, in terminal do same as False. Default is -1, meaning ‘ask the user’.