# nuke.filename
nuke.filename(_node_ , _i_)  str

Return the filename(s) this node or group is working with.
For a Read or Write operator (or anything else with a filename knob) this will return the current filename, based on the root.proxy settings and which of the fullsize/proxy filenames are filled in. All expansion of commands and variables is done. However by default it will still have %%04d sequences in it, use REPLACE to get the actual filename with the current frame number.
If the node is a group, a search is done for executable (i.e. Write) operators and the value from each of them is returned. This will duplicate the result of calling execute() on the group.
Parameters

  * **node** – Optional node.
  * **i** – Optional nuke.REPLACE. Will replace %%04d style sequences with the current frame number.
Returns

Filename, or None if no filenames are found.