# nukescripts.registerLUTPath
nukescripts.registerLUTPath(_flipbookApplication_ , _lut_ , _path_)

Register a LUT for a specific flipbook. The path should refer to a file that contains the LUT for the given flipbook identified by the name in flipbookApplication. It is up to the flipbook subimplementation to actually use this file and the format may vary. :param flipbook: The unique name of the flipbook :param lut: The unique name for the LUT, e.g. ‘sRGB’ and ‘rec709’ :param path: Location of the flipbook specific file.