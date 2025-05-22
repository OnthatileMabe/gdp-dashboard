import streamlit as st
import pandas as pd
import math
from pathlib import Path
import numpy as np
import datetime


# -------------------
# Page Config
# -------------------
st.set_page_config(page_title="Ciovita Dashboard", layout="wide")

# -------------------
# Branding
# -------------------
st.sidebar.title("🚴‍♂️ Ciovita")
st.sidebar.markdown("### Quality Meets Performance")

# -------------------
# Sidebar Navigation
# -------------------
menu = st.sidebar.selectbox(
    "🔽 Navigation",
    options=[
        "Menu",
        "Dashboard",
        "Return Records",
        "Return Tasks",
        "Products",
        "Tools: Settings",
        "Tools: Help"
    ]
)

# -------------------
# Sample Data
# -------------------
@st.cache_data
def generate_data():
    dates = pd.date_range(start="2023-01-01", periods=60)
    return pd.DataFrame({
        "date": dates,
        "sales": np.random.randint(100, 1000, size=len(dates)),
        "returns": np.random.randint(0, 50, size=len(dates)),
        "tasks": np.random.randint(1, 20, size=len(dates)),
        "product": np.random.choice(["Jersey", "Bib Shorts", "Cap", "Gloves"], size=len(dates))
    })

df = generate_data()

# -------------------
# Page Routing
# -------------------
st.title(f"📘 {menu}")

if menu == "Menu":
    st.write("Welcome to Ciovita's internal dashboard.")
    st.image("https://ciovita.com/cdn/shop/files/logo.png?v=1614324820", width=200)

elif menu == "Dashboard":
    st.subheader("Performance Overview")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", f"${df['sales'].sum():,}")
    col2.metric("Returns", f"{df['returns'].sum()} items")
    col3.metric("Tasks Completed", f"{df['tasks'].sum()}")

    st.line_chart(df.set_index("date")[["sales", "returns"]])

elif menu == "Return Records":
    st.subheader("Return Records Table")
    st.dataframe(df[["date", "returns"]])

elif menu == "Return Tasks":
    st.subheader("Return Tasks")
    st.bar_chart(df.set_index("date")["tasks"])

elif menu == "Products":
    st.subheader("Product Sales Distribution")
    product_data = df["product"].value_counts()
    st.bar_chart(product_data)

elif menu == "Tools: Settings":
    st.subheader("Settings")
    st.write("Configure company dashboard settings here.")

elif menu == "Tools: Help":
    st.subheader("Help")
    st.markdown("For support, contact: [support@ciovita.com](mailto:support@ciovita.com)")





