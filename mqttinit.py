import paho.mqtt.client as mqtt
import config as mqttconfig

class MQTT_Handler:

    def on_message(self, client, userdata, message):
        text = "New message: {}, Topic: {}, QOS: {}, Retain Flag: {}".format(message.payload.decode("utf-8"),
                                                                         message.topic,
                                                                         message.qos,
                                                                         message.retain)
        print(text)
        #self.ledcontroll()


    def __init__(self,ledcontroll):
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect
        self.client.connect(mqttconfig.broker_adress, keepalive=60)
        self.client.subscribe("uhr/on")
        self.client.subscribe("uhr/hsv")
        self.client.loop_start()
        self.ledcontroll=ledcontroll

    def on_connect(self, client, userdata, flags, rc):
        print("CONNACK")