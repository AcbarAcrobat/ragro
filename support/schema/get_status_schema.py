schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        'result': {
            'type': 'object',
            'required': ['RFID_driver_state', 'RFID_guest_state', 'device_id',
                         'neighbors_count', 'RFID_guest_unload_request', 'state',
                         'mechanization', 'vehicle',
                         'availability'],
            'additionalProperties': False,
            'properties': {
                'RFID_driver_state':         {  'type': 'integer'  },
                'RFID_guest_state':          {  'type': 'integer'  },
                'device_id':                 {  'type': 'string'   },
                'neighbors_count':           {  'type': 'integer'  },
                'RFID_guest_unload_request': {  'type': 'boolean'  },
                'state':                     {  'type': 'integer'  },
                'driver': {
                    'type': 'object',
                    'required': ['card_uid', 'sap_id', 'ver',
                                 'stat', 'fio', 'phone'],
                    'additionalProperties': False,
                    'properties': {
                        'card_uid': { 'type': 'string' },
                        'sap_id':   { 'type': 'string' },
                        'ver':      { 'type': 'string' },
                        'stat':     { 'type': 'string' },
                        'fio':      { 'type': 'string' },
                        'phone':    { 'type': 'string' }
                    }
                },
                'mechanization': {
                    'type': 'object',
                    'required': ['worm', 'bunker'],
                    'additionalProperties': False,
                    'properties': {
                        'worm': {
                            'type': 'object',
                            'required': ['lock', 'rotate', 'idle_rotate', 'bypass'],
                            'additionalProperties': False,
                            'properties': {
                                'lock':   {  'type': 'boolean'  },
                                'rotate': {  'type': 'boolean'  },
                                'bypass': {  'type': 'boolean'  },
                                'idle_rotate': {
                                    'type': 'object',
                                    'required': ['available', 'remaining_time'],
                                    'additionalProperties': False,
                                    'properties': {
                                        'remaining_time': { 'type': 'integer' },
                                        'available':      { 'type': 'boolean' }
                                    }
                                }
                            }
                        },
                        'bunker': {
                            'type': 'object',
                            'required': ['percentage', 'sap_id', 'sense', 'connected'],
                            'additionalProperties': False,
                            'properties': {
                                'percentage': {  'type': 'integer'  },
                                'sap_id':     {  'type': 'string'   },
                                'connected':  {  'type': 'boolean'  },
                                'sense': {
                                    'type': 'object',
                                    'required': ['1', '2', '3', '4', '5'],
                                    'additionalProperties': False,
                                    'properties': {
                                        '1': {'type': 'boolean'},
                                        '2': {'type': 'boolean'},
                                        '3': {'type': 'boolean'},
                                        '4': {'type': 'boolean'},
                                        '5': {'type': 'boolean'}
                                    }
                                }
                            }
                        }
                    }
                },
                'vehicle': {
                    'type': 'object',
                    'required': ['brand', 'type', 'reg_num'],
                    'additionalProperties': False,
                    'properties': {
                        'brand':   { 'type': 'string' },
                        'type':    { 'type': 'string' },
                        'reg_num': { 'type': 'string' }
                    }
                },
                'availability': {
                    'type': 'object',
                    'required': ['SSPTI', 'WiFi', 'GPS', 'GSM'],
                    'additionalProperties': False,
                    'properties': {
                        'SSPTI': { 'type': 'boolean' },
                        'WiFi':  { 'type': 'boolean' },
                        'GPS':   { 'type': 'boolean' },
                        'GSM':   { 'type': 'boolean' },
                    },
                },
            }
        }
    }
}
