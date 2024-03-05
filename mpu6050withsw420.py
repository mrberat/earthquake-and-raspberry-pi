import RPi.GPIO as GPIO
import time
import subprocess


SW420_PIN = 17
 


GPIO.setmode(GPIO.BCM)
GPIO.setup(SW420_PIN, GPIO.IN)


try:
    while True:
        if GPIO.input(SW420_PIN) == GPIO.HIGH:
            print("Titreşim Algılandı!")
            
            
            time.sleep(0.5)  
            
            x= "/home/mero/Desktop/2023/buzzer.py"
            subprocess.run(["python",x])
            print("buzzer.py çalıştı")
           
        else:
            print("Titreşim Algılanmadı.")
        time.sleep(1)  
except KeyboardInterrupt:
    GPIO.cleanup() 
finally:
    GPIO.cleanup() 