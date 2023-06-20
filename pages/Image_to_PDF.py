# Receipt.png file to 'searchable' pdf file
import streamlit as st
import os

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write(bytes_data)

## first file in current dir (with full path)
file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
st.wrtie(file)




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
