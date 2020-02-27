schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        "result": {
            'type': 'object',
            'required': ['IDLE_ROTATE', 'KAGAT', 'NETWORK', 'RFID'],
            'additionalProperties': False,
            'properties': {
                "IDLE_ROTATE": {'type': 'integer'},
                "KAGAT": {'type': 'integer'},
                "NETWORK": {'type': 'integer'},
                "RFID": {'type': 'integer'}
            }
        }
    }
}
