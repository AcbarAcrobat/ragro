schema = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'required': ['result'],
    'additionalProperties': False,
    'properties': {
        "result": {
            'type': 'object',
            'required': ['^[0-9]+$'],
            '': [
                {
                    "driver": {
                        "sap_id": "10000562",
                        "phone": "",
                        "card_uid": "95669095191300",
                        "stat": "1",
                        "ver": "1562163831",
                        "fio": "Труфанов Виталий Станиславович"
                    },
                    "reg_num": "7997ЕЕ31",
                    "host": "192.168.201.11:9194",
                    "device_id": "AC35EE2644B0",
                    "bunker_percentage": 0,
                    "brand": "ДОН 1500Б",
                    "type": "C020",
                    "guest_device_id": null,
                    "state": 0,
                    "distance": null
                }
            ]
        }
    }
}
