import paho.mqtt.client as mqtt
import config as mqttconfig

class MQTT_Handler:

    def on_message(self, client, userdata, message):
        text = "New message: {}, Topic: {}, QOS: {}, Retain Flag: {}".format(message.payload.decode("utf-8"),
                                                                         message.topic,
                                                                         message.qos,
                                                                         message.retain)
        print(text)
        msg=message.payload.decode("utf-8")
        topic=message.topic
        if topic=="uhr/hsv":
            hsv=msg.split(",")
            self.ledcontroll(int(hsv[0]),int(hsv[1]),int(hsv[2]))

       # with open('mqtt.log','a') as fileLog:
       #     fileLog.write(text+"\n")
        

        if topic=="uhr/manualbrightness":
            if msg=="true":
                self.setflag(True)
            elif msg=="false":
                self.setflag(False)
            
                    


        #self.ledcontroll()


    def __init__(self,ledcontroll,setflag):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.on_disconnect=self.onDisconnect
        self.client.connect(mqttconfig.broker_adress, keepalive=60)
        self.client.subscribe("uhr/on")
        self.client.subscribe("uhr/hsv")
        self.client.subscribe("uhr/manualbrightness")
        self.client.loop_start()
        self.ledcontroll=ledcontroll
        self.setflag=setflag
        self.isConnected=False

    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK")
        self.isConnected=True
    
    def getStatus(self):
        return self.isConnected
    def onDisconnect(self,userdata,rc):
        self.isConnected=False
        
        