
# ## 🔧 **MÓDULO 3: Programación Orientada a Objetos (45 min)**

# ### **🎯 Objetivo del Módulo**
# Entender cómo las aplicaciones backend modernas organizan código usando clases, especialmente para modelos de base de datos.

# ### **📚 ¿Qué es este módulo?**
# POO (Programación Orientada a Objetos) es un paradigma donde agrupas datos y funciones relacionadas en "objetos". En aplicaciones backend:
# # - Cada tabla de BD se representa como una clase (User, Product, Order, etc.)
# # - Los ORMs como SQLAlchemy usan POO para mapear tablas a objetos Python
# - Servicios y funcionalidades se organizan en clases reutilizables

# ### **💡 ¿Por qué es importante?**
# Los modelos de base de datos en aplicaciones backend pueden tener miles de líneas definiendo clases. Para trabajar profesionalmente DEBES entender:
# - Cómo se definen clases
# - Cómo crear instancias de objetos
# - Cómo usar métodos de instancia y de clase
# - Cómo funciona la herencia y composición

# ### **🔍 Casos de Uso Reales**
# Ejemplo típico de un modelo ORM:

class Route(db.Model):
    __tablename__ = "routes"
    id = db.Column(db.Integer, primary_key=True)
    completed = db.Column(db.Boolean, default=False)
    carrier_id = db.Column(db.Integer)


# Esto te permite interactuar con la base de datos así:

route = Route.query.filter_by(id=12345).first()
route.completed = True
db.session.commit()

