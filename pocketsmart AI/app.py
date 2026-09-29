import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Pocket Smart AI", layout="wide")
st.title("💰 Pocket Smart AI - Your Personal Expense Tracker")

if 'expenses' not in st.session_state:
    st.session_state.expenses = []

# Sidebar
st.sidebar.header("Add Expense")
amount = st.sidebar.number_input("Amount (₹)", min_value=1, value=100)
category = st.sidebar.selectbox("Category", ["Food", "Transport", "Shopping", "Bills", "Others"])
note = st.sidebar.text_input("Note", "lunch")

if st.sidebar.button("Add Expense"):
    st.session_state.expenses.append({"Amount": amount, "Category": category, "Note": note})
    st.sidebar.success("Added da!")

# Main
if len(st.session_state.expenses) == 0:
    st.info("No expenses yet da! Sidebar la add pannu!")
else:
    df = pd.DataFrame(st.session_state.expenses)
    c1, c2, c3 = st.columns(3)
    c1.metric("Total Spent", f"₹{df['Amount'].sum()}")
    c2.metric("Total Bills", len(df))
    c3.metric("Avg Spend", f"₹{df['Amount'].mean():.0f}")

    tab1, tab2 = st.tabs(["Charts", "Data"])
    with tab1:
        fig = px.pie(df, values='Amount', names='Category', title="Category Wise Spend")
        st.plotly_chart(fig, use_container_width=True)
    with tab2:
        st.dataframe(df, use_container_width=True)