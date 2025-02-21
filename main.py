import streamlit as st

def main():
    st.title("🏠 Bienvenido al Mapa Doctrinario del Ejército")
    st.write("Usa los botones para navegar por las opciones.")
    
    # Centrar la imagen usando columnas
    col1, col2, col3 = st.columns(3)
    with col2:
        st.image("cede.png", width=200)
    
    # Centrar los botones usando columnas
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("Mapa Doctrinario"):
            st.switch_page("pages/Mapa_Doctrinario.py")
        if st.button("Mapa de Publicaciones Militares"):
            st.switch_page("pages/Mapa_de_Publicaciones_Militares.py")

if __name__ == "__main__":
    main()
