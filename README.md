# MicroBanco - Proyecto de Testing
## Clase 12: Pruebas Automatizadas

Este proyecto simula una API básica de servicios bancarios para aprender testing automatizado con Python y pytest.

## Instalación

1. Asegúrate de tener Python 3.7+ instalado:
```bash
python --version
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecuta los tests:
```bash
pytest -v tests/
```

## Estructura del Proyecto

```
microbanco_project/
├── src/
│   ├── __init__.py
│   └── microbanco.py        # API principal de MicroBanco
├── tests/
│   ├── __init__.py
│   └── test_microbanco.py   # Tests para la API
├── requirements.txt         # Dependencias del proyecto
└── README.md               # Este archivo
```

## Funcionalidades a Testear

### 1. Transferir Dinero
- Transferencias exitosas
- Validación de montos negativos
- Validación de cuentas inexistentes
- Validación de saldo insuficiente

### 2. Calcular Interés
- Cálculo con valores normales
- Manejo de días = 0
- Manejo de tasas negativas
- Manejo de capitales muy grandes

### 3. Validar Cuenta
- Formatos válidos de cuenta
- Formatos inválidos
- Cuentas nulas o vacías
- Longitudes incorrectas

## Casos de Prueba Sugeridos

### Tests Positivos (Deberían funcionar):
- `test_transferir_monto_positivo()`
- `test_calcular_interes_normal()`
- `test_validar_cuenta_valida()`

### Tests Negativos (Deberían fallar elegantemente):
- `test_transferir_monto_negativo()`
- `test_calcular_interes_dias_cero()`
- `test_validar_cuenta_formato_incorrecto()`

## Comandos Útiles

```bash
# Ejecutar todos los tests
pytest

# Ejecutar con más detalle
pytest -v

# Ejecutar con cobertura
pytest --cov=src

# Ejecutar un test específico
pytest tests/test_microbanco.py::test_transferir_monto_positivo
```

## Para Sprint 2

Este ejercicio te prepara para implementar testing en tu proyecto real. Considera:

1. ¿Cuáles son las 3 funciones más críticas de tu proyecto?
2. ¿Qué tipo de pruebas necesita cada una?
3. ¿Qué framework de testing usarás en tu tecnología?

¡Buena suerte, Testing Heroes! 🚀