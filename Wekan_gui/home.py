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
import models
#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et
import wekanapi
import logintk
import board

username = "antoine"
password = "ntri33"
api_url = "http://localhost:8080/"
api = wekanapi.WekanApi(api_url, {"username": "antoine", "password": "ntri33"}, )
boards = api.get_user_boards()

	# print('board.idandtitle() => ',board.idandtitle())
# 	# print('board.get_cardslists() => ',board.get_cardslists())
# 	for cardslist in board.get_cardslists():
# 	# print('cardslist=>',cardslist)
# 		print('cardslist=>', cardslist.pprint())

	# print('swinlane =>',swinlane)

# for cardslist in board.get_cardslists():
# 	# print('cardslist=>',cardslist)
# 	print('cardslist=>', cardslist.pprint())

# for board in boards:

# 	# print('cardslist=>',board.get_cardslists())
# 	cardlist = board.get_cardslists()
# 		print('cardslist=>', cardslist.pprint())


# exemple : 	
# 		for board in boards:
# 			print('board.pprint() =>',board.pprint())

class GetAllBoards:
	def __init__(self):
		self.api = api
		self.tk = tk.Tk()
		self.tree = ttk.Treeview(self.tk)
		self.id = id

	def item_selected(self, event):
		for selected_item in self.tree.selection():
			item = self.tree.item(selected_item)
			record = item['values']
			showinfo(title='Information',
			message=','.join(record))
			print('record[0] =>',record[0])
			print('record[1] =>',record[1])
			print(self.api)
			board_data={
				"_id": record[0],
				"title": record[1],
				}
			titleboard = record[1]
			# print(type(self.id),self.id)
			listcards = models.Board(api, board_data)
			listcards.get_cardslists()
			listcards.get_swimlanes()
			# self.tk.destroy()
			# getboard = GetBoard()

		# return record
		# print(boardid)
		# return boardid

	def treeview_boards(self):   
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
		#print(boards.pprint())
		# print(listboard)
		# for i in listboard:
		# 	print(listboard)
		for board in boards:
			print('board.pprint() =>',board.idandtitle())
			name = board.idandtitle()[0]
			idboard = board.idandtitle()[1]
			data.append((f' {idboard}', f'{name}'))
		for i in data:
			self.tree.insert('', "end", values=i)
		
	# # print('board=>',board)
	# 		print('board.pprint() =>',board.pprint())
	# 	return dashboards
		# self.tree.insert('', "end", values=listboard)
		# for key in listboard:
		# 	print(listboard)
		# 	# name = key[0]
			# idboard = key[1]
			# data.append((f' {idboard}', f'{name}'))
			# self.tree.insert('', "end", values=self.boardlist)
			# data.append(self.boardlist)  
			# print(data)
		# for i in listboard:
		# 	print(i)
		# 	self.tree.insert('', "end", values=i)
			# self.tree.insert('', "end", values=i)
		# self.tree.insert('', "end", values=boardlist)

		# scrollbar = ttk.Scrollbar(tk, orient=tk.VERTICAL, command=tree.yview)
		# tree.configure(yscroll=scrollbar.set)
		self.tree.pack()
		self.tk.mainloop()


class GetBoardListCard(GetAllBoards): 
	def __init__(self):
		self.api = api
		self.tk = tk.Tk()
		self.tree = ttk.Treeview(self.tk)
	# def __init__(self, api):
	# 	self.api = api
	# 	self.tk = tk.Tk()
	# 	self.tree = ttk.Treeview(self.tk)

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
		
		boards = boards.get_user_boards()
		for board in boards:
			print('board.pprint() =>',board.pprint())
	
		# getallboard = GetAllBoards
		# record = getallboard.item_selected

		# print(record)
		# test = models.Cardlist()

		# print(test)
		# data = []
		# print(data)

		# root = rootmain.get_list_car
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




tkhome = GetAllBoards()
tkhome.treeview_boards()