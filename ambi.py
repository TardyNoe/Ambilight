import paho.mqtt.client as mqtt
import time
from PIL import Image,ImageGrab
import numpy as np


Adresse = "Leds/Bureau/set"
broker_address="IP of MQTT Broker" 
client = mqtt.Client("P1")
client.username_pw_set("username", password="password")
client.connect(broker_address)
depart = r,g,b = 255,255,255

delay = 0.03
nbimage = 15
while True:
    img = ImageGrab.grab((760,640,1160,840))
    im = img
    size = width, height = im.size
    im_matrix = np.array(im)
    moy = np.mean(im_matrix,axis=(0,1))
    fin = r1, g1, b1 = moy[0],moy[1],moy[2]
    r2 = np.linspace(r,r1,nbimage)
    g2 = np.linspace(g,g1,nbimage)
    b2 = np.linspace(b,b1,nbimage)
    for i in range(0,nbimage):
        client.publish(Adresse,"{\"state\": \"ON\", \"color\": {\"r\": "+ str(int(r2[i])) +", \"g\": "+ str(int(g2[i])) +", \"b\": "+ str(int(b2[i])) +"}}")
        time.sleep(delay)
    depart = r, g, b = moy[0],moy[1],moy[2]
