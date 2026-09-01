from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Global Development Explorer", page_icon="🌍", layout="wide")
DATA = Path(__file__).resolve().parent.parent / "data" / "global_development.csv"
df = pd.read_csv(DATA)
year = st.sidebar.slider("Year", int(df.year.min()), int(df.year.max()), 2007)
d = df[df.year == year].copy()
continent = st.sidebar.multiselect("Continent", sorted(d.continent.unique()), default=sorted(d.continent.unique()))
d = d[d.continent.isin(continent)]

st.title("🌍 Global Development Explorer")
st.caption("Explore the relationship between prosperity, longevity and population.")
c1,c2,c3 = st.columns(3)
c1.metric("Countries", len(d))
c2.metric("Median life expectancy", f"{d.lifeExp.median():.1f} years")
c3.metric("Median GDP per capita", f"${d.gdpPercap.median():,.0f}")

left,right = st.columns(2)
with left:
    top = d.nlargest(10, "lifeExp").sort_values("lifeExp")
    fig = px.bar(top, x="lifeExp", y="country", orientation="h",
                 title="Countries with the longest life expectancy",
                 labels={"lifeExp":"Life expectancy (years)","country":""})
    st.plotly_chart(fig, use_container_width=True)
with right:
    fig = px.scatter(d, x="gdpPercap", y="lifeExp", size="pop", color="continent",
                     hover_name="country", log_x=True, size_max=45,
                     title="Higher incomes generally coincide with longer lives",
                     labels={"gdpPercap":"GDP per capita (log scale)","lifeExp":"Life expectancy"})
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Country details")
st.dataframe(d[["country","continent","lifeExp","gdpPercap","pop"]].sort_values("lifeExp", ascending=False),
             use_container_width=True, hide_index=True)
