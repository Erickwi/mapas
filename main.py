import streamlit as st

def main():
    st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
    st.write("Usa los botones para navegar por las opciones.")
    
    # Centrar la imagen
    st.image("cede.png", width=200)  # Tamaño pequeño de la imagen
    
    # Centrar los botones
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mapa Doctrinario"):
            st.experimental_set_query_params(menu_choice="Mapa Doctrinario")
        if st.button("Mapa de Publicaciones Militares"):
            st.experimental_set_query_params(menu_choice="Mapa de Publicaciones Militares")

    query_params = st.experimental_get_query_params()
    if "menu_choice" in query_params:
        menu_choice = query_params["menu_choice"][0]
        if menu_choice == "Mapa Doctrinario":
            st.write("Mapa Doctrinario seleccionado")
            # Aquí puedes agregar el menú específico para "Mapa Doctrinario"
        elif menu_choice == "Mapa de Publicaciones Militares":
            st.write("Mapa de Publicaciones Militares seleccionado")
            # Aquí puedes agregar el menú específico para "Mapa de Publicaciones Militares"

if __name__ == "__main__":
    main()