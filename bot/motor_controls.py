import RPi.GPIO as GPIO
from time import sleep

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5
ENA = 26
ENB = 11

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)

GPIO.output(IN1, GPIO.LOW)
GPIO.output(IN2, GPIO.LOW)
GPIO.output(IN3, GPIO.LOW)
GPIO.output(IN4, GPIO.LOW)

# right motor
p_a = GPIO.PWM(ENA, 1000)
p_a.start(0)
# left motor
p_b = GPIO.PWM(ENB, 1000)
p_b.start(0)

p_a.ChangeDutyCycle(75)
p_b.ChangeDutyCycle(75)


def turn_left_wheel(forward=True):
    if forward:
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    else:
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)


def turn_right_wheel(forward=True):
    if forward:
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
    else:
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
