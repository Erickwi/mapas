import streamlit as st
from database import DatabaseManager
from forms import ManualForm
from visualization import Visualization
from excel_generator import ExcelGenerator

# Estilo personalizado para los colores de la interfaz
st.markdown(
    """
    <style>
    [data-testid="stSidebar"] {{
        display: none;
    }}
    [data-testid="stAppViewContainer"] {{
        background-color: #f5f5dc !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    # Configurar menú principal
    menu = ["Inicio", "Agregar Manual", "Ver Mapa", "Modificar Manual", "Generar Excel", "Borrar Manual"]
    choice = st.selectbox("Seleccione una opción:", menu)

    db_file = "doctrina.db"  # Ruta al archivo de la base de datos SQLite
    db = DatabaseManager(db_file)

    # Navegar entre las opciones
    if choice == "Inicio":
        st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
        st.write("Usa el menú desplegable para navegar por las opciones.")
        st.image("cede.png", use_container_width=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("Mapa Doctrinario"):
                st.session_state.menu_choice = "Mapa Doctrinario"
            if st.button("Mapa de Publicaciones Militares"):
                st.session_state.menu_choice = "Mapa de Publicaciones Militares"
        
        if "menu_choice" in st.session_state:
            if st.session_state.menu_choice == "Mapa Doctrinario":
                st.write("Mapa Doctrinario seleccionado")
                # Aquí puedes agregar el menú específico para "Mapa Doctrinario"
            elif st.session_state.menu_choice == "Mapa de Publicaciones Militares":
                st.write("Mapa de Publicaciones Militares seleccionado")
                # Aquí puedes agregar el menú específico para "Mapa de Publicaciones Militares"
    elif choice == "Agregar Manual":
        st.title("➕ Agregar Manual")
        ManualForm.agregar_manual_form(db)
    elif choice == "Ver Mapa":
        st.title("🗺️ Mapa Doctrinario Filtrado")
        Visualization.mostrar_mapa_filtrado(db_file)
    elif choice == "Modificar Manual":
        st.title("✏️ Modificar Manual")
        manual_id = st.text_input("ID del Manual a Modificar:")
        if manual_id:
            ManualForm.modificar_manual_form(db, manual_id)
    elif choice == "Generar Excel":
        st.title("📊 Generar Excel")
        ExcelGenerator.generar_excel_filtrado(db_file)
    elif choice == "Borrar Manual":
        st.title("🗑️ Borrar Manual")
        ManualForm.borrar_manual_form(db)

if __name__ == "__main__":
    main()