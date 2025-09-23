# pylint: disable=missing-module-docstring
import ast
import io
import os


import duckdb
import pandas as pd
import streamlit as st
from datetime import date, timedelta

# streamlit run Streamlit_test.py

con = duckdb.connect(database="data/exercices_sql_tables.duckdb", read_only=False)

ANSWER_STR = """
SELECT * FROM beverages
CROSS JOIN food_items
"""

if "data" not in os.listdir():
    os.mkdir("data")

if "exercices_sql_tables.duckdb" not in os.listdir("data"):
    exec(open("init_db.py").read())

def check_users_solution(user_query: str) -> None:
    """
    Check that user SQL query is correct by:
    1: checking the columns
    2: checking the values
    :param user_query: SQL query written by the user
    """
    result = con.execute(user_query).df()
    st.dataframe(result)

    try:
        result = result[solution_df.columns]
        if result.compare(solution_df).shape == (0, 0):
            st.write("Congratulations! Your solution is correct.")
            st.balloons()
        else:
            st.dataframe(result.compare(solution_df))
    except KeyError as e:
        st.write("some columns are missing")

    n_lines_difference = result.shape[0] - solution_df.shape[0]
    if n_lines_difference != 0:
        st.write(
            f"your result has {n_lines_difference} lines difference with the solution_df"
        )

st.write(
    """
		 SQL SAS
		 Spaced Repetition System SQL practice
		 """
)

with st.sidebar:
    available_themes_df = con.execute('SELECT DISTINCT theme FROM memory_state').df()
    theme = st.selectbox(
        "What woul you like to learn?",
        available_themes_df["theme"].unique(),
        index=None,
        placeholder="Select a topic",
    )

    st.write("You selected:", theme)

    if not theme:
        theme = "cross_joins"
    exercice = (
        con.execute(f"SELECT * FROM memory_state WHERE theme='{theme}'")
        .df()
        .sort_values(by="last_reveiwed")
        .reset_index()
    )
    st.write(exercice)

    exercise_name = exercice.loc[0, "exercise_name"]
    with open(f"answer/{exercise_name}.sql", "r") as file:
        answer = file.read()

    solution_df = con.execute(answer).df()

st.header("Enter your code:")
query = st.text_area(label="your SQL query", key="user_input")


if query:
    check_users_solution(query)

for n_days in [2, 7, 21]:
    if st.button(f"revoir dans {n_days} jours"):
        next_review = date.today() + timedelta(days=n_days)
        con.execute(
            f"UPDATE memory_state SET last_reveiwed = '{next_review}' WHERE exercise_name='{exercise_name}'"
        )
        st.rerun()

if st.button("Reset"):
    con.execute(f"UPDATE memory_state SET last_reveiwed = '1970-01-01'")
    st.rerun()

tab1, tab2 = st.tabs(["Tables", "solution"])

with tab1:
    exercice_tables = exercice.loc[0, "tables"]
    for table in exercice_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM {table}").df()
        st.dataframe(df_table)

with tab2:
    st.write(answer)
