
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
from io import StringIO, BytesIO

# ---------- Page setup ----------
st.set_page_config(page_title="Quick EDA for CSV", layout="wide")
st.title("📊 Quick EDA (Streamlit)")
st.caption("Upload your CSV and explore: summary, filters, charts, correlations, and group-by analysis.")

# Make Altair handle larger datasets
alt.data_transformers.disable_max_rows()

# ---------- Helpers ----------
@st.cache_data(show_spinner=False)
def load_csv(file) -> pd.DataFrame:
    if file is None:
        # Try to load a local fallback file if present
        try:
            return pd.read_csv("CARDATASET.csv")
        except Exception:
            return pd.DataFrame()
    else:
        try:
            return pd.read_csv(file)
        except Exception:
            # Try common encodings
            for enc in ["utf-8", "latin1", "cp1252"]:
                try:
                    file.seek(0)
                    return pd.read_csv(file, encoding=enc)
                except Exception:
                    pass
            return pd.DataFrame()

def split_columns(df: pd.DataFrame):
    num_cols = df.select_dtypes(include="number").columns.tolist()
    cat_cols = df.select_dtypes(exclude="number").columns.tolist()
    return num_cols, cat_cols

def add_derived_cols(df: pd.DataFrame):
    # Add car_age if 'year' exists
    if "year" in df.columns and np.issubdtype(df["year"].dtype, np.number):
        current_year = pd.Timestamp.today().year
        df = df.copy()
        df["car_age"] = current_year - df["year"]
    return df

def download_csv(df: pd.DataFrame, name="filtered.csv"):
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button("⬇️ Download filtered CSV", data=csv, file_name=name, mime="text/csv")

# ---------- Sidebar: Load data ----------
st.sidebar.header("1) Load data")
uploaded = st.sidebar.file_uploader("Upload a CSV file", type=["csv"])
df = load_csv(uploaded)

if df.empty:
    st.info("Upload a CSV (or place **CARDATASET.csv** next to this app and reload).")
    st.stop()

# Optional derived columns (e.g., car age)
df = add_derived_cols(df)

# ---------- Overview ----------
st.subheader("🔎 Dataset overview")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Rows", f"{len(df):,}")
c2.metric("Columns", f"{df.shape[1]:,}")
num_cols, cat_cols = split_columns(df)
c3.metric("Numeric cols", f"{len(num_cols)}")
c4.metric("Categorical cols", f"{len(cat_cols)}")

with st.expander("📄 Preview (first 50 rows)", expanded=False):
    st.dataframe(df.head(50), use_container_width=True)

with st.expander("ℹ️ Column types", expanded=False):
    st.dataframe(pd.DataFrame({"column": df.columns, "dtype": df.dtypes.astype(str)}))

with st.expander("❓ Missing values", expanded=False):
    na = df.isna().sum().reset_index()
    na.columns = ["column", "missing_count"]
    st.dataframe(na)

# ---------- Sidebar: Filters ----------
st.sidebar.header("2) Filter data")

# Build filters dynamically
filtered = df.copy()

# Categorical filters
for col in cat_cols:
    vals = filtered[col].dropna().astype(str).unique().tolist()
    vals = sorted(vals)[:500]  # cap to avoid huge lists
    selected = st.sidebar.multiselect(f"{col} (choose one or more)", options=vals, default=[])
    if selected:
        filtered = filtered[filtered[col].astype(str).isin(selected)]

# Numeric filters
for col in num_cols:
    min_v = float(np.nanmin(filtered[col].values)) if filtered[col].notna().any() else 0.0
    max_v = float(np.nanmax(filtered[col].values)) if filtered[col].notna().any() else 0.0
    if np.isfinite(min_v) and np.isfinite(max_v) and min_v != max_v:
        lo, hi = st.sidebar.slider(f"{col} range", min_value=float(np.floor(min_v)), max_value=float(np.ceil(max_v)), value=(float(np.floor(min_v)), float(np.ceil(max_v))))
        filtered = filtered[(filtered[col] >= lo) & (filtered[col] <= hi)]

st.sidebar.success(f"Filtered rows: {len(filtered):,} / {len(df):,}")
download_csv(filtered, "filtered.csv")

# ---------- Summary Stats ----------
st.subheader("📈 Summary statistics")
left, right = st.columns([2,3], gap="large")
with left:
    if num_cols:
        st.markdown("**Numeric (describe)**")
        st.dataframe(filtered[num_cols].describe().T, use_container_width=True)
    if cat_cols:
        st.markdown("**Categorical (top values)**")
        # Show top 10 for first 10 categorical columns
        tmp = []
        for c in cat_cols[:10]:
            vc = filtered[c].astype(str).value_counts().head(10).reset_index()
            vc.columns = [c, "count"]
            tmp.append(vc)
        if tmp:
            st.dataframe(pd.concat(tmp, axis=1), use_container_width=True)
with right:
    if len(num_cols) >= 2:
        corr = filtered[num_cols].corr(numeric_only=True)
        st.markdown("**Correlation matrix**")
        st.dataframe(corr, use_container_width=True)

        # Correlation heatmap with Altair
        corr_long = corr.reset_index().melt("index")
        corr_long.columns = ["x", "y", "corr"]
        heat = alt.Chart(corr_long).mark_rect().encode(
            x=alt.X("x:N", title=""),
            y=alt.Y("y:N", title=""),
            color=alt.Color("corr:Q", scale=alt.Scale(scheme="blueorange", domainMid=0)),
            tooltip=[alt.Tooltip("x:N"), alt.Tooltip("y:N"), alt.Tooltip("corr:Q", format=".2f")]
        ).properties(height=350)
        st.altair_chart(heat, use_container_width=True)

# ---------- Univariate Charts ----------
st.subheader("📊 Univariate charts")
col1, col2 = st.columns(2, gap="large")

with col1:
    if num_cols:
        num_col = st.selectbox("Choose a numeric column (histogram & boxplot)", options=num_cols, index=0)
        # Histogram
        hist = alt.Chart(filtered).mark_bar().encode(
            x=alt.X(f"{num_col}:Q", bin=alt.Bin(maxbins=30)),
            y=alt.Y("count()", title="Count"),
            tooltip=[alt.Tooltip("count()", title="Count")]
        ).properties(title=f"Histogram of {num_col}", height=300)
        st.altair_chart(hist, use_container_width=True)

        # Boxplot
        box = alt.Chart(filtered).mark_boxplot().encode(
            y=alt.Y(f"{num_col}:Q", title=num_col),
            tooltip=[alt.Tooltip(f"{num_col}:Q")]
        ).properties(title=f"Boxplot of {num_col}", height=300)
        st.altair_chart(box, use_container_width=True)

with col2:
    if cat_cols:
        cat_col = st.selectbox("Choose a categorical column (bar chart)", options=cat_cols, index=0)
        bar = alt.Chart(filtered).mark_bar().encode(
            x=alt.X(f"{cat_col}:N", sort="-y", title=cat_col),
            y=alt.Y("count()", title="Count"),
            tooltip=[alt.Tooltip(f"{cat_col}:N"), alt.Tooltip("count()", title="Count")]
        ).properties(title=f"Counts of {cat_col}", height=300).interactive()
        st.altair_chart(bar, use_container_width=True)

# ---------- Bivariate (Scatter) ----------
st.subheader("🟣 Bivariate: Scatter & trend")
if len(num_cols) >= 2:
    c1, c2, c3 = st.columns([2,2,2])
    x_col = c1.selectbox("X (numeric)", options=num_cols, index=0)
    y_col = c2.selectbox("Y (numeric)", options=[c for c in num_cols if c != x_col], index=0)
    color_by = c3.selectbox("Color by (categorical, optional)", options=["(none)"] + cat_cols, index=0)

    base = alt.Chart(filtered).mark_circle(opacity=0.7, size=60).encode(
        x=alt.X(f"{x_col}:Q", title=x_col),
        y=alt.Y(f"{y_col}:Q", title=y_col),
        tooltip=[alt.Tooltip(f"{x_col}:Q"), alt.Tooltip(f"{y_col}:Q")]
    )
    if color_by != "(none)":
        base = base.encode(color=alt.Color(f"{color_by}:N"))

    st.altair_chart(base.properties(height=420, title=f"{y_col} vs {x_col}"), use_container_width=True)

    add_reg = st.checkbox("Add linear regression trend", value=True)
    if add_reg:
        reg = alt.Chart(filtered).transform_regression(x_col, y_col).mark_line()
        st.altair_chart((base + reg).properties(height=420, title=f"{y_col} vs {x_col} (with trend)"), use_container_width=True)
else:
    st.info("Need at least two numeric columns for scatter plot.")

# ---------- Group-by analysis ----------
st.subheader("🧮 Group-by analysis")
if cat_cols and num_cols:
    g_col = st.selectbox("Group by (categorical)", options=cat_cols, index=0)
    m_col = st.selectbox("Metric (numeric)", options=num_cols, index=0)
    agg = st.selectbox("Aggregation", options=["mean", "median", "sum", "min", "max", "count"], index=0)

    grouped = filtered.groupby(g_col, dropna=False)[m_col].agg(agg).reset_index().sort_values(m_col, ascending=False)
    st.dataframe(grouped, use_container_width=True)

    gbar = alt.Chart(grouped).mark_bar().encode(
        x=alt.X(f"{g_col}:N", sort="-y", title=g_col),
        y=alt.Y(f"{m_col}:Q", title=f"{agg}({m_col})"),
        tooltip=[alt.Tooltip(f"{g_col}:N"), alt.Tooltip(f"{m_col}:Q", title=f"{agg}({m_col})")]
    ).properties(height=380, title=f"{agg.upper()} of {m_col} by {g_col}")
    st.altair_chart(gbar, use_container_width=True)
else:
    st.info("Need at least one categorical and one numeric column for group-by.")

st.caption("Made with ❤️ in Streamlit. Tip: Use the sidebar to slice your data, then download the filtered CSV.")
