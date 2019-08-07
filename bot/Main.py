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

p_a = GPIO.PWM(ENA, 1000)
p_a.start(0)
p_b = GPIO.PWM(ENB, 1000)
p_b.start(0)

p_a.ChangeDutyCycle(75)
p_b.ChangeDutyCycle(75)

print("\n")
print("The default speed & direction of motor is STOP & Forward.....")
print("s-stop f-forward b-backward r-right l-left e-exit")
print("\n")


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


while(1):

    x = input()

    if x == 's':
        print("stop")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)
        x = 'z'

    elif x == 'f':
        print("forward")
        turn_right_wheel()
        turn_left_wheel()
        x = 'z'

    elif x == 'b':
        print("backward")
        turn_right_wheel(False)
        turn_left_wheel(False)
        x = 'z'

    elif x == 'r':
        print('right')
        turn_right_wheel(False)
        turn_left_wheel()

    elif x == 'l':
        print('left')
        turn_right_wheel()
        turn_left_wheel(False)

    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
