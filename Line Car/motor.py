import RPi.GPIO as GPIO
import time
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

HIGH = 1
LOW  = 0


IN1 =  35
IN2 =  12 
IN3 =  31
IN4 =  29

DCpin1 = 32
DCpin2 = 33


GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)


GPIO.setup(DCpin1, GPIO.OUT)
GPIO.setup(DCpin2, GPIO.OUT)




pwm1 = GPIO.PWM(DCpin1, 100)
pwm2 = GPIO.PWM(DCpin2, 100)
pwm1.start(0)
pwm2.start(0)

def Forward(speed):
    GPIO.output(IN1,HIGH)
    GPIO.output(IN2,LOW)
    GPIO.output(IN3,LOW)
    GPIO.output(IN4,HIGH)
    pwm1.ChangeDutyCycle(speed)
    pwm2.ChangeDutyCycle(speed)

def Backward(speed):
    GPIO.output(IN1,LOW)
    GPIO.output(IN2,HIGH)
    GPIO.output(IN3,LOW)
    GPIO.output(IN4,HIGH)
    pwm1.ChangeDutyCycle(speed) 
    pwm2.ChangeDutyCycle(speed)

def Stop():
    GPIO.output(IN1,LOW)
    GPIO.output(IN1,LOW)
    GPIO.output(IN1,LOW)
    GPIO.output(IN1,LOW)
    pwm2.ChangeDutyCycle(0)
    pwm1.ChangeDutyCycle(0)
