# #! /usr/bin/env python3
# # -*- coding: utf-8 -*-
# # vi:ts=4:et
# import wekanapi
# import logintk
# import json
# import home
# import board

# username = "antoine"
# password = "ntri33"
# api_url = "http://localhost:8080/"

# # login = logintk.Login()
# # username, password = login.login(username, password)

# # api = WekanApi(api_url, {"username": username.get(), "password": password.get()}, )
# api = wekanapi.WekanApi(api_url, {"username": username, "password": password}, )
# # print(api)
# boards = api.get_boards()

# data = []

# for board in boards:
#     boardlist = board.idandtitle()
#     data.append(boardlist)

# tkhome = home.GetAllBoards(data)
# tkhome.treeview_boards()

# # tree = home.GetAllBoards(data)

