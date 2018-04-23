# -*- coding: utf-8 -*-
"""
Created on Mon Apr 23 19:25:30 2018

@author: 10566
"""
#-*- coding: utf-8 -*-

import cv2
import sys
from PIL import Image
camera_idx = 0;
window_name = "yyx_test"
window_grey = "grey"
def CatchUsbVideo(window_name, camera_idx):
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
            for faceRect in faceRects:  #单独框出每一张人脸
                x, y, w, h = faceRect        
                cv2.rectangle(frame, (x - 10, y - 10), (x + w + 10, y + h + 10), color, 2)
                        
        #显示图像
        cv2.imshow(window_name, frame)
        
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break        
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    CatchUsbVideo("识别人脸区域", camera_idx)