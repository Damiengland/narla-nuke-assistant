# nuke.Undo
_class _nuke.Undo

Bases: `object`
Methods
`begin`  Begin a new user-visible group of undo actions.---
`cancel`  Undoes any actions recorded in the current set and throws it away.
`disable`  Prevent recording undos until matching enable()
`disabled`  True if disable() has been called
`enable`  Undoes the previous disable()
`end`  Complete current undo set and add it to the undo list.
`name`  Name current undo set.
`new`  Same as end();begin().
`redo`  Redoes 0'th redo.
`redoDescribe`  Return short description of redo n.
`redoDescribeFully`  Return long description of redo n.
`redoSize`  Number of redo's that can be done.
`redoTruncate`  Destroy any redo's greater or equal to n.
`undo`  Undoes 0'th undo.
`undoDescribe`  Return short description of undo n.
`undoDescribeFully`  Return long description of undo n.
`undoSize`  Number of undo's that can be done.
`undoTruncate`  Destroy any undo's greater or equal to n.

begin()

Begin a new user-visible group of undo actions.
cancel()

Undoes any actions recorded in the current set and throws it away.
disable()

Prevent recording undos until matching enable()
disabled()

True if disable() has been called
enable()

Undoes the previous disable()
end()

Complete current undo set and add it to the undo list.
name()

Name current undo set.
new()

Same as end();begin().
redo()

Redoes 0’th redo.
redoDescribe()

Return short description of redo n.
redoDescribeFully()

Return long description of redo n.
redoSize()

Number of redo’s that can be done.
redoTruncate()

Destroy any redo’s greater or equal to n.
undo()

Undoes 0’th undo.
undoDescribe()

Return short description of undo n.
undoDescribeFully()

Return long description of undo n.
undoSize()

Number of undo’s that can be done.
undoTruncate()

Destroy any undo’s greater or equal to n.