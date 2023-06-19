# Receipt.png file to 'searchable' pdf file
import streamlit as st

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename1:", uploaded_file.name)
    st.write("filename2:", uploaded_file)
    st.write(bytes_data)

file=r'/home/frederic/Documents/Rognac/Conseils Municipaux/Rognac Mag'
PDF = pytesseract.image_to_pdf_or_hocr(file, extension='pdf')# export to searchable.pdf
with open("searchable.pdf", "w+b") as f:
    f.write(bytearray(PDF))
