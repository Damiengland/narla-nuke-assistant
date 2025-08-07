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
  * [Custom Flipbooks](flipbook.html)
  * [Metadata](metadata.html)
  * [Working with Channels and Layers](channels.html)
  * [Manipulating the Node Graph](dag.html)
  * [Formats](formats.html)
  * [Math](math.html)
  * [Asset Management Systems / Pipeline Integration](asset.html)
  * OpenAssetIO Integration
    * File Knob evaluation
    * Deassetization
    * Performance
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
  * OpenAssetIO Integration
  * 


* * *

# OpenAssetIO Integration

Nuke currently has a basic OpenAssetIO integration. Nuke acts as an OpenAssetIO host application talking to an OpenAssetIO manager.

This also means that we have exposed some experimental Python APIs to evaluate the current state. In order to connect Nuke to your asset management system using OpenAssetIO, you will need a suitable Manager Plugin. These are described in more detail in the OpenAssetIO documentation.

We currently support File Paths, Frame Range, Original Range and Colorspace properties in the following ingest nodes: Read, ReadGeo, GeoImport, DeepRead, OCIOFileTransform, OCIOCDLTransform and Precomp.

Nuke 16.0v1 is shipped with the following libraries:
    

  * OpenAssetIO-v1.0.0-rc.1.0

  * OpenAssetIO-MediaCreation-v1.0.0-alpha.10



|   
---|---  
Supported Nodes | Read, ReadGeo, GeoImport, DeepRead, OCIOFileTransform, OCIOCDLTransform and Precomp.  
Parameters | File Paths, Frame Range, Original Range and Colorspace  
Libraries | OpenAssetIO-v1.0.0-rc.1.0, OpenAssetIO-MediaCreation-v1.0.0-alpha.10  
  
Warning

Please note that the Python API is not frozen just yet as we might need to adjust it based on feedback! In order to have access to any of the functionality, one needs to import the corresponding python module. This would be:
    
    
    ```python
    import _asset
    ```

The module name currently starts with an underscore to follow the Python ecosystem advice on marking APIs private to indicate that they should not be relied on. They are not private in the strict sense, but it is just an indication from us that the API may change at this point until finally stabilised.

OpenAssetIO can be set up in different ways. One can use the `OPENASSETIO_DEFAULT_CONFIG` environment variable to point to a valid toml configuration file, for example:
    
    
    ```python
    export OPENASSETIO_DEFAULT_CONFIG=~/.nuke/asset_manager_config.toml
    ```

Or on Windows with PowerShell:
    
    
    ```python
    $Env:OPENASSETIO_DEFAULT_CONFIG = '$Env:USERPROFILE\.nuke\asset_manager_config.toml'
    ```

Then, Nuke will initialise the OpenAssetIO manager during its startup sequence. One can also enable OpenAssetIO after Nuke has launched, using the following API:
    
    
    ```python
    _asset.setupManager(config_path)
    ```

It is also possible to “disable” OpenAssetIO by clearing the OpenAssetIO manager used in Nuke with the following code:
    
    
    ```python
    _asset.clearManager()
    ```

It is also possible to retrieve access to the asset manager that was set up in Nuke by running the following code:
    
    
    ```python
    _asset.getManager()
    ```

This can be used then to resolve assets and obtain information such as their file locations utilising the locatable content trait from OpenAssetIO-MediaCreation:
    
    
    ```python
    import _asset
    from openassetio_mediacreation.traits.content import LocatableContentTrait
    
    manager = _asset.getManager()
    entity_reference = manager.createEntityReference('MyAssets:///valid/uri/to/asset’)
    context = _asset.getContext()
    resolved_asset = manager.resolve(
            entity_reference, {LocatableContentTrait.kId}, context)
    LocatableContentTrait(resolved_asset).getLocation()
    ```

## File Knob evaluation

This is the order of evaluation for the Read node’s file knob:

>   1. GSV expression evaluation (e.g. `MyAssets:///things/%{asset_gsv}.0`)
> 
>   2. TCL expression evaluation (e.g. `MyAssets:///[value show]/asset.0`)
> 
>   3. OpenAssetIO resolution (e.g. `MyAssets:///things/asset.0`)
> 
>      1. If the result of the TCL expression is an entity reference recognised by the configured asset manager, Nuke will resolve it and retrieve its OpenAssetIO-MediaCreation LocatableContentTrait. properties.
> 
>      2. If the location property holds a file scheme URL (e.g. `file:///mnt/things/asset/0/frame_%23%23%23%23.exr`) then it will be decoded to extract the file path (e.g. `/mnt/things/asset/0/frame_####.exr`)
> 
>   4. File path variables are then expanded (e.g. `####`, `%4d`, `%V`, etc)
> 
> 


The location retrieved from the OpenAssetIO manager is a URL but only the `file` URI schema is supported, so Nuke is decoding it so that the file knob can consume it as a standard file path.

At the moment we support File Paths, Frame Range, Original Range and Colorspace properties in the next nodes: Read, ReadGeo, GeoImport, DeepRead, OCIOFileTransform, OCIOCDLTransform and Precomp

The OpenAssetIO resolved content location can contain frame and view tokens which will be substituted as normal by Nuke in image and sequence paths, as well as stereoscopic views. Please note that the frame range knobs must be set explicitly.

One can execute the following code to get the resolved location from a file knob based on an entity reference input:
    
    
    ```python
    read_node['file'].getEvaluatedValue()
    ```

The unresolved input can also be retrieved as usual via:
    
    
    ```python
    read_node['file'].getValue()
    ```

## Deassetization

One can also deassetize a nuke script so that it can be sent to a render farm for rendering. This would replace each entity reference in the nuke script with its resolved location. The code would look something like this:
    
    
    ```python
    nuke.deassetize(nukescripts.allNodes(recurseGroups=True))
    ```

## Performance

By its very nature, communication with an external data management system introduces additional overhead when evaluating the Nuke graph. Depending on the implementation of the specific Manager Plugin in use, this may impact the overall performance of the application. Optimization of entity reference resolution and data retrieval through OpenAssetIO is the subject of future work. We are looking forward to hearing your feedback if this happens with your implementation as we aim to reduce overhead wherever possible as part of maturing this feature to production-ready status.

[ Previous](asset.html "Asset Management Systems / Pipeline Integration") [Next ](gsv.html "Graph Scope Variables / Multi-shot Set-up")

* * *

© Copyright 2025, The Foundry. Python API Reference for Nuke 16.0v4. Last updated on Jun 03, 2025. 
