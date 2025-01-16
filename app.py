import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

df = pd.read_csv("pizzas.csv")

model = LinearRegression()
x = df[["diametro"]]
y = df[["preco"]]

model.fit(x, y)

print(model.predict([[115]])[0][0])

st.title("I.A prevendo o valor de uma pizza")
st.divider()

diametro = st.number_input("digite o tamanho do diâmetro da pizza:")

if diametro:
    preco_previsto = model.predict([[diametro]])[0][0]
    st.write(f"o valor da pizza com diametro de {diametro:.2f} é de R${preco_previsto:.2f}")
    st.balloons()

