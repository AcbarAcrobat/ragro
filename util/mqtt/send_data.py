from paho.mqtt import publish
from support import test_data2 as TD


def req83(ename, etype, evalue):
    host = TD.murl83()
    main_path = '/devices/vehicle/controls/'
    # need to be sent if first msg for entity. Wont break anything if will be send all the time
    publish.single(main_path + ename + "/meta/type", etype, hostname=host)
    # sending data
    publish.single(main_path + ename, evalue, hostname=host)


def req85(ename, etype, evalue):
    host = TD.murl85()
    main_path = '/devices/vehicle/controls/'
    # need to be sent if first msg for entity. Wont break anything if will be send all the time
    publish.single(main_path + ename + "/meta/type", etype, hostname=host)
    # sending data
    publish.single(main_path + ename, evalue, hostname=host)
