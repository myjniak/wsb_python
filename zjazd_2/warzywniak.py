stan_warzywniaka = {
    "ziemniak": 5,
    "kalafior": 10,
    "kabaczek": 2,
    "ogorek": 24
}


def czy_jest_na_stanie(warzywo, ilosc) -> bool:
    ilosc_warzywa_na_stanie = stan_warzywniaka.get(warzywo, 0)
    print(f"Mamy {ilosc_warzywa_na_stanie} sztuk warzywa, ktore sie zwie {warzywo}")
    return ilosc_warzywa_na_stanie >= ilosc


# print(czy_jest_na_stanie("ziemniak", 11))
print("ogore" in stan_warzywniaka)