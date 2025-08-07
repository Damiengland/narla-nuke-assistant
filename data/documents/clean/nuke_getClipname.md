# nuke.getClipname
nuke.getClipname(_prompt_ , _pattern =None_, _default =None_, _multiple =False_)  list of strings or string

Pops up a file chooser dialog box. You can use the pattern to restrict the displayed choices to matching filenames, normal Unix glob rules are used here. getClipname compresses lists of filenames that only differ by an index number into a single entry called a ‘clip’.
Parameters

  * **prompt** – Present the user with this message.
  * **pattern** – Optional file selection pattern.
  * **default** – Optional default filename and path.
  * **multiple** – Optional boolean convertible object to allow for multiple selection.
Returns

If multiple is True, the user input is returned as a list of strings, otherwise as a single string. If the dialog is cancelled, the return value is None.