from tkinter.ttk import Radiobutton as ttkRadio

def get_a_radio(frame, text="Radio", variable=None, value=None, row=0, column=0, padx=(10, 10), pady=(10, 10), sticky='w'):
	radio = ttk.Radiobutton(frame, text=text, variable=variable)
	radio.grid(row=row, column=column, padx=padx, pady=pady, sticky=sticky)
	if value is not None: radio.config(value=value)

	return radio
