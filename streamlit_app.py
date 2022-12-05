import streamlit
import pandas

streamlit.title('My Parents New Healithy Diner')

streamlit.header('Breakfast Menu')
streamlit.text('Veggie Sandwich')
streamlit.text('Corn Salad')
streamlit.text('Kale and Spinach Salad')
streamlit.text('Orange juice')
streamlit.text('Coffee')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
