import paho.mqtt.client as mqtt
import config as mqttconfig
import json
import colorsys

class MQTT_Handler:

    def __init__(self,ledcontroll,setflag):
        self.client = mqtt.Client(client_id="leduhr", clean_session=False)
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.on_disconnect=self.onDisconnect
        self.client.connect(mqttconfig.broker_adress, keepalive=60)

        self.client.subscribe("lights/andre/leduhr")
        self.client.subscribe("lights/andre/leduhr/switch")

        self.client.loop_start()
        self.ledcontroll=ledcontroll
        self.setflag=setflag
        self.isConnected=False

        self.last_state=[0,0,0]    

    def on_message(self, client, userdata, message):
        with open('mqtt.log','a') as fileLog:
           fileLog.write("Msg Received"+"\n")
	
        print("Message received")

        text = "New message: {}, Topic: {}, QOS: {}, Retain Flag: {}".format(message.payload.decode("utf-8"),
                                                                         message.topic,
                                                                         message.qos,
                                                                         message.retain)
        print(text)
        msg=message.payload.decode("utf-8")
        topic=message.topic
        if topic=="lights/andre/leduhr":
            input=json.loads(msg)
            if input["state"]=="OFF":
                self.last_state[2]=0
            else:
                if "brightness" in input:
                    self.last_state[2]= int(int(input["brightness"])/255*100)
                elif "color" in input:
                    output=colorsys.rgb_to_hsv(input["color"]["r"]/255, input["color"]["g"]/255, input["color"]["b"]/255)
                    self.last_state[0]=int(output[0]*360)
                    self.last_state[1]=int(output[1]*100)
                    self.last_state[2]=int(output[2]*100)

            self.ledcontroll(self.last_state[0],self.last_state[1],self.last_state[2])

       # with open('mqtt.log','a') as fileLog:
       #     fileLog.write(text+"\n")
        
        if topic=="lights/andre/leduhr/switch":
            self.setflag(json.loads(msg))
            
        print("message processed")


        #self.ledcontroll()
 
    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK")
        self.isConnected=True
    
    def getStatus(self):
        return self.isConnected

    def onDisconnect(self,client,userdata,rc):
        print("DISCONNECTED")
        self.isConnected=False
        
        
