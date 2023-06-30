import streamlit as st
import pytesseract
from pytesseract import Output
from PIL import Image
import pandas as pd
from pdf2image import convert_from_path
import PyPDF2
import os
# from functions.test import calcul

## first file in current dir (with full path)
file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
st.write("TEST RESULT PATH:",file)
st.write(os.getcwd())

st.write("# Convert a scanned PDF document into a searchable PDF file 👋")

st.sidebar.success("Select a demo above.")

st.markdown(
    """
    Streamlit is an open-source app framework built specifically for
    Machine Learning and Data Science projects.
    **👈 Select a demo from the sidebar** to see some examples
    of what Streamlit can do!
    ### Want to learn more?
    - Check out [streamlit.io](https://streamlit.io)
    
    - Ask a question in our [community
        forums](https://discuss.streamlit.io)
    ### See more complex demos
    - Use a neural net to [analyze the Udacity Self-driving Car Image
        Dataset](https://github.com/streamlit/demo-self-driving)
    - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
"""
)
# st.write(calcul(3,1))

input = st.text_input("Enter path where images are stored")
path_init="r/'"+input+"'"
st.write(path_init)
input = st.text_input("Enter path where searchable pdf have to be saved")
path_final="r/'"+input+"'"
st.write("path final: ", path_final)

all_files = []
for (path,dirs,files) in os.walk(path_init):

    st.write("PATH :",path)
    
    for file in sorted(files):
        file = os.path.join(path, file)
        st.write('file: ',file)
        all_files.append(file)
        pdf_writer = PyPDF2.PdfFileWriter()
        st.wrtie("TEST FILE :",all_files)
for file in all_files:
    page = pytesseract.image_to_pdf_or_hocr(file, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))
    
    
# with open(path_final + "/Conso.pdf", "wb") as f:
#    pdf_writer.write(f)
