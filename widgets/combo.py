from tkinter.ttk import Combobox as ttkCombobox

class Combobox:
    def __init__(self, root, class_="TCombobox", cursor="arrow", exportselection=1, height=24, justify="left", postcommand="", style="TCombobox", takefocus=1, textvariable=False, validate=None, validatecommand=False, values=['More', 'Long', 'Values'], width=24, xscrollcommand=False, font=("Calibri", 10), row=0, column=0, padx=0, pady=0, ipady=2, sticky='w', text="-----", default=0, state="normal", *args, **kwargs):
        super(Combobox, self).__init__(*args, **kwargs)
        values = [text] + list(values)

        self.main = ttkCombobox(root, class_=class_, cursor=cursor, exportselection=exportselection, height=height, justify=justify, postcommand=postcommand, validate=validate, validatecommand=validatecommand, style=style, takefocus=takefocus, textvariable=textvariable, values=values, width=width, xscrollcommand=xscrollcommand, font=font)

        print(self.main['postcommand'])

        self.main.grid(row=row, column=column, padx=padx, pady=pady, ipady=ipady, sticky=sticky)
        self.main.set(values[default])
