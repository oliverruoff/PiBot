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
print("s-stop f-forward b-backward e-exit")
print("\n")

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
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
        x = 'z'

    elif x == 'b':
        print("backward")
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
        x = 'z'

    elif x == 'e':
        GPIO.cleanup()
        break

    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
