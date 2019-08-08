import RPi.GPIO as GPIO

IN1 = 19
IN2 = 13
IN3 = 6
IN4 = 5
ENA = 26
ENB = 11
GPIO_TRIGGER = 17
GPIO_ECHO = 4
STEPPER_PINS = [21, 20, 16, 12]

GPIO.setmode(GPIO.BCM)

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

for pin in STEPPER_PINS:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

GPIO.cleanup()

print('Pins resetted.')
