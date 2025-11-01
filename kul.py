# app.py
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO

st.set_page_config(page_title="Interactive EDA - Car Dataset", layout="wide", initial_sidebar_state="expanded")

@st.cache_data
def load_data(path=r"C:\Users\kulde\Desktop\STREMLIT\CARDATASET.csv"):
    try:
        df = pd.read_csv(path)
    except Exception as e:
        st.error(f"Could not read CSV at {path}: {e}")
        return None
    return df

def convert_df_to_bytes(df):
    return df.to_csv(index=False).encode('utf-8')

# ---- Load data ----
df = load_data()  # default path is /mnt/data/CARDATASET.csv
if df is None:
    st.stop()

# ---- Sidebar controls ----
st.sidebar.header("Filters & Settings")
sample_size = st.sidebar.slider("Show sample rows", min_value=5, max_value=500, value=25, step=5)
numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()
all_cols = df.columns.tolist()

st.sidebar.markdown("### Column selection")
cols_to_show = st.sidebar.multiselect("Columns to display", options=all_cols, default=all_cols[:min(6, len(all_cols))])

st.sidebar.markdown("### Row filters (quick)")
filter_col = st.sidebar.selectbox("Filter column (optional)", options=[None] + all_cols, index=0)
filter_val = None
if filter_col:
    unique_vals = df[filter_col].dropna().unique().tolist()[:200]
    if df[filter_col].nunique() <= 50:
        filter_val = st.sidebar.multiselect("Filter values", options=unique_vals, default=unique_vals[:3])
    else:
        # for high-cardinality allow text match
        q = st.sidebar.text_input("Text contains (for filter)")
        if q:
            filter_val = q

st.sidebar.markdown("---")
st.sidebar.markdown("### Visual options")
plot_kind = st.sidebar.selectbox("Plot type", ["Count (categorical)", "Histogram (numeric)", "Boxplot", "Scatter", "Correlation heatmap"])
x_col = st.sidebar.selectbox("X column", options=all_cols, index=0)
y_col = st.sidebar.selectbox("Y column (for scatter/box)", options=[None] + all_cols, index=0 if len(all_cols)>0 else None)
agg_func = st.sidebar.selectbox("Aggregate function (for grouped views)", ["count", "mean", "median", "sum"], index=0)

st.sidebar.markdown("---")
st.sidebar.markdown("Download")
if st.sidebar.button("Download filtered CSV"):
    buf = convert_df_to_bytes(df if (not filter_col) else df[df[filter_col].astype(str).apply(lambda s: (filter_val in s) if isinstance(filter_val,str) else True)])
    st.sidebar.download_button("Download CSV", data=buf, file_name="filtered_data.csv", mime="text/csv")

# ---- Apply filters ----
df_view = df.copy()
if filter_col:
    if isinstance(filter_val, list):
        if len(filter_val) > 0:
            df_view = df_view[df_view[filter_col].isin(filter_val)]
    elif isinstance(filter_val, str) and filter_val.strip() != "":
        df_view = df_view[df_view[filter_col].astype(str).str.contains(filter_val, case=False, na=False)]

# ---- Main layout ----
st.title("🔎 Interactive EDA — Car Dataset")
st.markdown("Auto-generated EDA interface (filters, KPIs, plots).")

# KPI cards (top row)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Rows (filtered)", len(df_view), delta=len(df_view)-len(df))
with col2:
    st.metric("Columns", len(df.columns))
with col3:
    n_missing = df_view.isna().sum().sum()
    st.metric("Missing values", int(n_missing))
with col4:
    st.metric("Numeric cols", len(numeric_cols))

st.markdown("---")
# Data sample & summary
left, right = st.columns((1, 1))
with left:
    st.subheader("Data sample")
    st.dataframe(df_view[cols_to_show].head(sample_size), use_container_width=True)
    st.write("Show more / export below.")
with right:
    st.subheader("Quick summary (selected numeric cols)")
    if numeric_cols:
        desc = df_view[numeric_cols].describe().T
        st.dataframe(desc, use_container_width=True)
    else:
        st.info("No numeric columns detected.")

# Missing values detail
st.subheader("Missing values by column")
missing_df = df_view.isnull().sum().reset_index()
missing_df.columns = ["column", "missing_count"]
missing_df['missing_pct'] = (missing_df['missing_count'] / len(df_view) * 100).round(2)
st.dataframe(missing_df.sort_values("missing_count", ascending=False), use_container_width=True)

# Categorical distributions / value counts
st.subheader("Top value counts (categorical columns)")
for c in cat_cols[:6]:
    top = df_view[c].value_counts(dropna=True).head(8)
    if len(top) > 0:
        st.markdown(f"**{c}**")
        chart = alt.Chart(top.reset_index()).mark_bar().encode(
            x=alt.X('index:N', sort='-y', title=c),
            y=alt.Y(c + ':Q', title='count'),
            tooltip=['index', c]
        ).transform_calculate(**{
            c: 'datum["{}"]'.format(c)
        }).encode(
            x=alt.X('index:N', sort='-y', title=c),
            y=alt.Y('{}:Q'.format(c), title='count')
        )
        # we fallback to a simple bar with pandas if altair mapping complicated
        st.bar_chart(top)

st.markdown("---")
# Plots area
st.subheader("Plots")
if plot_kind == "Count (categorical)":
    if x_col in cat_cols:
        vc = df_view[x_col].value_counts().reset_index()
        vc.columns = [x_col, "count"]
        c = alt.Chart(vc).mark_bar().encode(
            x=alt.X(f"{x_col}:N", sort='-y'),
            y="count:Q",
            tooltip=[x_col, "count"]
        )
        st.altair_chart(c.interactive(), use_container_width=True)
    else:
        st.info("Choose a categorical column for Count plot (sidebar -> X column).")

elif plot_kind == "Histogram (numeric)":
    if x_col in numeric_cols:
        hist = alt.Chart(df_view).mark_bar().encode(
            alt.X(f"{x_col}:Q", bin=alt.Bin(maxbins=40)),
            y='count()'
        )
        st.altair_chart(hist, use_container_width=True)
    else:
        st.info("Choose a numeric column for Histogram.")

elif plot_kind == "Boxplot":
    if x_col in cat_cols and y_col in numeric_cols:
        box = alt.Chart(df_view).mark_boxplot(extent='min-max').encode(
            x=f"{x_col}:N",
            y=f"{y_col}:Q",
            tooltip=[x_col, y_col]
        )
        st.altair_chart(box, use_container_width=True)
    else:
        st.info("For Boxplot: choose categorical X and numeric Y in sidebar.")

elif plot_kind == "Scatter":
    if x_col in numeric_cols and y_col in numeric_cols:
        scatter = alt.Chart(df_view).mark_circle(size=60).encode(
            x=f"{x_col}:Q",
            y=f"{y_col}:Q",
            tooltip=[x_col, y_col]
        ).interactive()
        st.altair_chart(scatter, use_container_width=True)
    else:
        st.info("For Scatter: choose numeric X and numeric Y in sidebar.")

elif plot_kind == "Correlation heatmap":
    if len(numeric_cols) >= 2:
        corr = df_view[numeric_cols].corr()
        fig, ax = plt.subplots(figsize=(10, 8))
        sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", ax=ax)
        ax.set_title("Correlation matrix")
        st.pyplot(fig)
    else:
        st.info("Need at least two numeric columns for correlation heatmap.")

st.markdown("---")
# Advanced: grouped aggregation
st.subheader("Grouped aggregation (quick)")
group_by_col = st.selectbox("Group by column (optional)", options=[None] + all_cols, index=0)
if group_by_col:
    agg_col = st.selectbox("Aggregate column (numeric)", options=[None] + numeric_cols)
    if agg_col:
        grouped = df_view.groupby(group_by_col)[agg_col].agg(agg_func).reset_index().sort_values(agg_col, ascending=False).head(50)
        st.dataframe(grouped, use_container_width=True)
        st.bar_chart(grouped.set_index(group_by_col)[agg_col])
    else:
        st.info("Select a numeric column to aggregate.")

st.markdown("---")
# Data download and export
st.subheader("Export")
csv = convert_df_to_bytes(df_view[cols_to_show])
st.download_button("Download current view as CSV", data=csv, file_name="eda_view.csv", mime="text/csv")


