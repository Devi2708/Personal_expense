import streamlit as st
from PIL import Image
image = Image.open('C:\\Users\\Devipriya\\Desktop\\Devi_Learning\\Personal_expense_Proj1\\Personal_Expenses.jpg')
st.title('Analyzing Personal Expenses')
st.image(image,caption='Personal Expense',use_container_width=True)
st.write("""This project is about a detailed analysis of our personal expenses for a year. It will be very useful for all of us to estimate and plan our expenses for the future accordingly. """)