# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:25:30 2018

@author: 10566
"""
#-*- coding: utf-8 -*-
from aip import AipFace
import time
import cv2
import sys
from PIL import Image
camera_idx = 0;

APP_ID = '11145409'  
API_KEY = 'vVsNOqLoB1QwwyVITZaPswHq'  
SECRET_KEY = 'ub0n4T1oqGQ6NELSwm3kV2niN3EtYws9'
face = AipFace(APP_ID, API_KEY, SECRET_KEY)
options = {  
    'max_face_num': 1,  
    'face_fields': "age,beauty",  
}

def get_file_content(filePath):  
    with open(filePath, 'rb') as fp:  
        return fp.read()

def CatchVideo(window_name, camera_idx):
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
                cv2.imwrite('messigray.jpeg', frame)
                result = face.detect(get_file_content('messigray.jpeg'),options)
                #tot = result[result]
                #print(type(tot))
                fof=result['result']
                if fof[0]:
                    fof=fof[0]
                    fof=fof['beauty']
                    fof=str(fof)
                #单独框出每一张人脸
                x, y, w, h = faceRect        
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                cv2.putText(frame,fof,(x+w+20,y),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),1)
                
                
        #显示图像
        cv2.imshow(window_name, frame)
        #time.sleep(0.05)
        
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
        elif c & 0xFF == ord('s'):
            cv2.imwrite('messigray.jpeg', frame)
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    CatchVideo("yyx_test", camera_idx)