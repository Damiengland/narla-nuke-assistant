# nuke.pluginExists
nuke.pluginExists(_name_)  True if found, or False if not.

This function is the same as load(), but only checks for the existence of a plugin rather than loading it. If there is no slash in the name then the pluginPath() is searched for it. If there is a slash then the name is used directly as a filename, if it does not start with a slash the name is relative to the directory containing any plugin being currently loaded. If no filename extension is provided, it will try appending ‘.so’ (or whatever your OS dynamic library extension is) and finding nothing will also try to append ‘.tcl’ and ‘.py’.
Parameters

**name** – Plugin name or filename.
Returns

True if found, or False if not.