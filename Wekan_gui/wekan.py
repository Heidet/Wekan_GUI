# import requests
# import ssl
# import json


# ssl._create_default_https_context = ssl._create_unverified_context

# headers = {
#   'Content-Type': 'multipart/form-data',
#   'Accept': 'application/json',
#   'Authorization': 'API_KEY'
# }

# wekanurl = 'http://tools.ezdev.fr/wekan/'
# username = 'antoine'
# password = 'zaxPkKuRjTuAEc'
# email= 'antoine@ezdev.fr'

# loginurl = 'sign-in/'
# wekanloginurl = wekanurl + loginurl
# apiboards = 'api/boards/'
# apiattachments = 'api/attachments/'
# apiusers = 'api/users'
# e = 'export'
# s = '/'
# l = 'lists'
# sw = 'swimlane'
# sws = 'swimlanes'
# cs = 'cards'
# bs = 'boards'
# atl = 'attachmentslist'
# at = 'attachment'
# ats = 'attachments'
# users = wekanurl + apiusers

# data = {"username": username, "password": password}

# body = requests.post(wekanloginurl, params = {
#     "username" : 'antoine',
#     "password" : 'zaxPkKuRjTuAEc',
#     "email"    : 'antoine@ezdev.fr'
# }, verify=False, headers = headers)


# print "requests post => ",body
# print body