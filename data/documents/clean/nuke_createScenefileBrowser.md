# nuke.createScenefileBrowser
nuke.createScenefileBrowser(_fileName_ , _nodeName_)  None

Pops up a scene browser dialog box. Receives the path to an Alembic (abc) or Universal Scene Description (usd/usda/usdc/usdz) file, and displays a hierarchical tree of the nodes within the file. The user can select which nodes they are interested in, and nodes of the appropriate type will automatically. be created. If a valid scene file nodeName is specified, this node will be populated with the selected tree.
Parameters

  * **fileName** – Path and filename for an alembic or usd/usda/usdc/usdz file.
  * **nodeName** – name of a valid scene file node to populate. If the node is invalid, new nodes will be automatically created