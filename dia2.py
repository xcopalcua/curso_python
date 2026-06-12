# ### **🎯 Objetivo del Módulo**
# Dominar el trabajo con diccionarios y estructuras complejas que son el corazón del procesamiento de datos en aplicaciones backend.

# ### **📚 ¿Qué es este módulo?**
# Los datos en aplicaciones web vienen en formato JSON (JavaScript Object Notation), que en Python se representa como diccionarios anidados. Este módulo enseña:
# - Cómo agrupar datos (dispositivos por ubicación, registros por categoría)
# - Cómo transformar estructuras de datos
# - Cómo manejar datos anidados complejos

# ### **💡 ¿Por qué es importante?**
# El 70% del código backend consiste en:
# 1. Recibir datos de la BD (tuplas o consultas)
# 2. Transformarlos en diccionarios/JSON
# 3. Agruparlos/filtrarlos según lógica de negocio
# 4. Enviarlos como respuesta JSON a clientes

# Sin dominar esto, no podrás trabajar efectivamente en desarrollo backend.

# ### **🔍 Casos de Uso Reales**
# Un patrón muy común es agrupar elementos por una clave:
# Agrupar dispositivos por ubicación
warehouses_dict = {}
for device in devices_with_location:
    location = device["location"]   #CDMX, Tlaxcala, Oaxaca
    if location not in warehouses_dict:
        warehouses_dict[location] = [] 
        #warehouses_dict = {"CDMX": []}
    
    warehouses_dict[location].append(device)


# Esto convierte:
devices_with_location=[{"location": "CDMX", "id": "001"}, 
 {"location": "CDMX", "id": "002"},
 {"location": "Tlaxcala", "id": "003"},
 {"location": "Oaxaca", "id": "004"},
 {"location":"Tlaxcala", "id": "005"}]

#En:
warehouses_dict={"CDMX": [{"location": "CDMX", "id": "001"}, {"location": "CDMX", "id": "002"}],
                 "Tlaxcala":[{"location": "Tlaxcala", "id": "003"},{"location":"Tlaxcala", "id": "005"}],
                 "Oaxaca":[{"location": "Oaxaca", "id": "004"}]
 }

### **2.1 Trabajo con Diccionarios**
# ============================================================
# PATRÓN: AGRUPAR POR CLAVE (Muy usado en desarrollo backend)
# ============================================================
"""
Este es el patrón más importante del módulo.
Se usa para agrupar registros por categoría, ubicación, estado, etc.
"""

# Datos de entrada: Dispositivos con ubicación asignada
devices_with_location = [
    {"id": "DEV001", "warehouse": "CDMX", "route": "RT001", "date": "2026-06-01"},
    {"id": "DEV005", "warehouse": "GDL", "route": "RT002", "date": "2026-06-02"},
    {"id": "DEV003", "warehouse": "CDMX", "route": "RT003", "date": "2026-06-03"},
    {"id": "DEV005", "warehouse": "MTY", "route": "RT004", "date": "2026-06-04"},
    {"id": "DEV005", "warehouse": "CDMX", "route": "RT005", "date": "2026-06-05"},
]

# Objetivo: Agrupar dispositivos por almacén
print("=== AGRUPANDO DISPOSITIVOS POR ALMACÉN ===")

# Método 1: Loop tradicional (más claro para principiantes)
warehouses_dict = {}

for device in devices_with_location:
    warehouse = device["warehouse"]
    
    # Si el almacén no existe en el dict, crear lista vacía
    if warehouse not in warehouses_dict:
        warehouses_dict[warehouse] = []
    
    # Agregar dispositivo a la lista del almacén
    warehouses_dict[warehouse].append(device)

# Resultado:
# {
#   "CDMX": [dev001, dev003, dev005],
#   "GDL": [dev002],
#   "MTY": [dev004]
# }

print(f"Almacenes encontrados: {list(warehouses_dict.keys())}")
for warehouse, devices in warehouses_dict.items():
    print(f"  {warehouse}: {len(devices)} dispositivos")

# ============================================================
# MÉTODO ALTERNATIVO: defaultdict (más pythónico)
# ============================================================
from collections import defaultdict

warehouses_dict2 = defaultdict(list)  # Crea lista automáticamente
for device in devices_with_location:
    warehouses_dict2[device["warehouse"]].append(device)

# ============================================================
# MÉTODOS ÚTILES DE DICCIONARIOS
# ============================================================
payload = {
    "organization": "ORG123",
    "date": "2026-06-08",
    "country": "Mexico"
}

# 1. get() - Acceso seguro con default
org = payload.get("organization")          # "ORG123"
status = payload.get("status", "pending")  # "pending" (no existe)

# 2. keys(), values(), items()
claves = list(payload.keys())     # ["organization", "date", "country"]
valores = list(payload.values())  # ["ORG123", "2026-06-08", "Mexico"]
pares = list(payload.items())     # [("organization", "ORG123"), ("date", "2026-06-08"), ("country", "Mexico")]

# 3. in - Verificar existencia de clave
if "organization" in payload:
    print("✓ Organización presente")

if "status" not in payload:
    print("⚠️ Status no proporcionado")

# 4. update() - Agregar múltiples items
payload.update({
    "status": "processing",
    "user_id": 123
})

# 5. pop() - Obtener y remover
country = payload.pop("country")  # Retorna "Mexico" y lo remueve
default_val = payload.pop("missing", None)  # Retorna None sin error

# ============================================================
# DICCIONARIOS ANIDADOS (Datos complejos)
# ============================================================
"""
Respuestas de APIs y configuraciones complejas usan
diccionarios dentro de diccionarios.
"""

# Ejemplo: Configuración de notificaciones por país
notification_config = {
    "Mexico": {
        "almacen": "main.return_gps_in_warehouse",
        "transportista": "main.return_gps",
        "warehouse_label": "Almacén",
        "greeting": "Atentamente"
    },
    "Colombia": {
        "almacen": "main.return_gps_in_warehouse_colombia",
        "transportista": "main.return_gps_colombia",
        "warehouse_label": "Bodega",
        "greeting": "Cordialmente"
    }
}

# Acceso a datos anidados
pais = "Mexico"
endpoint = notification_config[pais]["transportista"] #"main.return_gps",
label = notification_config[pais]["warehouse_label"] #"Almacén"

print(f"País: {pais}")
print(f"Endpoint: {endpoint}")
print(f"Label: {label}")

# Acceso seguro con get() anidado
config_col = notification_config.get("Colombia", {})
greeting = config_col.get("greeting", "Best regards")

# ============================================================
# TRANSFORMAR ESTRUCTURAS: Lista → Diccionario
# ============================================================
"""
Común al procesar resultados de base de datos
"""
# id, gps, ubicacion....
# where warehouse_country="Mexico"
# limit 100
# Resultado de query SQL (lista de tuplas)
db_results = [
    (1, "DEV001", "CDMX"),#0
    (2, "DEV002", "GDL"),#1
    (3, "DEV003", "CDMX"),#2
]

# Transformar a lista de diccionarios (más fácil de usar)
devices_list = []
for row in db_results:
    devices_list.append({
        "id": row[0],
        "device_id": row[1],
        "warehouse": row[2]
    })
devices_list = [{"id":1,"device_id":"DEV001","warehouse":"CDMX"},
                {"id":2,"device_id":"DEV002","warehouse":"GDL"},]
# O con list comprehension:
devices_list = [
    {"id": row[0], "device_id": row[1], "warehouse": row[2]}
    for row in db_results
]

# Crear diccionario indexado por Device ID
devices_by_id = {
    device["device_id"]: device
    for device in devices_list
}
# {"DEV001": {...}, "DEV002": {...}}

# Ahora acceso rápido por ID
dev_001 = devices_by_id.get("DEV001")

# #### **🎓 Conceptos Clave**
# - **Agrupación**: Patrón clave para consolidar datos relacionados
# - **Acceso seguro**: Siempre usar `.get()` para evitar KeyError
# - **Transformación**: Convertir entre estructuras según necesidad
# - **Índices**: Crear diccionarios indexados para acceso rápido



### **2.2 Sets y Tuplas (20 min)**

# ============================================================
# SETS - Colecciones de elementos únicos
# ============================================================
"""
Uso en el proyecto: Eliminar duplicados, verificar pertenencia rápida
"""

# Problema: Emails duplicados en lista
emails = [
    "admin@test.com",
    "user@test.com",
    "admin@test.com",  # Duplicado
    "manager@test.com",
    "user@test.com"    # Duplicado
]

print(f"Emails originales: {len(emails)}")  # 5

# Solución: Convertir a set (elimina duplicados automáticamente)
unique_emails = list(set(emails))
print(f"Emails únicos: {len(unique_emails)}")  # 3

# Operaciones de conjuntos
admins = {"admin@test.com", "superadmin@test.com"}
users = {"user@test.com", "admin@test.com"}

# Unión - Todos los emails
todos = admins | users
# {"admin@test.com", "superadmin@test.com", "user@test.com"}

# Intersección - Emails en ambos grupos
ambos = admins & users
# {"admin@test.com"}

# Diferencia - Solo en admins
solo_admins = admins - users
# {"superadmin@test.com"}

# Verificar pertenencia (muy rápido, O(1))
if "admin@test.com" in admins:
    print("Es admin")

# ============================================================
# TUPLAS - Colecciones inmutables
# ============================================================
"""
Uso en desarrollo backend:
1. Resultados de queries SQL
2. Coordenadas geográficas o pares de datos
3. Datos que no deben cambiar
"""

# 1. Resultados de base de datos (muy común)
# Query retorna tupla: (id_record, device_id, date, warehouse)
query_result = (12345, "DEV001", "2026-06-08", "CDMX")

# Acceso por índice (menos legible)
record_id = query_result[0]
device_id = query_result[1]

# MEJOR: Desempaquetado (muy usado en backend)
record_id, device_id, date, warehouse = query_result
print(f"Registro: {record_id}, Dispositivo: {device_id}")

# Desempaquetado parcial con *
first, *middle, last = (1, 2, 3, 4, 5)
# first=1, middle=[2,3,4], last=5

# 2. Named Tuples (más legibles que tuplas simples)
from collections import namedtuple

# Definir estructura
RecordDevice = namedtuple("RecordDevice", ["record_id", "device_id", "date", "warehouse"])

# Crear instancia
result = RecordDevice(
    record_id=12345,
    device_id="DEV001",
    date="2026-06-08",
    warehouse="CDMX"
)

# Acceso por nombre (más claro)
print(f"Dispositivo: {result.device_id}")
print(f"Almacén: {result.warehouse}")

# También funciona acceso por índice
print(f"ID Registro: {result[0]}")

# Convertir a diccionario
result_dict = result._asdict()
# {"record_id": 12345, "device_id": "DEV001", ...}

# 3. Tuplas como claves de diccionario
# (no se puede con listas porque son mutables)

# Índice de registros por (country, carrier)
records_index = {
    ("Mexico", "DHL"): [("RT001", "DEV001"), ("RT002", "DEV002")],
    ("Mexico", "FedEx"): [("RT002", "DEV005")],
    ("Colombia", "FedEx"): [("RT003", "DEV003")]
}

# Acceso
records_dhl_mx = records_index.get(("Mexico", "DHL"))

# ============================================================
# CUANDO USAR CADA UNO
# ============================================================

# Lista: Orden importa, puede tener duplicados, mutable
notifications = ["email1", "email2", "email3"]
notifications.append("email4")  # ✓ Modificable

# Tupla: Orden importa, inmutable, más eficiente que lista
coordinates = (19.4326, -99.1332)  # Lat, Lon de CDMX
# coordinates[0] = 20  # ❌ Error: No se puede modificar

# Set: Sin orden, sin duplicados, operaciones de conjunto
processed_devices = {"DEV001", "DEV002", "DEV003"}
processed_devices.add("DEV004")  # ✓ Se puede agregar
processed_devices.add("DEV001")  # No hace nada (ya existe)

# Diccionario: Pares clave-valor, acceso rápido por clave
device_data = {"id": "DEV001", "status": "active"}
device_data["status"] = "inactive"  # ✓ Modificable


# #### **🎓 Conceptos Clave**
# - **Inmutabilidad**: Tuplas no se pueden modificar (más seguras)
# - **Hashing**: Solo objetos inmutables pueden ser claves de diccionario
# - **Named tuples**: Mejor legibilidad que tuplas simples
# - **Sets**: Operaciones de conjunto y eliminación de duplicados

#### **⚠️ Errores Comunes**
# Error 1: Intentar modificar tupla
coords = (19.43, -99.13)
coords[0] = 20  # ❌ TypeError

# Error 2: Crear set con elementos mutables
devices_set = {["DEV001"], ["DEV002"]}  # ❌ No se puede (listas no hashables)
devices_set = {("DEV001",), ("DEV002",)}  # ✅ Tuplas sí

# Error 3: Confundir tupla de un elemento
tupla = (5)      # ❌ Es un int, no tupla
tupla = (5,)     # ✅ Tupla de un elemento (nota la coma)