[ Nuke Python API Reference ![Logo](_static/NukeApp128.png) ](index.html)

16.0 

  * [Introduction](intro.html)
  * [Start-up Scripts](startup.html)
  * [Getting Started](basics.html)
  * [Nuke as a Python Module](nuke_as_python_module.html)
  * [Animation](animation.html)
  * [Using the Command-line](command_line.html)
  * [Callbacks](callbacks.html)
  * [Stereo](stereo.html)
  * [3D](3D.html)
  * [Roto and RotoPaint](rotopaint.html)
  * [Accessing Image Data](image_data.html)
  * [Custom Panels](custom_panels.html)
  * [Extending NUKE with PySide](custom_panels.html#extending-nuke-with-pyside)
  * [Customizing the UI](custom_ui.html)
  * Custom Flipbooks
    * Using Tweak Software’s RV as the Default Flipbook Application
  * [Metadata](metadata.html)
  * [Working with Channels and Layers](channels.html)
  * [Manipulating the Node Graph](dag.html)
  * [Formats](formats.html)
  * [Math](math.html)
  * [Asset Management Systems / Pipeline Integration](asset.html)
  * [OpenAssetIO Integration](openassetio.html)
  * [Graph Scope Variables / Multi-shot Set-up](gsv.html)
  * [Threading](threading.html)
  * [Render Farm Integration (Concept)](render_farm.html)
  * [Performance Profiling](performance.html)
  * [Installing Plug-ins](installing_plugins.html)
  * [Sample Scripts](samples.html)



API Reference

  * [nuke](_autosummary/nuke.html)
  * [nuke.curveknob](_autosummary/nuke.curveknob.html)
  * [nuke.curvelib](_autosummary/nuke.curvelib.html)
  * [nuke.gsv](_autosummary/nuke.gsv.html)
  * [nuke.localization](_autosummary/nuke.localization.html)
  * [nuke.memory2](_autosummary/nuke.memory2.html)
  * [nuke.nukemath](_autosummary/nuke.nukemath.html)
  * [nuke.rotopaint](_autosummary/nuke.rotopaint.html)
  * [nuke.splinewarp](_autosummary/nuke.splinewarp.html)
  * [nukescripts](_autosummary/nukescripts.html)



__[Nuke Python API Reference](index.html)

  * [](index.html) »
  * Custom Flipbooks
  * 


* * *

# Custom Flipbooks

This chapter describes how to customise and extend NUKE’s flipbook workflow.

## Using Tweak Software’s RV as the Default Flipbook Application
    
    
    ```python
    # Copyright (c) 2010 The Foundry Visionmongers Ltd.  All Rights Reserved.
    import nuke
    import nukescripts
    import nukescripts.flipbooking as flipbooking
    import os
    
    class RVFlipbook(flipbooking.FlipbookApplication):
      """ This is an example implementation of how to deal with implementing a
          flipbook application other than NUKE's Player for NUKE. This script
          needs to be modified in several places before it can work, so please
          read all of the notes marked with TODO and modify them where
          necessary."""
      def __init__(self):
        # TODO: Please put your own path in here or add RV path discovery.
        self._rvPath = "/Applications/RV64.app/Contents/MacOS/RV64"
    
      def name(self):
        return "RV"
    
      def path(self):
        return self._rvPath
    
      def cacheDir(self):
        return os.environ["NUKE_TEMP_DIR"]
    
      def run(self, filename, frameRanges, views, options):
        # TODO: You probably want more involved handling of frame ranges!
        sequence_interval = str(frameRanges.minFrame())+"-"+str(frameRanges.maxFrame())
        for frame in range(frameRanges.minFrame(), frameRanges.maxFrame()):
          if frame not in frameRanges.toFrameList():
            print("This example only supports complete frame ranges.")
            return
    
        os.path.normpath(filename)
    
        args = []
        if nuke.env['WIN32']:
          args.append( "\"" + self.path() + "\"" )
          filename = filename.replace("/", "\\")
          filename = "\"" + filename + "\""
        else:
          args.append( self.path() )
    
    
        roi = options.get("roi")
        if roi and any(roi[i] for i in ('xywh')):
          args.append("-c " + str(int(roi["x"])))
          for i in ('ywh'):
            args.append(str(int(roi[i])))
    
        lut = options.get("lut", "")
        if lut == "linear-sRGB":
          args.append("-sRGB")
        elif lut == "linear-rec709":
          args.append('-rec709')
    
        args.append(filename)
        args.append(sequence_interval)
    
        # print(args)
        os.spawnv(os.P_NOWAITO, self.path(), args)
    
      def capabilities(self):
        return {
          'proxyScale': False,
          'crop': True,
          'canPreLaunch': False,
          'supportsArbitraryChannels': True,
          'maximumViews' : 2,
          # TODO: This list is compiled from running rv with the following:
          # RV64 -formats | grep 'format "' | awk '{print $2}' | tr '[:space:]' ','; echo
          # This may differ for your platform!
          'fileTypes' : ["j2k","jpt","jp2","dpx","cin","cineon","jpeg","jpg","rla","rpf","yuv","exr","openexr","sxr","tif","tiff","sm","tex","tx","tdl","shd","targa","tga","tpic","rgbe","hdr","iff","png","z","zfile","sgi","bw","rgb","rgba","*mraysubfile*","movieproc","stdinfb","aiff","aif","aifc","wav","snd","au","mov","avi","mp4","m4v","dv"]
    
        }
    
    flipbooking.register( RVFlipbook() )
    nukescripts.setFlipbookDefaultOption("flipbook", "RV")
    ```

[ Previous](custom_ui.html "Customizing the UI") [Next ](metadata.html "Metadata")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
