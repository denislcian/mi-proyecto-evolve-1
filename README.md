# Conversor de Unidades en Python

Un conversor de unidades sencillo y práctico desarrollado con Python. Permite realizar conversiones de longitud, temperatura y masa desde la terminal.

## Estructura del Proyecto

```
mi-proyecto-evolve/
│
├── scripts/
├── src/
│   └── conversores/
│       ├── __init__.py
│       ├── longitud.py
│       ├── temperatura.py
│       └── masa.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_longitud.py
│   ├── test_temperatura.py
│   └── test_masa.py
├── .gitignore
├── README.md
├── requirements.txt
└── setup.py
```


## Desarrollo

1. Clona este repositorio
   ```bash
   git clone https://github.com/denislcian/mi-proyecto-evolve-1.git
   cd mi-proyecto-evolve
   ```
2. Accede a la carpeta src:
   ```bash
   cd src
   ```
3. Ejecuta el programa:
   ```bash
   python main.py
   ```
No necesitas instalar nada mas, solo tener Python 3 instalado en tu PC

## Como funciona
Al ejecutar el programa, aparecerá un menú interactivo con las siguientes opciones:

1. Metros a Kilómetros
2. Pulgadas a Centímetros
3. Celsius a Fahrenheit
4. Gramos a Kilos

El usuario selecciona una opción e introduce el valor a convertir. El programa muestra el resultado de la conversión en pantalla.


## Ejemplo de uso
```text
Conversor de Unidades
1. Metros a Kilómetros
2. Pulgadas a Centímetros
3. Celsius a Fahrenheit
4. Gramos a Kilos
Elige una opción (1-4): 1
Introduce metros: 1500
1500.0 metros son 1.5 kilómetros
```
## Pruebas

El proyecto incluye una carpeta tests con pruebas automaticas. Para ejecutarlas, puedes usar cualquier framework de testing como pytest:
```bash
pytest tests/
```

## Tecnologías utilizadas

** Python 3.x

No requiere librerias externas

## Licencia

Este proyecto es de uso libre con fines educativos