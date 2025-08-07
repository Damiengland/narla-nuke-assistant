# nuke.recentFile
nuke.recentFile(_index_)  str

Returns a filename from the recent-files list.
Parameters

**index** – A position in the recent files list. This must be a non-negative number.
Returns

A file path.
Raises

  * **ValueError** – if the index is negative.
  * **RuntimeError** – if there is no entry in the recent files list for the specified index.