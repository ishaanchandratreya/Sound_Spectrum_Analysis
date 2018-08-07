import serial
import json
import time
import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish

ser= serial.Serial('/dev/ttyACM0', 9600)
s= [0.0,0.0]
while True:
        try:
            #print ser.readline()
            StringData= ser.readline()
            arr= StringData.split(',')
            if len(arr) == 2:
                arr= StringData.split(',')
                arr[0]=arr[0].replace("\r","")
                arr[0]=arr[0].replace("\n","")
                arr[1]=arr[1].replace("\r","")
                arr[1]=arr[1].replace("\n","")
                print arr[0]
                print arr[1]
                dataupload ={"Noise in dB relative to least possible value" : float (arr[0]),"frequency in Hz (range: value -150" : float (arr[1])}
                
                jsonpayload = json.dumps(dataupload)
                print jsonpayload
                publish.single("/api/dump", payload=jsonpayload, qos=0, retain=True, hostname="192.168.9.55", port=1883, client_id="592d52ecdf35be410df8ea1f")
                
        except:
            print("Error occure")
            time.sleep(1)
            
        #time.sleep(120)
    
