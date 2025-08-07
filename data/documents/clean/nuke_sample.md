# nuke.sample
nuke.sample(_n_ , _c_ , _x_ , _y_ , _dx_ , _dy_)  float.

Get pixel values from an image. Deprecated, use Node.sample instead.
This requires the image to be calculated, so performance may be very bad if this is placed into an expression in a control panel. Produces a cubic filtered result. Any sizes less than 1, including 0, produce the same filtered result, this is correct based on sampling theory. Note that integers are at the corners of pixels, to center on a pixel add .5 to both coordinates. If the optional dx,dy are not given then the exact value of the square pixel that x,y lands in is returned. This is also called ‘impulse filtering’.
Parameters

  * **n** – Node.
  * **c** – Channel name.
  * **x** – Centre of the area to sample (X coordinate).
  * **y** – Centre of the area to sample (Y coordinate).
  * **dx** – Optional size of the area to sample (X coordinate).
  * **dy** – Optional size of the area to sample (Y coordinate).
Returns

Floating point value.