
# -*- coding:utf-8 -*-

from Tkinter import *


root = Tk()
v = StringVar()
def printValue(event):
    print listbox.get(listbox.curselection())


#listbox = Listbox(root)
#listbox = Listbox(root, selectmode = MULTIPLE)
listbox = Listbox(root, selectmode=EXTENDED, listvariable=v)
for item in ['linux', 'unix', 'windows']:
    listbox.insert(END, item)

listbox.insert(0, ['a', 'b', 'v'])
listbox.insert(END, '1', '2', '3')

print listbox.size()  # 输出item数量
listbox.delete(3, 5)
print listbox.size()

print listbox.get(0, 1)  # 打印1，2item的值

listbox.selection_set(2, 3)  # 选择3，4item
print listbox.curselection()  # 获取当前索引

print listbox.selection_includes(0)  # 判断是否选中1 item
print listbox.selection_includes(2)

print v.get()
v.set((777, 3412, 678, 1234))

listbox.bind('<Double-Button-1>', printValue)

listbox.pack()

root.mainloop()
