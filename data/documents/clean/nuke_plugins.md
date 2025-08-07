# nuke.plugins
nuke.plugins(_switches =0_, _* pattern_)  list of str

Returns a list of every loaded plugin or every plugin available. By default each plugin is returned as the full pathname of the plugin file.
You can give a glob-style matching pattern and only the plugins whose filenames (not path) match the pattern will be returned. You can give more than one glob pattern if desired.
You can also put options before the glob patterns. Currently supported:
> ALL Return all plugins in each of the plugin_path() directories,
>
>
> rather than only the currently loaded plugins.
>
> NODIR Just put the filenames in the list, not the full path. There
>
>
> may be duplicates.
>
> REGISTERED Include Ops which have been registered by the loaded plugins.
>
>
> This is useful for plugin bundles where there are registered Ops which do not have their own plugin file. Please note that these Ops will not have a directory path or file extension. They are not filtered by the pattern.
>
> NOREADERWRITER Do not include Reader or Writer plugins. These cannot be used
>
>
> as stand-alone plugins.
If you don’t specify any switches, the default behaviour is to return a list with the full paths of all loaded plugins.
Parameters

  * **switches** – Optional parameter. Bitwise OR of nuke.ALL, nuke.NODIR, nuke.REGISTERED, nuke.NOREADERWRITER.
  * **pattern** – Zero or more glob patterns.
Returns

List of plugins.