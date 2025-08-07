# nuke.getFilename
nuke.getFilename(_message_ , _pattern =None_, _default =None_, _favorites =None_, _type =None_, _multiple =False_)  list of strings or single string

Pops up a file chooser dialog box. You can use the pattern to restrict the displayed choices to matching filenames, normal Unix glob rules are used here.
Parameters

  * **message** – Present the user with this message.
  * **pattern** – Optional file selection pattern.
  * **default** – Optional default filename and path.
  * **favorites** – Optional. Restrict favorites to this set. Must be one of ‘image’, ‘script’, or ‘font’.
  * **type** – Optional the type of browser, to define task-specific behaviors; currently only ‘save’ is recognised.
  * **multiple** – Optional boolean convertible object to allow for multiple selection. If this is True, the return value will be a list of strings; if not, it will be a single string. The default is
Returns

If multiple is True, the user input is returned as a list of strings, otherwise as a single string. If the dialog was cancelled, the return value will be None.