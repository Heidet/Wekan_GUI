#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et
import functools
from tkinter import *
from functools import partial
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import json
import models
import wekanapi
import logintk
import board
from custom_button import TkinterCustomButton
import ssl

board_data = ""
username = "antoine"
password = "ntri33"
api_url = "http://localhost:8080"
api = wekanapi.WekanApi(api_url, {"username": "antoine", "password": "ntri33"})
boards = api.get_user_boards()


root = tk.Tk()
tree = ttk.Treeview(root)
frame = tk.Frame(root)


class GetAllBoards():

	def board_selected(self, event):
		for selected_item in tree.selection():
			item = tree.item(selected_item)
			record = item['values']
			# showinfo(title='Information',
			# message=','.join(record))
			

			board_data={
				"title": record[0],
				"_id": record[1],
				}
			
			listcards = models.Board(api, board_data)
			listcards.get_cardslists()
			viewlist = GetBoardListCard()
			viewlist.view_lists(board_data)


	def treeview_boards(self):   
		root.title('Liste Dashboards')
		root.geometry('300x250')
		root['bg']='#2980b9'

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
		root.mainloop()


class GetBoardListCard(GetAllBoards): 

	def lists_selected(self, event):
		for lists_selected in tree.selection():
			item = tree.item(lists_selected)
			record = item['values']
			# showinfo(title='Information',
			# message=','.join(record))
			
			# print('title =>',record[0])
			# print('_id =>',record[1])
			# print('boardid =>',record[2])

			cardslist_data={
				"title": record[0],
				"_id": record[1],
				"boardid": record[2]
				}

			board = record[2]
			cardslist = models.Cardslist(api, board, cardslist_data)
			cardsdata = cardslist.get_cards()
			# print('cardsdata=>',cardsdata)
			listcards = GetCardsOfList()
			listcards.view_cards(cardslist_data,cardsdata)

	def view_lists(self, board_data):  

		for i in tree.get_children():
			tree.delete(i)

		root.title('Liste')
		root.geometry('300x250')
		root['bg']='#2980b9'

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
		boardid = board_data["_id"]

		# print('boardid =>',boardid)

		for i in cardslists_data: 
			# print('listcards_id =>', i["_id"])
			# print('listcards_title =>', i["title"])
			id = i["_id"]
			title = i["title"]
			data.append((f' {title}', f'{id}', f'{boardid}'))

		for i in data:
			tree.insert('', "end", values=i)

		tree.pack()
		root.mainloop()
	
class GetCardsOfList(): 

	def cards_selected(self, event):
		pass

	def view_cards(self, cardslist_data, cardsdata):  
		tree.delete(*tree.get_children())
		tree.destroy()
		root.geometry('400x350')
		titlelistcard = cardslist_data['title']
		Label(root, text=titlelistcard, font=('Helvetica bold',20), fg= "white",bg="#2980b9").pack(pady=20)
		# frame = Frame(root,  width=100, height=100)
		# frame.pack(fill=None, expand=False)


		frame = tk.Frame(root, bg='#ffffff', width=350, height=240)
		frame.pack()
		frame.pack_propagate(0)
		frame.columnconfigure(index=0, weight=1)
		frame.columnconfigure(index=2, weight=1)
		frame.rowconfigure(index=0, weight=1)
		frame.rowconfigure(index=2, weight=1)
						

		def func(name):
			print (name)


		for item in cardsdata:
			title = item['title']
			button = TkinterCustomButton(master=frame, width=250, height=80, text=title,command=functools.partial(func,item))
			#  width=30, height=2,  bg="#2980b9", 
			button.pack(pady=10)


		root.mainloop()

	


tkhome = GetAllBoards()
tkhome.treeview_boards()