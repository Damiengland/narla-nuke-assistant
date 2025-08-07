# nukescripts.udim_import
nukescripts.udim_import(_udim_parsing_func= <function parseUdimFile>_, _udim_column_label='UDIM'_)

Imports a sequence of UDIM files and creates the node material tree needed.

This function simplifies the process of importing textures. It generates a tree of nodes which adjusts the texture coordinates at rendering time for a model containing multiple texture tiles. In general a tile texture coordinate can be expressed with a single value(UDIM) or with a tuple(ST or UV). The udim_import function can decode a UDIM number from a filename. To determine the tile coordinate encoding for a generic filename convention, the udim_import script can use an external parsing function.
The redefined parsing function needs to decode a filename string and return the udim or the u,v tile coordinate as an integer or tuple of integers. It should return None if the tile coordinate id can not be determined.
Parameters

  * **udim_parsing_func** – The parsing function. This parses a filename string and returns a tile id.
  * **udim_column_label** – The name of the column in the dialog box used to show the tile id.
Returns

None