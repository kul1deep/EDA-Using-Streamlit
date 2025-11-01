# import streamlit as st
# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# st.write("Hello Kuldeep1234")
# st.write({"key":"value","firstname":"kuldeep","lastname":"nathchouhan"})
# button=st.button(label="submit")
# print(button)


# st.title("kuldeep")
# st.header("kuldeep")
# st.subheader("kuldeep")
# st.markdown("_kuldeep_")
# st.caption("kuldeep")
# code_example="""
# def greet (name):
#     print("hello",name)
# """
# st.code(code_example,language="python")
# st.divider()
# st.image("https://thfvnext.bing.com/th/id/OIP.lcMq-dcUyZdIH45PpeH_4wHaE8?w=238&h=180&c=7&r=0&o=5&cb=thfvnext&dpr=1.3&pid=1.7",width=300)

# st.subheader("data")
# df=pd.DataFrame({"Name":["kuldeep","sandeep","prince"],"Age":[22,25,23],"occuption":["engineer","doctor","artist"]})
# st.dataframe(df)

# st.subheader("data editor")
# edit=st.data_editor(df)
# print(edit)

# st.subheader("static table")
# st.table(df)


# st.subheader("metrix")
# st.metric(label="totle rows",value=len(df))
# st.metric(label="avg age",value=round(df["Age"].mean(),1))


# st.subheader("json and dict.")
# dict={"name":["kuldeep","kapli","karan","kavish","kalu"],"age":[12,13,14,15],"skills":["python","sql","ml"]}
# st.json(dict)


# graphdata=pd.DataFrame(np.random.randint(1,20,size=(20,3)),columns=["a","b","c"])
# graphdata=pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
# graphdata=pd.DataFrame(np.random.rand(20,3),columns=["a","b","c"])
# graphdata=pd.DataFrame(np.random.random((20,3)),columns=["a","b","c"])
# graphdata
# st.subheader("Area chart")
# st.area_chart(graphdata)

# st.subheader("Bar chart")
# st.bar_chart(graphdata)

# st.subheader("line chart")
# st.line_chart(graphdata)

# st.subheader("scatter chart")
# st.scatter_chart(graphdata)

# stdata=pd.DataFrame({"x":np.round(np.random.rand(200),1),"y":np.round(np.random.rand(200),2)})
# stdata

# data=pd.DataFrame(np.round(np.random.rand(20,3),1),columns=["a","b","c"])
# data=pd.DataFrame(np.random.randint(1,20,size=[20,3]),columns=["a","b","c"])
# data





# st.title("Streamlit Form Demo")
# with st.form(key="sample_form"):
#     st.subheader("user information")
#     name=st.text_input("Enter your name")
#     area=st.text_area("Enter youe message")
#     date=st.date_input("Enter date")
#     time=st.time_input("Enter time")
#     select=st.selectbox("select any one",["Male","Female","Other"])
#     mtselect=st.multiselect("select any one",["male","Female","Other"])
#     choice=st.radio("select any one",["male","female","other"])
#     slider=st.select_slider("use slider",[1,2,3,4,5])
#     checkbox=st.checkbox("sandeep")
#     check1=st.checkbox("kuldeep")
#     button=st.form_submit_button("submit")
#     if button:
#         st.write("your form is successfully submitted")



# import streamlit as st
# import time
# from datetime import datetime

# min_date=datetime(1990,1,1)
# max_date=datetime.now()

# with st.form(key="sample form"):
#     name = st.text_input("Enter your name")
#     date = st.date_input("Enter date", value=None,max_value=max_date,min_value=min_date)
#     select = st.selectbox("Select any one", ["Male", "Female", "Other"], index=None, placeholder="Choose...")
#     choice = st.radio("Select any one", ["male", "female", "other"], index=None)
#     slider=st.select_slider("select value",[0,1,2,3,4,5,6])
#     button = st.form_submit_button("Submit")

#     if button:
#         if not (name and date and select and choice):
#             st.warning("Please fill all info.")
#         else:
#             st.balloons()
#             st.snow()
#             # st.toast("🎉 Data submitted successfully!", icon="✅")
#             # st.success("Successfully submitted!")
#             with st.spinner("Please wait..."):
#                 time.sleep(3)
#                 st.success("Done!")


# import time
# from datetime import datetime

# min_date=datetime(1990,1,1)
# max_date=datetime.now()

# st.subheader("Sample Form")
# with st.form("User Info."):
#     name=st.text_input("Enter Your Name")
#     email=st.text_input("Enter Your Email",placeholder="Enter Your Email")
#     DOB=st.date_input("Enter Your DOB",min_value=min_date,max_value=max_date,value=None)
#     select=st.selectbox("Select Your Fav. Fruit",["Mango","banana","Orange","Grapes","WaterMelon"],index=None,placeholder="Choose......")
#     radio=st.radio("Select Your Gender",["Male","Female","other"],index=None)
#     slider=st.select_slider("Select Your T-Shirt Size",["S","M","L","XL"])
#     button=st.form_submit_button("button")

#     if button:
#         if not(name and email and DOB and select and radio):
#             st.warning("Please Fill All Information")
#         else:
#             st.balloons()
#             st.snow()
#             with st.spinner("Please Wait"):
#                 time.sleep(3)
#                 st.success("Done!")
                


# from datetime import datetime 

# min_date=datetime(1990,1,1)
# max_date=datetime.now()

# with st.form(key="user information"):
#     name=st.text_input("Enter your name")
#     birthdate=st.date_input("Enter your DOB",min_value=min_date,max_value=max_date)
#     if birthdate:
#         age=max_date.year-birthdate.year
#         if birthdate.month > max_date.month or (birthdate.month == max_date.month and birthdate.day > max_date.day):
#             age -= 1
#         # st.write(f"your calculated age is {age} years")
    
#     button=st.form_submit_button("Submit")
#     if button:
#         if not name or not birthdate:
#             st.warning("Please fill in all form input")
#         else:
#             st.success(f"Thank You {name}. Your Age is {age} Year.")
#             st.balloons() 
#             st.snow()   



# COUNTER
# counter=0
# st.write(f"counter value:{counter}")
# button=st.button("increment counter")
# if button:
#     counter+=1
#     st.write(f"counter increment to {counter}")
# else:
#     st.write(f"counter stays at {counter}")


# if "counter" not in st.session_state:
#     st.session_state.counter=0
# button=st.button("increment counter")
# if button:
#     st.session_state.counter+=1
#     st.write(f"counter incremented to {st.session_state.counter}")
# button1=st.button("Reset")
# if button1:
#     st.session_state.counter=0
# else:
#     st.write(f"counter did not reset")
#     st.write(f"counter value:{st.session_state.counter}")


# if "step" not in st.session_state:
#     st.session_state.step=1
# if "info" not in st.session_state:
#     st.session_state.info={}
# if st.session_state.step==1:
#     st.header("part1:info")
#     name=st.text_input("name",value=st.session_state.info.get("name",""))
#     if st.button("next"):
#         st.session_state.info["name"]=name
#         st.session_state.step=2
# elif st.session_state.step==2:
#     st.header("part2:review")
#     st.subheader("please review this:")
#     st.write(f"**Name**:{st.session_state.info.get("name","")}")

#     if st.button("submit"):
#         st.success("great")
#         st.balloons()
#         st.session_state.info={}
#     if st.button("Back"):
#         st.session_state.step=1



# slider=st.slider("this is slider",0,50,25)
# st.slider("this is 2nd slider",slider,100)


import streamlit as st
import pandas as pd
import datetime
import plotly.express as px
from PIL import Image 
import plotly.graph_objects as go

df=pd.read_excel(r"C:\Users\kulde\Downloads\Adidas.xlsx")
st.set_page_config(layout="wide")
st.markdown("<style>div.block-container{padding-top:1rem:}</style>",unsafe_allow_html=True)
image=Image.open("adidas.png")

col1,col2=st.columns([0.1,0.9])
with col1:
    st.image(image,width=100)

html_title = """
<style>
  h1.title-test {
    color:purple;
    font-weight: bold;
    padding: 5px;
    border-radius: 6px;
    text-align: center;
  }
</style>

<h1 class="title-test">Adidas Interactive Sales Dashboard</h1>
"""
with col2:
    st.markdown(html_title, unsafe_allow_html=True)



col3,col4,col5=st.columns([0.2,0.45,0.45])
with col3:
    box_date=str(datetime.datetime.now().strftime("%d %B %Y"))
    st.write(f"Last update by:  \n{box_date}")

with col4:
    fig=px.bar(df,x="Retailer",y="TotalSales",
           title="Total Sales by Retailer",hover_data=["TotalSales"],
           height=500)
    st.plotly_chart(fig,use_container_width=True)

_,view1,dwn1,view2,dwn2=st.columns([0.15,0.20,0.20,0.20,0.20])
with view1:
    expander=st.expander("Retailer wise Sales")
    data=df[["Retailer","TotalSales"]].groupby(by="Retailer")["TotalSales"].sum()
    expander.write(data)

with dwn1:
    st.download_button("Get Date",data=data.to_csv().encode("utf-8"),
                       file_name="RetailerSales.csv",mime="text/csv")

df["Month_Year"]=df["InvoiceDate"].dt.strftime("%b'%y")
result=df.groupby(by=df["Month_Year"])["TotalSales"].sum().reset_index()

with col5:
    fig1=px.line(result,x="Month_Year",y="TotalSales",title="Total Sales Over Time",
                 template="gridon")
    st.plotly_chart(fig1,use_container_width=True)

with view2:
    expander=st.expander("Monthly Sales")
    data=result
    expander.write(data)

with dwn2:
    st.download_button("Get Data",data=result.to_csv().encode("utf-8"),
                       file_name="Monthly Sales.csv",mime="text/csv")
st.divider()


result1=df.groupby(by="State")[["TotalSales","UnitsSold"]].sum().reset_index()

fig3=go.Figure()
fig3.add_trace(go.Bar(x=result1["State"],y=result1["TotalSales"],name="Total Sales"))
fig3.add_trace(go.Scatter(x=result1["State"],y=result1["UnitsSold"],mode="lines",
                          name="Units Sold",yaxis="y2"))
fig3.update_layout(
    title="Total Sales and Units Sold by State",
    xaxis=dict(title="State"),
    yaxis=dict(title="Total Sales",showgrid=False),
    yaxis2=dict(title="Units Sold",overlaying="y",side="right"),
    template="gridon",
    legend=dict(x=1,y=1.5)
)

_,col6=st.columns([0.1,1])
with col6:
    st.plotly_chart(fig3,use_container_width=True)


_,view3,dwn3=st.columns([0.5,0.45,0.45])
with view3:
    expander=st.expander("View Data for Sales by Units Sold")
    expander.write(result1)

with dwn3:
    st.download_button("Get Data",data=result1.to_csv().encode("utf-8"),
                       file_name="Sales_by_UnitsSold.csv",mime="text/csv")
st.divider()


_,col7=st.columns([0.1,1])
treemap=df[["Region","City","TotalSales"]].groupby(by=["Region","City"])["TotalSales"].sum().reset_index()

fig4=px.treemap(treemap,path=["Region","City"],values="TotalSales",
                hover_data=["TotalSales"],
                color="City",height=700,width=600)
fig4.update_traces(textinfo="label+value")

with col7:
    st.subheader(":point_right: Total Sales by Region and City in Treemap")
    st.plotly_chart(fig4,use_container_width=True)