import streamlit as st
import plotly.express as px
import pandas as pd

# Example dataset
df = pd.DataFrame({
    "name": ["A", "B", "C", "D", "E", "F"],
    "value": [10, 20, 30, 40, 50, 60],
    "category": ["X", "Y", "X", "Y", "X", "Y"]
})

# 1. Pie Chart
fig = px.pie(df, names="category", values="value", title="Pie Chart Example")
st.plotly_chart(fig, use_container_width=True)

# 2. Bar Chart
fig = px.bar(df, x="name", y="value", color="category", title="Bar Chart Example")
st.plotly_chart(fig, use_container_width=True)

# 3. Line Chart
fig = px.line(df, x="name", y="value",color="category", title="Line Chart Example", markers=True)
st.plotly_chart(fig, use_container_width=True)

# 4. Area Chart
fig = px.area(df, x="name", y="value", color="category", title="Area Chart Example")
st.plotly_chart(fig, use_container_width=True)

# 5. Scatter Plot
fig = px.scatter(df, x="name", y="value", color="category", size="value", title="Scatter Plot Example")
st.plotly_chart(fig, use_container_width=True)

# 6. Histogram
fig = px.histogram(df, x="value", color="category", nbins=5, title="Histogram Example")
st.plotly_chart(fig, use_container_width=True)

# 7. Box Plot
fig = px.box(df, x="category", y="value", color="category", title="Box Plot Example")
st.plotly_chart(fig, use_container_width=True)

# 8. Violin Plot
fig = px.violin(df, x="category", y="value", box=True, points="all", title="Violin Plot Example")
st.plotly_chart(fig, use_container_width=True)

# 9. Density Heatmap
fig = px.density_heatmap(df, x="name", y="value", title="Density Heatmap Example")
st.plotly_chart(fig, use_container_width=True)

# 10. Scatter Matrix (similar to seaborn pairplot)
fig = px.scatter_matrix(df, dimensions=["value"], color="category", title="Scatter Matrix Example")
st.plotly_chart(fig, use_container_width=True)

# 11. Treemap
fig = px.treemap(df, path=["category", "name"], values="value", title="Treemap Example")
st.plotly_chart(fig, use_container_width=True)

# 12. Sunburst
fig = px.sunburst(df, path=["category", "name"], values="value", title="Sunburst Example")
st.plotly_chart(fig, use_container_width=True)




# ✅ Charts that need x & y:

# (because they plot relationships between two variables)

# Bar Chart → px.bar(df, x="col1", y="col2")

# Line Chart → px.line(df, x="date", y="sales")

# Area Chart → px.area(df, x="date", y="sales")

# Scatter Plot → px.scatter(df, x="height", y="weight")

# Box Plot → px.box(df, x="category", y="value")

# Violin Plot → px.violin(df, x="category", y="value")

# Density Heatmap → px.density_heatmap(df, x="x_col", y="y_col")



# ✅ Charts that don’t always need x & y:

# (you just give one column, or names + values)

# Pie Chart → px.pie(df, names="category", values="value")

# Histogram → px.histogram(df, x="value") (y is auto-calculated = counts)

# Scatter Matrix → px.scatter_matrix(df, dimensions=[...])

# Treemap → px.treemap(df, path=["category", "subcat"], values="value")

# Sunburst → px.sunburst(df, path=["category", "subcat"], values="value")



import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Example Data
df = sns.load_dataset("tips")  # restaurant tips dataset
df

# 1. Scatter Plot (x,y,hue)
fig, ax = plt.subplots()
sns.scatterplot(data=df, x="total_bill", y="tip", hue="sex", ax=ax)
st.pyplot(fig)

# 2. Line Plot (x,y,hue)
fig, ax = plt.subplots()
sns.lineplot(data=df, x="total_bill", y="tip", hue="sex", ax=ax)
st.pyplot(fig)

# 3. Bar Plot (x,y,hue)
fig, ax = plt.subplots()
sns.barplot(data=df, x="sex", y="tip", hue="smoker", ax=ax)
st.pyplot(fig)

# 4. Count Plot (only x, hue optional)
fig, ax = plt.subplots()
sns.countplot(data=df, x="day", hue="sex", ax=ax)
st.pyplot(fig)

# 5. Histogram (only x)
fig, ax = plt.subplots()
sns.histplot(data=df, x="total_bill", bins=20, kde=True, ax=ax)
st.pyplot(fig)

# 6. KDE Plot (only x or both x,y)
fig, ax = plt.subplots()
sns.kdeplot(data=df, x="total_bill", fill=True, ax=ax)
st.pyplot(fig)

# 7. Box Plot (x,y,hue)
fig, ax = plt.subplots()
sns.boxplot(data=df, x="day", y="total_bill", hue="sex", ax=ax)
st.pyplot(fig)

# 8. Violin Plot (x,y,hue)
fig, ax = plt.subplots()
sns.violinplot(data=df, x="day", y="total_bill", hue="sex", split=True, ax=ax)
st.pyplot(fig)

# 9. Strip Plot (x,y,hue)
fig, ax = plt.subplots()
sns.stripplot(data=df, x="day", y="total_bill", hue="sex", ax=ax)
st.pyplot(fig)

# 10. Swarm Plot (x,y,hue)
fig, ax = plt.subplots()
sns.swarmplot(data=df, x="day", y="total_bill", hue="sex", ax=ax)
st.pyplot(fig)

# 11. Heatmap (matrix data, no x,y)
fig, ax = plt.subplots()
corr = df.corr(numeric_only=True)
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# 12. Pairplot (no x,y needed, just dataset)
pairplot = sns.pairplot(df, hue="sex")
st.pyplot(pairplot.figure)

# 13. Jointplot (x,y,hue optional)
joint = sns.jointplot(data=df, x="total_bill", y="tip", kind="reg", hue="sex")
st.pyplot(joint.figure)






import streamlit as st
import plotly.express as px
import pandas as pd

# Example Data
df = px.data.tips()   # restaurant tips dataset

# 1. Scatter Plot (needs x,y; color optional)
fig = px.scatter(df, x="total_bill", y="tip", color="sex", title="Scatter Plot")
st.plotly_chart(fig, use_container_width=True)

# 2. Line Plot (needs x,y; color optional)
fig = px.line(df, x="total_bill", y="tip", color="sex", title="Line Plot")
st.plotly_chart(fig, use_container_width=True)

# 3. Bar Plot (needs x,y; color optional)
fig = px.bar(df, x="day", y="total_bill", color="sex", title="Bar Plot")
st.plotly_chart(fig, use_container_width=True)

# 4. Area Plot (needs x,y; color optional)
fig = px.area(df, x="day", y="total_bill", color="sex", title="Area Plot")
st.plotly_chart(fig, use_container_width=True)

# 5. Histogram (needs only x; color optional)
fig = px.histogram(df, x="total_bill", color="sex", nbins=20, title="Histogram")
st.plotly_chart(fig, use_container_width=True)

# 6. Box Plot (needs x,y; color optional)
fig = px.box(df, x="day", y="total_bill", color="sex", title="Box Plot")
st.plotly_chart(fig, use_container_width=True)

# 7. Violin Plot (needs x,y; color optional)
fig = px.violin(df, x="day", y="total_bill", color="sex", box=True, points="all", title="Violin Plot")
st.plotly_chart(fig, use_container_width=True)

# 8. Pie Chart (needs names, values)
fig = px.pie(df, names="day", values="total_bill", title="Pie Chart")
st.plotly_chart(fig, use_container_width=True)

# 9. Donut Chart (same as pie, with hole)
fig = px.pie(df, names="day", values="total_bill", hole=0.4, title="Donut Chart")
st.plotly_chart(fig, use_container_width=True)

# 10. Sunburst Chart (needs path + values)
fig = px.sunburst(df, path=["sex", "day"], values="total_bill", title="Sunburst Chart")
st.plotly_chart(fig, use_container_width=True)

# 11. Treemap (needs path + values)
fig = px.treemap(df, path=["sex", "day"], values="total_bill", title="Treemap")
st.plotly_chart(fig, use_container_width=True)

# 12. Density Heatmap (needs x,y)
fig = px.density_heatmap(df, x="total_bill", y="tip", title="Density Heatmap")
st.plotly_chart(fig, use_container_width=True)

# 13. Scatter Matrix (like pairplot; needs dimensions)
fig = px.scatter_matrix(df, dimensions=["total_bill", "tip", "size"], color="sex", title="Scatter Matrix")
st.plotly_chart(fig, use_container_width=True)

# 14. Funnel Chart (needs x,y)
fig = px.funnel(df, x="day", y="total_bill", title="Funnel Chart")
st.plotly_chart(fig, use_container_width=True)

# 15. Timeline / Time Series (needs date as x, y values)
df_time = px.data.stocks()   # built-in stock dataset
fig = px.line(df_time, x="date", y="GOOG", title="Time Series")
st.plotly_chart(fig, use_container_width=True)

# 16. Polar / Radar Chart (needs r, theta)
fig = px.line_polar(df, r="total_bill", theta="day", color="sex", line_close=True, title="Polar Chart")
st.plotly_chart(fig, use_container_width=True)


