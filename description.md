# earthquake-and-raspberry-pi
The aim of the project is to provide warnings to users during earthquakes and also to inform relevant institutions whether there is damage in the building. Hardware components such as vibration sensor (SW420), gyroscope for measuring wall tilt, and devices emitting sound (buzzer) and light (LED) have been used in the project. The project has been implemented on a Raspberry Pi embedded computer. The hardware used in the project application is detailed as follows:

MPU6050 gyroscope module
SW-420 vibration module
11 jumper cables
1 LED
1 resistor
1 buzzer
1 breadboard
1 Raspberry Pi
The GPIO connections of the modules listed above are as follows:
buzzer_pin = 24
led_pin = 27
SW-420 = 17

The gyroscope communicates via I2C and has an address of 0x68. Python has been used for coding the project, employing a modular coding system. Python libraries such as RPi.GPIO, time, subprocess, smbus, math, EmailMessage, ssl, and smtplib have been included in the project.

The project has successfully completed its final stage. It has successfully passed all stages of warning during earthquakes, measuring wall tilt and sending emails to relevant institutions, and detecting earthquake vibrations.
