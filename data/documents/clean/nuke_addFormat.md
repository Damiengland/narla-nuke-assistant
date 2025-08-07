# nuke.addFormat
nuke.addFormat(_s_)  Format or None.

Create a new image format, which will show up on the pull-down menus for image formats. You must give a width and height and name. The xyrt rectangle describes the image area, if it is smaller than the width and height (for Academy aperture, for example). The pixel aspect is the ratio of the width of a pixel to the height.
Parameters

**s** – String in TCL format w h ?x y r t? ?pa? name.
Returns

Format or None.