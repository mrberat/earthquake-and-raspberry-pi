import RPi.GPIO as GPIO
import time
import subprocess

buzzer_pin = 24
led_pin = 27

print("buzzer çalıştı")
GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.setup(led_pin, GPIO.OUT)

x= "/home/mero/Desktop/2023/mpu6050.py"
subprocess.run(["python",x])
print("mpu6050.py çalıştı")




try:
    while True:
        GPIO.output(led_pin, GPIO.HIGH)  
        GPIO.output(buzzer_pin, GPIO.HIGH)  
        time.sleep(0.1) 
        GPIO.output(led_pin, GPIO.LOW)   
        GPIO.output(buzzer_pin, GPIO.LOW)   
        time.sleep(0.1)  
except KeyboardInterrupt:
    GPIO.cleanup()