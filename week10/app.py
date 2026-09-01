from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Market Performance Dashboard", page_icon="📈", layout="wide")
DATA = Path(__file__).resolve().parent.parent / "data" / "stocks.csv"
df = pd.read_csv(DATA, parse_dates=["date"])
long = df.melt("date", var_name="company", value_name="price")
companies = st.sidebar.multiselect("Companies", sorted(long.company.unique()),
                                   default=sorted(long.company.unique()))

d = long[long.company.isin(companies)].copy()
first = d.groupby("company")["price"].transform("first")
d["index_100"] = d["price"] / first * 100

st.title("📈 Market Performance Dashboard")
st.caption("Compare relative performance without confusing different starting price levels.")
c1,c2,c3 = st.columns(3)
c1.metric("Companies", d.company.nunique())
c2.metric("Latest date", d.date.max().strftime("%Y-%m-%d"))
best = d.sort_values("date").groupby("company").tail(1).sort_values("index_100", ascending=False).iloc[0]
c3.metric("Best indexed result", f"{best.company}: {best.index_100:.0f}")

fig = px.line(d, x="date", y="index_100", color="company",
              title="Relative performance (start = 100)",
              labels={"index_100":"Indexed value","date":"Date","company":""})
fig.add_hline(y=100, line_dash="dash")
st.plotly_chart(fig, use_container_width=True)

latest = d.sort_values("date").groupby("company").tail(1).sort_values("index_100", ascending=False)
fig2 = px.bar(latest, x="index_100", y="company", orientation="h",
              text="index_100", title="Latest indexed performance")
fig2.update_traces(texttemplate="%{text:.0f}", textposition="outside")
st.plotly_chart(fig2, use_container_width=True)
