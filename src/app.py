import streamlit as st

st.set_page_config(page_title="Neuronas")

st.image("media/neuronas.jpg")

st.title("Neuronas")

def show_result(y, key):
    if st.button("Calcular la salida", key=key):
        st.write("El resultado es ", y)

one_entry, two_entries, three_entries = st.tabs(["Una Entrada", "Dos Entradas", "Tres Entradas"])

with one_entry:
    x = st.slider("Peso", 0.0, 5.0, 0.5)

    w = st.number_input("Entrada")

    y = x * w

    show_result(y, "one")

with two_entries:
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("w01", 0.0, 5.0, 0.5, key="w01", label_visibility="hidden")

        x0 = st.number_input("Entrada x0", key="x01")

    with col2:
        st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("w01", 0.0, 5.0, 0.5, key="w11", label_visibility="hidden")

        x1 = st.number_input("Entrada x1", key="x11")

    y = x0 * w0 + x1 * w1

    show_result(y, "two")

with three_entries:
    col3, col4, col5 = st.columns(3)

    with col3:
        st.markdown("Peso w<sub>0</sub>", unsafe_allow_html=True)
        w0 = st.slider("w02", 0.0, 5.0, 0.5, key="w02", label_visibility="hidden")

        x0 = st.number_input("Entrada x0", key="x02")

    with col4:
        st.markdown("Peso w<sub>1</sub>", unsafe_allow_html=True)
        w1 = st.slider("w02", 0.0, 5.0, 0.5, key="w12", label_visibility="hidden")

        x1 = st.number_input("Entrada x1", key="x12")

    with col5:
        st.markdown("Peso w<sub>2</sub>", unsafe_allow_html=True)
        w2 = st.slider("w2", 0.0, 5.0, 0.5, key="w2", label_visibility="hidden")

        x2 = st.number_input("Entrada x2", key="x2")

    b = st.number_input("Sesgo")

    y = x0 * w0 + x1 * w1 + x2 * w2 + b

    show_result(y, "three")

st.divider()

st.write("Autor: Alberto Moreno González - ")
st.write("Máster FP en Inteligencia Artificial y Big Data del Centro Integrado en CPIFP Alan Turing (Málaga)")
