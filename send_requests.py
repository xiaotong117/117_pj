#!/usr/bin/python
# -*- coding: UTF-8 -*- 

import requests

URL = 'http://youli.uban360.net/gift-manager/operation/scene/list'
DATA = {}
COOKIE = {'nsp_token':'eyJ1aWQiOiIxMDEwMTAwMTM4MTcwNzIiLCJ0aW1lc3RhbXAiOiIxNTU2NDE1MDAwODA2IiwidG9rZW4iOiI2OGVkMWVmNzEwZWI1N2IxZjA3OTZkNWE0YmU5MTM0YiJ9',
                      'G_AUTH_TOKEN':'eyJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiIxNTk1ODAzMjkyNSIsImV4cCI6MTU1NjUyMjY2NiwidXNlcklkIjoxNCwiZ2lmdERlYWxlcklkIjoyMn0._dnY6I1MtCEJC6vXEEe5n1BpGMgtf_qE-TwRc6xvrKg'}

# params=urllib.urlencode({'spam':1,'eggs':2,'bacon':0})
# f=urllib.urlopen("http://python.org/query?%s" % params)
# print(f.read())

def make_data(dict):
    s = '?'
    for k,v in dict:
        s.add(k +'=' + v + '&')
    return s
    pass

def res(url,data,cookie):
    s = requests.session()
    r = s.get(url + data, cookies=cookie, verify=False)
    print(r.text)

res(URL,make_data(DATA), COOKIE)