# nukescripts.FlipbookApplication
_class _nukescripts.FlipbookApplication

Bases: `object`
An interface, for so far as Python supports it. To add support for a flipbook this needs to be subclassed and the 3 methods implemented. The default implementation just raises an exception so any sub implementer will soon find out whether his implementation works.
Methods
`cacheDir`  Return the preferred directory for rendering.---
`capabilities`  Return the capabilities of the flipbook application in a dict. Currently used are: canPreLaunch: bool, whether the flipbook can display a frames that are still being rendered by Nuke. maximumViews: int, the number of views supported by this flipbook, should be 1 or higher. fileTypes: list, the extensions of the file types supported by this format. Must all be lowercase, e.g ["exr", "jpg", ...]. A wildcard ["*"] can also be used to indicate support for any file type Nuke supports "roi: bool, whether the flipbook supports region-of-interest :return: dict with the capabilities above.
`dialogKnobChanged`  Called whenever this flipbook is selected and one of the knobs added in dialogKnobs was changed.
`dialogKnobs`  This is called when the user has selected this flipbook application, and will be interested in any knobs that you might have to show for custom settings.
`getExtraOptions`  Called whenever this flipbook is selected to retrieve extra options from the node selected to flipbook and the flipbook dialog.
`name`  Return the name of the flipbook.
`path`  Return the executable path required to run a flipbook.
`run`  Execute the flipbook on a path.
`runFromNode`  Execute the flipbook on a node.

cacheDir()

Return the preferred directory for rendering. :return: String
capabilities()

Return the capabilities of the flipbook application in a dict. Currently used are: canPreLaunch: bool, whether the flipbook can display a frames that are still being rendered by Nuke. maximumViews: int, the number of views supported by this flipbook, should be 1 or higher. fileTypes: list, the extensions of the file types supported by this format. Must all be lowercase, e.g [“exr”, “jpg”, …].
> A wildcard [“*”] can also be used to indicate support for any file type Nuke supports
“roi: bool, whether the flipbook supports region-of-interest :return: dict with the capabilities above.
dialogKnobChanged(_dialog_ , _knob_)

Called whenever this flipbook is selected and one of the knobs added in dialogKnobs was changed. :param dialog: The FlipbookDialog that contains the knob :param knob: The knob added in dialogKnobs that was modified. :return: None
dialogKnobs(_dialog_)

This is called when the user has selected this flipbook application, and will be interested in any knobs that you might have to show for custom settings. :param dialog: The FlipbookDialog that has requested the knobs to be added to it, e.g. dialog.addKnob(…) :return: None
getExtraOptions(_flipbookDialog_ , _nodeToFlipbook_)

Called whenever this flipbook is selected to retrieve extra options from the node selected to flipbook and the flipbook dialog. :param flipbookDialog: the flipbook dialog :param nodeToFlipbook: node selected to flipbook :return: a dictionary with the extra options
name()

Return the name of the flipbook. :return: String
path()

Return the executable path required to run a flipbook. :return: String
run(_path_ , _frameRanges_ , _views_ , _options_)

Execute the flipbook on a path. :param path: The path to run the flipbook on. This will be similar to /path/to/foo%03d.exr :param frameRanges: A FrameRanges object representing the range that should be flipbooked. Note that in 6.2v1-2 this was a FrameRange object. :param views: A list of strings comprising of the views to flipbook. Willnot be more than the maximum supported by the flipbook. :param options: A dictionary of options to use. This may contain the keys pixelAspect, roi, dimensions, audio and lut. These contain a float, a dict with bounding box dimensions, a dict with width and height, a path to audio file and a string indicating the LUT conversion to apply. :return: None
runFromNode(_nodeToFlipbook_ , _frameRanges_ , _views_ , _options_)

Execute the flipbook on a node. This method will use the node’s filename to call run() :param node: The node to run the flipbook :param frameRanges: A FrameRanges object representing the range that should be flipbooked. Note that in 6.2v1-2 this was a FrameRange object. :param views: A list of strings comprising of the views to flipbook. Willnot be more than the maximum supported by the flipbook. :param options: A dictionary of options to use. This may contain the keys pixelAspect, roi, dimensions, audio and lut. These contain a float, a dict with bounding box dimensions, a dict with width and height, a path to audio file and a string indicating the LUT conversion to apply. :return: None