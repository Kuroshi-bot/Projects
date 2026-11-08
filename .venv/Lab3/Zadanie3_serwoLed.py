from gpiozero import AngularServo
from  gpiozero import LED
from time import sleep

led = LED(23) 
servo = AngularServo(24, min_angle=-90, max_angle=90)
while True:
    servo.angle = -90
    for _ in range(5):
        led.on()
        sleep(0.5)
        led.off()
        sleep(0.5)

    servo.angle = 90
    for _ in range(10):
        led.on()
        sleep(0.1)
        led.off()
        sleep(0.1)