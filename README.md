# Trabajo práctico 2: Stack frame

## Colaboradores:
- Cazajous Miguel A.
- Marclé Emiliano
- Garella Andrés

## Description

El proyecto es una calculadora de cotización de criptomonedas donde la capa superior recupera la cotización de dos criptomonedas (implementación en Python) de alguna REST API y envía los datos de la consulta al código escrito en C que convoca rutinas en ensamblador para hacer los cálculos de conversión.
El resultado final es luego mostrado dentro del script en Python.

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

