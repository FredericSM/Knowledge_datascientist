import streamlit as st
import numpy as np
import duckdb

# streamlit run Streamlit_test.py

st.write("""
		 SQL SAS
		 Spaced Repetition System SQL practice
		 """)

option = st.selectbox(
	"What woul you like to learn?",
	("Joins", "GroupBy", "Windows Functions"),
	index=None,
	placeholder="Select a topic",
)

st.write("You selected:", option)