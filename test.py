import streamlit as st
import os
from utils import *
def main():
    st.set_page_config(page_title="PDF Summerizer")

    st.title("PDF Summerizing app")
    st.write("Summerize your pdf files in just a few seconds.")
    st.divider()

    pdf=st.file_uploader('Upload your pdf Document',type='pdf')

    submit=st.button("Generate Summary")
    os.environ["OPENAI_API_KEY"]="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"
    if submit:
        response=summarizer(pdf)
        st.subheader('summary of file:')
        st.write(response)
if __name__=='__main__':
    main()

