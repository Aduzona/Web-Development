import streamlit as st

# Title
st.title("Streamlit Crash Course")
# Header
st.header("Simple Header")
# Subheader
st.subheader("Another sub header")

# Text
st.text("For a simple text")

# Markdown
st.markdown("#### A Markdown ")

# USING COLORS
html_temp = """
    <div style="background-color:tomato;"><p style="color:white;font-size:60px;"> Streamlit is Awesome</p></div>
    """
st.markdown(html_temp,unsafe_allow_html=True)

# Adding A Link
url_link = "https://jcharistech.com"
st.markdown(url_link)

st.markdown("[Google](https://google.com)")




# Error text
st.success("Successful")

st.info("This is an info alert ")

st.warning("This is a warning ")

st.error("This shows an error ")

st.exception("NameError('name not defined')")

# Getting Help Info From Python
st.help(range)

# Writing Text/Super Fxn
st.write("Text with write")

st.write("Python Range with write",range(10))

## MEDIA
# Images
from PIL import Image 
img = Image.open("example.jpeg")
st.image(img,width=300,caption='Streamlit Images')

# Videos
video_file = open("example.mp4",'rb')
video_bytes = video_file.read()
st.video(video_bytes)

# Videos From URL(Youtube)
# yt_url =''
# st.video(yt_url)

# # Audio
# audio_file = open("",'rb')
# audio_bytes = audio_file.read()
# st.audio(audio_bytes,format='audio/mp3')


# Widget
# Checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing or Hiding Widget")

# Radio Button
status = st.radio("What is your status",('Active','Inactive'))
if status == 'Active':
	st.text("Status is Active")
else:
	st.warning("Not Active Yet")

# SelectBox
occupation = st.selectbox("Your Occupation",['Data Scientist','Programmer','Doctor','Businessman'])
st.write("You selected this option",occupation)

# MultiSelect
location = st.multiselect("Where do you stay",("London","New York","Accra","Kiev","Berlin","New Delhi"))
st.write("You selected",len(location),"location")


# Slider
salary = st.slider("What is your salary",1000,10000)

# Buttons
st.button("Simple Button")


# Text Input
name = st.text_input("Enter Name","Type Here...")
if st.button('Submit'):
    result = name.title()
    st.success(result)
else:
    st.write("Press the above button..")

# Text Area
c_text = st.text_area("Enter Text","Type Here...")
if st.button('Analyze'):
    c_result = c_text.title()
    st.success(c_result)
else:
    st.write("Press the above button..")


# Number Input
number = st.number_input('Enter Number')
st.write("The Number was",number)

# With Limits
level = st.number_input('Enter Level',5,10)
st.write("You are in level",level)


#  Date Input
import datetime,time
today = st.date_input("Today is",datetime.datetime.now())


# Time Input
t = st.time_input("The time now is",datetime.time(10,00))
st.write("The time will be",t)

# SIDE Bar
st.sidebar.header("Side Bar Header")
st.sidebar.text("Hello")


# Display JSON
st.text("Display JSON")
st.json({'name':'John','age':34})

# Display Raw Code
st.text("Display Raw Code")
# Auto Detect Language
st.code("import numpy as np")
# Specify Language
jl_code = """function doit(n::Int)
		println(n)
end
"""
st.code(jl_code,language='julia')


st.text("Display Raw Code Alternative Method")
with st.echo():
	# This will also be shown
	import pandas as pd 

	df = pd.DataFrame()


# Progress Bar
# import time
# my_bar = st.progress(0)
# for p  in range(10):
# 	my_bar.progress(p +1)

# Spinner
with st.spinner("Waiting .."):
	time.sleep(5)
st.success("Finished!")

# Placeholder with empty
# age = st.empty()
# age.text("Your Age")
# Replace with image
# age.image(img)

# Balloons
st.balloons()

# Cache For Performance
@st.cache
def run_multiple():
	return range(100)
# Display the result of function
st.write(run_multiple())
import pandas as pd
import numpy as np
import os
# DATASCIENCE 
# Data Frame
df = pd.read_csv('iris.csv')
# Method 1
st.dataframe(df)

# Method 2
st.write(df)

# Method 3 (STATIC)
st.table(df)

# Setting Width
st.dataframe(df,width=10,height=10)
st.dataframe(df,200,100)

# Add Styling
st.dataframe(df.style.highlight_max(axis=0))

# Mutate Data
df1 = df 

# df1.add_rows(df2)

## Plots
import matplotlib.pyplot as plt 
import matplotlib
# Backend
matplotlib.use('Agg')
import seaborn as sns 

# Method 1
# plt.hist(df,bins=20)
# st.pyplot()

# Method 2
df.plot(kind='bar')
st.pyplot()

## Line Charts
st.line_chart(df)

## Area Chart
st.area_chart(df)

## Bar Chart
st.bar_chart(df)




## Heatmap
st.write(sns.heatmap(df.corr(),annot=True))
st.pyplot()


if st.checkbox("Simple Correlation Plot with Matplotlib "):
    plt.matshow(df.corr())
    st.pyplot()

## Map Plot
df = pd.DataFrame(np.random.randn(500,2)/[50,50] + [37.76, -122.4],columns=['latitude','longitude'])
st.map(df)

# Disable Zoom
st.map(df,zoom=False)


## Work Around
# USING CSS ICONS
def load_css(file_name):
    with open(file_name) as f:
        st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

def load_icon(icon_name):
    st.markdown('<i class="material-icons">{}</i>'.format(icon_name), unsafe_allow_html=True)

def remote_css(url):
    st.markdown('<style src="{}"></style>'.format(url), unsafe_allow_html=True)

def icon_css(icone_name):
    remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

# USING COLORS
html_temp = """
	<div style="background-color:tomato;"><p style="color:white;font-size:60px;"> Streamlit is Awesome</p></div>
	"""
st.markdown(html_temp,unsafe_allow_html=True)

# FILE SELECTION
# def file_selector(folder_path='./datasets'):
#     filenames = os.listdir(folder_path)
#     selected_filename = st.selectbox('Select a file', filenames)
#     return os.path.join(folder_path, selected_filename)

# filename = file_selector()
# st.write('You selected `%s`' % filename)
# df = pd.read_csv(filename)	

load_css('icon.css')
load_icon('show_charts')
# # SVG
import base64
import textwrap

def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)

def render_svg_example():
    svg = """
        <svg xmlns="http://www.w3.org/2000/svg" width="100" height="100">
            <circle cx="50" cy="50" r="40" stroke="green" stroke-width="4" fill="yellow" />
        </svg>
    """
    st.write('## Rendering an SVG in Streamlit')

    st.write('### SVG Input')
    st.code(textwrap.dedent(svg), 'svg')

    st.write('### SVG Output')
    render_svg(svg)

render_svg_example()
# Save Data
f_name = st.text_input("Firstname","Type Firstname here")
l_name = st.text_input("Lastname","Type Lastname here")
my_data = {
'firstname':f_name,
'Lastname':l_name
}

st.json(my_data)
import json
if st.button("Save Data"):
    with open('data.json', 'w') as f:
        json.dump(my_data, f)
    st.success("Data Saved!")

