# Descripción General

mi_conversor es una librería Python que ofrece funciones para convertir:

Metros a kilómetros

Pulgadas a centímetros

Gramos a Kilos

Celsius a Fahrenheit

Fahrenheit a Celsius

El objetivo es practicar la creación de paquetes Python reutilizables, con estructura profesional, documentación y ejemplos de uso.

## Estructura del Proyecto

```
mi-proyecto-evolve-1/
│
├── src/
│   └── mi_conversor/
│       ├── __init__.py
│       ├── longitud.py
│       ├── temperatura.py
│       └── masa.py
├── tests/
│   ├──  __init__.py
│   ├── test_longitud.py
│   ├── test_temperatura.py
│   └── test_masa.py
├── main.py
├── .gitignore
├── README.md
├── pyproject.toml
├── requirements.txt
└── setup.py
```


## Instalación

1. Clona este repositorio
   ```bash
   git clone https://github.com/denislcian/mi-proyecto-evolve-1.git
   cd mi-proyecto-evolve-1
   ```
2. Instala la librería en modo editable:
    ```bash
   pip install -e .
   ```

Esto permite importar mi_conversor desde cualquier script Python en tu entorno 

## Uso
Puedes importar las funciones directamente en tu código:

```python
from mi_conversor import metros_a_kilometros, pulgadas_a_centimetros, celsius_a_fahrenheit, fahrenheit_a_celsius

print(metros_a_kilometros(1500))        # 1.5
print(pulgadas_a_centimetros(10))       # 25.4
print(gramos_a_kilos(1000))             # 1.0
print(celsius_a_fahrenheit(0))          # 32.0
print(fahrenheit_a_celsius(32))         # 0.0
```
O ejecutar el ejemplo incluido:

```bash
python main.py
```
También puedes probar en tu terminal: 
```bash
python -c "
import sys; sys.path.append('src')
from mi_conversor import *
print('Conversiones:')
print(f'1000m = {metros_a_kilometros(1000)}km')
print(f'100 pulgadas = {pulgadas_a_centimetros(100)}cm')
print(f'25°C = {celsius_a_fahrenheit(25)}°F')
"
```

## Pruebas

El proyecto incluye pruebas unitarias con pytest.

Para ejecutarlas

```bash
pytest 
```

## Documentación de funciones

metros_a_kilometros(metros): Convierte metros a kilómetros.

pulgadas_a_centimetros(pulgadas): Convierte pulgadas a centímetros.

celsius_a_fahrenheit(celsius): Convierte grados Celsius a Fahrenheit.

fahrenheit_a_celsius(fahrenheit): Convierte grados Fahrenheit a Celsius.


## Requisitos 
** Python 3.7 o superior

** No requiere dependencias externas

## Autor

DENIS LUCIAN MORAR OCHIS 

## Licencia

Uso educativo 

## Notas 

El proyecto está subido a GitHub en la rama main.

Puedes modificar o ampliar la librería fácilmente añadiendo nuevas funciones y módulos.

Si tienes dudas o sugerencias, abre un issue en el repositorio.

