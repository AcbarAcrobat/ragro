from paho.mqtt import publish
from support.testdata import TestData

T = TestData


entity_name = 'SIRENA'
entity_type = 'int'  # possible values: value(int or float), switch(bool), json, text. Case doesn't matter
entity_value = '0'
host = T.url()
main_path = '/devices/vehicle/controls/'
# need to be sent if first msg for entity. Wont break anything if will be send all the time
publish.single(main_path + entity_name + "/meta/type", entity_type, hostname=host)
# sending data
publish.single(main_path + entity_name + "/on", entity_value, hostname=host)
