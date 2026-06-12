
### **🏋️ EJERCICIOS MÓDULO 2**

#### **Ejercicio 2.1: Agrupador de Dispositivos**
def agrupar_por_region(devices_list):
    """
    Agrupa dispositivos por región y cuenta cuántos hay en cada una.
    
    Args:
        devices_list: [{"id": "DEV001", "region": "North"}, ...]
    
    Returns:
        dict: {"North": 3, "South": 2}
    """
    # TU CÓDIGO AQUÍ
    pass

# Prueba
devices = [
    {"id": "DEV001", "region": "North"},
    {"id": "DEV002", "region": "South"},
    {"id": "DEV003", "region": "North"},
    {"id": "DEV004", "region": "North"},
    {"id": "DEV005", "region": "East"}
]
resultado = agrupar_por_region(devices)
# {"North": 3, "South": 1}


#### **Ejercicio 2.2: Eliminar Duplicados Manteniendo Orden**
def eliminar_duplicados_ordenado(items):
    """
    Elimina duplicados de lista manteniendo orden original.
    
    Args:
        items: Lista con posibles duplicados
    
    Returns:
        list: Lista sin duplicados, orden preservado
    """
    # PISTA: No uses set() directamente (no mantiene orden en Python < 3.7)
    # Usa dict.fromkeys() o loop manual
    pass