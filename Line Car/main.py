# -*- coding: utf8 -*-
import cv2
import time
import sys
import line_detect as ld
import motor
import servo


cap = cv2.VideoCapture(0)
motor.Forward(16)
servo.Go()
while cap.isOpened():
    
    ret, frame = cap.read()
    frame = cv2.flip(frame,0)
    frame = cv2.flip(frame,1)
    if ret:
        frame = cv2.resize(frame, (640, 360))
        cv2.imshow('ImageWindow', ld.DetectLineSlope(frame)[0])
        l, r = ld.DetectLineSlope(frame)[1], ld.DetectLineSlope(frame)[2]
        

        if abs(l) <= 155 or abs(r) <= 155:
            if l ==0 or r == 0:
                if l < 0 or r < 0:
                    servo.Turnleft()
                    print('left')
                elif l > 0 or r > 0:
                    servo.Turnright()
                    print('right')
            elif abs(l-15) > abs(r):  # 우회전 해야하는상황
                servo.Turnright()
                print('right')
            elif abs(r+15) > abs(l):  # 좌회전 해야하는상황
                servo.Turnleft()
                print('left')
            else:                                   # 직진
                servo.Go()
                print('go')
        else:
            if l > 155 or r > 155:
                servo.HardTurnright()
                print('hard right')
            elif l < -155 or r < -155:
                servo.HardTurnleft()
                print('hard left')

        key = cv2.waitKey(1)
        if key & 0xFF == ord('q'):
            motor.Stop()
            break
    
