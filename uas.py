import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit

# emojis: https://www.webfx.com/tools/emoji-cheat-sheet/
# Streamlit page configuration 
st.set_page_config(page_title="Dashboard Interactive", page_icon=":bar_chart:", layout="wide")

# ---- READ EXCEL ----

df = pd.read_excel(
    io="juni.xlsx",
    engine="openpyxl",
    sheet_name="juni",
    nrows=20,
)
    # Add 'hour' column to dataframe
    #df["hour"] = pd.to_datetime(df["Time"], format="%H:%M:%S").dt.hour
    #return df

st.dataframe(df) # view dataframe on page

# ---- SIDEBAR ----
st.sidebar.header("Please Filter Here:")
wilayah = st.sidebar.multiselect(
    "Select the wilayah:",
    options=df["wilayah"].unique(),
    default=df["wilayah"].unique()
)

df_selection = df.query(
    "wilayah == @wilayah "
)

# ---- MAINPAGE ----
st.title(":bar_chart: Dashboard Interactive")
st.markdown("##")

# SALES BY WILAYAH [BAR CHART]
sales_by_branch = (
    df_selection.groupby(by=["wilayah"]).sum()[["penderekan"]].sort_values(by="penderekan")
)
fig_product_sales = px.bar(
    sales_by_branch,
    x="penderekan",
    y=sales_by_branch.index,
    orientation="h",
    title="<b>Penderekan Berdasarkan Wilayah</b>",
    color_discrete_sequence=["#BF00FF"] * len(sales_by_branch),
    template="plotly_white",
)
fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

st.plotly_chart(fig_product_sales, use_container_width=True)


