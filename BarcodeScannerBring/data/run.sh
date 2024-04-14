#!/usr/bin/with-contenv bashio

USERMQTT=$(bashio::config 'usermqtt')
PASSMQTT=$(bashio::config 'passmqtt')
IPMQTT=$(bashio::config 'ipmqtt')
PORTMQTT=$(bashio::config 'portmqtt')
USERBRING=$(bashio::config 'userbring')
PASSBRING=$(bashio::config 'passbring')

python3 /init.py USERMQTT PASSMQTT IPMQTT PORTMQTT USERBRING PASSBRING