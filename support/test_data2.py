from support import config


def murl():
    return config.get("murl")

def murl85():
    return config.get("murl85")

def url():
    return config.get("url")

def url85():
    return config.get("url85")

def headers():
    return {"Content-Type": "application/json"}

def device_id(mech_type):
    pass