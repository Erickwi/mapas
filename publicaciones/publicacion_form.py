import streamlit as st

class PublicacionForm:

    @staticmethod
    def agregar_publicacion_form(db):
        """
        Muestra el formulario para agregar una nueva publicación.
        """
        # Categorías principales (Eje X) y subcategorías
        categorias_x = [
            "ARTILLERÍA",
            "INGENIERÍA",
            "COMUNICACIONES",
            "INTELIGENCIA MILITAR",
            "AVIACIÓN DEL EJÉRCITO",
            "FUERZAS ESPECIALES",
            "SELVA",
            "SOSTENIMIENTO",
            "ESPECIALISTAS",
            "PERSONAL",
            "LOGÍSTICA EN GENERAL",
            "INTENDENCIA",
            "TRANSPORTES",
            "MATERIAL DE GUERRA",
            "SANIDAD",
            "CIENCIAS DE LA EDUCACIÓN",
            "MÚSICOS",
            "AYUDANTÍA GENERAL",
            "COMUNICACIÓN SOCIAL",
            "VETERINARIA",
            "AGROPECUARIA"
        ]

        subcategorias_x = {
            "ARTILLERÍA": [],
            "INGENIERÍA": [],
            "COMUNICACIONES": [],
            "INTELIGENCIA MILITAR": [],
            "AVIACIÓN DEL EJÉRCITO": [],
            "FUERZAS ESPECIALES": [],
            "SELVA": [],
            "SOSTENIMIENTO": ["Subcat S1", "Subcat S2", "Subcat S3"],
            "ESPECIALISTAS": ["Subcat E1", "Subcat E2", "Subcat E3"],
            "PERSONAL": [],
            "LOGÍSTICA EN GENERAL": [],
            "INTENDENCIA": [],
            "TRANSPORTES": [],
            "MATERIAL DE GUERRA": [],
            "SANIDAD": [],
            "CIENCIAS DE LA EDUCACIÓN": [],
            "MÚSICOS": [],
            "AYUDANTÍA GENERAL": [],
            "COMUNICACIÓN SOCIAL": [],
            "VETERINARIA": [],
            "AGROPECUARIA": []
        }

        categoria_x = st.selectbox("Categoría X:", categorias_x)

        # Mostrar subcategoría sólo si la categoría X la tiene
        posibles_subcats = subcategorias_x.get(categoria_x, [])
        if posibles_subcats:
            subcategoria_x = st.selectbox("Subcategoría X:", posibles_subcats)
        else:
            subcategoria_x = ""

        # Ejemplo de categorías Y (ajusta según tu proyecto)
        categorias_y = [
            "Documento Interno",
            "Manual de Operaciones",
            "Guía de Procedimientos",
            "Reglamento",
            "Plan de Acción",
            "Otro"
        ]
        categoria_y = st.selectbox("Categoría Y:", categorias_y)

        # Nombre
        nombre = st.text_input("Nombre de la Publicación:")

        # Año: opción "No Publicado" + rango
        opciones_anio = ["No Publicado"] + list(range(2018, 2031))
        anio = st.selectbox("Año de Publicación:", opciones_anio)

        # Estados posibles
        estados = ["Publicado", "Actualización", "En Generación", "Virtualizado", "Por Generar"]
        estado = st.selectbox("Estado de la Publicación:", estados)

        # Subproceso si está "En Generación"
        subproceso_estado = None
        if estado == "En Generación":
            subprocesos_estado = ["Investigación", "Experimentación", "Edición y Difusión"]
            subproceso_estado = st.selectbox("Subproceso del Estado:", subprocesos_estado)

        # Botón para agregar
        if st.button("Agregar Publicación"):
            if not nombre.strip():
                st.error("❌ El campo 'Nombre de la Publicación' es obligatorio.")
            else:
                db.add_publicacion(
                    categoria_x,
                    subcategoria_x,
                    categoria_y,
                    nombre,
                    str(anio),  # Convertir a string si anio es TEXT en DB
                    estado,
                    subproceso_estado
                )
                st.success(f"✅ Publicación '{nombre}' agregada correctamente.")

    @staticmethod
    def modificar_publicacion_form(db, publicacion_id):
        """
        Muestra el formulario para modificar una publicación existente.
        """
        publicacion = db.fetch_publicacion_by_id(publicacion_id)
        if not publicacion:
            st.error(f"❌ No se encontró una publicación con el ID {publicacion_id}.")
            return

        # Definimos las mismas categorías para re-poblar el formulario
        categorias_x = [
            "ARTILLERÍA",
            "INGENIERÍA",
            "COMUNICACIONES",
            "INTELIGENCIA MILITAR",
            "AVIACIÓN DEL EJÉRCITO",
            "FUERZAS ESPECIALES",
            "SELVA",
            "SOSTENIMIENTO",
            "ESPECIALISTAS",
            "PERSONAL",
            "LOGÍSTICA EN GENERAL",
            "INTENDENCIA",
            "TRANSPORTES",
            "MATERIAL DE GUERRA",
            "SANIDAD",
            "CIENCIAS DE LA EDUCACIÓN",
            "MÚSICOS",
            "AYUDANTÍA GENERAL",
            "COMUNICACIÓN SOCIAL",
            "VETERINARIA",
            "AGROPECUARIA"
        ]
        subcategorias_x = {
            "ARTILLERÍA": [],
            "INGENIERÍA": [],
            "COMUNICACIONES": [],
            "INTELIGENCIA MILITAR": [],
            "AVIACIÓN DEL EJÉRCITO": [],
            "FUERZAS ESPECIALES": [],
            "SELVA": [],
            "SOSTENIMIENTO": ["Subcat S1", "Subcat S2", "Subcat S3"],
            "ESPECIALISTAS": ["Subcat E1", "Subcat E2", "Subcat E3"],
            "PERSONAL": [],
            "LOGÍSTICA EN GENERAL": [],
            "INTENDENCIA": [],
            "TRANSPORTES": [],
            "MATERIAL DE GUERRA": [],
            "SANIDAD": [],
            "CIENCIAS DE LA EDUCACIÓN": [],
            "MÚSICOS": [],
            "AYUDANTÍA GENERAL": [],
            "COMUNICACIÓN SOCIAL": [],
            "VETERINARIA": [],
            "AGROPECUARIA": []
        }

        # Recuperar valores actuales de la DB
        categoria_x_value = publicacion.get("categoria_x", "")
        subcategoria_x_value = publicacion.get("subcategoria_x", "")
        categoria_y_value = publicacion.get("categoria_y", "")
        nombre_value = publicacion.get("nombre", "")
        anio_value = publicacion.get("anio", "No Publicado")
        estado_value = publicacion.get("estado", "Publicado")
        subproceso_estado_value = publicacion.get("subproceso_estado", "")

        # Asegurarnos de que la categoría X esté en la lista
        if categoria_x_value not in categorias_x:
            categoria_x_value = categorias_x[0]
        categoria_x_index = categorias_x.index(categoria_x_value)
        categoria_x = st.selectbox("Categoría X:", categorias_x, index=categoria_x_index)

        # Subcategorías correspondientes
        posibles_subcats = subcategorias_x.get(categoria_x, [])
        if subcategoria_x_value not in posibles_subcats:
            subcategoria_x_value = posibles_subcats[0] if posibles_subcats else ""
        if posibles_subcats:
            subcategoria_x_index = posibles_subcats.index(subcategoria_x_value)
            subcategoria_x = st.selectbox("Subcategoría X:", posibles_subcats, index=subcategoria_x_index)
        else:
            subcategoria_x = ""

        # Categoría Y
        categorias_y = [
            "Documento Interno",
            "Manual de Operaciones",
            "Guía de Procedimientos",
            "Reglamento",
            "Plan de Acción",
            "Otro"
        ]
        if categoria_y_value not in categorias_y:
            categoria_y_value = categorias_y[0]
        categoria_y_index = categorias_y.index(categoria_y_value)
        categoria_y = st.selectbox("Categoría Y:", categorias_y, index=categoria_y_index)

        # Nombre
        nombre = st.text_input("Nombre de la Publicación:", value=nombre_value)

        # Año
        opciones_anio = ["No Publicado"] + list(range(2018, 2031))
        # Convertir a str para compararlo con la lista de opciones
        if str(anio_value) not in [str(a) for a in opciones_anio]:
            anio_value = "No Publicado"
        anio_index = [str(a) for a in opciones_anio].index(str(anio_value))
        anio = st.selectbox("Año de Publicación:", opciones_anio, index=anio_index)

        # Estado
        estados = ["Publicado", "Actualización", "En Generación", "Virtualizado", "Por Generar"]
        if estado_value not in estados:
            estado_value = "Publicado"
        estado_index = estados.index(estado_value)
        estado = st.selectbox("Estado de la Publicación:", estados, index=estado_index)

        # Subproceso
        subproceso_estado = st.text_input("Subproceso del Estado:", value=subproceso_estado_value)

        # Botón para guardar cambios
        if st.button("Guardar Cambios"):
            db.update_publicacion(
                publicacion_id,
                categoria_x,
                subcategoria_x,
                categoria_y,
                nombre,
                str(anio),
                estado,
                subproceso_estado
            )
            st.success(f"✅ Publicación con ID {publicacion_id} actualizada correctamente.")

    @staticmethod
    def borrar_publicacion_form(db):
        """
        Muestra el formulario para borrar una publicación (requiere el ID).
        """
        publicacion_id = st.number_input("Ingrese el ID de la publicación a borrar:", min_value=1, step=1)

        if st.button("❌ Borrar Publicación"):
            if db.delete_publicacion(publicacion_id):
                st.success(f"✅ Publicación con ID {publicacion_id} eliminada correctamente.")
            else:
                st.error(f"❌ No se encontró una publicación con ID {publicacion_id}.")

    @staticmethod
    def ver_publicaciones(db):
        """
        Muestra todas las publicaciones en una tabla.
        """
        publicaciones = db.fetch_all_publicaciones()
        if publicaciones:
            st.write("### Publicaciones")
            st.table(publicaciones)
        else:
            st.write("No hay publicaciones disponibles.")