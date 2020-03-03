from paho.mqtt import publish
from support.testdata import TestData


T = TestData()


def example(ename, etype, evalue):
    host = T.murl()
    main_path = '/devices/vehicle/controls/'
    # need to be sent if first msg for entity. Wont break anything if will be send all the time
    publish.single(main_path + ename + "/meta/type", etype, hostname=host)
    # sending data
    publish.single(main_path + ename, evalue, hostname=host)
