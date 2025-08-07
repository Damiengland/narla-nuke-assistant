# nuke.addBeforeBackgroundRender
nuke.addBeforeBackgroundRender(_call_ , _args =()_, _kwargs ={}_)

Add code to execute before starting any background renders. The call must be in the form of: def foo(context):
> pass
The context object that will be passed in is a dictionary containing the following elements: id => The identifier for the task that’s about to begin
Please be aware that the current Nuke context will not make sense in the callback (e.g. nuke.thisNode will return a random node).