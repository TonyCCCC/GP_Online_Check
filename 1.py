# coding=utf-8
import tkinter as tk

root = tk.Tk()

def center_window(w, h):
    # 获取屏幕 宽、高
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # 计算 x, y 位置
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

center_window(500, 500)

# 单击键盘
def key(event):
    print ("pressed", repr(event.char))

# 单击左键
def callback_1(event):
    #当前框架被选中，意思是键盘触发，只对这个框架有效
    frame.focus_set()
    print ("left clicked at : (window coordinate {}, {}), (screen coordinate {}, {}) ".format(event.x, event.y, event.x_root, event.y_root))

# 单击滚轮
def callback_2(event):
    #当前框架被选中，意思是键盘触发，只对这个框架有效
    frame.focus_set()
    print ("middle clicked at : (window coordinate {}, {}), (screen coordinate {}, {}) ".format(event.x, event.y, event.x_root, event.y_root))

# 单击右键
def callback_3(event):
    #当前框架被选中，意思是键盘触发，只对这个框架有效
    frame.focus_set()
    print ("right clicked at : (window coordinate {}, {}), (screen coordinate {}, {}) ".format(event.x, event.y, event.x_root, event.y_root))

frame = tk.Frame(root, width=500, height=500, bg='blue')
frame.bind("<Key>", key)
frame.bind("<Button-1>", callback_1)
frame.bind("<Button-2>", callback_2)
frame.bind("<Button-3>", callback_3)
frame.bind('<Control-q>', lambda event: frame.quit())
frame.pack()

root.mainloop()