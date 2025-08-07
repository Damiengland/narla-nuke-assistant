# nukescripts.renderdialog.bboxToTopLeft
nukescripts.renderdialog.bboxToTopLeft(_height_ , _roi_)

Convert the roi passed from a origin at the bottom left to the top left. Also replaces the r and t keys with w and h keys. :param height: the height used to determine the top. :param roi: the roi with a bottom left origin, must have x, y, r & t keys. @result dict with x, y, w & h keys