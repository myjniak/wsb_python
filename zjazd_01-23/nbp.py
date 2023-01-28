from typing import List

import requests
from pydantic import BaseModel

response = requests.get("https://api.nbp.pl/api/exchangerates/rates/a/usd/last/10")


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float


class TableA(BaseModel):
    table: str
    code: str
    currency: str
    rates: List[Rate]


# Kiedy kurs dolara był najwyższy?


json_resp = response.json()
table = TableA(**json_resp)

biggest_rate = max(table.rates, key=lambda rate: rate.mid)
print(f"{biggest_rate.effectiveDate} kurs dolara byl najwyzszy i wynosil {biggest_rate.mid}")
