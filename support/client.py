import paho.mqtt.client as mqtt


client = mqtt.Client()
client.connect("192.168.0.85", 9194, 60)

client.publish("/devices/vehicle/controls/RFID_1/on", payload=b"2147792821", qos=0, retain=False)
print("done")

client.loop_forever()
