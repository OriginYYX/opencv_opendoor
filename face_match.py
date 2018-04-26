# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 21:36:23 2018

@author: 10566
"""

import cv2
import base64
import requests

API_KEY = 'vVsNOqLoB1QwwyVITZaPswHq'  
SECRET_KEY = 'ub0n4T1oqGQ6NELSwm3kV2niN3EtYws9'
url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=vVsNOqLoB1QwwyVITZaPswHq&client_secret=ub0n4T1oqGQ6NELSwm3kV2niN3EtYws9'


def get_token():
    response = requests.post(url)
    
    return response.json()['access_token']
    
def pic_base64(filePath):
    with open(filePath, 'rb') as fp:  
        return base64.b64encode(fp.read)
        
if __name__ == '__main__':
    print(get_token())