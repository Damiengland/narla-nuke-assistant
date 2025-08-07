# nukescripts.FlipbookFactory
_class _nukescripts.FlipbookFactory

Bases: `object`
Methods
`getApplication`  Returns the flipbook app implementation with the given name, raises an exception if none could be found.---
`getNames`  Returns a list of the names of all available flipbook apps.
`isRegistered`  Return whether a flipbook app with that name has already been registered.
`register`  Register a flipbook app.

getApplication(_name_)

Returns the flipbook app implementation with the given name, raises an exception if none could be found. :param name: The name of a flipbook that was registered. :return: FlipBookApplication
getNames()

Returns a list of the names of all available flipbook apps. :return: list
isRegistered(_flipbook_)

Return whether a flipbook app with that name has already been registered. :param flipbook: FlipBookApplication object that’s tested for. :return: bool
register(_flipbookApplication_)

Register a flipbook app. It will fail if the flipbook app name isn’t unique. :param flipbook: FlipBookApplication object to register :return: None