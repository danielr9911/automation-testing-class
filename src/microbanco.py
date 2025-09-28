"""
MicroBanco API - Sistema de Servicios Bancarios (Discovery Version)
================================================================

Esta es una simulación de una API bancaria para el Challenge de Testing Discovery.
Contiene bugs sutiles que los estudiantes deben encontrar mediante testing sistemático.

🎯 CHALLENGE: Encuentra los bugs mediante testing, no leyendo código!

Autor: Testing Masterclass 2025-2  
Fecha: Septiembre 2025
"""

import datetime
from typing import Dict, Union, Optional


class MicroBanco:
    """
    API principal de MicroBanco - Startup Fintech
    
    🎯 TU MISIÓN: Crear tests que encuentren los bugs ocultos
    
    ⚠️ ADVERTENCIA: Este código tiene bugs sutiles.
    ¡No los busques leyendo código - encuéntralos testeando!
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
            monto: Cantidad a transferir
            
        Returns:
            Dict con status, mensaje, monto y saldos actualizados
        """
        
        # Validación básica de parámetros
        if not cuenta_origen or not cuenta_destino:
            return {
                "status": "error",
                "mensaje": "Cuentas no pueden estar vacías",
                "monto": 0
            }
        
        # 🐛 BUG #1: ¿Qué pasa si monto es negativo?
        # El código actual NO valida montos negativos
        # Esto permite "robar" dinero usando montos negativos
        
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
        
        Fórmula: Interés = Capital * Tasa * (Días / 365)
        
        Args:
            capital: Monto principal  
            dias: Número de días
            tasa_anual: Tasa de interés anual (default 5%)
            
        Returns:
            float: Interés calculado
        """
        
        # 🐛 BUG #2: ¿Qué pasa si dias es 0?
        # División por cero potencial en algunos casos edge
        
        # 🐛 BUG #3: ¿Qué pasa con valores negativos?
        # ¿Es lógico tener interés negativo? ¿Capital negativo?
        
        # Cálculo básico
        if dias <= 0:
            return 0.0  # ¿Es correcto? ¿O debería dar error?
        
        interes = capital * tasa_anual * (dias / 365)
        return round(interes, 2)
    
    def validar_cuenta(self, numero_cuenta: str) -> bool:
        """
        Valida el formato de un número de cuenta bancaria
        
        Formato esperado: Exactamente 6 dígitos numéricos
        
        Args:
            numero_cuenta: String con el número de cuenta
            
        Returns:
            bool: True si es válida, False si no
        """
        
        # 🐛 BUG #4: ¿Qué pasa si numero_cuenta es None?
        # ¿Qué pasa si es un número en lugar de string?
        
        # Validaciones básicas
        if not numero_cuenta:
            return False
            
        # 🐛 BUG #5: ¿Qué pasa con espacios al inicio o final?
        # "123456 " vs "123456" - ¿Son iguales o diferentes?
        
        if len(numero_cuenta) != 6:
            return False
            
        if not numero_cuenta.isdigit():
            return False
            
        return True
    
    def consultar_saldo(self, numero_cuenta: str) -> Dict[str, Union[str, float]]:
        """
        Consulta el saldo de una cuenta bancaria
        
        Args:
            numero_cuenta: Número de cuenta a consultar
            
        Returns:
            Dict con status, mensaje, saldo y timestamp
        """
        
        if not self.validar_cuenta(numero_cuenta):
            return {
                "status": "error",
                "mensaje": "Formato de cuenta inválido",
                "saldo": 0
            }
        
        # 🐛 BUG #6: ¿Qué pasa si la cuenta tiene formato válido 
        # pero no existe en self.cuentas_activas?
        # El código actual asume que si el formato es válido, existe
        
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


def crear_banco_con_datos_test() -> MicroBanco:
    """
    Crea una instancia de MicroBanco con datos predecibles para testing
    
    Returns:
        MicroBanco: Instancia configurada
    """
    return MicroBanco()


if __name__ == "__main__":
    # Demo básico - muestra que "funciona" en casos normales
    print("🏦 MicroBanco API - Demo Básico")
    print("=" * 35)
    
    banco = MicroBanco()
    
    # Caso que funciona bien
    print("\n✅ Caso normal:")
    resultado = banco.transferir("123456", "789012", 100)
    print(f"Status: {resultado['status']}")
    print(f"Saldo origen: ${resultado['saldo_origen']}")
    
    # Caso que funciona bien  
    print("\n✅ Cálculo interés normal:")
    interes = banco.calcular_interes(1000, 30, 0.05)
    print(f"Interés: ${interes}")
    
    # Caso que funciona bien
    print("\n✅ Validación cuenta normal:")
    es_valida = banco.validar_cuenta("123456")
    print(f"¿Válida?: {es_valida}")
    
    print("\n🎯 Todo parece funcionar... ¿o no? 🤔")
    print("🐛 Usa testing para encontrar los bugs ocultos!")
    
    # 🎯 HINTS para testing (no spoilers):
    print("\n💡 Hints para testing:")
    print("- ¿Qué pasa con valores extremos?")
    print("- ¿Qué pasa con inputs inesperados?")
    print("- ¿Qué pasa con edge cases?")
    print("- ¿Todos los errores se manejan bien?")
    print("- ¿El comportamiento es lógico en todos los casos?")