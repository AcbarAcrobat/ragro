from support import config


def murl83():
    return config.get("murl83")


def murl85():
    return config.get("murl85")


def url83():
    return config.get("url83")


def url85():
    return config.get("url85")


def headers():
    return {"Content-Type": "application/json"}


def device_id(mech_type):
    pass
