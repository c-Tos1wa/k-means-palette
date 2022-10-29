import streamlit as st

st.title('Gerador de paleta')

image = st.file_uploader("Faça upload da imagem", ["jpg", "jpeg"])

if image:
    st.image(image)
    button_palette = st.button("Gerar paleta")