"""
MicroBanco API - Sistema de Servicios Bancarios
===============================================

Esta es una simulación simple de una API bancaria para propósitos educativos.
Contiene bugs intencionales para ser encontrados mediante testing.

Autor: Testing Masterclass 2025-2
Fecha: Septiembre 2025
"""

import datetime
from typing import Dict, Union, Optional


class MicroBanco:
    """
    API principal de MicroBanco - Startup Fintech
    
    Funcionalidades principales:
    1. Transferir dinero entre cuentas
    2. Calcular interés sobre capital
    3. Validar formato de cuentas bancarias
    
    ⚠️ ADVERTENCIA: Este código contiene bugs intencionales
    para propósitos educativos de testing.
    """
    
    def __init__(self):
        """Inicializa una nueva instancia de MicroBanco"""
        self.cuentas_activas = [
            "123456", "789012", "345678", "901234", "567890"
        ]
        self.saldos = {
            "123456": 1000.0,
            "789012": 2500.0,
            "345678": 500.0,
            "901234": 10000.0,
            "567890": 0.0
        }
    
    def transferir(self, cuenta_origen: str, cuenta_destino: str, monto: float) -> Dict[str, Union[str, float]]:
        """
        Transfiere dinero entre dos cuentas bancarias
        
        Args:
            cuenta_origen: Número de cuenta que envía el dinero
            cuenta_destino: Número de cuenta que recibe el dinero  
            monto: Cantidad a transferir (debe ser positiva)
            
        Returns:
            Dict con status ("exitoso" o "error"), monto transferido y mensaje
            
        Ejemplo:
            >>> banco = MicroBanco()
            >>> resultado = banco.transferir("123456", "789012", 100.0)
            >>> print(resultado["status"])
            "exitoso"
        """
        
        # Validación básica de parámetros
        if not cuenta_origen or not cuenta_destino:
            return {
                "status": "error",
                "mensaje": "Cuentas no pueden estar vacías",
                "monto": 0
            }
        
        # ¿BUG? ¿Qué pasa si monto es negativo?
        # Los estudiantes deben encontrar este caso
        
        # Verificar que las cuentas existen
        if cuenta_origen not in self.cuentas_activas:
            return {
                "status": "error", 
                "mensaje": "Cuenta origen no existe",
                "monto": 0
            }
            
        if cuenta_destino not in self.cuentas_activas:
            return {
                "status": "error",
                "mensaje": "Cuenta destino no existe", 
                "monto": 0
            }
        
        # Verificar saldo suficiente
        if self.saldos[cuenta_origen] < monto:
            return {
                "status": "error",
                "mensaje": "Saldo insuficiente",
                "monto": 0
            }
        
        # Realizar la transferencia
        self.saldos[cuenta_origen] -= monto
        self.saldos[cuenta_destino] += monto
        
        return {
            "status": "exitoso",
            "mensaje": f"Transferencia realizada exitosamente",
            "monto": monto,
            "saldo_origen": self.saldos[cuenta_origen],
            "saldo_destino": self.saldos[cuenta_destino]
        }
    
    def calcular_interes(self, capital: float, dias: int, tasa_anual: float = 0.05) -> float:
        """
        Calcula el interés simple sobre un capital
        
        Formula: Interés = Capital * Tasa * (Días / 365)
        
        Args:
            capital: Monto principal sobre el que calcular interés
            dias: Número de días para el cálculo
            tasa_anual: Tasa de interés anual (por defecto 5% = 0.05)
            
        Returns:
            float: Interés calculado
            
        Ejemplo:
            >>> banco = MicroBanco()
            >>> interes = banco.calcular_interes(1000, 30, 0.05)
            >>> round(interes, 2)
            4.11
        """
        
        # ¿BUG? ¿Qué pasa si dias es 0? ¿División por cero en algún lado?
        # ¿Qué pasa si capital es negativo?
        # ¿Qué pasa si tasa es negativa?
        
        # Cálculo de interés simple
        interes = capital * tasa_anual * (dias / 365)
        
        return round(interes, 2)
    
    def validar_cuenta(self, numero_cuenta: str) -> bool:
        """
        Valida el formato de un número de cuenta bancaria
        
        Formato válido: Exactamente 6 dígitos numéricos
        Ejemplos válidos: "123456", "000001", "999999"
        Ejemplos inválidos: "12345", "abc123", "1234567", None
        
        Args:
            numero_cuenta: String con el número de cuenta a validar
            
        Returns:
            bool: True si es válida, False si no
            
        Ejemplo:
            >>> banco = MicroBanco()
            >>> banco.validar_cuenta("123456")
            True
            >>> banco.validar_cuenta("abc123") 
            False
        """
        
        # ¿BUG? ¿Qué pasa si numero_cuenta es None?
        # ¿Qué pasa si es string vacío?
        # ¿Qué pasa si tiene espacios?
        
        # Validar que no sea None o vacío
        if not numero_cuenta:
            return False
            
        # Validar longitud exacta de 6 caracteres
        if len(numero_cuenta) != 6:
            return False
            
        # Validar que todos los caracteres sean dígitos
        if not numero_cuenta.isdigit():
            return False
            
        return True
    
    def consultar_saldo(self, numero_cuenta: str) -> Dict[str, Union[str, float]]:
        """
        Consulta el saldo de una cuenta bancaria
        
        Args:
            numero_cuenta: Número de cuenta a consultar
            
        Returns:
            Dict con status y saldo (si existe) o mensaje de error
        """
        
        if not self.validar_cuenta(numero_cuenta):
            return {
                "status": "error",
                "mensaje": "Formato de cuenta inválido",
                "saldo": 0
            }
            
        if numero_cuenta not in self.cuentas_activas:
            return {
                "status": "error", 
                "mensaje": "Cuenta no existe",
                "saldo": 0
            }
            
        return {
            "status": "exitoso",
            "mensaje": "Consulta exitosa",
            "saldo": self.saldos[numero_cuenta],
            "fecha": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }


# Función de utilidad para testing
def crear_banco_con_datos_test() -> MicroBanco:
    """
    Crea una instancia de MicroBanco con datos predecibles para testing
    
    Returns:
        MicroBanco: Instancia configurada con datos de prueba
    """
    banco = MicroBanco()
    # Los datos ya están configurados en __init__
    return banco


if __name__ == "__main__":
    # Ejemplos de uso - Solo para demostración
    print("🏦 MicroBanco API - Demo")
    print("=" * 30)
    
    banco = MicroBanco()
    
    # Ejemplo 1: Transferencia exitosa
    print("\n💰 Transferencia exitosa:")
    resultado = banco.transferir("123456", "789012", 100)
    print(f"Status: {resultado['status']}")
    print(f"Mensaje: {resultado['mensaje']}")
    
    # Ejemplo 2: Cálculo de interés
    print("\n📊 Cálculo de interés:")
    interes = banco.calcular_interes(1000, 30, 0.05)
    print(f"Interés calculado: ${interes}")
    
    # Ejemplo 3: Validación de cuenta
    print("\n🔍 Validación de cuenta:")
    es_valida = banco.validar_cuenta("123456")
    print(f"¿Cuenta válida?: {es_valida}")
    
    print("\n🎯 ¡Listo para testing!")