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
# tree = ttk.Treeview(root)
# frame = tk.Frame(root)

class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame,
       call the update() method to refresh the scrollable area.
    """

    def __init__(self, frame, width=16):

        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y, expand=False)

        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar.config(command=self.canvas.yview)

        self.canvas.bind('<Configure>', self.__fill_canvas)

        # base class initialization
        tk.Frame.__init__(self, frame)

        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)


    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"

        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)

    def update(self):
        "Update the canvas and the scrollregion"

        self.update_idletasks()


class ScrollbarFrame(tk.Frame):
    """
    Extends class tk.Frame to support a scrollable Frame 
    This class is independent from the widgets to be scrolled and 
    can be used to replace a standard tk.Frame
    """
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        # The Scrollbar, layout to the right
        vsb = tk.Scrollbar(self, orient="vertical")
        vsb.pack(side="right", fill="y")

        # The Canvas which supports the Scrollbar Interface, layout to the left
        self.canvas = tk.Canvas(self, borderwidth=0, background="#ffffff")
        self.canvas.pack(side="left", fill="both", expand=True)

        # Bind the Scrollbar to the self.canvas Scrollbar Interface
        self.canvas.configure(yscrollcommand=vsb.set)
        vsb.configure(command=self.canvas.yview)

        # The Frame to be scrolled, layout into the canvas
        # All widgets to be scrolled have to use this Frame as parent
        self.scrolled_frame = tk.Frame(self.canvas, background=self.canvas.cget('bg'), width=350, height=240)
        self.canvas.create_window((4, 4), window=self.scrolled_frame, anchor="nw")

        # Configures the scrollregion of the Canvas dynamically
        self.scrolled_frame.bind("<Configure>", self.on_configure)

    def on_configure(self, event):
        """Set the scroll region to encompass the scrolled frame"""
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


class GetAllBoards():

	def treeview_boards(self):   

		root.geometry('400x350')
		root['bg']='#2980b9'

		label = Label(root, text='Liste Dashboards', font=('Helvetica bold',20), fg="white", bg="#2980b9")
		label.pack(pady=20)

		sbf = ScrollbarFrame(root, width=350, height=240,bg="#2980b9")
		sbf.pack()
		sbf.pack_propagate(0)
		sbf.columnconfigure(index=0, weight=1)
		sbf.columnconfigure(index=2, weight=1)
		sbf.rowconfigure(index=0, weight=1)
		sbf.rowconfigure(index=2, weight=1)
		frame = sbf.scrolled_frame


		def func(name):
			print('item',name[0][0])
			print('item',name[0][1])

			board_data={
				"title": name[0][0],
				"_id": name[0][1],
				}
			sbf.destroy() 
			label.destroy()
			listcards = models.Board(api, board_data)
			listcards.get_cardslists()
			viewlist = GetBoardListCard()
			viewlist.view_lists(board_data)

		def funcadd(name):
			print(name)

		TkinterCustomButton(master=frame, fg_color="#999", hover_color="#999", width=250, height=80, text='(+) Ajouter un Dashboard ',command=functools.partial(funcadd)).pack(padx=30, pady=20)

		for item in boards:
			data = []
			title = item.idandtitle()[0]
			idboard = item.idandtitle()[1]
			data.append([f' {title}', f'{idboard}'])
			button = TkinterCustomButton(master=frame, width=250, height=80, text=title, command=functools.partial(func,data))
			button.pack(pady=10)
			# data.append((f' {title}', f'{idboard}'))

		root.mainloop()


class GetBoardListCard(GetAllBoards): 

	def view_lists(self, board_data): 
		root.geometry('400x350')
		root['bg']='#2980b9'

		label = Label(root, text='liste des vues', font=('Helvetica bold',20), fg= "white",bg="#2980b9")
		label.pack(pady=20)

		sbf = ScrollbarFrame(root, width=350, height=240)
		sbf.pack()
		sbf.pack_propagate(0)
		sbf.columnconfigure(index=0, weight=1)
		sbf.columnconfigure(index=2, weight=1)
		sbf.rowconfigure(index=0, weight=1)
		sbf.rowconfigure(index=2, weight=1)
		frame = sbf.scrolled_frame

		def func(name):
			print(name)
			print('item',name[0][0])
			print('item',name[0][1])
			print('item',name[0][2])
			cardslist_data={
				"title": name[0][0],
				"_id": name[0][1],
				"boardid": name[0][2]
				}
			sbf.destroy() 
			label.destroy()
			board = name[0][2]
			cardslist = models.Cardslist(api, board, cardslist_data)
			cardsdata = cardslist.get_cards()
			listcards = GetCardsOfList()
			listcards.view_cards(cardslist_data,cardsdata)

		data = []
		boardid = board_data["_id"]
		listcards = models.Board(api, board_data)
		cardslists_data = listcards.get_cardslists()

		def funcadd(name):
			print(name)

		TkinterCustomButton(master=frame, fg_color="#999", hover_color="#999", width=250, height=80, text='(+) Ajouter une liste ',command=functools.partial(funcadd)).pack(padx=30, pady=20)

		for item in cardslists_data:
			data = []
			id = item["_id"]
			title = item["title"]
			data.append((f' {title}', f'{id}', f'{boardid}'))
			button = TkinterCustomButton(master=frame, width=250, height=80, text=title, command=functools.partial(func,data))
			button.pack(pady=10)


	
class GetCardsOfList(GetAllBoards): 

	def cards_selected(self, event):
		pass

	def view_cards(self, cardslist_data, cardsdata):  


		root.geometry('400x350')
		titlelistcard = cardslist_data['title']
		Label(root, text=titlelistcard, font=('Helvetica bold',20), fg= "white",bg="#2980b9").pack(padx=30, pady=20)

		sbf = ScrollbarFrame(root, width=350, height=240)
		sbf.pack()
		sbf.pack_propagate(0)
		sbf.columnconfigure(index=0, weight=1)
		sbf.columnconfigure(index=2, weight=1)
		sbf.rowconfigure(index=0, weight=1)
		sbf.rowconfigure(index=2, weight=1)
		frame = sbf.scrolled_frame
						
		def func(name):
			print(name)

		def funcadd(name):
			print(name)

		TkinterCustomButton(master=frame, fg_color="#999", hover_color="#999", width=250, height=80, text='(+) Ajouter une Card ',command=functools.partial(funcadd)).pack(padx=30, pady=20)

		for item in cardsdata:
			title = item['title']
			button = TkinterCustomButton(master=frame, width=250, height=80, text=title,command=functools.partial(func,item))
			button.pack(pady=10)





if __name__ == "__main__":
	tkhome = GetAllBoards()
	tkhome.treeview_boards()
