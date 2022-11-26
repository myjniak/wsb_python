import json


akapit = """My name is Bonnie. I was born and raised in New York 
and summered in the Hamptons, where I learned to sail.
 I was the junior sail champion at the Hampton Yacht Club
  for many years running. I got my law degree at NYU and practiced 
  for 10 years with Bretz & Coven LLP on Broadway. I hated it."""


def dolicz_slowo_do_slownika(d: dict, s: str):
    d.setdefault(s, 0)
    d[s] += 1


def ladny_print_slownika(d: dict):
    print(json.dumps(d, indent=4))
    # for key, value in d.items():
    #     print(f"{key}: {value}")


def sformatuj_slowo(s: str) -> str:
    return s.replace(",", "").replace(".", "").lower()


d = {}

for s in akapit.split():
    s = sformatuj_slowo(s)
    dolicz_slowo_do_slownika(d, s)

ladny_print_slownika(d)
