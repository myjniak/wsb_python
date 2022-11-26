import json

d = {
    "Michal Szajkowski": {
        "PESEL": 954238765398,
        "birth": "12.11.12",
        "posession": [
            "TV",
            "laptop",
        ]
    },
    "Krzysztof X": {
        "possesion": {
            "laptop": {
                "cpu": "intel i7",
                "ram": 16
            }
        }
    }
}

print(json.dumps(d, indent=1))
