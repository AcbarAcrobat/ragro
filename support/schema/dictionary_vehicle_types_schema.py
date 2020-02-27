import jsonschema


schema = {
  '$schema': 'http://json-schema.org/draft-07/schema#',
  'type': 'object',
  'required': ['result'],
  'additionalProperties': False,
  'properties': {
    "result": {
      'type': 'object',
      'required': ['BEETROOT_HARVESTER',
                   'BEETROOT_TRANSPORTER',
                   'HARVESTER', 'REFUELLER',
                   'TRANSPORTER'],
      'additionalProperties': False,
      'properties': {
        'BEETROOT_HARVESTER':   { 'type': 'string' },
        'BEETROOT_TRANSPORTER': { 'type': 'string' },
        'HARVESTER':            { 'type': 'string' },
        'REFUELLER':            { 'type': 'string' },
        'TRANSPORTER':          { 'type': 'string' }
      }
    }
  }
}
