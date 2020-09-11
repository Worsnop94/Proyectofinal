import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt 
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)

def conexion(client,userdata,flags,rc):
    print("Conexion establecida")
    
def recepcion(client,userdata,msg):
    msgr=str(msg.payload.decode("utf-8"))
    if msgr=='prender led':
        GPIO.output(7,True)
        resp='La led ha sido encendida'
    if msgr=='apagar led':
        GPIO.output(7,False)
        resp='La led ha sido apagada'
    client.publish("link94j@gmail.com/test",resp)
    
client=mqtt.Client() 
client.on_connect=conexion
client.on_message=recepcion
client.username_pw_set("link94j@gmail.com","123456") 
client.connect("maqiatto.com", 1883)
client.subscribe("link94j@gmail.com/test1", 0)

rc=0
while rc==0:
    time.sleep(1)
    rc=client.loop()
    