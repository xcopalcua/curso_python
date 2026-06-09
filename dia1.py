### **1.1 Tipos de Datos y Variables (20 min)**

# **📖 ¿Qué aprenderás?**
#Los tipos de datos básicos que usa Python y cómo el proyecto los utiliza para representar información del sistema.

# ============================================================
# STRINGS - Representan texto
# ============================================================
# Uso en el proyecto: Nombres, IDs, endpoints, emails
carrier_name = 'DHL Express'        # Nombre de línea transportista
endpoint = 'main.return_gps'        # Endpoint de template de email
organization = 'ORG123'             # Clave de organización
gps_id = 'GPS001'                   # ID de dispositivo GPS

# Operaciones comunes con strings
email = "admin@example.com"
dominio = email.split("@")[1]       # "example.com"   xochitl.copalcua  @
                                                     #dynofleet.com 
nombre_upper = carrier_name.upper() # "DHL EXPRESS"
tiene_arroba = "@" in email         # True
if "@" in email:
    tiene_arroba = True

tiene_arroba = True if "@" in email else False  # True

# ============================================================
# NÚMEROS - Enteros y decimales
# ============================================================
# Uso en el proyecto: IDs de base de datos, contadores, precios
gps_count = 5                # Cantidad de GPS (int)
id_ruta = 12345             # ID de ruta en base de datos (int)
rate = 1500.50              # Tarifa de transporte (float)
emails_sent = 0             # Contador (int)

# Operaciones matemáticas
total = gps_count * 2       # 10
precio_con_iva = rate * 1.16  # 1740.58158
precio_con_iva_redondeado = round(precio_con_iva,2)  # 1740.58

# ============================================================
# BOOLEANOS - Verdadero o Falso
# ============================================================
# Uso en el proyecto: Estados, banderas, validaciones
is_completed = True          # Ruta completada
gps_returned = False         # GPS no devuelto
has_guide = False           # GPS sin guía asignada
id_monitoreo = ""
id_monitoreo=[]
id_monitoreo=None
# Se usan en condicionales
if is_completed and not gps_returned:
    print("Ruta completa pero GPS no devuelto")
    id_monitoreo = "123"
if id_monitoreo:
    print(id_monitoreo)
...
...


# ============================================================
# NONE - Representa ausencia de valor (como NULL en SQL)
# ============================================================
# Uso en el proyecto: Campos opcionales, valores no encontrados
id_monitoreo = None         # Proveedor no asignado
delivery_date = None        # Fecha aún no definida

# IMPORTANTE: Siempre validar antes de usar
if id_monitoreo is None:
    print("Advertencia: Sin proveedor de monitoreo")

# ============================================================
# LISTAS - Colección ordenada de elementos
# ============================================================
# Uso en el proyecto: Múltiples emails, GPS, rutas
emails = ["admin@example.com" ,#0
           "user@example.com", #1
           "manager@example.com", #2
           "monitoreo@example.com"]#3
email1=emails[1] #"user@example.com"

# Lista de diccionarios
gps_record = {
    "id_gps": "GPS001", 
    "ruta": "RT001",
    "fecha_de_salida_alm": "2026-06-01",
    "fecha_de_entrega": "2026-06-08",
    "linea_transportista": "DHL Express",
    "conductor": "Juan Pérez",
    "tipo_de_transporte": "Camioneta 1 Ton", 
}

gps_list = [
    {"id_gps": "GPS001", "ruta": "RT001", "fecha": "2026-06-08"}, #[0]
    {"id_gps": "GPS002", "ruta": "RT002", "fecha": "2026-06-07"}  #[1]
]

# Operaciones comunes con listas
emails.append("nuevo@example.com")      # Agregar al final
gps_list.append(gps_record)              # Agregar diccionario a lista
total_gps = len(gps_list)               # Contar: 2
primer_gps = gps_list[0]                # Acceder por índice
ultimos_dos = emails[-2:]               # Últimos 2 elementos

# Verificar si elemento existe
if "admin@example.com" in emails:
    print("Admin está en la lista")

# ============================================================
# DICCIONARIOS - Pares clave-valor (como JSON)
# ============================================================
# Uso en el proyecto: Datos estructurados, respuestas de API, configuración
gps_data = {
    "id_gps": "GPS123",
    "ruta": "RT456",
    "fecha": "2026-06-08",
    "almacen": "CDMX01",
    "returned": False
}

# Acceso seguro a valores
# ❌ MAL - Puede causar KeyError si no existe
# ruta = gps_data["ruta_id"]  

# ✅ BIEN - Retorna None si no existe
ruta_id = gps_data.get("ruta_id")

# ✅ MEJOR - Con valor por defecto
warehouse = gps_data.get("almacen", "N/A")
status = gps_data.get("status", "pending")

# Verificar si clave existe
if "almacen" in gps_data:
    print(f"Almacén: {gps_data['almacen']}")

# Agregar o modificar valores
gps_data["status"] = "processed"
gps_data["processed_at"] = "2026-06-08 15:30:00"

#### **🎓 Conceptos Clave**
# - **Inmutabilidad**: Strings, números y tuplas no se pueden modificar después de crearse
# - **Mutabilidad**: Listas y diccionarios sí se pueden modificar
# - **Type Hints**: En código moderno se agregan tipos: `def process(name: str) -> dict:`

#### **⚠️ Errores Comunes**
# Error 1: Acceder a clave inexistente
payload = {"organization": "ORG123"}
date = payload["date"]  # ❌ KeyError si no existe
date = payload.get("date")  # ✅ Retorna None sin error

# Error 2: No validar None
name = None
upper_name = name.upper()  # ❌ AttributeError
upper_name = name.upper() if name else "N/A"  # ✅

# Error 3: Comparar tipos diferentes
if gps_count == "5":  # ❌ int != string
    pass
if gps_count == 5:  # ✅ Comparar mismo tipo
    pass



    ##########################################################


### **1.2 Control de Flujo (20 min)**

#### **📖 ¿Qué aprenderás?**
# Cómo tomar decisiones en el código (if/else) y repetir operaciones (loops). Esto es fundamental para procesar datos dinámicamente.

#### **💡 Caso de Uso Real**
# En aplicaciones backend, necesitamos:
# - Decidir qué plantilla usar según configuración (país, idioma, tipo)
# - Iterar sobre colecciones de datos para procesarlos
# - Filtrar elementos válidos de una lista
# - Procesar múltiples registros secuencialmente
# ============================================================
# IF / ELIF / ELSE - Tomar decisiones
# ============================================================
# Ejemplo: Adaptar configuración según región
country = "Mexico"  # Puede venir de la base de datos o configuración
is_warehouse_notification = True  # Tipo de notificación

if country == "Colombia":
    warehouse_label = "Bodega"
    greeting = "Cordialmente"
    currency = "COP"
elif country == "Mexico":
    warehouse_label = "Almacén"
    greeting = "Atentamente"
    currency = "MXN"
else:
    warehouse_label = "Warehouse"
    greeting = "Best regards"
    currency = "USD"

print(f"País: {country}")
print(f"Label: {warehouse_label}")
print(f"Moneda: {currency}")

# ============================================================
# OPERADOR TERNARIO - If en una línea
# ============================================================
# Muy usado en plantillas y asignaciones rápidas
label = "Bodega" if country == "Colombia" else "Almacén"
status_text = "Completado" if is_completed else "Pendiente"

# Ejemplo en plantilla Jinja2:
# {{ 'Bodega' if country == 'Colombia' else 'Almacén' }}

# ============================================================
# OPERADORES LÓGICOS - AND, OR, NOT
# ============================================================
# Combinar múltiples condiciones
if is_returned and is_completed:
    print("Tarea completa y recurso devuelto ✓")

if not is_returned or has_loss:
    print("⚠️ Recurso pendiente o perdido")

# Validación de campos requeridos
if organization and endpoint:
    print("Datos completos")
else:
    print("Faltan datos requeridos")

# ============================================================
# FOR LOOP - Iterar sobre colecciones
# ============================================================
# Iterar sobre lista de dispositivos/recursos
devices_list = [
    {"id": "DEV001", "route": "RT001", "returned": False},
    {"id": "DEV002", "route": "RT002", "returned": True},
    {"id": "DEV003", "route": "RT003", "returned": False}
]

print("=== Dispositivos Pendientes ===")
for device in devices_list:
    if not device["returned"]:
        print(f"Dispositivo: {device['id']} - Ruta: {device['route']}")

# Iterar con índice usando enumerate
for index, device in enumerate(devices_list, start=1):
    print(f"{index}. {device['id']}")

# Iterar sobre diccionario
device_data = {"id": "DEV001", "route": "RT001", "date": "2026-06-08"}

# Solo claves
for key in device_data:
    print(key)  # id, route, date

# Claves y valores
for key, value in gps_data.items():
    print(f"{key}: {value}")

# ============================================================
# WHILE LOOP - Repetir mientras condición sea verdadera
# ============================================================
# Ejemplo: Enviar emails con límite
emails_to_send = ["user1@test.com", "user2@test.com", "user3@test.com"]
emails_sent = 0
max_emails = 100

while emails_sent < max_emails and emails_to_send:
    email = emails_to_send.pop(0)  # Obtener y remover primero
    print(f"Enviando a: {email}")
    emails_sent += 1

print(f"Total enviados: {emails_sent}")

# ⚠️ CUIDADO: Evitar loops infinitos
# while True:  # ❌ Se ejecuta infinitamente
#     pass

# ============================================================
# LIST COMPREHENSION - Crear listas de forma concisa
# ============================================================
# Muy usado en desarrollo backend para transformar datos

# Ejemplo 1: Extraer solo IDs
device_ids = [device["id"] for device in devices_list]
# Resultado: ["DEV001", "DEV002", "DEV003"]

# Ejemplo 2: Filtrar recursos pendientes
pending_devices = [device for device in devices_list if not device["returned"]]
# Resultado: Solo dispositivos con returned=False

# Ejemplo 3: Validar y filtrar emails
emails = ["admin@test.com", "invalid@", "user@test.com "]
valid_emails = [email for email in emails if "@" in email]
# Resultado: ["admin@test.com", "user@test.com"]

# Ejemplo 4: Transformar datos
emails_upper = [email.upper() for email in valid_emails]

# Equivalente con for loop tradicional:
valid_emails = []
for email in emails:
    if "@" in email and "." in email and " " not in email:
        valid_emails.append(email)

# ============================================================
# BREAK y CONTINUE - Control de loops
# ============================================================
# BREAK - Salir del loop inmediatamente
for device in devices_list:
    if device["id"] == "DEV002":
        print("Dispositivo encontrado, saliendo...")
        break
    print(f"Procesando: {device['id']}")

# CONTINUE - Saltar a la siguiente iteración
for device in devices_list:
    if device["returned"]:
        continue  # Saltar dispositivos ya devueltos
    print(f"Dispositivo pendiente: {device['id']}")


#### **🎓 Conceptos Clave**
# - **Truthy/Falsy**: En Python, valores como `None`, `0`, `""`, `[]`, `{}` son "falsy"
# - **Short-circuit**: `and` se detiene en el primer False, `or` en el primer True
# - **List comprehension**: Más eficiente y "pythónico" que loops tradicionales

#### **⚠️ Errores Comunes**
# Error 1: Comparar con = en lugar de ==
if x = 5:  # ❌ SyntaxError
if x == 5:  # ✅

# Error 2: Modificar lista mientras se itera
emails = ["a@test.com", "b@test.com"]
for email in emails:
    emails.remove(email)  # ❌ Comportamiento inesperado

# ✅ Correcto:
emails = [e for e in emails if condicion]

# Error 3: No inicializar contador
# counter += 1  # ❌ NameError
counter = 0
counter += 1  # ✅


####################################################


### **1.3 Funciones Básicas (20 min)**

#### **📖 ¿Qué aprenderás?**
# Cómo organizar código en funciones reutilizables. En aplicaciones backend profesionales, TODO el código está organizado en funciones para mantenerlo limpio y mantenible.

#### **💡 Caso de Uso Real**
# Los servicios backend típicamente tienen una función principal que:
# - Valida datos de entrada
# - Consulta la base de datos
# - Procesa resultados
# - Envía notificaciones o responde
# - Retorna resultado estructurado
# # ============================================================
# FUNCIÓN SIMPLE - Sin parámetros
# ============================================================
def get_current_date(fecha=None):
    """Retorna la fecha actual en formato string."""
    from datetime import datetime
    if fecha:
        return fecha.strftime("%Y/%m/%d")
    return datetime.now().strftime("%Y/%m/%d")

# Usar la función
fecha = get_current_date("2026-06-08")  # "2026/06/08"
print(fecha)  # "2026-06-08"

# ============================================================
# FUNCIÓN CON PARÁMETROS
# ============================================================
def format_date(date_value):
    """
    Formatea fecha a string legible.
    
    Función común en aplicaciones backend.
    Se usa para formatear fechas antes de mostrarlas.
    
    Args:
        date_value: datetime object o None
    
    Returns:
        str: Fecha formateada o "Sin asignar"
    """
    if date_value is None:
        return "Sin asignar"
    
    # Formato: "2026-06-08 15:30"
    return str(date_value)[:16].replace("T", " ")

# Uso
from datetime import datetime
fecha_actual = datetime.now()
fecha_formateada = format_date(fecha_actual)
fecha_vacia = format_date(None)  # "Sin asignar"

# ============================================================
# FUNCIÓN CON MÚLTIPLES PARÁMETROS Y DEFAULTS
# ============================================================
def send_notification(emails, subject, message, urgent=False, country="Mexico"):
    """
    Envía notificación por email.
    
    Patrón común en aplicaciones backend para notificaciones.
    
    Args:
        emails (list): Lista de destinatarios
        subject (str): Asunto del correo
        message (str): Contenido del mensaje
        urgent (bool, optional): Marca como urgente. Default: False
        country (str, optional): País para formato. Default: "Mexico"
    
    Returns:
        int: Número de emails enviados exitosamente
    """
    count = 0
    
    # Validar emails no vacíos
    if not emails:
        print("⚠️ No hay destinatarios")
        return 0
    
    # Procesar cada email
    for email in emails:
        print(f"📧 Enviando a {email}")
        print(f"   Asunto: {subject}")
        
        if urgent:
            print("   🔴 [URGENTE]")
        
        if country == "Colombia":
            print("   Cordialmente")
        else:
            print("   Atentamente")
        
        count += 1
    
    return count

# Llamar función - diferentes formas
# 1. Parámetros posicionales
resultado = send_notification(
    ["admin@test.com"],
    "Dispositivos Pendientes",
    "Tiene 5 dispositivos pendientes"
)

# 2. Parámetros nombrados (recomendado)
resultado = send_notification(
    emails=["admin@test.com", "manager@test.com"],
    subject="Dispositivos Pendientes",
    message="Tiene 5 dispositivos pendientes",
    urgent=True,
    country="Colombia"
)

# 3. Mezclar posicionales y nombrados
resultado = send_notification(
    "Dispositivos Pendientes",
    "Mensaje",
    emails=["admin@test.com"],
    urgent=True  # Solo especificar los que quiero cambiar
)

# ============================================================
# FUNCIÓN QUE RETORNA DICCIONARIO (Patrón backend estándar)
# ============================================================
def validate_data(payload):
    """
    Valida datos de entrada para procesamiento.
    
    Este patrón se usa en servicios backend modernos.
    Siempre retornan un diccionario con status y message/data.
    
    Args:
        payload (dict): Datos a validar
    
    Returns:
        dict: {"status": "ok"/"error", "message": str, "data": dict}
    """
    # Validar campos requeridos
    organization = payload.get("organization")
    if not organization:
        return {
            "status": "error",
            "message": "Campo 'organization' es requerido"
        }
    
    gps_list = payload.get("gps_list", [])
    if not gps_list:
        return {
            "status": "error",
            "message": "Lista de dispositivos vacía"
        }
    
    # Si todo está bien
    return {
        "status": "success",
        "message": "Datos válidos",
        "data": {
            "organization": organization,
            "gps_count": len(gps_list)
        }
    }

# Uso de la función
datos = [
    "ORG123",
    "id": "DEV001", 
    "id": "DEV002"
]

resultado = validate_data(datos)

if resultado["status"] == "success":
    print(f"✓ Validación exitosa")
    print(f"  Dispositivos: {resultado['data']['gps_count']}")
else:
    print(f"✗ Error: {resultado['message']}")

# ============================================================
# FUNCIÓN CON *args y **kwargs (Avanzado)
# ============================================================

def log_event(event_type, **kwargs):
    """
    Registra evento con datos variables.
    
    *args: Argumentos posicionales adicionales
    **kwargs: Argumentos nombrados adicionales
    """
    print(f"[{event_type}]")
    
    for arg in args:
        print(f"  - {arg}")
    
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

# Uso flexible
kwargs = {
    "device_id": "DEV001",
    "status": "returned",
    "timestamp": "2026-06-08T15:30:00"
}
args = ["Evento GPS", "Recurso DEV001"]

log_event("GPS_RETURNED", *args ,**kwargs)
log_event("GPS_RETURNED", "Evento GPS", "Recurso DEV001", 
          device_id="DEV001", status="returned", timestamp="2026-06-08T15:30:00")

#### **🎓 Conceptos Clave**
# - **Docstrings**: Documentación de la función (triple comillas)
# - **Type hints**: Opcionalmente puedes agregar tipos: `def func(x: int) -> str:`
# - **Return early**: Salir de función temprano si hay error (evita indentación excesiva)
# - **Single Responsibility**: Cada función debe hacer una cosa bien

#### **⚠️ Errores Comunes**
# Error 1: Olvidar return
def get_total(items):

    total = len(items)
    # ❌ Falta return, función retorna None

def get_total(items):
    total = len(items)
    return total  # ✅

# Error 2: Modificar parámetros mutables
def add_item(item, items=[]):  # ❌ Default mutable
    items.append(item)
    return items

def add_item(item, items=None):  # ✅
    if items is None:
        items = []
    items.append(item)
    return items

# Error 3: No validar None
def process(data):
    return data.upper()  # ❌ Falla si data es None

def process(data):
    if data is None:  # ✅
        return "N/A"
    return data.upper()