# nuke.defaultColorspaceMapper
nuke.defaultColorspaceMapper(_colorspace_ , _dataTypeHint_)

Called by libnuke. Calls into Node-level callbacks first, then global callbacks
Arguments:

colorspace - the name string of the initial colorspace dataTypeHint - sometimes Readers/Writer request the default for a
> particular data-type, i.e. int8, in16, float, etc.
Return:

The return should be the transformed/modified colorspace name. None is the same as returning the string unchanged.