# nuke.addFavoriteDir
nuke.addFavoriteDir(_name_ , _directory_ , _type_ , _icon_ , _tooltip_ , _key_)  None.

Add a path to the file choosers favorite directory list. The path name can contain environment variables which will be expanded when the user clicks the favourites button
Parameters

  * **name** – Favourite path entry (‘Home’, ‘Desktop’, etc.).
  * **directory** – FileChooser will change to this directory path.
  * **type** – Optional bitwise OR combination of nuke.IMAGE, nuke.SCRIPT, nuke.FONT or nuke.GEO.
  * **icon** – Optional filename of an image to use as an icon.
  * **tooltip** – Optional short text to explain the path and the meaning of the name.
  * **key** – Optional shortcut key.
Returns

None.