# Render Farm Integration (Concept)
Every render manager works in a different manner and facilities’ requirements for their pipeline integration vary, so here is a very brief example describing the basic concept of integrating a render manager.
Tip
You can find more information on this on (look for “Render Manager”).
Here is a simple panel example for collecting information that might be relevant to a render farm submission:


    ```python
    p = nuke.Panel( 'submit to farm' )

    p.addSingleLineInput( 'first', nuke.root().firstFrame() )
    p.addSingleLineInput( 'last', nuke.root().lastFrame() )

    p.addEnumerationPulldown( 'threads', '1 2 4 8' )
    p.addSingleLineInput( 'batch size', '10' )
    p.addBooleanCheckBox( 'local render', 0 )

    p.show()
    ```
You could then collect the user input in variables and build the required command for the submission. This snippet just generates pseudo code, which could be tweaked to create a valid submission command:


    ```python
    if p.show():
        args = dict( first = p.value('first'),
            last = p.value('last'),
            threads = p.value('threads'),
            batchSize = p.value('batch size'),
            local = p.value('local'))

        application = 'echo'
        #args = [ application, first, last, threads, batchSize, local ]
        cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args

        subprocess.Popen( cmdString.split() )
    ```
The above could then be wrapped into a function and placed in NUKE’s Render menu:


    ```python
    def submitToFarm():
        p = nuke.Panel( 'submit to farm' )

        p.addSingleLineInput( 'first', nuke.root().firstFrame() )
        p.addSingleLineInput( 'last', nuke.root().lastFrame() )

        p.addEnumerationPulldown( 'threads', '1 2 4 8' )
        p.addSingleLineInput( 'batch size', '10' )
        p.addBooleanCheckBox( 'local render', 0 )

        if p.show():
            args = dict( first = p.value('first'),
                last = p.value('last'),
                threads = p.value('threads'),
                batchSize = p.value('batch size'),
                local = p.value('local'))

            application = 'echo'
            #args = [ application, first, last, threads, batchSize, local ]
            cmdString = application + ' -range %(first)s-%(last)s -threads %(threads)s -batch %(batchSize)s' % args

            subprocess.Popen( cmdString.split() )

    nuke.menu( 'Nuke' ).addCommand( 'Render/Send to Farm', submitToFarm )
    ```
You can use to create more complex panels and non-modal panels that can be docked to the UI and saved with layouts. You could also add custom knobs to the Write nodes to launch a network render. See for details on this.