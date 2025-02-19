import streamlit as st

def main():
    st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
    st.write("Usa los botones para navegar por las opciones.")
    st.image("cede.png", width=200)  # Tamaño pequeño de la imagen
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mapa Doctrinario"):
            st.session_state.menu_choice = "Mapa Doctrinario"
            st.experimental_rerun()
        if st.button("Mapa de Publicaciones Militares"):
            st.session_state.menu_choice = "Mapa de Publicaciones Militares"
            st.experimental_rerun()

    if "menu_choice" in st.session_state:
        if st.session_state.menu_choice == "Mapa Doctrinario":
            st.write("Mapa Doctrinario seleccionado")
            # Redirigir a app.py
            st.experimental_set_query_params(page="app")
        elif st.session_state.menu_choice == "Mapa de Publicaciones Militares":
            st.write("Mapa de Publicaciones Militares seleccionado")
            # Redirigir a app.py
            st.experimental_set_query_params(page="app")

if __name__ == "__main__":
    main()