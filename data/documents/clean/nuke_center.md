# nuke.center
nuke.center()  array with x, then y

Return the center values of a group’s display, these values are suitable to be passed to nuke.zoom as the DAG center point. Like so:


    ```python
    center = nuke.center()
    zoom = nuke.zoom()
    print center[0]
    print center[1]
    ## move DAG back to center point without changing zoom.
    nuke.zoom( zoom, center )
    ```
Returns

Array of x, y.