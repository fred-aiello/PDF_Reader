# Receipt.png file to 'searchable' pdf file
import streamlit as st
import os
from typing import Dict

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    st.write("Path_filename:", uploaded_file)
    #st.write(bytes_data)

## first file in current dir (with full path)
file = os.path.join(os.getcwd(), os.listdir(os.getcwd())[0])
st.write("TEST RESULT PATH:",file)

"""

@st.cache(allow_output_mutation=True)
def get_static_store() -> Dict:
    """This dictionary is initialized once and can be used to store the files uploaded"""
    return {}

def file_selector(folder_path):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)

def main():
    fileslist = get_static_store()
    folderPath = st.text_input('Enter folder path:')
    if folderPath:    
        filename = file_selector(folderPath)
        if not filename in fileslist.values():
            fileslist[filename] = filename
    else:
        fileslist.clear()  # Hack to clear list if the user clears the cache and reloads the page
        st.info("Select one or more files.")

    if st.button("Clear file list"):
        fileslist.clear()
    if st.checkbox("Show file list?", True):
        finalNames = list(fileslist.keys())
        st.write(list(fileslist.keys()))

main()
"""




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
