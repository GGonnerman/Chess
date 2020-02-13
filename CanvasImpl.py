from Tkinter import Canvas


class CanvasImpl(Canvas):
	def create_centered_rectangle(self, x0, y0, x1, y1, rectangle_width, rectangle_height, **kw):
		if rectangle_width > abs(x0 - x1) or rectangle_height > abs(y0 - y1): return
		spare_x = (abs(x0 - x1) - rectangle_width) / 2
		spare_y = (abs(y0 - y1) - rectangle_height) / 2
		return super(CanvasImpl, self).create_rectangle(x0 + spare_x, y0 + spare_y, x1 - spare_x, y1 - spare_y, **kw)

	def create_centered_circle(self, x0, y0, x1, y1, diameter, **kw):
		return self.create_centered_oval(x0, y0, x1, y1, diameter, diameter, **kw)

	def create_centered_oval(self, x0, y0, x1, y1, oval_width, oval_height, **kw):
		if oval_width > abs(x0 - x1) or oval_height > abs(y0 - y1): return
		spare_x = (abs(x0 - x1) - oval_width) / 2
		spare_y = (abs(y0 - y1) - oval_height) / 2
		return super(CanvasImpl, self).create_oval(x0 + spare_x, y0 + spare_y, x1 - spare_x, y1 - spare_y, **kw)
