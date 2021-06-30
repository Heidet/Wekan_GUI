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
import board


class GetAllBoards:
	def __init__(self):
		self.tk = tk.Tk()
		self.tree = ttk.Treeview(self.tk)

	def item_selected(self, event):
		for selected_item in self.tree.selection():
			item = self.tree.item(selected_item)
			record = item['values']
			boardid = record[0]
			print('boardid =>', boardid)
			# board(boardid)
			showinfo(title='Information',
			message=','.join(record))
		# print(boardid)
		# return boardid

	def treeview_boards(self, data2):   
		# tk = tk.Tk() 
		# tree = ttk.Treeview(tk)
		self.tk.title('Liste Dashboards')
		self.tk.geometry('300x250')
		self.tk['bg']='#2980b9'

		self.tree['columns']=('Rank', 'Name')

		self.tree.column('#0', width=0, stretch=NO) 
		self.tree.column('Rank', anchor=CENTER, width=120)
		self.tree.column('Name', anchor=CENTER, width=120)
		self.tree.heading('#0', text='', anchor=CENTER)
		self.tree.heading('Rank', text='Id Dashboard', anchor=CENTER)
		self.tree.heading('Name', text='Nom Dashboard', anchor=CENTER)
		self.tree.bind('<<TreeviewSelect>>', self.item_selected)
		self.tree.grid(row=0, column=0, sticky='nsew')

		data = []

		#Call jsondata packages ApiWekan./
		jsondata= json.loads(data2)

		for key in jsondata:
			it = iter(key.values())    
			idboard, name = next(it), next(it)   
			name = name
			idboard = idboard
			data.append((f' {idboard}', f'{name}', f'{name}'))  

		for i in data:
			print(i)
			self.tree.insert('', "end", values=i)

		# scrollbar = ttk.Scrollbar(tk, orient=tk.VERTICAL, command=tree.yview)
		# tree.configure(yscroll=scrollbar.set)
		self.tree.pack()
		self.tk.mainloop()


