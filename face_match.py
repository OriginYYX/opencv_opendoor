# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:36:23 2018

@author: 10566
"""

import cv2
import base64
import urllib.request

API_KEY = 'vVsNOqLoB1QwwyVITZaPswHq'  
SECRET_KEY = 'ub0n4T1oqGQ6NELSwm3kV2niN3EtYws9'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vVsNOqLoB1QwwyVITZaPswHq&client_secret=ub0n4T1oqGQ6NELSwm3kV2niN3EtYws9'
headers={'Content-Type', 'application/json; charset=UTF-8'}
request=urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read()
if (content):
    print(content)
    
def pic_base64(filePath):
    with open(filePath, 'rb') as fp:  
        return base64.b64encode(fp.read)
        
