#!/usr/bin/with-contenv bashio

USERMQTT=$(bashio::config 'usermqtt')
PASSMQTT=$(bashio::config 'passmqtt')
IPMQTT=$(bashio::config 'ipmqtt')
PORTMQTT=$(bashio::config 'portmqtt')
USERBRING=$(bashio::config 'userbring')
PASSBRING=$(bashio::config 'passbring')
URIDATABASE=$(bashio::config 'uridatabase')
NAMEDATABASE=$(bashio::config 'namedatabase')

python3 /init.py ${USERMQTT} ${PASSMQTT} ${IPMQTT} ${PORTMQTT} ${USERBRING} ${PASSBRING} ${URIDATABASE} ${NAMEDATABASE}