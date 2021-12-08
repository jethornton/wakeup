#!/usr/bin/env python3

from tkinter import *
from astral import Location


class MyApp(Tk):
	def __init__(self):
		Tk.__init__(self)
		fr = Frame(self)
		fr.pack()
		self.canvas  = Canvas(fr, height = 200, width = 300)
		self.canvas.pack()
		self.rect = self.canvas.create_rectangle(100, 25, 150, 75, fill = "white")
		self.do_blink = False
		start_button = Button(self, text="start blinking", command=self.start_blinking)
		stop_button = Button(self, text="stop blinking", command=self.stop_blinking)
		start_button.pack()
		stop_button.pack()
		self.location = Location()
		self.location.name = 'Poplar Bluff'
		self.location.region = 'Missouri'
		self.location.latitude = 36.873543
		self.location.longitude = -90.488055
		self.location.timezone = 'US/Central'
		self.location.elevation = 110

	def start_blinking(self):
		self.do_blink = True
		self.blink()

	def stop_blinking(self):
		self.do_blink = False

	def blink(self):
		if self.do_blink:
			current_color = self.canvas.itemcget(self.rect, "fill")
			new_color = "red" if current_color == "white" else "white"
			self.canvas.itemconfigure(self.rect, fill=new_color)
			self.after(1000, self.blink)


if __name__ == "__main__":
	root = MyApp()
	root.mainloop()
