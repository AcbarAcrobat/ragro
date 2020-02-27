schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        'result': {
            'type': 'object',
            'required': ['REMOVE_CARD', 'NO_CARD', 'BAD_CARD',
                         'AUTH_OK', 'NO_CONNECTION'],
            'additionalProperties': False,
            'properties': {
                "REMOVE_CARD":   { 'type': 'integer' },
                "NO_CARD":       { 'type': 'integer' },
                "BAD_CARD":      { 'type': 'integer' },
                "AUTH_OK":       { 'type': 'integer' },
                "NO_CONNECTION": { 'type': 'integer' }
            }
        }
    }
}