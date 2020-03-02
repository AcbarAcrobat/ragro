from paho.mqtt import publish


entity_name = 'bunker_level'
entity_type = 'value'  # possible values: value(int or float), switch(bool), json, text. Case doesn't matter
entity_value = '1000000000'
host = '192.168.0.85'
main_path = '/devices/vehicle/controls/'
# need to be sent if first msg for entity. Wont break anything if will be send all the time
publish.single(main_path + entity_name + "/meta/type", entity_type, hostname=host)
# sending data
publish.single(main_path + entity_name + "/on", entity_value, hostname=host)
