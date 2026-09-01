# Data Visualization Exercises — Improved Edition

This is a **new, separate version** of the original coursework repository. The original folders are not overwritten.

## What changed

- Replaced the original exercise datasets with more focused datasets.
- Increased analytical variety: flowers, financial time series, wine chemistry, restaurant bills, global development, car-share demand and African economic geography.
- Reworked every exercise around a clear visualization question.
- Added consistent chart design, informative titles and more meaningful labels.
- Added two refreshed Streamlit dashboards.
- Added a single `requirements.txt` for reproducibility.

## Structure

`week02`–`week08` contain Jupyter exercises.  
`week09` and `week10` contain Streamlit dashboards.  
`data/` contains the new datasets and the map GeoJSON.

## Run

```bash
pip install -r requirements.txt
jupyter notebook
```

For dashboards:

```bash
streamlit run week09/app.py
streamlit run week10/app.py
```

## Dataset notes

- Iris, Stocks, Tips, Carshare and Gapminder are distributed through Plotly Express example datasets.
- Wine chemistry comes from scikit-learn's built-in wine recognition dataset.
- African indicators are extracted from the included Natural Earth GeoJSON attributes so the map join is reproducible.
