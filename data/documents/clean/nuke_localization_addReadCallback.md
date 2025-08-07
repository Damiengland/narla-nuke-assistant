# nuke.localization.addReadCallback
nuke.localization.addReadCallback(_callback_)  None

Adds a callback for read localization events.
Parameters

**callback** – is a python callable object with arguments for Read and status.
See also
nuke.localization.ReadStatus
Usage Example:


    ```python
    1def myCallback( read, event ):
    2    if event == nuke.localization.ReadStatus.LOCALIZED:
    3        print(\read : \ + read.name() + \ localized\)
    4    elif event == nuke.localization.ReadStatus.OUT_OF_DATE:
    5        print(\file : \ + read.name() + \ is out of date\)
    6
    7nuke.localization.addReadCallback( myCallback )\n
    8# do some localization and process callbacks, when finished call:
    9nuke.localization.removeReadCallback( myCallback )
    ```