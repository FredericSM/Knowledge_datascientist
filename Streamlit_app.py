import streamlit as st
import numpy as np
import pandas as pd
import duckdb

# streamlit run Streamlit_test.py

st.write("""
		 SQL SAS
		 Spaced Repetition System SQL practice
		 """)

with st.sidebar:
	option = st.selectbox(
		"What woul you like to learn?",
		("Joins", "GroupBy", "Windows Functions"),
		index=None,
		placeholder="Select a topic",
	)

	st.write("You selected:", option)

data = {"a": [1, 2, 3, 4, 5], "b": [10, 20, 30, 40, 50]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(['Dog', 'Cat', 'Panda'])

with tab1:
	sql_query = st.text_area(label="Write your SQL query here")
	result = duckdb.query(sql_query).df()
	st.write(f"Your query result is: {result}")
	st.dataframe(result)

