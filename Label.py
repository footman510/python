#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import cv2
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import numpy as np
import matplotlib.pyplot as plt

class exp(QMainWindow):
    signal = pyqtSignal()
    def __init__(self):
        super(exp,self).__init__()

        self.initUI()

    def initUI(self):
        self.statusBar()
        exitAction2 = QAction ('&Open', self)
        exitAction2.setShortcut('Ctrl+O')
        exitAction2.setStatusTip('open picture')
        exitAction2.triggered.connect(self.open_image)

        exitAction1 = QAction ('&Exit', self)
        exitAction1.setShortcut('Ctrl+Q')
        exitAction1.setStatusTip('Exit app')
        exitAction1.triggered.connect(qApp.quit)
   
        exitAction7 = QAction ('&Save', self)
        exitAction7.setShortcut('Ctrl+S')
        exitAction7.setStatusTip('save picture and label')
        exitAction7.triggered.connect(qApp.quit)
  
        exitAction8 = QAction ('&Add label', self)
        exitAction8.setShortcut('Ctrl+A')
        exitAction8.setStatusTip('add label')
        exitAction8.triggered.connect(qApp.quit)
    
        exitAction3 = QAction ('&Next', self)
        exitAction3.setShortcut('Ctrl+N')
        exitAction3.setStatusTip('next picture')
        exitAction3.triggered.connect(qApp.quit)
   
        exitAction4 = QAction ('&Last', self)
        exitAction4.setShortcut('Ctrl+L')
        exitAction4.setStatusTip('last picture')
        exitAction4.triggered.connect(qApp.quit)
   
        exitAction5 = QAction ('&Bigger', self)
        exitAction5.setShortcut('Ctrl+B')
        exitAction5.setStatusTip('bigger picture')
        exitAction5.triggered.connect(self.bigger)
  
        exitAction6 = QAction ('&Smaller', self)
        exitAction6.setShortcut('Ctrl+X')
        exitAction6.setStatusTip('smaller picture')
        exitAction6.triggered.connect(qApp.quit)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('file')
        fileMenu.addAction(exitAction1)
        fileMenu.addAction(exitAction2)
        fileMenu.addAction(exitAction7)
        fileMenu.addAction(exitAction8)

        fileMenu = menubar.addMenu('switch picture')
        fileMenu.addAction(exitAction3)
        fileMenu.addAction(exitAction4)

        fileMenu = menubar.addMenu('change size')
        fileMenu.addAction(exitAction5)
        fileMenu.addAction(exitAction6)
 
        self.setGeometry(600, 600, 600, 400)
        self.setWindowTitle('Label')
        self.show()
    def open_image(self):#打开图片
        img=cv2.imread("picture/exit24.jpg")
        cv2.imshow("image",img)
        cv2.waitKey()
        cv2.destroyAllWindows() 
    def open_video(self):
        cap = cv2.VideoCapture("picture/test.ogg")
        while(1):
           # get a frame
           ret, frame = cap.read()
           # show a frame
           cv2.imshow("capture", frame)
           if cv2.waitKey(100) & 0xFF == ord('q'):
              break
        cap.release()
        cv2.destroyAllWindows()
    def bigger(self):

        img = cv2.imread('picture/exit24.jpg')
        res1 = cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)

        height,width = img.shape[:2]
        res2 = cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
        plt.subplot(131)
        plt.imshow(img)
        plt.subplot(132)
        plt.imshow(res1)
        plt.subplot(133)
        plt.imshow(res2)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = exp()   
    sys.exit(app.exec_())
