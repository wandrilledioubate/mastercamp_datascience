
import json 
import requests
import matplotlib.pyplot as plt
from datetime import datetime


url="http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=VU9TRFYoUHICL1NkUCZSe1c%2FDjsPeQAnVysAY1w5VisBagRlBmYGYARqUi9SfQcxUH1SMVtgBDRUP1UtWigDYlU%2FUz9WPVA3Am1TNlB%2FUnlXeQ5vDy8AJ1c2AGZcNlYrAWAEZgZ7BmYEa1I0UnwHMVBnUjVbewQjVDZVNFo%2FA2ZVNFM3Vj1QNwJoUzNQf1J5V2IOag84ADlXPABnXDNWPQFiBDIGYQZmBGtSMFJ8BzZQZlIzW2cEPlQzVTNaNQN%2FVSlTTlZGUC8CLVNzUDVSIFd5DjsPbgBs&_c=fb54283835e3bfb68a87b45016a5a6dc"

try:
    api_request=requests.get(url)
    data=json.loads(api_request.content)
except Exception as e:
    data="Error..."


# d. Vérifiez le type(data), il s’agit bien d’un dictionnaire, Explorez data. (for k in data, for k, v in..)

print(type(data))  

for k in data:
    print(k)  

for k, v in data.items():
    print(k, v) 



# e. Vérifiez data des clés suivantes : request_state, request_key, message, model_run, source

keys_to_check = ['request_state', 'request_key', 'message', 'model_run', 'source']
for key in keys_to_check:
    if key in data:
        print(f'La clé {key} existe dans data et sa valeur est {data[key]}')
    else:
        print(f'La clé {key} n\'existe pas dans data')

# f. Supprimez-les de votre dictionnaire

for key in keys_to_check:
    data.pop(key, None)

# g. Explorez la valeur pour une clé (texte représentant une date) et vérifiez bien qu’il s’agit d’un dictionnaire également.

print(data['2023-06-09 08:00:00'])
print(type(data))  

# h. Comment accéder à la température à 2m à cette date? La température au sol?

date = '2023-06-09 08:00:00'
if date in data:
    temp_2m = data[date]['temperature']['2m']
    temp_sol = data[date]['temperature']['sol']
    print(f"Température à 2m : {temp_2m}")
    print(f"Température au sol : {temp_sol}")
else:
    print("Aucune donnée disponible pour cette date.")



# i. Comment accéder à l’humidité?

date = '2023-06-09 08:00:00'
if date in data:
    if 'humidite' in data[date]:
        humidity = data[date]['humidite']
        print(f"Humidité : {humidity}")
    else:
        print("Données d'humidité non disponibles pour cette date.")
else:
    print("Aucune donnée disponible pour cette date.")



dt=datetime.strptime("2023-06-09 08:00:00", "%Y-%m-%d %H:%M:%S")


# k. En s’appuyant sur la Compréhension des listes calculez les listes suivantes

lesDates = [datetime.strptime(date, "%Y-%m-%d %H:%M:%S") for date in data.keys() if isinstance(data[date], dict) and 'temperature' in data[date] and '2m' in data[date]['temperature']]

lesDatesStr = [date.strftime("%Y-%m-%d %H:%M:%S") for date in lesDates]
lesTempA2m = [data[date]['temperature']['2m'] - 273.15 for date in lesDatesStr]
lesTempAuSol = [data[date]['temperature']['sol'] - 273.15 for date in lesDatesStr]
lesHumiditesA2m = [data[date]['humidite']['2m'] for date in lesDatesStr]


# m. Tracez lesTempA2m, lesTempAuSol et lesHumiditesA2m en fonction de lesDates


plt.figure(figsize=(10,6))
plt.plot(lesDates, lesTempA2m, label='Température à 2m')
plt.plot(lesDates, lesTempAuSol, label='Température au sol')
plt.plot(lesDates, lesHumiditesA2m, label='Humidité à 2m')

plt.xlabel('Dates')
plt.ylabel('Valeurs')
plt.title('Température et humidité en fonction du temps')

plt.legend()

plt.show()


# %% Infoclimat avec Pandas 

import requests
import pandas as pd
import matplotlib.pyplot as plt

url="http://www.infoclimat.fr/public-api/gfs/json?_ll=48.85341,2.3488&_auth=VU9TRFYoUHICL1NkUCZSe1c%2FDjsPeQAnVysAY1w5VisBagRlBmYGYARqUi9SfQcxUH1SMVtgBDRUP1UtWigDYlU%2FUz9WPVA3Am1TNlB%2FUnlXeQ5vDy8AJ1c2AGZcNlYrAWAEZgZ7BmYEa1I0UnwHMVBnUjVbewQjVDZVNFo%2FA2ZVNFM3Vj1QNwJoUzNQf1J5V2IOag84ADlXPABnXDNWPQFiBDIGYQZmBGtSMFJ8BzZQZlIzW2cEPlQzVTNaNQN%2FVSlTTlZGUC8CLVNzUDVSIFd5DjsPbgBs&_c=fb54283835e3bfb68a87b45016a5a6dc"
api_request=requests.get(url)


api_content = api_request.content.decode('utf-8')

dfjson = pd.read_json(api_content, orient='index')


keys_to_check = ['request_state', 'request_key', 'message', 'model_run', 'source']
keys_to_drop = [key for key in keys_to_check if key in dfjson.index]
dfjson = dfjson.drop(keys_to_drop, axis=0)

dfjson.index = pd.to_datetime(dfjson.index)

dfsplited = pd.json_normalize(dfjson[0])

dfsplited.index = dfjson.index

dfsplited['temperature.2m'] -= 273.15
dfsplited['temperature.sol'] -= 273.15

# Tracer les températures et l'humidité
dfsplited[['temperature.2m', 'temperature.sol', 'humidite.2m']].plot()

plt.show()




# %% Web scraping avec Beautiful soup 

import requests
from bs4 import BeautifulSoup
import pandas as pd 

url="https://www.worldometers.info/world-population/population-by-country"

req = requests.get(url)

soup = BeautifulSoup(req.text, 'html.parser')

data = soup.find_all('table')[0]

df_population = pd.read_html(str(data), header=0)[0]

print(df_population.head())

export_csv = df_population.to_csv(r'extract.csv', index=False, header=True)



