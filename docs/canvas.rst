========
Canvas
========

ntk will solve your problem when you can't learn and implement,
python tkinter to create desktop application in concern to
good looking and os level implementation.

Canvas is highly customizable and most usedful widget for drawing anything

ntk Canvas is extended version of tkinter base Canvas with more functionality and responsive grid system, to use
this Canvas window we need to import first it from ntk by

    from ntk import Canvas

and initialize it by calling it

    window = Canvas(root)

This will create wrapper and basic style will be applied, you need to pass parameters described 
below to get your desired window size and style

available parameters are:

* root, # root is a master window to place this button into it
* bg="bg-white", # background color
* highlightbackground="bg-white", # background color when canvas is highlighted
* highlightcolor="fg-dark", # foreground color when canvas is highlighted
* selectbackground="bg-primary", # element background color when canvas element is selected
* scrollregion=[0,0,350,96], # [x1, y1, x2, y2] region when canvas is scrolling via scrollbar or mouse
* relief="flat", # relief design can be flat, groove etc
* width=350, # canvas width
* height=96, # canvas height
* row=0, # row position
* column=0, # column position
* rowspan=1, # row spanning size
* columnspan=1, # column spanning size
* padx=1, # padding in left and right
* pady=1, # padding in top and bottom
* mousescroll=True, # set False if you don't want to scrolling when scrolling via mouse
* gridcolumn=1, # set 0 if you don't want responsiveness by column in it's root window
* gridrow=1, # set 0 if you don't want responsiveness by row in it's root window

an example of creating Canvas widget:


    from ntk import Tk, Canvas

    root = Tk(title='Example of ntk window')

    canvas = Canvas(root)

    root.mainloop()

canvas widget have some other custom method to get extra power

select_clicked is one of method which can be used for selecting clicked item from canvas widget
for doing this, we can call it in anywhere, using callback or event binding

    canvas.select_clicked()

mousewheel method is used by canvas itself, to scroll on canvas height when scrolling by mouse

increase_scrollragion is can be used to increase canvas scrollable area, it take's four parameters

    x1=False, # area start left position

    y1=False, # area start top position

    x2=False, # area start right position

    y2=False # area start bottom position

decrease_scrollragion is can be used to decrease canvas scrollable area, it take's four parameters

    x1=False, # area start left position

    y1=False, # area start top position

    x2=False, # area start right position

    y2=False # area start bottom position

you can pass extra arguments and keyword arguments, and those will be passed
to tkinter Canvas class.