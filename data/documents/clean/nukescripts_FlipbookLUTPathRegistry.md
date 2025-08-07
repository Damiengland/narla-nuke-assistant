# nukescripts.FlipbookLUTPathRegistry
_class _nukescripts.FlipbookLUTPathRegistry

Bases: `object`
A registery of all LUT files against LUTs for each specific flipbook.
Methods
`getLUTPathForFlipbook`  Return the path for the given flipbook and lut.---
`registerLUTPathForFlipbook`  Register the given LUT file.

getLUTPathForFlipbook(_flipbook_ , _lut_)

Return the path for the given flipbook and lut. May return an empty string if none registered. :param flipbook: The unique name of the flipbook :param lut: The unique name for the LUT, e.g. ‘sRGB’ and ‘rec709’
registerLUTPathForFlipbook(_flipbook_ , _lut_ , _path_)

Register the given LUT file. :param flipbook: The unique name of the flipbook :param lut: The unique name for the LUT, e.g. ‘sRGB’ and ‘rec709’ :param path: Location of the flipbook specific file.