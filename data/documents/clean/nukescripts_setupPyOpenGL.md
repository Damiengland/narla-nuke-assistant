# nukescripts.setupPyOpenGL
nukescripts.setupPyOpenGL()

Configure PyOpenGL for use with Nuke.
On most platforms this has no effect, however, on MacOS it is necessary to call this method before importing OpenGL.platform in order to ensure PyOpenGL uses FoundryGL rather than the system OpenGL libraries.