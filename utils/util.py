from ntk.objects import gv

def bg_colors():
    return {
        "bg-primary": "#007BFF",
        "bg-secondary": "#6C757D",
        "bg-success": "#28A745",
        "bg-danger": "#DC3545",
        "bg-warning": "#FFC107",
        "bg-info": "#17A2B8",
        "bg-light": "#F8F9FA",
        "bg-dark": "#343A40",
        "bg-white": "#FFFFFF"
    }

def fg_colors():
    return {
        "fg-primary": "#007BFF",
        "fg-secondary": "#6C757D",
        "fg-success": "#28A745",
        "fg-danger": "#DC3545",
        "fg-warning": "#FFC107",
        "fg-info": "#17A2B8",
        "fg-light": "#F8F9FA",
        "fg-dark": "#343A40",
        "fg-white": "#FFFFFF"
    }

def color(name):
    if name in bg_colors():
        return bg_colors()[name]
    elif name in fg_colors():
        return fg_colors()[name]
    else: return name

def delete_child(master, exclude=False, just=False):
    children = master.children
    if exclude:
        children = dict((k, v) for k,v in children.items() if not k.startswith("!%s" %exclude.lower()))
    if just:
        children = dict((k, v) for k,v in children.items() if k.startswith("!%s" %just.lower()))

    for k, child in children.items():
        child.destroy()

def w(w=0.1):
    return int(w*gv.wpc)

def h(h=0.1):
    return int(h*gv.hpc)

gv.w    = w
gv.h    = h
