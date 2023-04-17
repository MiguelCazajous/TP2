# Trabajo práctico 2: Stack frame

## Colaboradores:
- Cazajous Miguel A.
- Marclé Emiliano
- Garella Andrés

## Description

El proyecto es una simple calculadora de cotización de criptomonedas donde la capa superior recupera la cotización de dos criptomonedas (implementación en Python) de alguna REST API y envía los datos de la consulta al código escrito en C que convoca rutinas en ensamblador para hacer los cálculos de conversión.
El resultado final es luego mostrado dentro del script en Python.

## Diseño con entorno virtual

### Entorno

Debido a que la librería en C está compilada para x86, debemos usar python compatible con esa arquitectura.
Para ese propósito se creó un entorno virtual (virtual env) usando `conda`

- Seteamos variable de entorno
`export CONDA_FORCE_32BIT=1`

- Creamos el entorno
`conda create -n TP2 python=3.7`
**3.7 is the last version compatible with 32bits https://repo.anaconda.com/pkgs/**

- Activamos el entorno
`conda activate TP2`

### API REST

La API REST elegida es financialmodelingprep, mediante un simple registro con una cuenta de gmail ya disponemos de un TOKEN para hacer requests, además de que la documentación es muy intuitiva, completa y proporciona la información necesaria para nuestra implementación.

Más información: https://site.financialmodelingprep.com/developer/docs/

Se hizo uso de la librería json-c para el manejo de archivos JSON dentro de nuestra librería. De esta forma podemos manipular de manera sencilla la información que viene
desde la parte de frontend.

Para más información: https://github.com/json-c/json-c

Los datos enviados desde Python al código en C es en formato JSON string que es como el que se muestra a continuación

<details>
<summary> Expandir </summary>

```json
[
  {
    "symbol": "BTCUSD",
    "price": 30424.96
  },
  {
    "symbol": "ETHUSD",
    "price": 2020.1797
  },
  {
    "symbol": "USDARS",
    "price": 214.67
  },
  {
    "symbol": "USDEUR",
    "price": 0.9042
  }
]
```

</details>

La respuesta que el código C envía a Python con el resultado de los cálculos es como sigue.

<details>
<summary>Expandir</summary>

```json
[
  {
    "symbol": "BTCUSD",
    "price": 30424.96
  },
  {
    "symbol": "ETHUSD",
    "price": 2020.1797
  },
  {
    "symbol": "BTCARG",
    "price": "0.0"
  },
  {
    "symbol": "BTCEUR",
    "price": "0.0"
  },
  {
    "symbol": "ETHARG",
    "price": "0.0"
  },
  {
    "symbol": "ETHEUR",
    "price": "0.0"
  }
]

```

</details>

**Donde los valores "0.0" serán los valores calculados mediante la librería de conversión**

## Diseño simplificado

Para este diseño simple de la calculadora de cotización de criptomonedas se trabajó en Python para realizar las solicitudes a las API REST, invocar programa en lenguaje C e impresión de resultados.

### APIs utilizadas

Este diseño utiliza dos API REST:

- Cotización de criptomoneda: https://binance-docs.github.io/apidocs/spot/en/#general-info
- Factores de conversión de divisas: https://www.exchangerate-api.com/docs/standard-requests

### Python

Mediante la librería **requests** para Python, el script realiza solicitudes a las http donde se encuentran los API, las cuales se declararon como:

- url_1: avgPrice del Bitcoin en dólares (BTCUSD) 
- url_2: avgPrice del Etherum en dólares (ETHUSD)
- url_3: tasas de cambio (exchangerate) a USD

La librería **json** se utiliza luego para formatear los datos de una manera más legible.

```Py
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
```
Con la función **run** del módulo **subprocess** se invoca un programa de C que es el encargado de realizar los cálculos de conversión.
Se pasa los parámetros en formato str y con el parámetro **capture_output = True** se indica que se capturará la salida del programa ejecutado.
```Py
# Cálculos de conversión con floats
BTC_to_EUR = subprocess.run(["./converter_float_ejecutable", str(BTCUSD) , str(USD_to_EUR)], capture_output = True)
BTC_to_ARS = subprocess.run(["./converter_float_ejecutable", str(BTCUSD) , str(USD_to_ARS)], capture_output = True)
ETH_to_EUR = subprocess.run(["./converter_float_ejecutable", str(ETHUSD) , str(USD_to_EUR)], capture_output = True)
ETH_to_ARS = subprocess.run(["./converter_float_ejecutable", str(ETHUSD) , str(USD_to_ARS)], capture_output = True)
```
Los resultados de los cálculos se imprimen finalmente dentro del script de Python.
```Py
print("Precio del Bitcoin (BTC) en Euros (EUR): ", float(BTC_to_EUR.stdout))
print("Precio del Bitcoin (BTC) en pesos argentinos (ARS): ", float(BTC_to_ARS.stdout))
print("Precio de Ethereum (ETH) en Euros (EUR): ", float(ETH_to_EUR.stdout))
print("Precio de Ethereum (ETH) en pesos argentinos (ARS): ", float(ETH_to_ARS.stdout))
```
### Programa en C

```C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "cdecl.h"

extern float converter_float(float, float);

int main(int argc, char *argv[])
{
   if(argc != 3){
       printf("Número de parámetros no válido.\n");
       exit(1);
   }
  
   float source_currency = atof(argv[1]);    // Criptomoneda en USD
   float convertion_factor = atof(argv[2]);  // Factor de conversión a EUR o ARS
   float dest_currency = converter_float( source_currency, convertion_factor);

   printf("%f\n",dest_currency);
    return 0;
}
```
En el programa en C , la función main tiene dos parámetros, **argc** que indica la cantidad de parámetros pasados y **argv** que es un array de punteros a str y contiene los argumentos que se pasaron al invocar el programa
Con la función **atof** se convierte los argumentos str en números de punto flotante que se almacenan en las variables:

- source_currency: Cotización de criptomoneda en USD
- convertion_factor: Tasa de conversion a EUR o ARS

Para realizar los cálculos se invoca una rutina en lenguaje ensamblador, y el resultado se guarda en la variable dest_currency.
El resultado se imprime mediante printf , y luego este valor de salida es capturado e imprimido en Python.

### Código Assembler

El programa en lenguaje ensamblador define dos macros mediante las directivas %define.
```
%define source_currency     dword  [ebp+8]
%define convertion_factor   dword  [ebp+12]
```
Primero se guarda el registro EBX original y se hace EBP = ESP.
Con la instrucción de punto flotante **fld** se carga source_currency en la cima de la pila. 
Con **fmul** se hace la multiplicación en punto flotante con el factor de conversión y el resultado queda en el registro **ST0**.
Antes de retornar se hace el pop del registro EBP original.

```
converter_float:
       push    ebp                     ; Se guarda el EBX original
       mov     ebp, esp                ; EBP = ESP


       fld     source_currency;        ; stack: source_currency
       fmul    convertion_factor       ; stack: source_currency * convertion_factor


       pop     ebp
       ret
```
