usermqtt=$(bashio::config 'usermqtt')
passmqtt=$(bashio::config 'passmqtt')
ipmqtt=$(bashio::config 'ipmqtt')
portmqtt=$(bashio::config 'portmqtt')
userbring=$(bashio::config 'userbring')
passbring=$(bashio::config 'passbring')

python init.py usermqtt passmqtt ipmqtt portmqtt userbring passbring