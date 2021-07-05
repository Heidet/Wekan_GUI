#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et

from tkinter import *
from functools import partial
from tkinter import ttk
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json


class GetBoard: 
	def __init__(self,boardid):
		self.tk = tk.Tk()
		self.tree = ttk.Treeview(self.tk)

	def view_board(self):   
		# tk = tk.Tk() 
		# tree = ttk.Treeview(tk)
			
		# tk = Tk() 
		# tree = ttk.Treeview(tk)
		self.tk.title('Liste Dashboards')
		self.tk.geometry('300x250')
		self.tk['bg']='#2980b9'

		self.tree['columns']=('Rank', 'Name')

		self.tree.column('#0', width=0) 
		self.tree.column('Rank', anchor=CENTER, width=120)
		self.tree.column('Name', anchor=CENTER, width=120)
		self.tree.heading('#0', text='', anchor=CENTER)
		self.tree.heading('Rank', text='Id Dashboard', anchor=CENTER)
		self.tree.heading('Name', text='Nom Dashboard', anchor=CENTER)
		# tree.bind('<<TreeviewSelect>>')
		self.tree.grid(row=0, column=0, sticky='nsew')

		data = []
		print(data)
		# root = rootmain.get_list_card()
		api = get_cardslists(api)  
		# get_cardt = model.get_cardslists(api)  
		# print(get_cardt)
		# for cardslist in get_cardslists():
		# 	print(cardslist)
            # pprint += "\n{}".format(cardslist.pprint(indent + 1))
        # return pprint
		# for cardslist in self.get_cardslists():
        #     pprint += "\n{}".format(cardslist.pprint(indent + 1))
        # return pprint

		# #Call jsondata packages ApiWekan./
		# jsondata = json.loads(data2)

		# for key in jsondata:
		# 	print(jsondata)
		# 	it = iter(key.values())    
		# 	idboard, name = next(it), next(it)   
		# 	name = name
		# 	idboard = idboard
		# 	print(idboard)
		# 	print(name)
		# 	data.append((f' {idboard}', f'{name}', f'{name}'))  

		# for i in data:
		# 	print(i)
		# 	self.tree.insert('', "end", values=i)

		# scrollbar = ttk.Scrollbar(tk, orient=tk.VERTICAL, command=tree.yview)
		# tree.configure(yscroll=scrollbar.set)
		self.tree.pack()
		self.tk.mainloop()
