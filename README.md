# MicroBanco - Proyecto Testing Discovery Challenge
## Clase 12: Pruebas Automatizadas (Versión Discovery)

**🎯 OBJETIVO:** Crear tests desde cero mediante descubrimiento colaborativo

## ¿Qué es diferente en esta versión?

- ❌ **NO** hay ejemplos de tests completos
- ✅ **SÍ** hay código real con bugs para encontrar
- ✅ **SÍ** hay coverage analysis integrado
- ✅ **SÍ** hay discovery auténtico

## Instalación

1. Clonar/descargar este proyecto
2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Explorar el código:
```bash
python src/microbanco.py
```

4. Crear tu primer test:
```bash
# El archivo tests/test_microbanco.py está vacío
# ¡Es tu trabajo llenarlo!
```

## Tu Challenge

### 🎯 **Meta Principal:**
Crear una suite de tests que tenga **80%+ de coverage** y encuentre los bugs ocultos en MicroBanco.

### 📊 **Comandos de Coverage:**
```bash
# Tests básicos
pytest tests/ -v

# Con coverage
pytest --cov=src tests/

# Coverage detallado con líneas faltantes
pytest --cov=src --cov-report=term-missing tests/

# Coverage con reporte HTML bonito
pytest --cov=src --cov-report=html tests/
# Después abre: htmlcov/index.html
```

### 🐛 **Bugs a Encontrar:**
El código de MicroBanco tiene **al menos 3 bugs intencionales**. ¿Puedes encontrarlos todos?

### 🏆 **Targets de Success:**
- 📝 **Mínimo 5 tests** diferentes
- 📊 **Coverage 80%+** 
- 🐛 **Al menos 2 bugs** encontrados
- ✅ **Todos los tests** pasan (después de arreglar bugs)

## Funciones a Testear

### 1. `transferir(origen, destino, monto)`
- ¿Qué pasa con montos negativos?
- ¿Qué pasa si las cuentas no existen?
- ¿Qué pasa si no hay saldo suficiente?

### 2. `calcular_interes(capital, dias, tasa)`  
- ¿Qué pasa si días = 0?
- ¿Qué pasa con números muy grandes?
- ¿Qué pasa con valores negativos?

### 3. `validar_cuenta(numero_cuenta)`
- ¿Qué formatos son válidos?
- ¿Qué pasa con None o strings vacíos?
- ¿Qué pasa con caracteres especiales?

### 4. `consultar_saldo(numero_cuenta)`
- ¿Funciona con cuentas válidas?
- ¿Maneja cuentas inválidas correctamente?

## Tips para el Success

### 🔍 **Strategy de Testing:**
1. **Empieza simple**: Un test que funcione
2. **Piensa en edge cases**: ¿Qué puede salir mal?
3. **Usa coverage**: Identifica código no testeado
4. **Busca bugs**: Si algo se ve raro, ¡probablemente lo es!

### ⚡ **Pytest Tips:**
```python
# Estructura básica de un test
def test_nombre_descriptivo():
    # ARRANGE: Preparar datos
    banco = MicroBanco()
    
    # ACT: Ejecutar función
    resultado = banco.alguna_funcion()
    
    # ASSERT: Verificar resultado
    assert resultado == valor_esperado
```

### 📊 **Coverage Tips:**
- **Verde** = línea testeada ✅
- **Rojo** = línea NO testeada ❌
- **Target**: Todas las líneas importantes en verde

## Recursos

### 📚 **Documentación:**
- [pytest docs](https://docs.pytest.org/)
- [coverage docs](https://coverage.readthedocs.io/)

### 🆘 **Si te atascas:**
1. Lee los mensajes de error cuidadosamente
2. Usa `print()` para debug
3. Pregunta al instructor
4. Colabora con otros equipos

## 🏁 **Entrega Final**

Al terminar debes tener:
- `tests/test_microbanco.py` con tus tests
- Coverage report mostrando 80%+
- Lista de bugs encontrados
- Plan de mejoras para el código

**¡Good luck, Testing Heroes!** 🚀