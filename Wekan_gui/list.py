# liste
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et

from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import apiwekan 


# def selected_item():
#     for i in liste.curselection():
#         print(liste.get(i))
ws = tk.Tk()
tree = ttk.Treeview(ws)

def item_selected(event):
    for selected_item in tree.selection():
        print(tree)
        print(selected_item)
        item = tree.item(selected_item)
        record = item['values']
        showinfo(title='Information',
                message=','.join(record))



def treeview_boards(ws, tree):
    ws.title('PythonGuides')
    ws.geometry('620x200')
    ws['bg']='#fb0'

    tree['columns']=('Rank', 'Name')
    # # add a scrollbar  

    tree.column('#0', width=0, stretch=NO)
    tree.column('Rank', anchor=CENTER, width=80)
    tree.column('Name', anchor=CENTER, width=80)
    # tv.column('Badge', anchor=CENTER, width=80)
    # tree = ttk.Treeview(ws, columns=columns, show='headings')
    tree.heading('#0', text='', anchor=CENTER)
    tree.heading('Rank', text='Id', anchor=CENTER)
    tree.heading('Name', text='rank', anchor=CENTER)
    tree.bind('<<TreeviewSelect>>', item_selected)
    tree.grid(row=0, column=0, sticky='nsew')
    data = []
    # dict = [{"_id":"PAcCMBTujxvYPqAR4","title":"toto"}
    #         ,{"_id":"KEGYfNxSRDJ84eP6a","title":"tata"}
    #         ,{"_id":"t5yce6vh6tKP7kAzc","title":"titi"}
    #         ,{"_id":"vTd3gNRRZkLtRJ7J9","title":"tata"}
    #     ]
    apiwekan.boards()
    # print(data2)

    for key in dict:
        # print(key)
        it = iter(key.values())    
        idboard, name = next(it), next(it)   
        name = name
        idboard = idboard
        print(idboard)
        print(name)
        data.append((f' {idboard}', f'{name}', f'{name}'))  

    print(data)
    for i in data:
        tree.insert('', tk.END, values=i)

    scrollbar = ttk.Scrollbar(ws, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    tree.pack()
    ws.mainloop()



# run the app
treeview_boards(ws, tree)

