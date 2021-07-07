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

board_data = ""
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

tk = tk.Tk()
tree = ttk.Treeview(tk)
class GetAllBoards():
	# def __init__(self):
		# self.api = api
		# self.tk = tk.Tk()
		# self.tree = ttk.Treeview(self.tk)

	def board_selected(self, event):
		for selected_item in tree.selection():
			item = tree.item(selected_item)
			record = item['values']

			board_data={
				"title": record[0],
				"_id": record[1],
				}

			listcards = models.Board(api, board_data)
			listcards.get_cardslists()
			viewlist = GetBoardListCard()
			viewlist.view_lists(board_data)

		

	def treeview_boards(self):   
		tk.title('Liste Dashboards')
		tk.geometry('300x250')
		tk['bg']='#2980b9'

		treeScroll = ttk.Scrollbar(tree)
		treeScroll.configure(command=tree)
		tree.configure(yscrollcommand=treeScroll.set)

		tree['columns']=('Name')

		tree.column('#0', width=0, stretch=NO) 
		tree.column('Name', anchor=CENTER, width=240)
		tree.heading('#0', text='', anchor=CENTER)
		tree.heading('Name', text='Nom Dashboard', anchor=CENTER)
		tree.bind('<<TreeviewSelect>>', self.board_selected)
		tree.grid(row=0, column=0, sticky='nsew')
		data = []


		for board in boards:
			name = board.idandtitle()[0]
			idboard = board.idandtitle()[1]
			data.append((f' {name}', f'{idboard}'))
		for i in data:
			tree.insert('', "end", values=i)
		
		tree.pack()
		tk.mainloop()



class GetBoardListCard(GetAllBoards): 
	# def __init__(self):
	# 	self.api = api
	# 	self.tk = tk.Tk()
	# 	self.tree = ttk.Treeview(self.tk)

	def lists_selected(self, event):
		for lists_selected in tree.selection():
			item = tree.item(lists_selected)
			record = item['values']
			showinfo(title='Information',
			message=','.join(record))
			# print('record[0] =>',record[0])
			# print('record[1] =>',record[1])
			# print(self.api)

			# print(type(self.id),self.id)
			# listcards.get_swimlanes()
			# # self.tk.destroy()
			# listcards = models.Board(api, board_data)
			# listcards.get_cardslists()
			# GetBoardListCard.view_board(self, board_data)

	def view_lists(self, board_data):  
		# print('api=>',self.api)
		# print('tk=>',self.tk)
		# print('tree=>',self.tree)
		for i in tree.get_children():
			# print(i)
			tree.delete(i)

		tk.title('Liste')
		tk.geometry('300x250')
		tk['bg']='#2980b9'

		
		treeScroll = ttk.Scrollbar(tree)		
		treeScroll.configure(command=tree)
		tree.configure(yscrollcommand=treeScroll.set)

		tree['columns']=('lists')

		tree.column('#0', width=0, stretch=NO) 
		tree.column('lists', anchor=CENTER, width=240)
		tree.heading('#0', text='', anchor=CENTER)
		tree.heading('lists', text='Listes', anchor=CENTER)
		tree.bind('<<TreeviewSelect>>', self.lists_selected)
		tree.grid(row=0, column=0, sticky='nsew')

		listcards = models.Board(api, board_data)
		cardslists_data = listcards.get_cardslists()

		data = []

		for i in cardslists_data: 
			print('listcards_id =>', i["_id"])
			print('listcards_title =>', i["title"])
			id = i["_id"]
			title = i["title"]
			data.append((f' {title}', f'{id}'))

		for i in data:
			tree.insert('', "end", values=i)

		tree.pack()
		tk.mainloop()
		# for board in cardslists_data:
		# 	name = board.idandtitle()[0]
		# 	idboard = board.idandtitle()[1]
		# 	data.append((f' {name}', f'{idboard}'))
		# for i in data:
		# 	self.tree.insert('', "end", values=i)
		
		# self.tree.pack()
		# self.tk.mainloop()
		# for j in range(total_columns):
		# 	print('j=>',j)
		# 	toto = j
		# 	self.tree['columns']=(toto)
		# 	self.tree.column('#0', width=0, stretch=NO) 
		# 	self.tree.column(j, anchor=CENTER, width=120)
		# 	self.tree.heading(j, text='')

			# 	print('i=>',i['title'])
			# 	titlelist = i['title']
			# 	total_columns = len(listcards)
			# 	print(total_columns)
				# self.tree['columns']=()

				# self.entry.insert(total_columns, 'end')

		# 	print(listcards)
		# 	# it = iter(i.values())
		# 	# id, title = next(it), next(it)   
		# 	# id = id
		# 	# title = title   
		# 	# print('id =>',id) 
		# 	# print('title => ',title) 
		# 	# self.tree['columns']=(title)
		# 	total_columns = len(listcards)
		# 	# total_columns = len(listcards)
		# 	# print(total_rows)
		# 	print(total_columns)

			# total_columns = len(lst[0])

			# for j in range(total_columns):
			# 	print('j',j)
			# 	# self.tree['columns']= j
			# 	self.tree = Entry(self.tk, width=20, fg='blue',
			# 				font=('Arial',16,'bold'))
				# /self.tree.grid(column=total_columns)
				# self.tree.grid(row=0, column=2, sticky='nsew')


				# self.e.insert(END, title)
		# self.tree.pack()

		# print('GetBoardListCard() , view_board BOARDDATA=>',board_data["_id"])
		# self.tree.heading('Rank', text='tata', anchor=CENTER)
		# self.tree.heading('Name', text='Nom Dashboard', anchor=CENTER)
		# self.tree.bind('<<TreeviewSelect>>', self.item_selected)
			# print(i)
		# tk = tk.Tk() 
		# tree = ttk.Treeview(tk)
			
		# tk = Tk() 
		# tree = ttk.Treeview(tk)
		# self.tk.title('Liste Dashboards')
		# self.tk.geometry('300x250')
		# self.tk['bg']='#2980b9'

		# self.tree['columns']=('Rank', 'Name')

		# self.tree.column('#0', width=0) 
		# self.tree.column('Rank', anchor=CENTER, width=120)
		# self.tree.column('Name', anchor=CENTER, width=120)
		# self.tree.heading('#0', text='', anchor=CENTER)
		# self.tree.heading('Rank', text='Id Dashboard', anchor=CENTER)
		# self.tree.heading('Name', text='Nom Dashboard', anchor=CENTER)
		# # tree.bind('<<TreeviewSelect>>')
		# self.tree.grid(row=0, column=0, sticky='nsew')
		
		# boards = boards.get_user_boards()
		# for board in boards:
		# 	print('board.pprint() =>',board.pprint())
	
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
		# self.tree.pack()
		# self.tk.mainloop()


tkhome = GetAllBoards()
tkhome.treeview_boards()