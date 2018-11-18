import requests

def getPopulation():
    response = requests.get('https://pkgstore.datahub.io/core/population/population_json/data/43d34c2353cbd16a0aa8cadfb193af05/population_json.json')
    return response.json()

