# Ejercicio 01 — Servicio HTTP básico con FastAPI

## Objetivo

Crear desde cero un pequeño servicio HTTP con **Python + FastAPI** para practicar:

* Crear y levantar un servicio.
* Recibir JSON.
* Trabajar con diccionarios.
* Acceder a claves y listas.
* Validar datos.
* Crear funciones.
* Devolver respuestas JSON.
* Manejar errores HTTP.
* Probar una API con `curl`.

---

## Herramientas

Usar únicamente:

* Python
* `venv`
* FastAPI
* Uvicorn
* `curl`

Puedes consultar:

* Documentación oficial.
* Google.
* Stack Overflow.

No usar IA para generar el código.

---

## Preparación

Crear el proyecto:

```bash
mkdir ejercicio_fastapi_01
cd ejercicio_fastapi_01

python3 -m venv .venv
source .venv/bin/activate

pip install fastapi uvicorn
```

Estructura mínima:

```text
ejercicio_fastapi_01/
├── .venv/
└── main.py
```

El servicio debe poder arrancarse con:

```bash
python -m uvicorn main:app --reload
```

Al finalizar debes entender qué significan:

* `python -m uvicorn`
* `main`
* `app`
* `--reload`

---

# Requisitos

## 1. Endpoint `GET /health`

Debe responder:

```json
{
    "status": "ok"
}
```

---

## 2. Endpoint `POST /v1/turn`

Debe recibir un JSON como:

```json
{
    "user_id": 2,
    "user_name": "Adria",
    "message": "Quiero consultar mis facturas",
    "allowed_company_ids": [1, 3, 7]
}
```

El payload debe recibirse inicialmente como un **diccionario Python**.

Debes trabajar con valores como:

```python
payload["user_id"]
payload["message"]
payload["allowed_company_ids"]
```

Investiga también la diferencia entre:

```python
diccionario["clave"]
```

y:

```python
diccionario.get("clave")
```

---

## Respuesta esperada

Construir una respuesta similar a:

```json
{
    "received": true,
    "user": {
        "id": 2,
        "name": "Adria"
    },
    "message": {
        "text": "Quiero consultar mis facturas",
        "length": 28
    },
    "companies_count": 3
}
```

---

# Validaciones

Los siguientes campos son obligatorios:

```text
user_id
message
```

Si falta alguno, responder con HTTP `400`.

Ejemplo:

```json
{
    "detail": "user_id and message are required"
}
```

Investigar:

```text
FastAPI HTTPException
```

---

Un mensaje compuesto únicamente por espacios también debe considerarse inválido:

```json
{
    "user_id": 2,
    "message": "     "
}
```

Investigar:

```text
Python string strip
```

---

# Organización del código

No realizar toda la lógica dentro del endpoint.

Crear **al menos una función Python independiente** encargada de parte del procesamiento.

Conceptualmente:

```text
endpoint
   ↓
función Python
   ↓
diccionario de respuesta
```

---

# Pruebas obligatorias

Probar el servidor usando `curl`.

## Prueba 1

```text
GET /health
```

Debe devolver:

```json
{
    "status": "ok"
}
```

---

## Prueba 2

Enviar un `POST /v1/turn` con un payload correcto.

---

## Prueba 3

Enviar un payload sin:

```text
user_id
```

Debe devolver HTTP `400`.

---

## Prueba 4

Enviar:

```json
{
    "user_id": 2,
    "message": "   "
}
```

Debe devolver HTTP `400`.

---

# Conceptos a investigar

Buscar únicamente lo necesario para resolver el ejercicio:

```text
Python dictionary get
Python dictionary key exists
Python string strip
Python len list

FastAPI basic app
FastAPI GET endpoint
FastAPI POST request body dict
FastAPI HTTPException

Uvicorn run FastAPI application

curl POST JSON
```

Priorizar documentación oficial.

---

# Restricciones

No utilizar:

* Pydantic `BaseModel`.
* `dataclass`.
* PostgreSQL.
* Odoo.
* Docker.
* Clases innecesarias.
* Arquitecturas complejas.
* `TurnService`.
* Código generado por IA.

---

# Criterios para dar el ejercicio por terminado

Debes ser capaz de explicar:

* Cómo se levanta el servidor.
* Qué hace Uvicorn.
* Cómo llega una petición HTTP hasta una función Python.
* Cómo FastAPI convierte JSON en datos Python.
* Cómo acceder a valores de un diccionario.
* Diferencia entre `dict["clave"]` y `dict.get("clave")`.
* Cómo acceder a una lista dentro de un diccionario.
* Cómo contar elementos con `len()`.
* Cómo validar que existe una clave.
* Cómo comprobar que un string no está vacío.
* Cómo construir un nuevo diccionario.
* Cómo FastAPI devuelve ese diccionario como JSON.
* Cómo devolver un error HTTP `400`.

---

# Entrega

Entregar:

1. `main.py` completo.
2. Resultado de las pruebas realizadas con `curl`.
3. Explicación breve de cómo funciona el flujo:

```text
curl
 ↓
HTTP
 ↓
FastAPI
 ↓
endpoint
 ↓
función Python
 ↓
diccionarios
 ↓
respuesta JSON
```

Después se realizará una revisión del código antes de pasar al siguiente ejercicio.
