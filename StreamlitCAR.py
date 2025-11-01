import streamlit as st
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import datetime 

# st.title("Interactive EDA - Car Dataset")
st.markdown(
    "<h2 style='color:olive;'>Interactive EDA - Car Dataset</h2>", 
    unsafe_allow_html=True)


col1,col2=st.columns(2)
with col1:
    st.image("https://tse3.mm.bing.net/th/id/OIP.gfIJla3BSR2sTKtBLLadtgHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3",width=400)
with col2:
    st.image("https://www.motortrend.com/uploads/2023/09/every-type-of-car-motortrend.jpg",width=400)



# st.subheader("Data Read")
st.markdown(
    "<h5 style='color:purple;'>Data Read</h5>", 
    unsafe_allow_html=True)
df=pd.read_csv(r"C:\Users\kulde\Desktop\STREMLIT\CARDATASET.csv")
df


# st.subheader("shape of data")
st.markdown(
    "<h5 style='color:purple;'>shape of data</h5>", 
    unsafe_allow_html=True)
df.shape


# st.subheader("describe of data")
st.markdown(
    "<h5 style='color:purple;'>describe of data</h5>", 
    unsafe_allow_html=True)
st.write(df.describe())


# st.subheader("Column Names")
st.markdown(
    "<h5 style='color:purple;'>Column Names</h5>", 
    unsafe_allow_html=True)
st.selectbox("Total column name",df.columns.tolist())


# st.subheader("Null value in each column")
st.markdown(
    "<h5 style='color:purple;'>Null value in each column</h5>", 
    unsafe_allow_html=True)
st.write(df.isnull().sum())


# st.subheader("Data Type of column")
st.markdown(
    "<h5 style='color:purple;'>Data Type of column</h5>", 
    unsafe_allow_html=True)
st.write(df.dtypes)


# st.subheader("See First Five Rows Using Head() Function")
st.markdown(
    "<h5 style='color:purple;'>See First Five Rows Using Head() Function</h5>", 
    unsafe_allow_html=True)
st.write(df.head())


# st.subheader("See Last Five Rows Using Tail() Function")
st.markdown(
    "<h5 style='color:purple;'>See Last Five Rows Using Tail() Function</h5>", 
    unsafe_allow_html=True)
st.write(df.tail())


st.markdown(
    "<h5 style='color:purple;'>Add a New Column - Age</h5>", 
    unsafe_allow_html=True)
df["Age"]=2025-df["year"]
df.drop("year",axis=1,inplace=True)
df


st.markdown(
    "<h5 style='color:purple;'>Call Describe Function Again</h5>", 
    unsafe_allow_html=True)
st.write(df.describe())



st.markdown(
    "<h5 style='color:purple;'>Count Plot of Fuel, Seller_type, Transmission, Owner</h5>", 
    unsafe_allow_html=True)
graph=["fuel","seller_type","transmission","owner"]
i=0
while i<4:
    fig=plt.figure(figsize=[20,5])

    plt.subplot(1,2,1)
    sns.countplot(x=graph[i],hue=graph[i],data=df)
    i+=1

    plt.subplot(1,2,2)
    sns.countplot(x=graph[i],hue=graph[i],data=df)
    i+=1

    st.pyplot(fig)



st.markdown(
    "<h5 style='color:purple;'>Boxplot of Fuel, Seller_type, Transmission, Owner</h5>", 
    unsafe_allow_html=True)
graph1=["selling_price","km_driven","Age","selling_price"]
i=0
while i<4:
    fig=plt.figure(figsize=[12,3])

    plt.subplot(1,2,1)
    sns.boxplot(x=graph1[i],data=df)
    i+=1

    plt.subplot(1,2,2)
    sns.boxplot(x=graph1[i],data=df)
    i+=1
    st.pyplot(fig)


st.markdown(
    "<h5 style='color:purple;'>99th Percentile of Selling Price</h5>", 
    unsafe_allow_html=True)
Sq99 = df["selling_price"].quantile(0.99)
st.write("99th Quantile Value:", Sq99)



st.markdown(
    "<h5 style='color:purple;'>Data After Remove Outlier of Selling Price</h5>", 
    unsafe_allow_html=True)
remove_outlier_of_selling_price = df[df["selling_price"] > df["selling_price"].quantile(0.99)].sort_values(by="selling_price", ascending=False)
remove_outlier_of_selling_price

st.markdown(
    "<h5 style='color:purple;'>Boxplot After Remove Outlier of Selling Price</h5>", 
    unsafe_allow_html=True)
fig,ax=plt.subplots()
sns.boxplot(x=remove_outlier_of_selling_price["selling_price"],color="red",ax=ax)  
st.pyplot(fig)



st.markdown(
    "<h5 style='color:purple;'>99th Percentile of km_driven</h5>", 
    unsafe_allow_html=True)
kq99=df["km_driven"].quantile(0.99)
st.write("99th Quantile Value:",kq99)


st.markdown(
    "<h5 style='color:purple;'>Data After Remove Outlier of km_driven</h5>", 
    unsafe_allow_html=True)
remove_outlier_of_km_driven = df[df["km_driven"]>df["km_driven"].quantile(0.99)].sort_values(by="km_driven",ascending=False)
remove_outlier_of_km_driven



st.markdown(
    "<h5 style='color:purple;'>Boxplot After Remove Outlier of km_driven</h5>", 
    unsafe_allow_html=True)
fig,ax=plt.subplots()
sns.boxplot(x=remove_outlier_of_selling_price["km_driven"],color="yellow",ax=ax)
st.pyplot(fig)



st.markdown(
    "<h5 style='color:purple;'>Bar Plot of Top 10 Most Frequent Names</h5>", 
    unsafe_allow_html=True)
top_10names = df["name"].value_counts().sort_values(ascending=False).head(10)
top_df = top_10names.reset_index()
top_df.columns = ["name", "count"]
fig = px.bar(top_df, x="name", y="count",color_discrete_sequence=["orange"])
st.plotly_chart(fig)





st.markdown(
    "<h5 style='color:purple;'> Bar Plot (Groupby the km_driven and Seller_type Using Mean() Function)</h5>", 
    unsafe_allow_html=True)
grp = df.groupby("seller_type")
mean = grp.km_driven.mean().sort_values(ascending=False)
mean_df = mean.reset_index()
mean_df.columns = ["seller_type","km_driven"]
fig=px.bar(mean_df,x="seller_type",y="km_driven",color_discrete_sequence=["pink"])
st.plotly_chart(fig)



st.markdown(
    "<h5 style='color:purple;'> Bar Plot (Groupby the km_driven and Seller_type Using Sum() Function)</h5>", 
    unsafe_allow_html=True)
grp = df.groupby("seller_type")
sum = grp.km_driven.sum().sort_values(ascending=False)
sum_df = sum.reset_index()
sum_df.columns = ["seller_type","km_driven"]
fig=px.bar(sum_df,x="seller_type",y="km_driven",color_discrete_sequence=["red"])
st.plotly_chart(fig)



st.markdown(
    "<h5 style='color:purple;'> Bar Plot (Groupby the km_driven and Seller_type Using Std() Function)</h5>", 
    unsafe_allow_html=True)
grp = df.groupby("seller_type")
std = grp.km_driven.std().sort_values(ascending=False)
std_df = std.reset_index()
std_df.columns = ["seller_type","km_driven"]
fig=px.bar(std_df,x="seller_type",y="km_driven",color_discrete_sequence=["purple"])
st.plotly_chart(fig)



col3, col4 = st.columns(2)
with col3:
    st.markdown(
        "<h5 style='color:purple;'>Pie Chart of Transmission Column</h5>", 
        unsafe_allow_html=True
    )
    fig = px.pie(df, names="transmission", width=300, height=300)
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.markdown(
        "<h5 style='color:purple;'>Pie Chart of Fuel Column</h5>", 
        unsafe_allow_html=True
    )
    fig = px.pie(df, names="fuel", width=300, height=300)
    st.plotly_chart(fig, use_container_width=True)


st.markdown(
    "<h5 style='color:purple;'>Area Chart Between Name & Year</h5>", 
    unsafe_allow_html=True)
fig=px.area(df,x="owner",y="selling_price")
st.plotly_chart(fig)

st.markdown(
    "<h5 style='color:purple;'>violin Plot Between fuel & Age</h5>", 
    unsafe_allow_html=True)
fig=px.violin(df,x="fuel",y="Age")
st.plotly_chart(fig)




st.markdown(
    """
    <style>
    div.stButton {text-align:center;}
    div.stButton > button:first-child {
        width: 600px;
        height: 20px;
        font-size: 20px;
        border-radius: 10px;
        background-color: purple;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

button = st.button("THANK YOU")
if button:
    st.balloons()
    st.snow()

