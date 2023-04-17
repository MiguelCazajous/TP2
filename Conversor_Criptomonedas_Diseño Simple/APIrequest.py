# from ctypes import *
import subprocess
import json
import requests

# APIs
url_1 = 'https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT'
url_2 = 'https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT'
url_3 = 'https://v6.exchangerate-api.com/v6/e82e98773d1e8ed35949e3b1/latest/USD'

# Solicitudes a API
response1 = requests.get(url_1)
response2 = requests.get(url_2)
response3 = requests.get(url_3)
data = response1.json()
data2 = response2.json()
data3 = response3.json()

# Obtención de cotización de BTC y ETH en USD
BTCUSD =  data['price']
ETHUSD = data2['price']
print("Cotización de BTC (USD): ", BTCUSD)
print("Cotización de ETH (USD): ", ETHUSD)

# Obtención de factor de conversión de USD a EUR y ARS
USD_to_EUR   =  data3['conversion_rates']['EUR']
USD_to_ARS   =  data3['conversion_rates']['ARS']
print("Factor de conversión de USD a EUR: ", USD_to_EUR)
print("Factor de conversión de USD a ARS: ", USD_to_ARS)

# Cálculos de conversión con floats
BTC_to_EUR = subprocess.run(["./converter_float_ejecutable", str(BTCUSD) , str(USD_to_EUR)], capture_output = True)
BTC_to_ARS = subprocess.run(["./converter_float_ejecutable", str(BTCUSD) , str(USD_to_ARS)], capture_output = True)
ETH_to_EUR = subprocess.run(["./converter_float_ejecutable", str(ETHUSD) , str(USD_to_EUR)], capture_output = True)
ETH_to_ARS = subprocess.run(["./converter_float_ejecutable", str(ETHUSD) , str(USD_to_ARS)], capture_output = True)

# Impresión de resultados
print("Precio del Bitcoin (BTC) en Euros (EUR): ", float(BTC_to_EUR.stdout))
print("Precio del Bitcoin (BTC) en pesos argentinos (ARS): ", float(BTC_to_ARS.stdout))
print("Precio de Ethereum (ETH) en Euros (EUR): ", float(ETH_to_EUR.stdout))
print("Precio de Ethereum (ETH) en pesos argentinos (ARS): ", float(ETH_to_ARS.stdout))










