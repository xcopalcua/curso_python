# Crea una función validar_email(email) que:

# Retorne True si el email contiene "@" y "."
# Retorne False en caso contrario
# Use la función para filtrar una lista de emails

def validar_email(email):
    """
    Valida que un email sea válido.
    
    Criterios:
    - Debe contener exactamente un @
    - Debe contener al menos un .
    - No debe estar vacío
    - No debe tener espacios
    
    Returns:
        bool: True si es válido, False si no
    """
    # TU CÓDIGO AQUÍ
    if not email:
        return False

    split_email = email.split("@")
    if len(split_email) != 2:
        return False

    if "." not in email:
        return False

    if " " in email:
        return False

    return True

    pass

emails = [
    "juan@example.com",
    "maria.lopez@gmail.com",
    "juanexample.com",
    "",
    "usuario123@empresa.com",
    "juan@@example.com",
    "test@dominio.mx",
    "juan@",
    "correo@universidad.edu",
    "juan@example",
    "user_01@test.net",
    "juan @example.com"
]

for email in emails:
    print(f"{email}: {validar_email(email)}")

#### **Ejercicio 1.2: Filtrador de Dispositivos**
def filtrar_pendientes(devices_list):
    """
    Filtra dispositivos que NO han sido devueltos y NO están perdidos.
    
    Args:
        devices_list: Lista de diccionarios con keys: id, returned, is_lost
    
    Returns:
        list: Lista filtrada de dispositivos pendientes
    """
    # TU CÓDIGO AQUÍ
    devices_pendientes = []

    for device in devices_list:
        if not device["returned"] and not device["is_lost"]:
            devices_pendientes.append(device)

    return devices_pendientes

    pass

# Prueba
devices = [
    {"id": "DEV001", "returned": False, "is_lost": False},
    {"id": "DEV002", "returned": True, "is_lost": False},
    {"id": "DEV003", "returned": False, "is_lost": True},
]
resultado = filtrar_pendientes(devices)
print(resultado)
# Debe retornar solo DEV001



#### **Ejercicio 1.3: Agrupador por Región**

records = [
    {"id": 1, "region": "North"},
    {"id": 2, "region": "South"},
    {"id": 3, "region": "North"},
    {"id": 4, "region": "East"},
    {"id": 5, "region": "South"},
    {"id": 6, "region": "North"},
]

def agrupar_por_region(records):
    """
    Agrupa registros por región y cuenta cuántos hay en cada uno.
    
    Args:
        records: Lista de dicts con key 'region'
    
    Returns:
        dict: {"North": 3, "South": 2}
    """
    # TU CÓDIGO AQUÍ
    region_count = {}

    for record in records:
        region = record["region"]
        if region in region_count:
            region_count[region] += 1
        else:
            region_count[region] = 1

    return region_count

    pass

print(agrupar_por_region(records))
