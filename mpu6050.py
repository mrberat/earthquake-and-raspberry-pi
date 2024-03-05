import smbus
import math
import time
import subprocess


bus = smbus.SMBus(1)
address = 0x68
power_mgmt_1 = 0x6b

bus.write_byte_data(address, power_mgmt_1, 0)

def read_word(reg):
    high = bus.read_byte_data(address, reg)
    low = bus.read_byte_data(address, reg + 1)
    value = (high << 8) + low
    return value

def read_word_2c(reg):
    val = read_word(reg)
    if val >= 0x8000:
        return -((65535 - val) + 1)
    else:
        return val

def dist(a, b):
    return math.sqrt((a * a) + (b * b))

def get_rotation_x(y, z):
    radians = math.atan2(y, dist(x, z))
    return math.degrees(radians)

def get_rotation_y(x, z):
    radians = math.atan2(x, dist(y, z))
    return math.degrees(radians)

    

v = 0  # Başlangıçta sayacı sıfırla

while True:
    x = read_word_2c(0x3b)
    y = read_word_2c(0x3d)
    z = read_word_2c(0x3f)

    rotation_x = get_rotation_x(x, y)
    rotation_y = get_rotation_y(x, y)
    print("X Rotasyon: ", rotation_x)
    print("Y Rotasyon: ", rotation_y)

    if rotation_x > 20 or rotation_x < -20 or rotation_y > 20 or rotation_y < -20:
        print("yüksek tehdit")
        v += 1
        print(v)
    
    if v >= 1 and v <= 3:  # E-posta gönderme sınırı
        u = "/home/mero/Desktop/2023/buzzer.py"
        subprocess.run(["python", u])
        print("buzzer.py dosyasına geçiş")
        time.sleep(5)  # 5 saniye bekleme süresi
        
    if v >= 3:
        break
    
      # Döngüyü her turda 5 saniye beklet
    
