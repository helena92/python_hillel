from pygal.maps.world import COUNTRIES


def getCountryCode(country):
    for code, name in COUNTRIES.items():
        if country == name:
            return code
    return None