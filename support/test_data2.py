from support import config


def murl():
    return config.get("murl")

def url83():
    return config.get("url")

def url85():
    return config.get("url85")

def headers():
    return {"Content-Type": "application/json"}
