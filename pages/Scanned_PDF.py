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

pdf_writer = PyPDF2.PdfFileWriter()
images = convert_from_path(os.path.join(path,file))

for image in images:
    page = pytesseract.image_to_pdf_or_hocr(image, extension='pdf')
    pdf = PyPDF2.PdfFileReader(io.BytesIO(page))
    pdf_writer.addPage(pdf.getPage(0))# export the searchable PDF to searchable.pdf
with open(path + "/searchable.pdf", "wb") as f:
    pdf_writer.write(f)
