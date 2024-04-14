import sys
import paho.mqtt.client
from BringExtract import BringExtract

class mqttBarScanner:
    def __init__(self, userMqtt, passMqtt, ipMqtt, portMqtt, userBring, passBring) -> None:
        self.userMqtt = userMqtt
        self.passMqtt = passMqtt
        self.ipMqtt = ipMqtt
        self.portMqtt = portMqtt
        self.userBring = userBring
        self.passBring = passBring
    
    def on_connect(self, client, userdata, flags, rc):
        print('connected (%s)' % client._client_id)
        client.subscribe(topic='lector_codigo_barras/out', qos=2)

    def on_message(self, client, userdata, message):
        print(str(message.payload, encoding='utf-8'))
        Bring = BringExtract(str(message.payload, encoding='utf-8'), self.userBring, self.passBring)
        result = Bring.search()
        if (result == None):
            client.publish("lector_codigo_barras/in", "Error 404")
        else:
            client.publish("lector_codigo_barras/in", "" + result)

    def main(self):
        client = paho.mqtt.client.Client(paho.mqtt.client.CallbackAPIVersion.VERSION1, client_id='API-Codigo_barras', clean_session=False)
        client.username_pw_set(username=self.userMqtt, password=self.passMqtt)
        client.connect(host=self.ipMqtt, port=int(self.portMqtt))
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.loop_forever()