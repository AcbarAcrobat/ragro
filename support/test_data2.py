from support import config


def murl():
    return config.get("murl")

<<<<<<< HEAD
def url83():
=======
def murl85():
    return config.get("murl85")

def url():
>>>>>>> 2b3fa145f4d1bc12c3701fd2595b437ab00e1748
    return config.get("url")

def url85():
    return config.get("url85")

def headers():
    return {"Content-Type": "application/json"}
