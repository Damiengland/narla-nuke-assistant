# nuke.ofxMenu
nuke.ofxMenu()  bool

Find all the OFX plugins (by searching all the directories below $OFX_PLUGIN_PATH, or by reading a cache file stored in $NUKE_TEMP_DIR), then add a menu item for each of them to the main menu.
Returns

True if succeeded, False otherwise.