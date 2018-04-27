# -*- coding: utf-8 -*-
"""
Created on Fri Apr 27 22:54:56 2018

@author: 10566
"""

import cv2
global i
i=1
def CatchVideo(window_name='test', camera_idx=0):
    cv2.namedWindow(window_name)
    
    cap = cv2.VideoCapture(camera_idx)                
    
    #告诉OpenCV使用人脸识别分类器
    
    
    color = (0, 255, 0)
    
    while cap.isOpened():
        ok, frame = cap.read() #读取一帧数据
        
        if not ok:            
            break  

        #将当前帧转换成灰度图像
        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)                 
        
        #人脸检测，1.2和2分别为图片缩放比例和需要检测的有效点数
        
                
                
                
        #显示图像
        cv2.imshow(window_name, frame)
        #time.sleep(0.05)
        
        c = cv2.waitKey(1)
        if c & 0xFF == ord('q'):
            break
        elif c & 0xFF == ord('s'):
            cv2.imwrite('pic/%s.jpg'%i, frame)
            global i
            i+=1
    
    #释放摄像头并销毁所有窗口
    cap.release()
    cv2.destroyAllWindows() 
    
if __name__ == '__main__':
    CatchVideo()