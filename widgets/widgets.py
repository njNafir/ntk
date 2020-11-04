from tkinter import *
from tkinter import ttk
from dev_help.timepicker import TimePicker
from dev_help import global_var as gv

def get_a_checkbutton(frame, text="", variable=None, row=0, column=1, padx=(10, 10), pady=(10, 10), sticky="w", use_ttk=True, style=None):
	if use_ttk:
		check = ttk.Checkbutton(frame, text=text, variable=variable)
	else: check = Checkbutton(frame, text=text, variable=variable)

	check.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
	if style: check.config(style=style)

	return check

def get_a_progressbar(frame, variable, orient=HORIZONTAL, max=100, length=100, row=0, column=0, columnspan=1, padx=(0, 0), pady=(0, 0)):
	pbar = ttk.Progressbar(frame, orient=orient, max=max, length=length, variable=variable)
	pbar.grid(row = row, column = column, columnspan = columnspan, padx = padx, pady = pady)

	return pbar



# def show_clock(event, widget, u=0, d=0, r=0, l=0):
# 	if gv.timepicker: gv.timepicker.destroy()
#
# 	x, y, h = (widget.winfo_rootx() + (r if r!=0 else 0)) - (l if l!=0 else 0), (widget.winfo_rooty() - (u if u!=0 else 0)) + (d if d!=0 else 0), widget.winfo_height()
#
# 	window = TimePicker(x, y + h, widget)
# 	return window

import time
def ltte(t):
    with open('log.txt', 'a+') as lf:
        lf.write(time.strftime('%d-%m-%Y %H:%M:%S') + ' ' + t + '\n')
