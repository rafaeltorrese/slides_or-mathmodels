---
title: "Requisitos para Cursar la Materia"
...

# Herramientas que se usarán en la materia


## Correo Institucional Gmail
Solicitar cuenta institucional de Google Workspace for Education Fundamentals.  Es de dominio institucional, lo cual te ayudará a separar tus herramientas personales de las académicas o profesionales. Hacer la solicitud en este enlace: [Google Workspace for Education Fundamentals](https://sites.google.com/universidad.anahuac.mx/software-anahuac-mexico/google-workspace)


## Anaconda Python

Durante el curso estaremos usando el lenguaje de programción Python. Puedes trabajar de manera local o remota. Si usted desea trabajar de manera local puede hacer la descarga de la descarga en el siguiente enlace: [Distribución Anaconda Python](https://www.anaconda.com/download). Recuerde elegir la descarga correspondiente a su sistema operativo.

## Gurobi Python
Para resolver los modelos de optimización propuestos usaremos un optimizador que requiere [una licencia](https://portal.gurobi.com/iam/register/), por lo anterior se le pide hacer su registro en la siguiente página [Gurobi Academic WLS license](https://www.gurobi.com/features/academic-wls-license/)  para obtener una [licencia académica](https://portal.gurobi.com/iam/register/).

Las instrucciones para instalar la licencia en su notebook con Google Colab están aquí: [Google Colab: Installation and Licensing](https://support.gurobi.com/hc/en-us/articles/4409582394769-Google-Colab-Installation-and-Licensing). Le sugiero colocar todas las intrucciones en la primer celda de su notebook.

```python
# Create an environment with your WLS license
params = {
"WLSACCESSID": 'your wls accessid (string)',
"WLSSECRET": 'your wls secret (string)',
"LICENSEID": <your license id (integer)>,
           }

!pip install gurobipy>=10
import gurobipy as gp

env = gp.Env(params=params)

# Create the model within the Gurobi environment
model = gp.Model(env=env)

```

## Trabajo en Equipos

Vamos a trabajar en equipos de tres integrantes. Solo un equipo tendrá 3 integrantes. El próximo lunes les pediré la lista de integrantes por de cada equipo. Ponerse de acuerdo entre ustedes caso contrario integraré los equipos.