"""
Tests para MicroBanco API - Testing Masterclass 2025-2
=====================================================

Este archivo contiene las pruebas automatizadas para la API de MicroBanco.
Los estudiantes completarán estos tests durante el challenge hands-on.

Comandos para ejecutar:
- pytest tests/test_microbanco.py -v
- pytest tests/test_microbanco.py::test_transferir_monto_positivo -v
- pytest --cov=src tests/
"""

import pytest
from src.microbanco import MicroBanco, crear_banco_con_datos_test


class TestMicroBanco:
    """Suite de pruebas para la clase MicroBanco"""
    
    def setup_method(self):
        """
        Configuración que se ejecuta antes de cada test
        Crea una instancia fresca de MicroBanco para cada prueba
        """
        self.banco = crear_banco_con_datos_test()
    
    # ========================================
    # TESTS PARA TRANSFERIR DINERO
    # ========================================
    
    def test_transferir_monto_positivo(self):
        """
        Test básico: Transferencia exitosa con monto positivo
        Este test está completo como ejemplo para los estudiantes
        """
        # ARRANGE (Preparar)
        cuenta_origen = "123456"  # Tiene $1000
        cuenta_destino = "789012"  # Tiene $2500
        monto = 100.0
        
        # ACT (Actuar)
        resultado = self.banco.transferir(cuenta_origen, cuenta_destino, monto)
        
        # ASSERT (Verificar)
        assert resultado["status"] == "exitoso"
        assert resultado["monto"] == 100.0
        assert resultado["mensaje"] == "Transferencia realizada exitosamente"
        assert resultado["saldo_origen"] == 900.0  # 1000 - 100
        assert resultado["saldo_destino"] == 2600.0  # 2500 + 100
    
    def test_transferir_monto_negativo(self):
        """
        Test negativo: ¿Qué pasa si intentamos transferir monto negativo?
        ESTUDIANTES: Completar este test
        """
        # ARRANGE
        cuenta_origen = "123456"
        cuenta_destino = "789012" 
        monto = -100.0  # ¡Monto negativo!
        
        # ACT
        resultado = self.banco.transferir(cuenta_origen, cuenta_destino, monto)
        
        # ASSERT - ¿Qué esperamos que pase?
        # ESTUDIANTES: Descubrir cuál es el comportamiento actual
        # y decidir si es correcto o es un bug
        pass  # TODO: Completar assertions
    
    def test_transferir_saldo_insuficiente(self):
        """
        Test negativo: Transferir más dinero del que hay en cuenta
        """
        # ARRANGE
        cuenta_origen = "567890"  # Esta cuenta tiene $0
        cuenta_destino = "123456"
        monto = 100.0
        
        # ACT
        resultado = self.banco.transferir(cuenta_origen, cuenta_destino, monto)
        
        # ASSERT
        assert resultado["status"] == "error"
        assert resultado["mensaje"] == "Saldo insuficiente"
        assert resultado["monto"] == 0
    
    def test_transferir_cuenta_origen_inexistente(self):
        """
        Test negativo: Cuenta origen no existe
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        pass
    
    def test_transferir_cuenta_destino_inexistente(self):
        """
        Test negativo: Cuenta destino no existe  
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        pass
    
    def test_transferir_cuentas_vacias(self):
        """
        Test edge case: ¿Qué pasa con strings vacíos?
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        pass
    
    # ========================================
    # TESTS PARA CALCULAR INTERÉS
    # ========================================
    
    def test_calcular_interes_caso_normal(self):
        """
        Test básico: Cálculo de interés con valores normales
        Fórmula: Interés = Capital * Tasa * (Días / 365)
        """
        # ARRANGE
        capital = 1000.0
        dias = 30
        tasa = 0.05  # 5% anual
        
        # Cálculo manual esperado: 1000 * 0.05 * (30/365) = 4.11 aprox
        interes_esperado = round(1000 * 0.05 * (30/365), 2)
        
        # ACT
        interes_calculado = self.banco.calcular_interes(capital, dias, tasa)
        
        # ASSERT
        assert interes_calculado == interes_esperado
        assert isinstance(interes_calculado, float)
    
    def test_calcular_interes_dias_cero(self):
        """
        Test edge case: ¿Qué pasa si días = 0?
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        # ¿El resultado debería ser 0? ¿O debería dar error?
        pass
    
    def test_calcular_interes_capital_negativo(self):
        """
        Test edge case: ¿Qué pasa con capital negativo?
        ESTUDIANTES: Completar este test  
        """
        # TODO: Implementar test
        pass
    
    def test_calcular_interes_tasa_negativa(self):
        """
        Test edge case: ¿Qué pasa con tasa negativa?
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        pass
    
    def test_calcular_interes_valores_muy_grandes(self):
        """
        Test edge case: ¿Qué pasa con números muy grandes?
        ¿Hay overflow? ¿Problemas de precisión?
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test con capital = 999999999999
        pass
    
    # ========================================
    # TESTS PARA VALIDAR CUENTA
    # ========================================
    
    def test_validar_cuenta_formato_correcto(self):
        """
        Test básico: Cuenta con formato correcto (6 dígitos)
        """
        # ARRANGE & ACT & ASSERT - Casos válidos
        assert self.banco.validar_cuenta("123456") == True
        assert self.banco.validar_cuenta("000001") == True  
        assert self.banco.validar_cuenta("999999") == True
        assert self.banco.validar_cuenta("000000") == True
    
    def test_validar_cuenta_formato_incorrecto_longitud(self):
        """
        Test negativo: Longitudes incorrectas
        """
        # ASSERT - Muy corto
        assert self.banco.validar_cuenta("12345") == False   # 5 dígitos
        assert self.banco.validar_cuenta("1") == False       # 1 dígito
        assert self.banco.validar_cuenta("") == False        # Vacío
        
        # ASSERT - Muy largo
        assert self.banco.validar_cuenta("1234567") == False # 7 dígitos
        assert self.banco.validar_cuenta("12345678901234567890") == False
    
    def test_validar_cuenta_formato_incorrecto_caracteres(self):
        """
        Test negativo: Caracteres no numéricos
        ESTUDIANTES: Completar este test
        """
        # TODO: Testear casos como "abc123", "12a456", "123-45", etc.
        pass
    
    def test_validar_cuenta_none_y_tipos_incorrectos(self):
        """
        Test edge case: ¿Qué pasa con None y otros tipos?
        ESTUDIANTES: Completar este test
        """
        # TODO: Testear None, números enteros, listas, etc.
        pass
    
    # ========================================
    # TESTS PARA CONSULTAR SALDO
    # ========================================
    
    def test_consultar_saldo_cuenta_existente(self):
        """
        Test básico: Consultar saldo de cuenta que existe
        """
        # ACT
        resultado = self.banco.consultar_saldo("123456")
        
        # ASSERT
        assert resultado["status"] == "exitoso"
        assert resultado["saldo"] == 1000.0
        assert "fecha" in resultado
    
    def test_consultar_saldo_cuenta_inexistente(self):
        """
        Test negativo: Consultar cuenta que no existe
        ESTUDIANTES: Completar este test
        """
        # TODO: Implementar test
        pass
    
    # ========================================
    # TESTS DE INTEGRACIÓN
    # ========================================
    
    def test_flujo_completo_transferencia_y_consulta(self):
        """
        Test de integración: Hacer transferencia y verificar saldos
        ESTUDIANTES: Completar este test
        """
        # TODO: 
        # 1. Consultar saldos iniciales
        # 2. Hacer transferencia
        # 3. Consultar saldos finales
        # 4. Verificar que todo cuadra
        pass
    
    def test_multiples_transferencias_misma_cuenta(self):
        """
        Test de integración: Hacer varias transferencias seguidas
        ESTUDIANTES: Completar este test
        """
        # TODO: Hacer 3-4 transferencias y verificar saldos finales
        pass


# ========================================
# TESTS PARAMÉTRICOS (AVANZADO)
# ========================================

class TestParametricos:
    """
    Tests paramétricos para probar múltiples casos con el mismo código
    Estos son opcionales/avanzados para estudiantes que terminen temprano
    """
    
    def setup_method(self):
        self.banco = crear_banco_con_datos_test()
    
    @pytest.mark.parametrize("cuenta,esperado", [
        ("123456", True),
        ("000001", True), 
        ("999999", True),
        ("12345", False),   # Muy corto
        ("1234567", False), # Muy largo
        ("abc123", False),  # Con letras
        ("", False),        # Vacío
    ])
    def test_validar_cuenta_casos_multiples(self, cuenta, esperado):
        """
        Test paramétrico: Validar múltiples formatos de cuenta
        """
        resultado = self.banco.validar_cuenta(cuenta)
        assert resultado == esperado
    
    @pytest.mark.parametrize("capital,dias,tasa", [
        (1000, 30, 0.05),
        (500, 15, 0.03),
        (2000, 60, 0.07),
    ])
    def test_calcular_interes_casos_multiples(self, capital, dias, tasa):
        """
        Test paramétrico: Calcular interés con diferentes valores
        """
        interes = self.banco.calcular_interes(capital, dias, tasa)
        # El interés debería ser positivo para estos casos
        assert interes > 0
        assert isinstance(interes, float)


# ========================================
# FIXTURES PARA CASOS ESPECIALES
# ========================================

@pytest.fixture
def banco_vacio():
    """
    Fixture: Banco sin cuentas para tests especiales
    """
    banco = MicroBanco()
    banco.cuentas_activas = []
    banco.saldos = {}
    return banco


class TestCasosEspeciales:
    """Tests con fixtures especiales"""
    
    def test_transferir_sin_cuentas_activas(self, banco_vacio):
        """
        Test con fixture: ¿Qué pasa si no hay cuentas activas?
        """
        resultado = banco_vacio.transferir("123456", "789012", 100)
        assert resultado["status"] == "error"


if __name__ == "__main__":
    # Ejecutar tests si se corre el archivo directamente
    pytest.main([__file__, "-v"])