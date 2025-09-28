"""
Tests para MicroBanco API - Discovery Challenge
===============================================

🎯 TU MISIÓN: Crear tests desde cero para encontrar bugs ocultos

📊 COMANDOS ÚTILES:
- pytest tests/test_microbanco.py -v
- pytest --cov=src tests/
- pytest --cov=src --cov-report=html tests/

🏆 TARGETS:
- Mínimo 5 tests diferentes  
- Coverage 80%+
- Encontrar al menos 2 bugs
- Todos los tests deben pasar

🚀 ¡EMPIEZA AQUÍ!
"""

import pytest
from src.microbanco import MicroBanco, crear_banco_con_datos_test


# 🎯 Tu código va aquí...
# Tip: Empieza con un test simple que funcione
# Después busca edge cases y situaciones problemáticas

# ¿Qué función quieres testear primero?
# ¿Qué casos crees que pueden fallar?
# ¿Qué pasa con valores extremos?

# Estructura básica de un test:
# def test_nombre_descriptivo():
#     # ARRANGE: Preparar datos
#     banco = crear_banco_con_datos_test()
#     
#     # ACT: Ejecutar función 
#     resultado = banco.alguna_funcion()
#     
#     # ASSERT: Verificar resultado
#     assert resultado == valor_esperado


# 💡 HINTS (sin spoilers):
# - Prueba montos negativos en transferencias
# - Prueba días = 0 en cálculo de interés  
# - Prueba strings con espacios en validación
# - Prueba cuentas con formato válido pero que no existen
# - Prueba valores None como parámetros
# - Usa coverage para encontrar líneas no testeadas