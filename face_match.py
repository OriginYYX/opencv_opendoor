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

def CatchVideo(window_name='test', camera_idx=0):
    cv2.namedWindow(window_name)
    
    cap = cv2.VideoCapture(camera_idx)                
    
    #告诉OpenCV使用人脸识别分类器
    classfier = cv2.CascadeClassifier("E:\Program\opencv-3.4.1\data\haarcascades\haarcascade_frontalface_alt2.xml")
    
    color = (0, 255, 0)
        
    while cap.isOpened():
        ok, frame = cap.read() #读取一帧数据
        
        if not ok:            
            break  

        #将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                 
        
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        faceRects = classfier.detectMultiScale(grey, scaleFactor = 1.2, minNeighbors = 3, minSize = (32, 32))
        if len(faceRects) > 0:            #大于0则检测到人脸                                   
            for faceRect in faceRects:
                x, y, w, h = faceRect
                face = frame[y - 30:y + h + 30,x - 30:x + w + 30]
                cv2.imwrite('face.jpeg', face)
                cv2.rectangle(frame, (x - 30, y - 30), (x + w + 30, y + h + 30), color, 2)
                
                
        #显示图像
        cv2.imshow(window_name, face)
        #time.sleep(0.05)
        
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
        elif c & 0xFF == ord('s'):
            cv2.imwrite('messigray.jpeg', frame)
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 

def get_token():
    response = requests.post(url)
    return response.json()['access_token']
    
def pic_base64(filePath):
    f = open(filePath, 'rb')
    
    return base64.b64encode(f.read())

if __name__ == '__main__':
    #print(get_token())
    #CatchVideo()
    test=pic_base64('face_pic/1.jpg')