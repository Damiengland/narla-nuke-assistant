# nuke.ofxAddPluginAliasExclusion
nuke.ofxAddPluginAliasExclusion(_fullOfxEffectName_)  None

Adds the ofx effect name to a list of exclusions that will not get tcl aliases automatically created for them.
For example, if there is an ofx plugin with a fully qualified name of: ‘OFXuk.co.thefoundry.noisetools.denoise_v100’.
Nuke by default would automatically alias that so that nuke.createNode(‘Denoise’) will create that node type.
By calling nuke.ofxAddPluginAliasExclusion(‘OFXuk.co.thefoundry.noisetools.denoise_v100’), you’d be changing that such that the only way to create a node of that type would be to call nuke.createNode(‘OFXuk.co.thefoundry.noisetools.denoise_v100’) This does not change saving or loading of Nuke scripts with that plugin used in any way.
Parameters

**fullOfxEffectName** – The fully qualified name of the ofx plugin to add to the exclusion list.
Returns

None.