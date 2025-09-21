# pylint: disable=missing-module-docstring
import io

import streamlit as st
import pandas as pd
import duckdb

# streamlit run Streamlit_test.py

CSV = """
beverage,price
orange juice,2.5
Expresso,2
Tea,3
"""

beverages=pd.read_csv(io.StringIO(CSV))

CSV2 = """
food_item, food_price
cookie juice,2.5
chocolatine,2
muffin,3
"""

food_items = pd.read_csv(io.StringIO(CSV2))

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

solution_df = duckdb.sql(ANSWER_STR).df()

st.write(
    """
		 SQL SAS
		 Spaced Repetition System SQL practice
		 """
)

with st.sidebar:
    option = st.selectbox(
        "What woul you like to learn?",
        ("Joins", "GroupBy", "Windows Functions"),
        index=None,
        placeholder="Select a topic",
    )

    st.write("You selected:", option)

st.header("Enter your code:")
query = st.text_area(label="your SQL query", key="user_input")
if query:
    result = duckdb.sql(query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"your result has {n_lines_difference} lines difference with the solution_df"
        )


tab1, tab2 = st.tabs(["Tables", "solution_df"])

with tab1:
    st.write("table: beverages")
    st.dataframe(beverages)
    st.write("table: food_items")
    st.dataframe(food_items)
    st.write("expected:")
    st.dataframe(solution_df)

with tab2:
    st.write(ANSWER_STR)
