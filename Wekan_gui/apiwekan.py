#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et


try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

import requests
import sys
import logintk
import home

    
username = ""
password = ""

login = logintk.Login(username, password)
req, userid, apikey = login.connect(username, password)
print('req=>',req)
print('userid=>',userid)
print('apikey=>',apikey)


wekanurl = 'http://localhost:8080/'

# ------- API URL GENERATION START -----------

loginurl = 'users/login'
wekanloginurl = wekanurl + loginurl
apiboards = 'api/boards/'
apiattachments = 'api/attachments/'
apiusers = 'api/users'
e = 'export'
s = '/'
l = 'lists'
sw = 'swimlane'
sws = 'swimlanes'
cs = 'cards'
bs = 'boards'
atl = 'attachmentslist'
at = 'attachment'
ats = 'attachments'
users = wekanurl + apiusers

def addcard(userid):
    # if arguments == 7:
    # if sys.argv[1] == 'addcard':

    authorid = sys.argv[2]
    boardid = sys.argv[3]
    swimlaneid = sys.argv[4]
    listid = sys.argv[5]
    cardtitle = sys.argv[6]
    carddescription = sys.argv[7]
    cardtolist = wekanurl + apiboards + boardid + s + l + s + listid + s + cs
    # Write to card
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    post_data = {'authorId': '{}'.format(authorid), 'title': '{}'.format(cardtitle), 'description': '{}'.format(carddescription), 'swimlaneId': '{}'.format(swimlaneid)}
    body = requests.post(cardtolist, data=post_data, headers=headers)
    print(body.text)
    return body.text



def editcard(userid) :
    # if arguments == 6:
    # if sys.argv[1] == 'editcard':
    boardid = sys.argv[2]
    listid = sys.argv[3]
    cardid = sys.argv[4]
    newcardtitle = sys.argv[5]
    newcarddescription = sys.argv[6]
    edcard = wekanurl + apiboards + boardid + s + l + s + listid + s + cs + s + cardid
    print(edcard)
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    put_data = {'title': '{}'.format(newcardtitle), 'description': '{}'.format(newcarddescription)}
    body = requests.put(edcard, data=put_data, headers=headers)
    print("=== EDIT CARD ===\n")
    body = requests.get(edcard, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def createlist(userid):
    # if arguments == 3:
    # if sys.argv[1] == 'createlist':
    boardid = sys.argv[2]
    listtitle = sys.argv[3]
    list = wekanurl + apiboards + boardid + s + l
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    post_data = {'title': '{}'.format(listtitle)}
    body = requests.post(list, data=post_data, headers=headers)
    print("=== CREATE LIST ===\n")
    print(body.text)
    return body.text


def list(userid):
    # if sys.argv[1] == 'list':
    boardid = sys.argv[2]
    listid = sys.argv[3]
    listone = wekanurl + apiboards + boardid + s + l + s + listid
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    print("=== INFO OF ONE LIST ===\n")
    body = requests.get(listone, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def boards(userid):
    # if arguments == 2:
    # userid = sys.argv[2]
    from home import GetAllBoards
    print('useridboard =>', userid)
    print('users =>', users)
    print('s =>', s)
    print('bs =>', bs)

    boards = users + s + userid + s + bs
    print('boards', boards )
    # if sys.argv[1] == 'boards':
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    #post_data = {'userId': '{}'.format(userid)}
    body = requests.get(boards, headers=headers)
    print("=== BOARDS ===\n")
    data2 = body.text.replace('}',"}\n")
    boards = GetAllBoards()
    boards.treeview_boards(data2)
    # boardid = boards.item_selected()
    # print('boardid',str(boardid))
    # return data2



def board(boardid, apikey):

    # if sys.argv[1] == 'board':
    # boardid = sys.argv[2]
    # boardid = 
    board = wekanurl + apiboards + boardid
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    body = requests.get(board, headers=headers)
    print("=== BOARD ===\n")
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def swilanes(userid):
    # if sys.argv[1] == 'swimlanes':
    boardid = sys.argv[2]
    swimlanes = wekanurl + apiboards + boardid + s + sws
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    print("=== SWIMLANES ===\n")
    body = requests.get(swimlanes, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def lists(userid):
    # if sys.argv[1] == 'lists':
    boardid = sys.argv[2]
    lists = wekanurl + apiboards + boardid + s + l
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    print("=== LISTS ===\n")
    body = requests.get(lists, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def listattachments(userid):
    # if sys.argv[1] == 'listattachments':
    boardid = sys.argv[2]
    listattachments = wekanurl + apiboards + boardid + s + ats
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    print("=== LIST OF ATTACHMENTS ===\n")
    body = requests.get(listattachments, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2


def userslist():
    # if arguments == 1:
    # if sys.argv[1] == 'users':
    headers = {'Accept': 'application/json', 'Authorization': 'Bearer {}'.format(apikey)}
    print(users)
    print("=== USERS ===\n")
    body = requests.get(users, headers=headers)
    data2 = body.text.replace('}',"}\n")
    print(data2)
    return data2





boards(userid)