# nukescripts.pyWxAppUtils.pyWxAppHelper
_class _nukescripts.pyWxAppUtils.pyWxAppHelper(_wxApp_ , _start =None_)

Bases:
Helper class to initialise wxWidgets in a separate thread
constructor
Methods
`getApplication` ---
`initiate`  Start the thread associated with this object
`run`  Runs the specified call in a separate thread.
`start`
`terminate`  Terminated the thread associated with this object

initiate()

Start the thread associated with this object
run(_call_ , _args =()_, _kwargs ={}_)

Runs the specified call in a separate thread.
terminate()

Terminated the thread associated with this object