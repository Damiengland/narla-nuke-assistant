# nukescripts.scripteditorknob.StringIO
_class _nukescripts.scripteditorknob.StringIO(_initial_value =''_, _newline ='\n'_)

Bases: `_io._TextIOBase`
Text I/O implementation using an in-memory buffer.
The initial_value argument sets the value of object. The newline argument is like the one of TextIOWrapper’s constructor.
Methods
`close`  Close the IO object.---
`detach`  Separate the underlying buffer from the TextIOBase and return it.
`fileno`  Returns underlying file descriptor if one exists.
`flush`  Flush write buffers, if applicable.
`getvalue`  Retrieve the entire contents of the object.
`isatty`  Return whether this is an 'interactive' stream.
`read`  Read at most size characters, returned as a string.
`readable`  Returns True if the IO object can be read.
`readline`  Read until newline or EOF.
`readlines`  Return a list of lines from the stream.
`seek`  Change stream position.
`seekable`  Returns True if the IO object can be seeked.
`tell`  Tell the current file position.
`truncate`  Truncate size to pos.
`writable`  Returns True if the IO object can be written.
`write`  Write string to file.
`writelines`  Write a list of lines to stream.

Attributes
`closed` ---
`encoding`  Encoding of the text stream.
`errors`  The error setting of the decoder or encoder.
`line_buffering`
`newlines`

close()

Close the IO object.
Attempting any further operation after the object is closed will raise a ValueError.
This method has no effect if the file is already closed.
detach()

Separate the underlying buffer from the TextIOBase and return it.
After the underlying buffer has been detached, the TextIO is in an unusable state.
encoding

Encoding of the text stream.
Subclasses should override.
errors

The error setting of the decoder or encoder.
Subclasses should override.
fileno()

Returns underlying file descriptor if one exists.
OSError is raised if the IO object does not use a file descriptor.
flush()

Flush write buffers, if applicable.
This is not implemented for read-only and non-blocking streams.
getvalue()

Retrieve the entire contents of the object.
isatty()

Return whether this is an ‘interactive’ stream.
Return False if it can’t be determined.
newlines

read(_size =- 1_, _/_)

Read at most size characters, returned as a string.
If the argument is negative or omitted, read until EOF is reached. Return an empty string at EOF.
readable()

Returns True if the IO object can be read.
readline(_size =- 1_, _/_)

Read until newline or EOF.
Returns an empty string if EOF is hit immediately.
readlines(_hint =- 1_, _/_)

Return a list of lines from the stream.
hint can be specified to control the number of lines read: no more lines will be read if the total size (in bytes/characters) of all lines so far exceeds hint.
seek(_pos_ , _whence =0_, _/_)

Change stream position.
Seek to character offset pos relative to position indicated by whence:

0 Start of stream (the default). pos should be >= 0; 1 Current position - pos must be 0; 2 End of stream - pos must be 0.
Returns the new absolute position.
seekable()

Returns True if the IO object can be seeked.
tell()

Tell the current file position.
truncate(_pos =None_, _/_)

Truncate size to pos.
The pos argument defaults to the current file position, as returned by tell(). The current file position is unchanged. Returns the new absolute position.
writable()

Returns True if the IO object can be written.
write(_s_ , _/_)

Write string to file.
Returns the number of characters written, which is always equal to the length of the string.
writelines(_lines_ , _/_)

Write a list of lines to stream.
Line separators are not added, so it is usual for each of the lines provided to have a line separator at the end.