#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et

from tkinter import *
from functools import partial


def login():
	#window
	tkWindow = Tk()  
	tkWindow.geometry('200x80')  
	tkWindow.title('Connexion Wekan')
	#username label
	usernameLabel = Label(tkWindow, text="User").grid(row=0, column=0)
	username = StringVar()
	usernameEntry = Entry(tkWindow, textvariable=username).grid(row=0, column=1)  

	#password label 
	passwordLabel = Label(tkWindow,text="Password").grid(row=1, column=0)  
	password = StringVar()
	passwordEntry = Entry(tkWindow, textvariable=password, show='*').grid(row=1, column=1)  
	# validateLogin = partial(validateLogin, username, password)
	# button Connect

	loginButton = Button(tkWindow, text="Login").grid(row=4, column=0)  
	tkWindow.mainloop()
	return username, password

