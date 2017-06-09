# -*- coding:utf-8 -*-
import requests


page = 2
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
r = requests.get(url)
print (r.text)
    