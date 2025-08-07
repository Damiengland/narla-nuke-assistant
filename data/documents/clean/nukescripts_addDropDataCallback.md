# nukescripts.addDropDataCallback
nukescripts.addDropDataCallback(_callback_)

Add a function to the list of callbacks. This function will called whenever data is dropped onto the DAG. Override it to perform other actions. If you handle the drop, return True, otherwise return None.