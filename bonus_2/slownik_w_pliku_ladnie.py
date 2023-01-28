import csv
import json



slownik = {
    "c": 1,
    "b": 2,
    "a": 3
}
print(slownik)
print(json.dumps(slownik, indent=4))
json.dump(slownik, open("ladny.json", "w"), indent=4)

zrekonstruowany_slownik = json.loads(open("ladny.json").read())
print(zrekonstruowany_slownik)

zrekonstruowany_slownik = json.load(open("ladny.json"))
print(zrekonstruowany_slownik)