# nukescripts.script.version_get
nukescripts.script.version_get(_string_ , _prefix_ , _suffix =None_)

Extract version information from filenames used by DD (and Weta, apparently) These are _v# or /v# or .v# where v is a prefix string, in our case we use “v” for render version and “c” for camera track version. See the version.py and camera.py plugins for usage.