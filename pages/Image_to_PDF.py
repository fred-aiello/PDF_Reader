# Receipt.png file to 'searchable' pdf file
import streamlit as st
import os

# File selector
def file_selector(folder_path='.'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

filename = file_selector()
st.write('You selected `%s`' % filename)

path = folder_path

all_files = []
for (path,dirs,files) in os.walk(path):
    
    for file in sorted(files):
        file = os.path.join(path, file)
        print('file',file)
        all_files.append(file)
        pdf_writer = PyPDF2.PdfFileWriter()
for file in all_files:
    page = pytesseract.image_to_pdf_or_hocr(file, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))
    
    
with open(path + "/" + selected_filename + "2.pdf", "wb") as f:
    pdf_writer.write(f)
