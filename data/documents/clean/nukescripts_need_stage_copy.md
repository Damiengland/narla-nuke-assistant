# nukescripts.need_stage_copy
nukescripts.need_stage_copy(_frame_range_ , _task =None_)

This method will either return true if a copy of the stage is needed, false otherwise. Currently, updating the task progress can cause recomposition of the stage from the viewer if changes have been made. We need a copy of the stage to ensure this wont change during the calculation.