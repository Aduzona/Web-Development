import streamlit as st

# TEXT
#title
st.title("Streamlit Crash Course")

#header/suheader
st.header("This is a header")
st.subheader("This is a subheader")

#text
st.text("This is so cool")

#Markdown
st.markdown("# This os markdown")

# Links
st.markdown("[Google](https://google.com)")

url_link="https://jcharistech.com"

st.markdown(url_link)

# Custom Color/Style
# html_page = """
# <div style="background-color:tomato; padding:10px">
#     <p style="font-size:50px">Streamlit is Awesome</p>
# </div>
# """
# st.markdown(html_page,unsafe_allow_html=True)

# html_form = """
# <div>
#     <form>
#         <input type="text" name="firstname"/>
#     </form>
# </div>

# """
# st.markdown(html_form,unsafe_allow_html=True)

# Bootstrap Alert/Color Text
st.success("Success!")
st.info("Information")
st.warning("This is a warning")
st.error("This is an error")

st.exception('NamError()')

# MEDIA
#Images
from PIL import Image
img=Image.open('puppy.jpg')
st.image(img,width=300,caption='puppy in the field')

# #Audio
# audio_file =open('example.mp3','rb')#rb read, write
# audio_bytes=audio_file.read()
# st.audio(audio_bytes, format="audio/mp3")

# #Video
# video_file=open("example.mp4",'rb')
# video_bytes=video_file.read()
# st.video(video_bytes)

#Video URL/YTB
st.video("https://www.youtube.com/watch?v=dYHwERU0ZBQ&ab_channel=ONIFHOTNEWS")

#WIDGET
st.button("Submit")

if st.button("Play"):
    st.text("Hello world")

# Checkbox
if st.checkbox("Show/hide"):
    st.success("Hiding or Showing")

# Radio
gender = st.radio("Your Gender",["Male","Female"])

if gender == 'Male':
    st.info("Is a male")

# Select
location = st.selectbox("Your Location",["UK","USA","India","Nigeria"])

# Multiselect
occupation= st.multiselect("Your Occupation",["Developer","Doctor","Businessman","Banker"])

# TEXT INPUT
name = st.text_input("Your Name","Type Here")
st.text(name)

# Number INPUT
age =st.number_input("Age")

# Slider
level = st.slider("Your Level",2,6,5)

# # Balloons
# st.balloons()

# Data Science
st.write(range(10))

#DATAFRAME

import pandas as pd
df = pd.read_csv("./datasets/diabetes.csv")

#Method1
st.dataframe(df.head())

#Method2
st.write(df.head())

#Tables
# Table is static while dataframe is movable
st.table(df.head())
# PLOT

#Plot Pkgs
import matplotlib.pyplot as plt
import seaborn as sns

# Area chart
st.area_chart(df.head(20))
# Bar chart
st.bar_chart(df.head(20))

# Line Chart
st.line_chart(df)

#Heatmap
c_plot= sns.heatmap(df.corr(),annot=True)
st.write(c_plot)
st.pyplot()

#Altair
#Vega

#Date/Time
import datetime

today = st.date_input("Today is",datetime.datetime.now())

import time
the_time =st.time_input("The time is",datetime.time(10,0))

# Display JSON CODE
data = {"name":"John","salary":50000}
st.json(data)

# Disploy code
st.code("import numpy as np")
st.code("import numpy as np",language='python')

julia_code="""
function doit(num::int)
    pritnln(num)
end

"""
st.code(julia_code,language='julia')

# with st.echo():
#     # This is a comment
#     import textblob

# Progressbar
import time
my_bar =st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

# Spinner
with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished")

## Plots and work Around
# Plot
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')#TAgg
import pandas as pd
# df=pd.read_csv("./datasets/diabetes.csv")
# st.dataframe(df)

# df.plot(kind='bar')
# st.pyplot()
import numpy as np

# df2=pd.DataFrame(np.random.randn(500,2)/[50,50] + [37.76, -127.4], columns=["latitude","longitude"])
# st.map(df2)

# File Selector
import os

#make the function to load faster
st.cache
def file_selector(folder_path='./datasets'):
    #get the list of files in our current directory
    filenames = os.listdir(folder_path)
    #use selectbox to select that particular file
    selected_filename =st.selectbox('Select a file',filenames)
    return os.path.join(folder_path,selected_filename)

filename= file_selector()
#wite the particular file there.
st.write('You selected`%s`' % filename)
df = pd.read_csv(filename)
st.write(df.head(4))

# SIDEBAR
st.sidebar.header("About")
st.sidebar.text("Hello")

# CSS logo
def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()),unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name),unsafe_allow_html=True)


load_css('icon.css')
load_icon('face')
load_icon('code')