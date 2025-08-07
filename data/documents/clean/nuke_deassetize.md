# nuke.deassetize
nuke.deassetize()

Finds all assetized File_Knobs in nodes and replaces their entity reference by their respective resolved file path.
:param nodes : A list of nodes to be deassetized
: return : A tuple.The first element is a boolean that is True if all assetized knobs were successfully deassetized and the second is a list of unresolved knobs that are assetized but failed to be resolved.
If OpenAssetIO isn’t correctly configured, (False, []) is returned.