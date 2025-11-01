import streamlit as st

# st.header("MY PROJECT")
# st.title("MY PROJECT")
# st.subheader("MY PROJECT")
# st.text("MY PROJECT")
# st.write("MY PROJECT")
# st.write(["st", "is <", 3])
# st.write_stream(my_generator)
# st.write_stream(my_llm_stream)
# st.text("Fixed width text")
# st.write(["kuldeep","prince","sandeep","raju"])

# st.markdown("_Markdown_")
# st.markdown("_kuldeep_")

# st.latex(r""" e^{i\pi} + 1 = 0 """)
# st.latex("""2^{3,4}+12=23""")
# st.latex("""2^{3^{2+3}}+12=23""")

# st.code("for i in range(8): foo()")

# st.badge("New")

# st.html("<p>Hi!</p>")
# st.html("<h1>kuldeep</h1>")

# st.image(r"C:\Users\kulde\Desktop\STREMLIT\DSC_0904.JPG")

# st.dataframe(my_dataframe)
# st.table(data.iloc[0:10])

# st.json({"foo":"bar","fu":"ba"})
# st.json({"1":"kuldeep","2":"sandeep","3":"prince"})

# st.metric("My metric", 42, 2)
# st.metric("kuldeep",23,24)

# st.button("Click me")

# st.download_button("Download file", data)

# st.link_button("Go to gallery", r"C:\Users\kulde\Pictures\Screenshots")

# st.page_link("app.py", label="Home")
# st.data_editor("Edit data", data)

# st.checkbox("I agree")
# st.feedback("stars")
# st.feedback("faces")
# st.feedback("thumbs")

# st.pills("Tags", ["Sports", "Politics"])
# st.pills("Language",["python","c","c++","R"])

# st.segmented_control("Filter", ["Open", "Closed"])
# st.segmented_control("language",["c","c++","python"])

# st.radio("Pick one", ["cats", "dogs","cow","buffalo","peaghon","hourse"])

# st.toggle("Enable")

# st.selectbox("Pick one", ["cats", "dogs","cow","buffalo","peaghon","hourse"])

# st.multiselect("Buy", ["milk", "apples", "potatoes","banana","bread","curd","lassi","eggs"])

# st.slider("Pick a number", 0, 100)

# st.select_slider("Pick a size", ["S", "M", "L"])
# st.select_slider("Pick a size", ["0","5","10"])

# st.text_input("First name")
# st.number_input("Pick a number", 0, 10)
# st.date_input("Your birthday")
# st.time_input("Meeting time")
# st.audio_input("Record a voice message")
# st.camera_input("Take a picture")
# st.chat_input("Take your chat")


# st.text_area("Text to translate")

# st.file_uploader("Upload a CSV")

# st.color_picker("Pick a color")

# select=st.selectbox("choose any one:",["1","2","3","4","5"])
# st.write(f"your choise is {select}, Good")

# st.success("you are good")

# st.selectbox("SELECT YOUR FAVERATE LANGUAGE:",["PYTHON","C","C++","JAVA","RUBY"])

button=st.button("submit")
if(button):
    st.write("congratualization you are selected")
    
select=st.selectbox("select",["one","two","three","four","five"])
st.write(f"your selection is {select}")

size=st.selectbox("select your T-shirt size",["S","M","L","XL"])
if (size=="S"):
    st.write("your age is between(10 to 18)")
elif (size=="M"):
    st.write("your age is between(18 to 29)")
elif (size=="L"):
    st.write("your age is between(30 to 39)")
else :
    st.write("your choice is between (39 to 50)")


age=st.text_input("Enter your age")
if age:
    age=int(age)
    if (age>=1 and age<=18):
        st.write("you are kid")
    elif (age>=19 and age<=50):
        st.write("you are adult")
    else:
        st.write("you are old")
  

import streamlit as st
from datetime import date

st.title("Age Calculator 🎂")

# Input: Date of Birth
dob = st.date_input("Enter your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

if dob:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    st.success(f"Your age is: {age} years")






















# import streamlit as st
# import pandas as pd
# df = pd.DataFrame({"values": [10, 20, 30, 40],
#                    "price":[8,18,28,38]})
# st.bar_chart(df)


# df = pd.DataFrame({
#     "Item": ["A", "B", "C", "D"], 
#     "values": [10, 20, 30, 40],
#     "price": [8, 18, 28, 38]}).
# st.bar_chart(df.set_index("Item")) 



# import altair as alt
# chart = alt.Chart(pd.DataFrame({
#                                "Item": ["A", "B", "C", "D"], 
#                                "values": [10, 20, 30, 40],
#                                "price": [8, 18, 28, 38]
#                                })).mark_bar().encode(
# x="Item",
# y="values",
# color=alt.value("steelblue")
# )
# st.altair_chart(chart, use_container_width=True)




# import streamlit as st
# import pandas as pd
# import altair as alt
# # Your Data
# df = pd.DataFrame({
#     "Item": ["A", "B", "C", "D"],
#     "values": [10, 20, 30, 40],
#     "price": [8, 18, 28, 38]
# })
# # Create Altair Chart
# chart = alt.Chart(df).mark_bar().encode(
#     x="Item",
#     y="values",
#     tooltip=["Item", "values", "price"],
#     color=alt.value("magenta")
# )
# # Show in Streamlit
# st.altair_chart(chart, use_container_width=True)



# st.area_chart
# st.line_chart
# st.bokeh_chart
# st.altair_chart
# st.plotly_chart
# st.pydeck_chart
# st.scatter_chart
# st.graphviz_chart
# st.vega_lite_chart


# import pandas as pd
# import numpy as np
# df=pd.DataFrame({"x":range(1,11),
#               "y":np.random.randint(10,50,10),
#               "z":np.random.randint(20,60,10)})
# st.write("sample data",df)
# st.line_chart(df[["x","y"]].set_index("x"))

# st.area_chart(df[["x","y"]].set_index("x"))

# st.scatter_chart(df,x="x",y="y")



# df=pd.read_csv(r"C:\Users\kulde\Desktop\STREMLIT\CARDATASET.csv")
# st.dataframe(df)
# st.line_chart(df[["name","selling_price"]])






































































# st.divider("")

# st.empty
# st.echo
# st.error
# st.exceptiost
# st.expander

# st.feedback
# st.file_uploader
# st.form
# st.form_submit_button
# st.fragment
# st.__file__

# st.link_button
# st.login
# st.logo
# st.__loader__

# st.map
# st.chat_message

# st.navigation
# st.__name__

# st.get_option
# st.set_option

# st.pdf
# st.pills
# st.popover
# st.progress

# st.rerun

# st.secrets
# st.segmented_control
# st.session_state
# st.snow
# st.spinner
# st.status

# st.table
# st.tabs
# st.toast
# st.toggle

# st.video
# st.__version__
# st.vega_lite_chart

# st.warning


