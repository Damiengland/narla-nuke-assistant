# nuke.clone
nuke.clone(_n_ , _args_ , _inpanel_)

Create a clone node that behaves identical to the original. The node argument is the node to be cloned, args and inpanel are optional arguments similar to createNode. A cloned node shares the exact same properties with its original. Clones share the same set of knobs and the same control panel. However they can have different positions and connections in the render tree. Any clone, including the original, can be deleted at any time without harming any of its clones.
Parameters

  * **n** – Node.
  * **args** – Optional number of inputs requested.
  * **inpanel** – Optional boolean.
Returns

Node