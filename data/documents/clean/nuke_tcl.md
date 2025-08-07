# nuke.tcl
nuke.tcl(_s_ , _* args_)  str.

Run a tcl command. The arguments must be strings and passed to the command. If no arguments are given and the command has whitespace in it then it is instead interpreted as a tcl program (this is deprecated).
Parameters

  * **s** – TCL code.
  * **args** – The arguments to pass in to the TCL code.
Returns

Result of TCL command as string.