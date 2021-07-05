#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et

from tkinter import *
from functools import partial
import ssl
import json
import requests
from wekanapi import WekanApi

ssl._create_default_https_context = ssl._create_unverified_context
arguments = len(sys.argv) - 1

# login = logintk.Login(username, password)
# req, userid, apikey = login.connect(username, password)
# # print('req=>',req)
# # print('userid=>',userid)
# # print('apikey=>',apikey)

# api_url = "http://localhost:8080/"
# api = WekanApi(api_url, {"username": username, "password": password}, )

# boards = api.get_user_boards()

# for board in boards:
#     print(board.pprint())


class Login:
	def __init__(self):
		self.username = ''
		self.password = ''

	def login(self,username,password):
		main_screen = Tk()   # create a GUI window 
		main_screen.geometry("300x250") # set the configuration of GUI window 
		main_screen.title("Connexion au compte")
		Label(main_screen, text="Veuillez entrer les détails ci-dessous pour vous connecter").pack()
		Label(main_screen, text="").pack()
	
		self.username = StringVar()
		self.password = StringVar()
	
	
		Label(main_screen, text="Username * ").pack()
		username_login_entry = Entry(main_screen, textvariable=self.username)
		username_login_entry.pack()
		Label(main_screen, text="").pack()
		Label(main_screen, text="Password * ").pack()
		password__login_entry = Entry(main_screen, textvariable=self.password, show= '*')
		password__login_entry.pack()
		Label(main_screen, text="").pack()
		Button(main_screen, text="Login", width=10, height=1).pack()
		main_screen.mainloop()
		return self.username, self.password


	# def api_url(self):

	# 	wekanurl = 'http://localhost:8080/'

	# 	# ------- API URL GENERATION START -----------

	# 	loginurl = 'users/login'
	# 	wekanloginurl = wekanurl + loginurl
	# 	apiboards = 'api/boards/'
	# 	apiattachments = 'api/attachments/'
	# 	apiusers = 'api/users'
	# 	e = 'export'
	# 	s = '/'
	# 	l = 'lists'
	# 	sw = 'swimlane'
	# 	sws = 'swimlanes'
	# 	cs = 'cards'
	# 	bs = 'boards'
	# 	atl = 'attachmentslist'
	# 	at = 'attachment'
	# 	ats = 'attachments'
	# 	users = wekanurl + apiusers

	# 	return wekanloginurl


	def connect(self, username, password, apiurl):
		# ------- LOGIN TOKEN START -----------
		username, password = self.login()

		username = username.get()
		password = password.get()

		data = {"username": username, "password": password}
		req = requests.post(wekanloginurl, data=data,  verify=False)
		print('request return => ',req)
		d = req.json()
		userid = list(d.values())[0]   
		apikey = d['token']
		print('dico login =>',d)
		print('userid =>', userid)
		print('apikey =>',apikey)
		self.status_req(req)
		return req, userid, apikey
		# ------- LOGIN TOKEN END -----------

	def status_req(self,req):
		print(req)
		if req.status_code == 200:
			print("=== Wekan API Python CLI: Shows IDs for addcard ===")
			print("AUTHORID is USERID that writes card.")
			print("If *nix:  chmod +x api.py => ./api.py users")
			print("Syntax:")
			print("  python3 api.py users              # All users")
			print("  python3 api.py boards USERID      # Boards of USERID")
			print("  python3 api.py board BOARDID      # Info of BOARDID")
			print("  python3 api.py swimlanes BOARDID  # Swimlanes of BOARDID")
			print("  python3 api.py lists BOARDID      # Lists of BOARDID")
			print("  python3 api.py list BOARDID LISTID # Info of LISTID")
			print("  python3 api.py createlist BOARDID LISTTITLE # Create list")
			print("  python3 api.py addcard AUTHORID BOARDID SWIMLANEID LISTID CARDTITLE CARDDESCRIPTION")
			print("  python3 api.py editcard BOARDID LISTID CARDID NEWCARDTITLE NEWCARDDESCRIPTION")
			print("  python3 api.py listattachments BOARDID # List attachments")
			exit
		else:
			print ('Boo!')


