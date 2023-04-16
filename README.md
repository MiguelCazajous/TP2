# Trabajo práctico 2: Stack frame

## Colaboradores:
- Cazajous Miguel A.
- Marclé Emiliano
- Garella Andrés

## Entorno

Debido a que la librería en C está compilada para x86, debemos usar python compatible con esa arquitectura.
Para ese propósito se creó un entorno virtual (virtual env) usando `conda`

- Seteamos variable de entorno
`export CONDA_FORCE_32BIT=1`

- Creamos el entorno
`conda create -n TP2 python=3.7`
**3.7 is the last version compatible with 32bits https://repo.anaconda.com/pkgs/**

- Activamos el entorno
`conda activate TP2`

## Description

El proyecto es una simple calculadora de cotización de criptomonedas donde la capa superior recupera la cotización de dos criptomonedas (implementación en Python) de alguna REST API y envía los datos de la consulta al código escrito en C que convoca rutinas en ensamblador para hacer los cálculos de conversión.
El resultado final es luego mostrado dentro del script en Python.

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
