schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        'result': {
            'type': 'object',
            'required': ['HOST_SEARCH_UNLOAD', 'TURN_OFF', 'IDLE_ROTATE', 'DEFAULT',
                         'NO_IGNITION', 'WAITING_FOR_INIT_END', 'HOST_START_UNLOAD',
                         'NO_DRIVER', 'WAITING_FOR_SECURITY', 'GUEST_ACCEPT_UNLOAD',
                         'HOST_SEARCH_UNLOAD_PERSONALLY', 'GUEST_START_UNLOAD',
                         'HOST_ACCEPT_UNLOAD'],
            'additionalProperties': False,
            'properties': {
                "HOST_SEARCH_UNLOAD": {'type': 'integer'},
                "TURN_OFF": {'type': 'integer'},
                "IDLE_ROTATE": {'type': 'integer'},
                "DEFAULT": {'type': 'integer'},
                "NO_IGNITION": {'type': 'integer'},
                "WAITING_FOR_INIT_END": {'type': 'integer'},
                "HOST_START_UNLOAD": {'type': 'integer'},
                "NO_DRIVER": {'type': 'integer'},
                "WAITING_FOR_SECURITY": {'type': 'integer'},
                "GUEST_ACCEPT_UNLOAD": {'type': 'integer'},
                "HOST_SEARCH_UNLOAD_PERSONALLY": {'type': 'integer'},
                "GUEST_START_UNLOAD": {'type': 'integer'},
                "HOST_ACCEPT_UNLOAD": {'type': 'integer'}
            }
        }
    }
}