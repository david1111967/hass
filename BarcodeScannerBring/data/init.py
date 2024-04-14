import sys
from mqtt import mqttBarScanner

userMqtt = str(sys.argv[1])
passMqtt = str(sys.argv[2])
ipMqtt = str(sys.argv[3])
portMqtt = str(sys.argv[4])
userBring = str(sys.argv[5])
passBring = str(sys.argv[6])
uridatabase = str(sys.argv[7])
namedatabase = str(sys.argv[8])

mqtt = mqttBarScanner(userMqtt, passMqtt, ipMqtt, portMqtt, userBring, passBring, uridatabase, namedatabase)
mqtt.main()