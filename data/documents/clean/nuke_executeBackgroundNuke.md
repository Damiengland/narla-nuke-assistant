# nuke.executeBackgroundNuke
nuke.executeBackgroundNuke(_exe_path_ , _nodes_ , _frameRange_ , _views_ , _limits_ , _continueOnError = False_, _flipbookToRun = "_, _flipbookOptions = {}_)  None

Run an instance of Nuke as a monitored sub process. Returns an integer that’s used as unique id for the started task. If it failed to launch this will be -1.
Param

exe_path: Path to Nuke or a script that can take Nuke arguments. You probably want to supply nuke.EXE_PATH.
Param

nodes: A list of nodes to execute.
Param

frameRanges: List of frame ranges to execute.
Param

views: A list of view names to execute.
Param

limits: A dictionary with system limits, currently uses keys maxThreads and maxCache.
Param

flipbookToRun: The name of the flipbook application to run after the render, or an empty string if not desired.
Param

flipbookOptions: A dictionary with options to pass to the flipbook. These should include roi and pixelAspect.
Returns

Int.