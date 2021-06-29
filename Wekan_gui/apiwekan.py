#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vi:ts=4:et

# Wekan API Python CLI, originally from here, where is more details:
# https://github.com/wekan/wekan/wiki/New-card-with-Python3-and-REST-API

try:
    # python 3
    from urllib.parse import urlencode
except ImportError:
    # python 2
    from urllib import urlencode

import json
import requests
import sys
import ssl
import logintk 

ssl._create_default_https_context = ssl._create_unverified_context
arguments = len(sys.argv) - 1

if arguments == 0:
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

# username = 'antoine'
# password = 'ntri33'


username, password = logintk.login()

# print('username',username.get())
# print('password',password.get())

username = username.get()
password = password.get()
wekanurl = 'http://localhost:8080/'


# ------- SETTINGS END -------------

"""
EXAMPLE:

python3 api.py

OR:
chmod +x api.py
./api.py

=== Wekan API Python CLI: Shows IDs for addcard ===
AUTHORID is USERID that writes card.
Syntax:
  python3 api.py users               # All users
  python3 api.py boards USERID       # Boards of USERID
  python3 api.py board BOARDID       # Info of BOARDID
  python3 api.py swimlanes BOARDID   # Swimlanes of BOARDID
  python3 api.py lists BOARDID       # Lists of BOARDID
  python3 api.py list BOARDID LISTID # Info of LISTID
  python3 api.py createlist BOARDID LISTTITLE # Create list
  python3 api.py addcard AUTHORID BOARDID SWIMLANEID LISTID CARDTITLE CARDDESCRIPTION
  python3 api.py editcard BOARDID LISTID CARDID NEWCARDTITLE NEWCARDDESCRIPTION
  python3 api.py listattachments BOARDID # List attachments
  python3 api.py attachmentjson BOARDID ATTACHMENTID # One attachment as JSON base64
  python3 api.py attachmentbinary BOARDID ATTACHMENTID # One attachment as binary file

=== USERS ===

python3 api.py users

=> abcd1234

=== BOARDS ===

python3 api.py boards abcd1234


=== SWIMLANES ===

python3 api.py swimlanes dYZ

[{"_id":"Jiv","title":"Default"}
]

=== LISTS ===

python3 api.py lists dYZ

[]

There is no lists, so create a list:

=== CREATE LIST ===

python3 api.py createlist dYZ 'Test'

{"_id":"7Kp"}

#  python3 api.py addcard AUTHORID BOARDID SWIMLANEID LISTID CARDTITLE CARDDESCRIPTION

python3 api.py addcard ppg dYZ Jiv 7Kp 'Test card' 'Test description'

=== LIST ATTACHMENTS WITH DOWNLOAD URLs ====

python3 api.py listattachments BOARDID

"""

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

# ------- API URL GENERATION END -----------

# ------- LOGIN TOKEN START -----------

data = {"username": username, "password": password}
req = requests.post(wekanloginurl, data=data,  verify=False)
print('body => ',req)
d = req.json()
userid = list(d.values())[0]   
apikey = d['token']
print('dico login =>',d)
print('userid =>', userid)
print('apikey =>',apikey)

# ------- LOGIN TOKEN END -----------

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


def boards():
    # if arguments == 2:
    # userid = sys.argv[2]
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
    print(data2)
    return data2


def board(userid):
    # if sys.argv[1] == 'board':
    boardid = sys.argv[2]
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



if req.status_code == 200:
    boards()
else:
    print ('Boo!')