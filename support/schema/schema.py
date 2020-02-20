# schema = {
#     "result": {
#         "mechanization": {
#             "reaper": {
#                 "rotate": "boolean"
#             },
#             "loader": {
#                 "rotate": "boolean"
#             },
#             "worm": {
#                 "idle_rotate": {
#                     "available": "boolean",
#                     "remaining_time": "int"
#                 },
#                 "bypass": "boolean",
#                 "rotate": "boolean",
#                 "lock": "boolean"
#             },
#             "unloader": {
#                 "idle_rotate": {
#                     "available": "boolean",
#                     "remaining_time": "int"
#                 },
#                 "bypass": "boolean",
#                 "rotate": "boolean",
#                 "lock": "boolean"
#             },
#             "bunker": {
#                 "sap_id": "string",
#                 "percentage": "int",
#                 "connected": "boolean",
#                 "sense": {}
#             }
#         },
#         "vehicle": {
#             "brand": "string",
#             "type": "string",
#             "reg_num": "string"
#         },
#         "availability": {
#             "SSPTI": "boolean",
#             "WiFi": "boolean",
#             "GPS": "boolean",
#             "GSM": "boolean"
#         },
#         "driver": {
#             "card_uid": "string",
#             "sap_id": "string",
#             "stat": "string",
#             "phone": "string",
#             "fio": "string"
#         },
#         "guest": {
#             "distance": "int",
#             "device_id": "string",
#             "host": "string",
#             "type": "string",
#             "reg_num": "string",
#             "brand": "string",
#             "bunker_percentage": "int",
#             "driver": {
#                 "card_uid": "string",
#                 "sap_id": "string",
#                 "stat": "string",
#                 "phone": "string",
#                 "fio": "string"
#             },
#             "state": "int",
#             "guest_device_id": "string",
#             "card_uid": "string"
#         },
#         "RFID_driver_state": "int",
#         "RFID_guest_state": "int",
#         "device_id": "string",
#         "neighbors_count": "int",
#         "RFID_guest_unload_request": "boolean",
#         "state": "int"
#     },
#     "error": "string"
# }

schema2 = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        'result': {
            'type': 'object',
            'required': ['RFID_driver_state', 'state', 'neighbors_count', 'mechanization', 'vehicle', 'device_id',
                         'availability', 'RFID_guest_state', 'RFID_guest_unload_request'],
            'additionalProperties': False,
            'properties': {
                'RFID_driver_state': {'type': 'integer'},
                'state': {'type': 'integer'},
                'neighbors_count': {'type': 'integer'},
                'device_id': {'type': 'string'},
                'RFID_guest_state': {'type': 'integer'},
                'RFID_guest_unload_request': {'type': 'boolean'},
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
                                'lock': {'type': 'boolean'},
                                'rotate': {'type': 'boolean'},
                                'bypass': {'type': 'boolean'},
                                'idle_rotate': {
                                    'type': 'object',
                                    'required': ['available', 'remaining_time'],
                                    'additionalProperties': False,
                                    'properties': {
                                        'available__boolean': {'type': 'boolean'},
                                        'available__boolean': {'type': 'integer'}
                                    }
                                }
                            }
                        },
                        'bunker': {
                            'type': 'object',
                            'required': ['percentage', 'sap_id', 'sense', 'connected'],
                            'additionalProperties': False,
                            'properties': {
                                'percentage': {'type': 'object'},
                                'sap_id': {'type': 'string'},
                                'connected': {'type': 'boolean'},
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
                        'brand': {'type': 'string'},
                        'type': {'type': 'string'},
                        'reg_num': {'type': 'string'}
                    }
                },
                'availability': {
                    'properties': {
                        'required': ['SSPTI', 'WiFi', 'GPS', 'GSM'],
                        'SSPTI': {'type': 'boolean'},
                        'WiFi': {'type': 'boolean'},
                        'GPS': {'type': 'boolean'},
                        'GSM': {'type': 'boolean'},
                        'additionalProperties': False
                    },
                },
                'driver': {
                    'type': 'object',
                    'required': ['card_uid', 'sap_id', 'stat', 'phone', 'fio'],
                    'properties': {
                        'card_uid': {'type': 'string'},
                        'stat': {'type': 'string'},
                        'phone': {'type': 'string'},
                        'fio': {'type': 'string'},
                        'additionalProperties': False
                    }
                }
            }
        }
    }
}
